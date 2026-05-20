# EPSS Vendor Triage

A lightweight Python utility for **KEV + EPSS enrichment** and **vendor-centric vulnerability triage**.

This project helps security teams prioritize vulnerabilities by combining:

- CISA KEV (Known Exploited Vulnerabilities)
- EPSS (Exploit Prediction Scoring System)
- Vendor-based risk analysis
- EPSS score filtering
- CVE-level drill-down

Useful for:

- CTEM (Continuous Threat Exposure Management)
- Vulnerability Management
- Patch Prioritization
- Vendor Risk Review
- Security Operations

---

## Features

### 1. KEV + EPSS Enrichment

Fetch KEV and EPSS data, merge by CVE, and export enriched results.

Supported capabilities:

- CISA KEV retrieval
- EPSS retrieval
- CVE correlation
- EPSS score filtering
- EPSS percentile filtering
- CSV export
- XLSX export

---

### 2. Vendor-centric Triage

Analyze high-risk CVEs by vendor.

Supported capabilities:

- EPSS score filtering
- Vendor ranking
- Total CVE count
- Vendor count
- Vendor-specific CVE details
- Product visibility
- Vulnerability summary visibility
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
    └── sample_kev_epss.csv
```

---

## Requirements

- Python 3.9+
- Internet access (for live KEV / EPSS retrieval)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Installation

```bash
git clone https://github.com/peridotan/epss-vendor-triage.git
cd epss-vendor-triage
pip install -r requirements.txt
```

---

## Usage

### CLI Help

Both tools provide built-in help when required arguments are missing.

```bash
python kev_epss_tool.py
python vendor_from_epss_csv.py
```

---

## 1) Fetch KEV + EPSS data

Retrieve KEV and EPSS, merge by CVE, and export enriched results.

```bash
python kev_epss_tool.py --xlsx
```

Output:

- `kev_epss_result.csv`
- `kev_epss_result.xlsx`

---

### Filter by EPSS score

```bash
python kev_epss_tool.py --epss-threshold 0.7 --xlsx
```

---

### Filter by EPSS percentile

```bash
python kev_epss_tool.py --percentile-threshold 0.99 --xlsx
```

---

### Combined filtering

```bash
python kev_epss_tool.py \
  --epss-threshold 0.7 \
  --percentile-threshold 0.99 \
  --xlsx
```

---

## Quick Test with Sample CSV

The sample CSV allows quick testing of the vendor analysis tool without fetching live KEV/EPSS data.

### Run vendor ranking

```bash
python vendor_from_epss_csv.py samples/sample_kev_epss.csv --score 0.9
```

Expected output:

```text
EPSS Score >= 0.9
Total CVEs : 5
Vendors    : 5

Vendor ranking

Microsoft: 1
Apache: 1
Cisco: 1
Ivanti: 1
Fortinet: 1
```

---

### Drill down by vendor

```bash
python vendor_from_epss_csv.py \
  samples/sample_kev_epss.csv \
  --score 0.9 \
  --vendor Microsoft
```

Displays:

- CVE
- EPSS Score
- EPSS Percentile
- Product
- Vulnerability Summary

---

### Why use sample CSV?

Useful for:

- Quick testing
- Demo usage
- Offline validation
- CI/CD sanity checks
- Understanding expected CSV structure

---

## 2) Vendor ranking

Analyze vendors by EPSS score threshold.

The vendor analysis tool also shows built-in help when no input CSV is provided.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
```

Example output:

```text
EPSS Score >= 0.9
Total CVEs : 555
Vendors    : 153

Vendor ranking

Microsoft: 95
Adobe: 38
Apache: 34
```

---

## 3) Drill down by vendor

Show CVE details for a specific vendor.

```bash
python vendor_from_epss_csv.py \
  kev_epss_result.csv \
  --score 0.9 \
  --vendor Microsoft
```

Displays:

- CVE
- EPSS Score
- EPSS Percentile
- Product
- Vulnerability Summary

---

## 4) Export vendor-specific CSV

Export filtered vendor results.

```bash
python vendor_from_epss_csv.py \
  kev_epss_result.csv \
  --score 0.9 \
  --vendor Microsoft \
  -o microsoft_cves.csv
```

---

## Example Workflow

1. Fetch KEV + EPSS
2. Filter high-risk CVEs
3. Identify risky vendors
4. Drill down into vendor-specific vulnerabilities
5. Prioritize remediation

---

## Defensive Security Use Only

This tool is intended for:

- Defensive vulnerability triage
- Vulnerability prioritization
- Security analysis
- Patch planning
- Risk-based remediation review

It does **not** perform:

- Exploitation
- Active scanning
- Penetration testing
- Unauthorized access
- Offensive operations

---

## Data Sources

- CISA KEV
- FIRST EPSS

---

## License

MIT License