# Research Decisions & AI Provenance Log

| Stage | Decision | Reason | Source / Evidence | Status |
| :--- | :--- | :--- | :--- | :--- |
| **0–5. Protocol Lock** | Froze RQ1–RQ3, 5-fold `StratifiedGroupKFold` (`SEED=42`) grouped by `cited_oa_id`, and corrected Eq. (2) cosine-similarity denominator. | Prevents document-level leakage and post-hoc threshold tuning. | `paper/main.tex` Eq. (1)–(4) (`[VERIFIED]`). | Complete |
| **7a. Baseline Execution** | Executed `B1–B4` on OpenAlex + `SciBERT` + `DeBERTa-v3` (`N=16`): `B4b (S_lex)` achieved `Macro-F1=0.9373`, `FPR_Foundational=0.0000` vs. `B1/B2` (`Macro-F1=0.5152`, `FPR=0.8571`). | Proved age-only heuristics misclassify `85.71%` of foundational landmarks. | Colab Cell 4–5 execution logs (`[VERIFIED]`). | Complete |
| **7b. Debugging Fixes** | Patched `cs_011` (*GPT-2*) from `2024` to `2019` (`T=0.5833`), added disk reload guard, and ran 8-row ablation (`w/o Intent (I)` dropped `Macro-F1` to `0.4353`). | Eliminated OpenAlex substring mismatch and proved Intent ($I$) is the critical safety signal. | Colab Cell 6 ablation table (`[VERIFIED]`). | Complete |
| **7d. Pathway C Lock** | Preserved `B4` untouched and introduced isolated `S_hybrid` feature (`I > 0.50` gated) in `scripts/evaluate_and_plot.py`. | Isolates one causal signal modification without brittle post-hoc overrides. | `scripts/evaluate_and_plot.py` (`[TEST REQUIRED]` for CLI run). | Locked |
