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

## Why this tool?

CVSS indicates **severity**, but not likelihood of exploitation.  
EPSS helps estimate **exploit probability**.  
KEV identifies vulnerabilities **known to be actively exploited in the wild**.

This tool combines those signals to support:

- Risk-based vulnerability prioritization
- Vendor-centric exposure review
- Threat-informed remediation planning
- Practical CTEM workflows

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
├── codex-skills/
│   └── epss-vendor-triage/
│       └── SKILL.md
└── samples/
    └── sample_kev_epss.csv
```

---

## Codex Skill

This repository includes a Codex Skill for operating and explaining the EPSS
Vendor Triage workflow consistently.

Purpose:

- Guide Codex when generating KEV + EPSS outputs
- Support vendor concentration review and patch prioritization
- Keep reporting defensive, practical, and customer-safe

Placement:

```text
codex-skills/epss-vendor-triage/
```

Example usage with Codex:

```text
Use the epss-vendor-triage skill to generate the default KEV + EPSS dataset.
```

```text
Use the epss-vendor-triage skill to rank vendors from kev_epss_result.csv with EPSS score >= 0.9.
```

Typical commands referenced by the skill:

```bash
python kev_epss_tool.py --xlsx
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
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

Both tools provide built-in help.

```bash
python kev_epss_tool.py
python vendor_from_epss_csv.py
```

You can also use `--help`.

```bash
python kev_epss_tool.py --help
python vendor_from_epss_csv.py --help
```

### Shell notes

Examples in this README are written for Git Bash and other Bash-compatible shells.
On Windows PowerShell, run the same command on one line, or use PowerShell's backtick
line continuation instead of `\`.

Git Bash / Bash:

```bash
python kev_epss_tool.py \
  --epss-threshold 0.7 \
  --percentile-threshold 0.99 \
  --xlsx
```

PowerShell:

```powershell
python kev_epss_tool.py `
  --epss-threshold 0.7 `
  --percentile-threshold 0.99 `
  --xlsx
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

By default, `kev_epss_tool.py` uses `kev_epss_result.csv` as the CSV output path.
When `--xlsx` is specified, the XLSX file is written next to the CSV output with
the `.xlsx` extension.

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

Defaults:

- `--epss-threshold` defaults to `0.0`
- `--percentile-threshold` defaults to `0.0`

This means that, unless thresholds are specified, the output includes KEV entries
regardless of EPSS score or percentile.

---

### Custom output path

Use `--output` or `-o` to choose the CSV output path.

```bash
python kev_epss_tool.py -o kev_epss_result_20260601.csv --xlsx
```

This writes:

- `kev_epss_result_20260601.csv`
- `kev_epss_result_20260601.xlsx`

If you write to a subdirectory, create the directory first. The tool does not
create missing output directories.

Git Bash / Bash:

```bash
mkdir -p output
python kev_epss_tool.py -o output/kev_epss_result.csv --xlsx
```

PowerShell:

```powershell
New-Item -ItemType Directory -Force output
python kev_epss_tool.py -o output/kev_epss_result.csv --xlsx
```

---

### Request timeout

Use `--timeout` when network access to CISA KEV or FIRST EPSS is slow.

```bash
python kev_epss_tool.py --timeout 60 --xlsx
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

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
```

`--score` defaults to `0.9` when it is omitted.

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

Quote vendor names that contain spaces.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 --vendor "Pulse Secure"
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

You can also export all rows that match the EPSS score threshold without limiting
the output to one vendor.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 -o high_epss_cves.csv
```

---

## Input CSV requirements

`vendor_from_epss_csv.py` can analyze the CSV produced by `kev_epss_tool.py` and
CSV files with compatible column names.

Minimum required data:

- Vendor column, such as `vendor`, `vendorProject`, `Vendor`, or `ベンダー`
- EPSS score column, such as `epss_score`, `epss`, `score`, `EPSS`, or `EPSS Score`

Optional columns improve drill-down output:

- CVE column, such as `cve`, `cveID`, `CVE`, or `CVE ID`
- Product column, such as `product`, `Product`, or `製品`
- EPSS percentile column, such as `epss_percentile`, `percentile`, or `EPSS Percentile`
- Description column, such as `description`, `summary`, `shortDescription`, `cveDescription`, or `Description`

---

## Example Workflow

1. Fetch KEV + EPSS
2. Filter high-risk CVEs
3. Identify risky vendors
4. Drill down into vendor-specific vulnerabilities
5. Prioritize remediation

---

## Practical Use Cases

- CTEM-driven vulnerability prioritization
- Vendor exposure analysis
- Threat-informed patch review
- Risk-based remediation planning
- Security operations reporting

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

## Interpretation Notes

EPSS estimates the likelihood of exploitation activity. It is not a complete
risk score and does not include business impact, asset exposure, compensating
controls, or operational criticality.

Use KEV and EPSS as prioritization signals, then confirm whether the affected
product is actually present, exposed, and unpatched in your environment.

---

## Roadmap

Potential future enhancements:

- Top N vendor filtering
- CVSS integration
- Historical diff comparison
- Risk scoring enhancements

---

## Data Sources

- CISA KEV
- FIRST EPSS

---

## License

MIT License
