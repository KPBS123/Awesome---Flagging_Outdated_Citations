# GitHub Implementations

## 1. SciFact

**Repository:** allenai/scifact

**GitHub:**
https://github.com/allenai/scifact

**What it implements:**
SciFact provides datasets and models for verifying scientific claims using evidence from research papers.

**Why it is relevant:**
The project is relevant because outdated-citation detection can benefit from checking whether a citation actually provides evidence supporting the claim in a document.

**Documentation:**
The repository contains a README, training instructions, scripts, dataset information, and examples.

**License:**
The repository provides a license file.

**Research Connection:**
The repository is directly connected to the paper *Fact or Fiction: Verifying Scientific Claims*.

## 2. SciCite

**Repository:** allenai/scicite

**GitHub:**
https://github.com/allenai/scicite

**What it implements:**
SciCite provides code and pretrained models for classifying the intent or purpose of citations in scientific publications.

**Why it is relevant:**
Citation intent can help determine whether an existing citation is being used for background information, comparison, methodology, results, or another purpose before recommending a replacement.

**Documentation:**
The repository contains installation information, training instructions, pretrained models, and citation information.

**License:**
Apache-2.0.

**Research Connection:**
The repository implements the research presented in *Structural Scaffolds for Citation Intent Classification in Scientific Publications*.

## 3. SPECTER

**Repository:** allenai/SPECTER

**GitHub:**
https://github.com/allenai/SPECTER

**What it implements:**
SPECTER generates document-level representations of scientific papers using citation-informed learning.

**Why it is relevant:**
The generated scientific-paper embeddings can be used to compare an old citation with candidate newer papers and identify semantically related research.

**Documentation:**
The repository provides installation instructions, sample data, model information, and commands for generating embeddings.

**Research Connection:**
SPECTER is directly connected to the research on citation-informed scientific-document representation.

## 4. MultiVerS

**Repository:** dwadden/multivers

**GitHub:**
https://github.com/dwadden/multivers

**What it implements:**
MultiVerS is a scientific claim-verification system that retrieves evidence from scientific documents and predicts whether evidence supports a claim.

**Why it is relevant:**
It is relevant to the project because evidence retrieval and claim verification can help determine whether an existing citation adequately supports a statement and whether another source should be considered.

**Documentation:**
The project provides source code, model information, configuration files, and instructions for working with the system.

**Research Connection:**
The implementation is associated with research on scientific claim verification and the SciFact task.

## 5. SciBERT

**Repository:** allenai/scibert

**GitHub:**
https://github.com/allenai/scibert

**What it implements:**
SciBERT provides a pretrained language model and resources specifically designed for scientific text.

**Why it is relevant:**
Scientific-domain language representations can help process citation contexts, abstracts, and research-paper text when identifying relevant or newer citations.

**Documentation:**
The repository provides model information, usage instructions, datasets, and code related to scientific NLP experiments.

**Research Connection:**
The repository is associated with the paper *SciBERT: A Pretrained Language Model for Scientific Text*.
