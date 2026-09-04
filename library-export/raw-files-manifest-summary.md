# Raw Library export — local file manifest summary

Generated: 2026-09-04

The current mounted export tree contains 785 materialized source-file snapshots totaling 1,817,527,864 bytes (about 1.69 GiB), excluding TAR packaging and the extraction-status report.

By extension:

- `.png`: 227 files, 264,699,223 bytes
- `.docx`: 129 files, 10,007,727 bytes
- `.xlsx`: 122 files, 138,173,958 bytes
- `.jpeg`: 123 files, 47,259,040 bytes
- `.pdf`: 76 files, 92,946,503 bytes
- `.mp4`: 36 files, 1,085,826,698 bytes
- `.zip`: 27 files, 131,583,747 bytes
- `.md`: 9 files, 244,377 bytes
- `.pptx`: 9 files, 29,597,279 bytes
- `.webp`: 5 files, 560,734 bytes
- `.xls`: 5 files, 227,328 bytes
- `.doc`: 4 files, 317,440 bytes
- `.html`: 3 files, 786,456 bytes
- `.bundle`: 2 files, 2,083,900 bytes
- `.svg`: 2 files, 56,522 bytes
- `.py`: 2 files, 11,002 bytes
- `.mov`: 2 files, 13,092,534 bytes
- `.jpg`: 1 file, 7,935 bytes
- `.txt`: 1 file, 45,461 bytes

A local CSV manifest was generated containing `relative_path`, `size_bytes` and SHA-256 for every one of these 785 snapshots. The complete Library inventory and the 61-entry raw-byte failure ledger are already stored in this repository under `library-export/`.

The raw binary corpus itself cannot be transferred through the currently exposed GitHub connector because its write actions accept UTF-8 content/Git blobs but no mounted-file parameter, Git LFS upload, or release-asset upload. See `library-export/upload-status.md`.
