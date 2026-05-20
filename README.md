# EPSS Vendor Triage

A lightweight Python utility for **KEV + EPSS enrichment** and **vendor-centric vulnerability triage**.

This project helps security teams prioritize vulnerabilities by combining:

- CISA KEV (Known Exploited Vulnerabilities)
- EPSS (Exploit Prediction Scoring System)
- Vendor-based risk analysis
- EPSS score filtering
- CVE-level drill-down

Useful for:

- CTEM
- Vulnerability Management
- Patch Prioritization
- Vendor Risk Review
- Security Operations

---

## Features

### 1. KEV + EPSS Enrichment
Fetch KEV and EPSS data, merge by CVE, and export enriched results.

- CISA KEV fetch
- EPSS score fetch
- CVE correlation
- CSV export
- XLSX export

---

### 2. Vendor-centric Triage
Analyze high-risk CVEs by vendor.

- EPSS score filtering
- Vendor ranking
- Total CVE count
- Vendor count
- Vendor-specific CVE details
- Product visibility
- Summary visibility
- CSV re-export

---

## Repository Structure

```text
epss-vendor-triage/
├── kev_epss_tool.py
├── vendor_from_epss_csv.py
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── samples/
