import os
import re
import requests

OPENALEX_BASE = "https://api.openalex.org/works"
POLITE_EMAIL = os.getenv("OPENALEX_EMAIL", "researcher@example.edu")
HEADERS = {"User-Agent": f"mailto:{POLITE_EMAIL}"}

def token_jaccard(a: str, b: str) -> float:
    ta = set(re.findall(r"\w+", a.lower()))
    tb = set(re.findall(r"\w+", b.lower()))
    return len(ta & tb) / max(1, len(ta | tb))

def fetch_openalex_work_safe(doi=None, title=None, expected_year=None, min_sim=0.75):
    """Safely resolves OpenAlex metadata with DOI priority and title/year verification."""
    if doi:
        clean_doi = doi.replace("https://doi.org/", "").strip()
        r = requests.get(f"{OPENALEX_BASE}/https://doi.org/{clean_doi}", headers=HEADERS, timeout=15)
        if r.status_code == 200:
            item = r.json()
            return {
                "openalex_id": item.get("id", "").split("/")[-1],
                "doi": item.get("doi"),
                "title": item.get("title", ""),
                "year": item.get("publication_year"),
                "cited_by_count": item.get("cited_by_count", 0),
                "abstract_inverted_index": item.get("abstract_inverted_index"),
            }
    if title:
        r = requests.get(OPENALEX_BASE, params={"search": title, "per-page": 5}, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            for item in r.json().get("results", []):
                cand_title = item.get("title", "")
                cand_year = item.get("publication_year")
                sim = token_jaccard(title, cand_title)
                year_ok = (expected_year is None) or (cand_year is not None and abs(int(cand_year) - int(expected_year)) <= 1)
                if sim >= min_sim and year_ok:
                    return {
                        "openalex_id": item.get("id", "").split("/")[-1],
                        "doi": item.get("doi"),
                        "title": cand_title,
                        "year": cand_year,
                        "cited_by_count": item.get("cited_by_count", 0),
                        "abstract_inverted_index": item.get("abstract_inverted_index"),
                    }
    return None
