#!/usr/bin/env bash
# Removes what the tutorial adds: the catalog graph Procurement Companion and its import in the base catalog.
# Uses cmemc with the connection from the environment (CMEM_BASE_URI, OAUTH_*), see ../README.md.
set -euo pipefail

GRAPH=https://ns.eccenca.com/data/companion/procurement/
QUERY=$(mktemp)
trap 'rm -f "$QUERY"' EXIT

cat > "$QUERY" <<EOF
DELETE WHERE { GRAPH <https://ns.eccenca.com/data/companion/> {
  <https://ns.eccenca.com/data/companion/> <http://www.w3.org/2002/07/owl#imports> <$GRAPH> } }
EOF
cmemc query execute "$QUERY" >/dev/null

# --id-only: the table output wraps long IRIs, so a grep on it can miss the graph.
# The list is read first: with pipefail, "cmemc ... | grep -q" fails when grep stops reading early.
GRAPHS=$(cmemc graph list --id-only)
if grep -qx "$GRAPH" <<< "$GRAPHS"; then
  cmemc graph delete "$GRAPH"
fi
