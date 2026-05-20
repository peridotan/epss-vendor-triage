# vendor_from_epss_csv.py
# -*- coding: utf-8 -*-

import argparse
import csv
from collections import Counter
from pathlib import Path


VENDOR_COLUMNS = ["vendorProject", "vendor", "vendor_name", "Vendor", "ベンダー"]
SCORE_COLUMNS = ["epss", "epss_score", "score", "EPSS", "EPSS Score"]
CVE_COLUMNS = ["cveID", "cve", "CVE", "CVE ID"]
PRODUCT_COLUMNS = ["product", "Product", "製品"]
PERCENTILE_COLUMNS = ["percentile", "epss_percentile", "EPSS Percentile"]
DESCRIPTION_COLUMNS = [
    "shortDescription",
    "description",
    "summary",
    "cveDescription",
    "Description",
    "脆弱性説明",
]


def find_column(fieldnames, candidates):
    normalized = {name.lower().strip(): name for name in fieldnames}
    for c in candidates:
        key = c.lower().strip()
        if key in normalized:
            return normalized[key]
    return None


def to_float(value):
    if value is None:
        return None
    value = str(value).strip().replace("%", "")
    if value == "":
        return None
    try:
        num = float(value)
        if num > 1:
            num = num / 100
        return num
    except ValueError:
        return None


def read_rows(csv_path, score_threshold):
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames:
            raise ValueError("CSVヘッダーが見つかりません。")

        vendor_col = find_column(reader.fieldnames, VENDOR_COLUMNS)
        score_col = find_column(reader.fieldnames, SCORE_COLUMNS)
        cve_col = find_column(reader.fieldnames, CVE_COLUMNS)
        product_col = find_column(reader.fieldnames, PRODUCT_COLUMNS)
        percentile_col = find_column(reader.fieldnames, PERCENTILE_COLUMNS)
        description_col = find_column(reader.fieldnames, DESCRIPTION_COLUMNS)

        if not vendor_col:
            raise ValueError(f"ベンダー列が見つかりません。実際の列: {', '.join(reader.fieldnames)}")
        if not score_col:
            raise ValueError(f"EPSS Score列が見つかりません。実際の列: {', '.join(reader.fieldnames)}")

        rows = []

        for row in reader:
            score = to_float(row.get(score_col))
            vendor = (row.get(vendor_col) or "").strip()

            if score is None or score < score_threshold or not vendor:
                continue

            rows.append({
                "vendor": vendor,
                "cve": (row.get(cve_col) or "").strip() if cve_col else "",
                "product": (row.get(product_col) or "").strip() if product_col else "",
                "epss_score": score,
                "epss_percentile": to_float(row.get(percentile_col)) if percentile_col else None,
                "description": (row.get(description_col) or "").strip() if description_col else "",
            })

        return rows


def print_summary(rows, score_threshold, vendor_name=None):
    if vendor_name:
        print(f"\nEPSS Score >= {score_threshold}")
        print(f"Vendor     : {vendor_name}")
        print(f"Total CVEs : {len(rows)}")
    else:
        total_vendors = len(set(row["vendor"] for row in rows))
        print(f"\nEPSS Score >= {score_threshold}")
        print(f"Total CVEs : {len(rows)}")
        print(f"Vendors    : {total_vendors}")


def print_vendor_ranking(rows):
    counter = Counter(row["vendor"] for row in rows)

    print("\nVendor ranking\n")
    for vendor, count in counter.most_common():
        print(f"{vendor}: {count}")


def print_vendor_details(rows, vendor_name, score_threshold):
    matched = [r for r in rows if r["vendor"].lower() == vendor_name.lower()]

    if not matched:
        print(f"\nNo records found: vendor={vendor_name}")
        return

    matched.sort(key=lambda r: r["epss_score"], reverse=True)

    print_summary(matched, score_threshold, vendor_name)

    print(f"\nCVE list for vendor: {vendor_name}\n")

    for row in matched:
        percentile = f"{row['epss_percentile']:.4f}" if row["epss_percentile"] is not None else ""

        print(row["cve"] or "(CVE unknown)")
        print(f"  EPSS       : {row['epss_score']:.4f}")
        print(f"  Percentile : {percentile}")
        print(f"  Product    : {row['product']}")
        print(f"  Summary    : {row['description']}")
        print()


def write_output(rows, output_path, vendor_name=None):
    if vendor_name:
        rows = [r for r in rows if r["vendor"].lower() == vendor_name.lower()]

    with output_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "vendor",
                "cve",
                "product",
                "epss_score",
                "epss_percentile",
                "description",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n出力しました: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Analyze KEV/EPSS-enriched CSV files by vendor and EPSS score.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
  python vendor_from_epss_csv.py kev_epss_result.csv --vendor Microsoft
  python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 --vendor Microsoft
  python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9 -o output.csv

Typical workflow:
  1. Fetch KEV + EPSS:
     python kev_epss_tool.py --xlsx

  2. Analyze vendors:
     python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
"""
    )

    parser.add_argument(
        "csv_file",
        nargs="?",
        help="Input CSV file (for example: kev_epss_result.csv)"
    )

    parser.add_argument(
        "--score",
        type=float,
        default=0.9,
        help="Minimum EPSS score threshold. Default: 0.9"
    )

    parser.add_argument(
        "--vendor",
        help="Show CVE details for the specified vendor. Example: Microsoft"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Export filtered result to CSV"
    )

    args = parser.parse_args()

    # Show help when csv_file is missing
    if not args.csv_file:
        parser.print_help()
        return

    csv_path = Path(args.csv_file)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    rows = read_rows(csv_path, args.score)

    if not rows:
        print(f"No records found for EPSS Score >= {args.score}")
        return

    if args.vendor:
        print_vendor_details(rows, args.vendor, args.score)
    else:
        print_summary(rows, args.score)
        print_vendor_ranking(rows)

    if args.output:
        write_output(rows, Path(args.output), args.vendor)

if __name__ == "__main__":
    main()