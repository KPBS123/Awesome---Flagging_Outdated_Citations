# An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Metadata: OpenAlex CC0](https://img.shields.io/badge/Metadata-OpenAlex%20CC0-green.svg)](https://openalex.org/)
[![Python 3.10–3.13](https://img.shields.io/badge/Python-3.10%E2%80%933.13-yellow.svg)](#setup--installation)

## Short Description

This repository contains both the **curated literature knowledge base** and the **reproducible Python/LaTeX implementation** for detecting outdated citations in AI-generated and AI-recommended scientific literature. It combines OpenAlex bibliographic verification, temporal age analysis ($T$), SciBERT dense semantic retrieval ($N$), lexical and NLI supersession detection ($S_{\text{lex}}, S_{\text{nli}}$), rhetorical citation intent ($I$), and foundational citation velocity ($F$) to compute a calibrated **Outdated Citation Risk Score ($OCRS$)**.

---

## Table of Contents
1. [Repository Structure](#repository-structure)
2. [Setup & Installation](#setup--installation)
3. [Verified Pilot Results](#verified-pilot-results)
4. [Reproduction Commands](#reproduction-commands)
5. [Research Paper & Citation Integrity Audit](#research-paper--citation-integrity-audit)
6. [Curated Research Resources](#curated-research-resources)
7. [License & Citation](#license--citation)

---

## Repository Structure

```text
Awesome---Flagging_Outdated_Citations/
├── README.md                        # Complete guide, verified results, & reproduction steps
├── requirements.txt                 # Version-bounded Python dependencies
├── research_decisions.md            # Logged methodological & debugging provenance
├── configs/
│   └── experiment_config.yaml       # Frozen random seed (42), thresholds, & model IDs
├── src/
│   ├── openalex_client.py           # DOI & title/year-verified OpenAlex resolver
│   └── features.py                  # Signal extractors (T, S_lex, S_hybrid, F)
├── scripts/
│   └── evaluate_and_plot.py         # [TEST REQUIRED] Leakage audit, CV evaluation, & plots
├── data/
│   └── processed/
│       └── extracted_signals.csv    # Verified 16-instance CS/NLP feature matrix
├── results/
│   ├── tables/
│   │   └── verified_pilot_results.csv
│   └── figures/                     # Generated 300-DPI PNG & PDF plots
├── paper/
│   ├── An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature.pdf
│   ├── main.tex                     # Camera-ready IEEEtran Overleaf manuscript source
│   └── references.bib               # Verified BibTeX bibliography
├── citation-audit/
│   └── Citation_Integrity_Audit.pdf # Bibliographic & claim audit report
├── datasets/
│   └── Datasets.md                  # Curated scholarly datasets
├── Implimentations/
│   └── github-repositories.md       # Related open-source repositories (SciFact, SciCite, SPECTER)
├── tools/
│   └── tools.md                     # Core NLP & ML libraries
├── Tutorial/
│   └── tutorials.md                 # Learning resources
└── LICENSE                          # MIT License
```

---

## Setup & Installation

```bash
git clone [https://github.com/KPBS123/Awesome---Flagging_Outdated_Citations.git](https://github.com/KPBS123/Awesome---Flagging_Outdated_Citations.git)
cd Awesome---Flagging_Outdated_Citations
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

*Optional environment variables (never hardcode secrets in tracked files):*
```bash
export HF_TOKEN="your_huggingface_token_here"
export OPENALEX_EMAIL="your_email@institution.edu"
```

---

## Verified Pilot Results

Evaluated on `data/processed/extracted_signals.csv` ($N=16$ verified CS/NLP citations; $8$ Valid/Foundational, $8$ Outdated/Superseded) under leak-free 5-fold `StratifiedGroupKFold` (`SEED = 42`) grouped strictly by `cited_oa_id`:

| Model / Ablation Configuration | Macro-F1 ($\uparrow$) | Precision ($\uparrow$) | Recall ($\uparrow$) | $\text{FPR}_{\text{found}}$ ($\downarrow$) | AUROC ($\uparrow$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `B1: Age-Only (>5y)` | `0.5152` | `0.5385` | `0.8750` | `0.8571` | `0.5625` |
| `B2: Age (>5y) + SciBERT Sim` | `0.5152` | `0.5385` | `0.8750` | `0.8571` | `0.5312` |
| `B3: Uncalibrated Linear OCRS` | `0.8730` | `1.0000` | `0.7500` | `0.0000` | `0.9375` |
| `B4a: Calibrated Linear OCRS (S_nli)` | `0.8750` | `0.8750` | `0.8750` | `0.0000` | `0.8750` |
| `B4b: Calibrated Linear OCRS (S_lex)` | **`0.9373`** | **`1.0000`** | `0.8750` | **`0.0000`** | `0.8750` |
| `P1: Hard-Gated Linear OCRS` | `0.8118` | `0.7778` | `0.8750` | `0.1429` | `0.7734` |
| `Ablation: w/o Citation Intent (I)` | `0.4353` | `0.4444` | `0.5000` | `0.5714` | `0.3750` |

---

## Reproduction Commands

```bash
# [TEST REQUIRED] Run dataset integrity audit, 5-fold CV comparison, and generate PDF/PNG figures
python scripts/evaluate_and_plot.py
```

---

## Research Paper & Citation Integrity Audit

* **Compiled Manuscript PDF:** [`paper/An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature.pdf`](paper/An%20Automated%20Pipeline%20for%20Flagging%20Outdated%20Citations%20in%20AI-Recommended%20Literature.pdf)
* **Overleaf LaTeX Source:** [`paper/main.tex`](paper/main.tex) & [`paper/references.bib`](paper/references.bib)
* **Citation Integrity Audit:** [`citation-audit/Citation_Integrity_Audit.pdf`](citation-audit/Citation_Integrity_Audit.pdf)

---

## Curated Research Resources

* **Curated References:** [`refrences/refrences.md`](refrences/refrences.md)
* **Datasets:** [`datasets/Datasets.md`](datasets/Datasets.md)
* **Tools & Libraries:** [`tools/tools.md`](tools/tools.md)
* **GitHub Implementations:** [`Implimentations/github-repositories.md`](Implimentations/github-repositories.md)
* **Tutorials:** [`Tutorial/tutorials.md`](Tutorial/tutorials.md)

---

## License & Citation

This repository is released under the [MIT License](LICENSE). OpenAlex metadata is licensed under CC0 1.0 Public Domain.

```bibtex
@unpublished{kaustubh2026ocrs,
  author = {Kaustubh},
  title  = {An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature via Intent-Conditioned Risk Scoring},
  note   = {Department of Information Technology, Indian Institute of Information Technology Allahabad (IIIT-A)},
  year   = {2026}
}
```
