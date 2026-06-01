---
name: epss-vendor-triage
description: Use this skill when working with the peridotan/epss-vendor-triage Python CLI to combine CISA KEV and FIRST EPSS data, generate CSV/XLSX outputs, rank vendors by high-risk CVEs, or create customer-facing and internal vulnerability triage summaries for defensive security, CTEM, or vulnerability management.
---

# EPSS Vendor Triage Skill

## Purpose

Use this skill to operate and explain the `peridotan/epss-vendor-triage` repository consistently.

The repository is a defensive Python CLI utility for vulnerability prioritization. It helps combine CISA Known Exploited Vulnerabilities (KEV) with FIRST EPSS data, then produce CSV/XLSX outputs and vendor-based summaries.

Use this skill for:

- KEV + EPSS vulnerability triage
- Vendor concentration review
- Patch prioritization support
- CTEM-oriented reporting
- Customer-facing vulnerability confirmation reports
- Internal sales or advisory follow-up themes

Do not use this skill for exploitation, unauthorized scanning, offensive operations, or instructions that enable intrusion.

## Mental model

The Python repository is the tool. This skill is the operating procedure for Codex.

When using this skill, do not replace the repository logic unless the user asks for code changes. Prefer running the existing CLI, inspecting outputs, and summarizing the results in a defensible way.

## Repository

Primary repository:

```text
https://github.com/peridotan/epss-vendor-triage
```

Expected core scripts:

```text
kev_epss_tool.py
vendor_from_epss_csv.py
```

Expected common outputs:

```text
kev_epss_result.csv
kev_epss_result.xlsx
```

## Standard workflows

### 1. Generate the default KEV + EPSS dataset

Use this when the user asks for the normal output or wants to refresh the dataset.

```bash
python kev_epss_tool.py --xlsx
```

Expected result:

- CSV output
- XLSX output when `--xlsx` is used
- Combined vulnerability rows with KEV and EPSS-related fields

### 2. Generate high-priority results

Use this when the user asks for high-risk vulnerabilities, urgent candidates, or a focused triage set.

```bash
python kev_epss_tool.py --epss-threshold 0.7 --percentile-threshold 0.99 --xlsx
```

Interpretation:

- `--epss-threshold 0.7` means EPSS score must be at least 0.7.
- `--percentile-threshold 0.99` means the CVE is in the top 1% by EPSS percentile.
- Treat these as prioritization signals, not proof of business impact.

### 3. Rank vendors from an existing CSV

Use this after generating `kev_epss_result.csv`.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
```

Expected result:

- Vendor ranking by number of CVEs meeting the EPSS score threshold
- Useful for concentration analysis and advisory targeting

### 4. Show CVE details for a specific vendor

Use quotes when the vendor name contains spaces.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 --vendor "Microsoft"
```

Important:

```bash
# Correct
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 --vendor "Pulse Secure"

# Incorrect: shell treats Secure as a separate argument
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 --vendor Pulse Secure
```

## Output review checklist

When reviewing command output or generated files, report:

1. Dataset date or generation date if available
2. Total CVE count
3. Number of CVEs after filtering
4. EPSS score threshold and percentile threshold used
5. Top vendors by count
6. CVEs that require immediate product-use confirmation
7. Clear next actions

Avoid presenting EPSS as a complete risk score. EPSS estimates likelihood of exploitation activity, not impact, asset exposure, compensating controls, or business criticality.

## Prioritization guidance

Use this order when explaining priority:

1. KEV-listed and confirmed in the user's environment
2. KEV-listed and externally exposed
3. High EPSS score and high percentile
4. Affected product is internet-facing, identity-related, remote access-related, or security infrastructure
5. Unsupported or difficult-to-patch assets
6. Internal-only assets with compensating controls

Always separate:

- Confirmed affected
- Possibly affected / needs confirmation
- Not affected
- Unknown

## Customer-facing reporting style

For customer-facing reports:

- Use calm, practical wording.
- Do not exaggerate or imply breach without evidence.
- Explain that KEV means known exploited vulnerability.
- Explain that EPSS is a probability signal for exploitation activity.
- Make the first action asset confirmation, not immediate patching in all cases.
- Use phrases such as `利用有無の確認`, `外部公開有無の確認`, `適用済みパッチの確認`, and `影響範囲の切り分け`.
- Separate executive summary from technical details.

Recommended customer-facing structure:

```text
1. サマリ
2. 今回確認すべきポイント
3. 優先確認対象ベンダー
4. 個別CVE確認表
5. 推奨アクション
6. 補足: KEVとEPSSの意味
```

## Internal reporting style

For internal or advisory use:

- Include vendor concentration.
- Include likely advisory themes.
- Identify products that map to common customer environments.
- Suggest proposal or support angles, but keep them grounded in the data.
- Mark assumptions explicitly.

Recommended internal structure:

```text
1. 今月の傾向
2. 高EPSS/KEVの集中ベンダー
3. 顧客確認につながる製品領域
4. 提案・支援テーマ
5. 注意点・データ限界
```

## Troubleshooting

### Vendor names with spaces fail

Symptom:

```text
error: unrecognized arguments: Secure
```

Cause:

The vendor name was not quoted.

Fix:

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 --vendor "Pulse Secure"
```

### Output file not found

Check whether `kev_epss_result.csv` exists in the current directory. If not, run the main KEV + EPSS command first.

```bash
python kev_epss_tool.py --xlsx
```

### Too many results

Raise the threshold.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.95
```

### Too few results

Lower the threshold, but explain that this broadens the review set.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.7
```

## Safety boundaries

This skill is for defensive analysis and reporting only.

Allowed:

- Vulnerability prioritization
- Report generation
- Vendor ranking
- Patch and asset confirmation guidance
- Defensive CTEM workflows

Not allowed:

- Exploit development
- Attack instructions
- Unauthorized scanning or enumeration
- Credential theft or persistence guidance
- Instructions to bypass security controls

## When changing the repository

If the user asks to modify `epss-vendor-triage`, preserve the CLI-first nature of the tool.

Prefer small, maintainable changes:

- Better help text
- Safer argument parsing
- Clearer output names
- README updates
- Error messages for common mistakes
- Optional reporting templates

Before changing behavior, check whether existing commands used by the user will remain compatible.
