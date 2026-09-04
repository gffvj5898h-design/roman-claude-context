# Recovered Library file manifests

This directory contains the complete SHA-256 manifest for the recovered working corpus.

- Total manifest rows: **785**
- Total materialized bytes represented: **1,817,527,864**
- Files: `all-local-files-manifest-01.csv` through `all-local-files-manifest-08.csv`
- Columns: `relative_path`, `size_bytes`, `sha256`

Parts 01–07 contain 100 rows each; part 08 contains 85 rows. Each part repeats the CSV header.

To reconstruct one CSV on a local shell:

```bash
cp all-local-files-manifest-01.csv all-local-files-manifest.csv
for f in all-local-files-manifest-{02..08}.csv; do
  tail -n +2 "$f" >> all-local-files-manifest.csv
done
```

These manifests identify the exact recovered snapshots and allow integrity verification after transfer.

The binary corpus itself is not yet stored in this Git repository because the GitHub connector exposed to this chat does not accept mounted binary files, Git LFS object uploads, or release-asset uploads. The repository is prepared for Git LFS via `/.gitattributes`, and `scripts/push-raw-library.sh` is included for a direct Git/LFS transfer from a machine that has the recovered files.

The separate Library inventory accounts for **841/841** Library entries. **61** entries were identifiable but their raw bytes could not be obtained from the source storage backend because it returned HTTP 403; see `../remaining-extraction-status.md`.
