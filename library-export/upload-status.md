# Library raw upload status

Updated: 2026-09-04

Repository visibility was verified as **private** before continuing.

## Inventory

- Library entries accounted for: **841 / 841**.
- Original files successfully materialized into the working filesystem: **780** according to the completed Library extraction ledger.
- Library entries whose raw bytes could not be materialized because the storage backend returned HTTP 403: **61**.
- Current working export tree contains **785 source-file snapshots** (some are duplicate/generated variants from the extraction workflow), totaling **1,817,527,864 bytes** before TAR packaging.

## Stored in this repository

- Full ChatGPT context export under `chatgpt-context/`.
- Library inventory files and extraction reports under `library-export/`.
- The complete 61-entry raw-byte failure ledger in `library-export/remaining-extraction-status.md`.
- Complete SHA-256 manifest for all **785** recovered local source snapshots, split into `library-export/manifests/all-local-files-manifest-01.csv` through `all-local-files-manifest-08.csv`.
- Manifest documentation in `library-export/manifests/README.md`.
- Git LFS rules in `/.gitattributes`.
- Direct Git/LFS import helper in `/scripts/push-raw-library.sh`.

## Binary-transfer limitation of the connected GitHub action

The connected GitHub write action available in this chat can create/update UTF-8 repository files and Git objects, but it has **no file-parameter/LFS/release-asset upload action that can take the mounted binary files directly**. The recovered corpus includes about 1.82 GB of PDFs, DOCX/XLSX/PPTX, images, videos, ZIPs and other binary data. Those bytes therefore cannot be streamed from the mounted working filesystem into GitHub through the current connector without serializing the entire dataset through chat tool arguments, which is not technically viable and would also fail GitHub's normal large-file limits for some objects.

This is a connector transport limitation, not a repository-permission problem. The repository itself is private and the connected account has push/admin permission.

## Integrity

Every one of the 785 materialized snapshots has a recorded relative path, byte size and SHA-256 digest in the eight CSV manifest parts. The local recovered export remains in `/mnt/data/library-export/` for this session. Once a direct Git/LFS-capable transfer route has access to those bytes, `scripts/push-raw-library.sh` can import them into `raw-library/` and the hashes can be used to verify the transfer.
