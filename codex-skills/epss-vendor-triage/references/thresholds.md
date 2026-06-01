# Threshold Guidance

## Default exploratory run

Use no threshold or the repository default when the user wants a broad dataset.

```bash
python kev_epss_tool.py --xlsx
```

## Focused high-risk run

Use this when the user wants a practical short list.

```bash
python kev_epss_tool.py --epss-threshold 0.7 --percentile-threshold 0.99 --xlsx
```

## Vendor ranking threshold

A score threshold of 0.9 is useful for a compact vendor concentration view.

```bash
python vendor_from_epss_csv.py kev_epss_result.csv --score 0.9
```

## Interpretation caution

EPSS is not a business risk score. It does not include local asset exposure, compensating controls, business impact, or whether the product exists in the user's environment.
