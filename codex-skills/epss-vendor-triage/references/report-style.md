# Report Style Guide

## Customer-facing tone

Use calm and practical language. The report should help the customer decide what to confirm first.

Avoid:

- 確実に侵害されています
- すぐに危険です
- 全社緊急対応が必要です

Prefer:

- 悪用が確認されている脆弱性として、利用有無の確認を優先してください
- EPSSが高いため、今後の悪用可能性を踏まえて確認優先度を上げることを推奨します
- 外部公開資産で利用している場合は、優先的にパッチ適用状況を確認してください

## Customer-facing table columns

Recommended columns:

| Priority | Vendor | CVE | Product | KEV | EPSS | Confirmation point | Recommended action |
|---|---|---|---|---|---|---|---|

## Internal advisory columns

Recommended columns:

| Vendor | CVE count | Representative CVEs | Product area | Customer relevance | Advisory theme |
|---|---:|---|---|---|---|
