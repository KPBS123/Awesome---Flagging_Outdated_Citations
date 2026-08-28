#An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature

Short Description

This repository explores automated detection of outdated citations in AI-generated and AI-recommended scientific literature. It combines bibliographic verification, temporal analysis, semantic retrieval, citation intent, and supersession detection to identify citations that may no longer provide the best evidence.

Table of Contents
Topic Overview
AI-Assisted Research Paper
Citation Integrity Audit
Curated Research Papers
Datasets
Tools and Libraries
GitHub Implementations
Tutorials and Learning Resources
License
Topic Overview

Large language models are increasingly used to discover, summarize, and recommend scientific literature. Although retrieval-augmented generation can improve access to external sources, AI-generated citations may still be outdated even when the cited papers are real and relevant.

An outdated citation occurs when an older publication no longer provides the most appropriate evidence for a current claim because newer studies have improved, contradicted, corrected, or replaced the earlier work. However, old papers are not automatically outdated because foundational theories and original methods can remain important.

This project proposes an automated pipeline that verifies citations, analyzes publication age, retrieves newer research, compares papers semantically, examines citation intent, and detects evidence of supersession. The system produces an Outdated Citation Risk Score to help researchers identify citations that require human review.

The main research directions include scientific claim verification, citation recommendation, scholarly information retrieval, citation-network analysis, and trustworthy AI-assisted research.

AI-Assisted Research Paper

Title: An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature

The paper proposes a multi-stage system for detecting citations that may have become outdated in AI-generated literature recommendations.

View the research paper

Citation Integrity Audit

The citations and major claims in the research paper were reviewed for bibliographic accuracy, relevance, and consistency.

View the Citation Integrity Audit

Curated Research Papers

Important research related to this topic includes:

Retrieval-Augmented Generation
Citation Recommendation
Citation Intent Classification
Scientific Claim Verification
S2ORC
SciBERT

View the complete references

Datasets

Relevant datasets and scholarly resources include:

S2ORC — Scholarly papers, metadata, and citation relationships.
SciFact — Scientific claim verification.
SciFact-Open — Open-domain scientific claim verification.
OpenAlex — Scholarly works and citation data.
Crossref — Bibliographic and DOI metadata.
Semantic Scholar — Academic literature and citation information.

View datasets

Tools and Libraries
Python — Main programming language.
Crossref — Bibliographic verification.
OpenAlex — Scholarly metadata.
Semantic Scholar — Literature retrieval.
SciBERT — Scientific NLP.
Sentence Transformers — Semantic similarity.
Scikit-learn — Machine learning.
NetworkX — Citation-network analysis.

View tools

GitHub Implementations

Relevant open-source implementations include projects related to:

Scientific claim verification
Scholarly citation analysis
Scientific language models
Semantic text similarity

View GitHub implementations

Tutorials and Learning Resources

Useful learning areas for this project include:

Retrieval-Augmented Generation (RAG)
Scientific NLP
Citation recommendation
Scientific claim verification
Semantic embeddings
Citation-network analysis
Bibliographic APIs
License

This repository's original content is released under the MIT License. Third-party papers, datasets, libraries, and other resources remain subject to their respective licenses.

See the LICENSE file for details.
