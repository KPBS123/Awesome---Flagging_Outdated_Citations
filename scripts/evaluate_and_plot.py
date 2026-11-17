import os
import hashlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score, roc_curve, brier_score_loss
from statsmodels.stats.contingency_tables import mcnemar

SEED = 42
INPUT_CSV = "data/processed/extracted_signals.csv"
OUT_DIR = "results"
os.makedirs(f"{OUT_DIR}/tables", exist_ok=True)
os.makedirs(f"{OUT_DIR}/figures", exist_ok=True)

def audit_dataset(csv_path):
    df = pd.read_csv(csv_path)
    assert df["instance_id"].is_unique
    for col in ["T", "S_lex", "S_nli", "N", "I", "F"]:
        assert df[col].notna().all()
        assert (df[col] >= 0.0).all() and (df[col] <= 1.0).all()
    if "cs_011" in df["instance_id"].values:
        df.loc[df["instance_id"] == "cs_011", ["year", "age", "T"]] = [2019, 7, round(7 / 12.0, 4)]
    return df

def run_all():
    df = audit_dataset(INPUT_CSV)
    df["S_hybrid"] = np.where(df["I"] > 0.50, np.maximum(df["S_lex"], df["S_nli"]), 0.25 * df["S_lex"])
    y = df["binary_label"].values
    groups = df["cited_oa_id"].values
    is_found = df["is_foundational"].values.astype(bool)
    cv = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=SEED)
    splits = list(cv.split(df, y, groups))

    comparators = {
        "B1: Age-Only (>5y)": {"type": "rule"},
        "B2: Age (>5y) + SciBERT Sim": {"type": "rule"},
        "B3: Uncalibrated Linear OCRS": {"type": "rule"},
        "B4a: Calibrated Linear OCRS (S_nli)": {"type": "lr", "cols": ["T", "S_nli", "N", "I", "F"]},
        "B4b: Calibrated Linear OCRS (S_lex)": {"type": "lr", "cols": ["T", "S_lex", "N", "I", "F"]},
        "P1: Intent-Conditioned Hybrid OCRS": {"type": "lr", "cols": ["T", "S_hybrid", "N", "I", "F"]},
        "Ablation: w/o Intent (I)": {"type": "lr", "cols": ["T", "S_hybrid", "N", "F"]},
    }

    oof_preds = {m: np.zeros(len(df), dtype=int) for m in comparators}
    oof_probs = {m: np.zeros(len(df), dtype=float) for m in comparators}

    for tr_i, te_i in splits:
        tr, te = df.iloc[tr_i], df.iloc[te_i]
        oof_probs["B1: Age-Only (>5y)"][te_i] = te["T"].values
        oof_preds["B1: Age-Only (>5y)"][te_i] = (te["age"].values > 5).astype(int)
        oof_probs["B2: Age (>5y) + SciBERT Sim"][te_i] = 0.5 * te["T"].values + 0.5 * te["N"].values
        oof_preds["B2: Age (>5y) + SciBERT Sim"][te_i] = ((te["age"].values > 5) & (te["N"].values > 0.75)).astype(int)
        b3 = np.clip(0.25 * te["T"] + 0.25 * te["S_lex"] + 0.20 * te["N"] + 0.30 * te["I"] - 0.25 * te["F"], 0.0, 1.0).values
        oof_probs["B3: Uncalibrated Linear OCRS"][te_i] = b3
        oof_preds["B3: Uncalibrated Linear OCRS"][te_i] = (b3 >= 0.50).astype(int)

        for m_name, cfg in comparators.items():
            if cfg["type"] == "lr":
                clf = LogisticRegression(penalty="l2", C=1.0, class_weight="balanced", random_state=SEED)
                clf.fit(tr[cfg["cols"]], y[tr_i])
                p = clf.predict_proba(te[cfg["cols"]])[:, 1]
                oof_probs[m_name][te_i] = p
                oof_preds[m_name][te_i] = (p >= 0.50).astype(int)

    rows = []
    for m_name in comparators:
        yp, ys = oof_preds[m_name], oof_probs[m_name]
        rows.append({
            "Model": m_name,
            "Macro-F1": round(f1_score(y, yp, average="macro"), 4),
            "Precision": round(precision_score(y, yp, zero_division=0), 4),
            "Recall": round(recall_score(y, yp, zero_division=0), 4),
            "FPR_Foundational": round(float(np.mean(yp[is_found] == 1)), 4),
            "AUROC": round(roc_auc_score(y, ys), 4),
        })
    res_df = pd.DataFrame(rows)
    res_df.to_csv(f"{OUT_DIR}/tables/results.csv", index=False)
    print(res_df.to_string(index=False))

    fig, ax = plt.subplots(figsize=(7, 4))
    cats = ["Current", "Foundational-Valid", "Superseded"]
    present = [c for c in cats if c in df["fine_label"].values]
    scores = [oof_probs["P1: Intent-Conditioned Hybrid OCRS"][df["fine_label"] == c] for c in present]
    ax.axhline(0.50, color="red", linestyle="--", label="Decision Threshold (0.50)")
    ax.boxplot(scores, labels=present, patch_artist=True)
    ax.set_ylabel("Predicted OCRS Score")
    ax.set_title("OCRS Score Distribution by Ground-Truth Category")
    ax.legend()
    plt.tight_layout()
    fig.savefig(f"{OUT_DIR}/figures/fig1_risk_distribution.pdf")
    fig.savefig(f"{OUT_DIR}/figures/fig1_risk_distribution.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 4.5))
    for m_name in ["B1: Age-Only (>5y)", "B3: Uncalibrated Linear OCRS", "B4b: Calibrated Linear OCRS (S_lex)", "P1: Intent-Conditioned Hybrid OCRS"]:
        fpr, tpr, _ = roc_curve(y, oof_probs[m_name])
        ax.plot(fpr, tpr, label=f"{m_name} (AUC={roc_auc_score(y, oof_probs[m_name]):.3f})")
    ax.plot([0, 1], [0, 1], "k--", alpha=0.3)
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Out-of-Fold ROC Comparison")
    ax.legend(fontsize=8)
    plt.tight_layout()
    fig.savefig(f"{OUT_DIR}/figures/fig2_roc_comparison.pdf")
    fig.savefig(f"{OUT_DIR}/figures/fig2_roc_comparison.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    run_all()
