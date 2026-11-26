#!/usr/bin/env bash
# Puts the project Product Feed back to the state the tutorial starts from: the project file that the
# tutorial ships, imported by a person, so that nothing in the change journal awaits review.
# Uses cmemc with the connection from the environment (CMEM_BASE_URI, OAUTH_*), see ../README.md.
set -euo pipefail

PROJECT=product-feed
GRAPH=https://example.org/product-feed/
ZIP="$(cd "$(dirname "$0")/../../.." && pwd)/docs/build/review-agent-changes/product-feed.project.zip"

# --id-only: the table output wraps long IRIs, so a grep on it can miss an entry.
# The lists are read first: with pipefail, "cmemc ... | grep -q" fails when grep stops reading early.
PROJECTS=$(cmemc project list --id-only)
if grep -qx "$PROJECT" <<< "$PROJECTS"; then
  cmemc project delete "$PROJECT" >/dev/null
fi
GRAPHS=$(cmemc graph list --id-only)
if grep -qx "$GRAPH" <<< "$GRAPHS"; then
  cmemc graph delete "$GRAPH" >/dev/null
fi
cmemc project import "$ZIP" "$PROJECT" >/dev/null
