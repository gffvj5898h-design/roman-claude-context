# iCloud transfer batches

Prepared: 2026-09-04

`raw-library/page-01/` has already been imported successfully through iCloud + Git LFS.

The remaining recovered raw corpus has been repacked into three TAR archives for manual upload to iCloud Drive and subsequent automated import into this private repository.

## Batch A

File: `roman-library-batch-A.tar`
Contains top-level directories:
- `page-02/`
- `page-03/`
- `page-04/`

Regular files: 253
Archive size: 578344960 bytes
SHA-256: `dbdd3b10dee704d75be04297db9e03e7be54e23b7bb005cfddf5996d6fd66112`

## Batch B

File: `roman-library-batch-B.tar`
Contains top-level directories:
- `page-05/`
- `page-06/`

Regular files: 113
Archive size: 659558400 bytes
SHA-256: `5b5011e4674ec854297e89804b24f1e13ce141a6eee56bdd8da4e8f33f6b7d7c`

## Batch C

File: `roman-library-batch-C.tar`
Contains top-level directories:
- `page63/`
- `page64/`
- `page65/`
- `page104/`

Regular files: 336
Archive size: 392949760 bytes
SHA-256: `62a8201d4d269cac5ea1ca5900e74ed20032269b493e78f0e90d70f1bc7d4715`

## Total represented by these batches

702 regular files.

Together with the already-imported 83-file `page-01` package, this covers the 785 materialized source snapshots in the working export tree. The separate 61-entry 403 failure ledger remains under `library-export/remaining-extraction-status.md`.

After each batch is uploaded to iCloud Drive and a public share link is provided, GitHub Actions should resolve the iCloud CloudKit download URL, validate byte size and SHA-256, validate TAR paths/file counts, extract into `raw-library/`, and commit/push binary objects through Git LFS.
