# Library raw upload status

Updated: 2026-09-04

Repository visibility was verified as **private** before continuing.

## Inventory

- Library entries accounted for: **841 / 841**.
- Original files successfully materialized into the working filesystem: **780** according to the completed Library extraction ledger.
- Library entries whose raw bytes could not be materialized because the storage backend returned HTTP 403: **61**.
- Current working export tree contains **785 source-file snapshots** (some are duplicate/generated variants from the extraction workflow), totaling **1,817,527,864 bytes** before TAR packaging.
- A SHA-256 manifest was generated locally for every file in that working export tree.

## What is already in this repository

The repository already contains the full ChatGPT context export, the Library inventory files, extraction reports, and the 61-file failure ledger under `chatgpt-context/` and `library-export/`.

## Binary-transfer limitation of the connected GitHub action

The connected GitHub write action available in this chat can create/update UTF-8 repository files and Git objects, but it has **no file-parameter/LFS/release-asset upload action that can take the mounted binary files directly**. The local export includes about 1.82 GB of PDFs, DOCX/XLSX/PPTX, images, videos, ZIPs and other binary data. Those bytes therefore cannot be streamed from the mounted working filesystem into GitHub through the current connector without serializing the entire dataset through chat tool arguments, which is not technically viable.

This is a connector transport limitation, not a repository-permission problem. The repository itself is private and the connected account has push/admin permission.

## Integrity

The local export is preserved in `/mnt/data/library-export/` in this session. The previously generated extraction status report includes the 61 raw-byte failures. SHA-256 hashes have also been computed for the materialized working set so files can be verified after any binary transfer route becomes available.
