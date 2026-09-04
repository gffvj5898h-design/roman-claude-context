#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/push-raw-library.sh /absolute/path/to/library-export
#
# Requires: git, git-lfs, rsync.
# The target repository must already be cloned and this script run from its root.

SOURCE_DIR="${1:-}"
if [[ -z "$SOURCE_DIR" || ! -d "$SOURCE_DIR" ]]; then
  echo "Usage: $0 /absolute/path/to/library-export" >&2
  exit 2
fi

REPO="gffvj5898h-design/roman-claude-context"
DEST="raw-library"

if [[ ! -d .git ]]; then
  echo "Run this script from the root of the cloned $REPO repository." >&2
  exit 2
fi

git lfs install
mkdir -p "$DEST"

# Copy the recovered source tree. TAR packaging is omitted because it duplicates
# the individual files; extraction reports/manifests are retained separately.
rsync -a --info=progress2 \
  --exclude='*.tar' \
  "$SOURCE_DIR/" "$DEST/"

# LFS patterns are defined in the repository-level .gitattributes.
git add .gitattributes "$DEST"
git status --short

git commit -m "Import recovered ChatGPT Library raw files" || true
git push origin main

echo "Done. Verify with: git lfs ls-files && git status"
