#!/usr/bin/env bash
# push.sh — publish a new version of neptune-assets
#
# Usage:
#   ./push.sh v1.0.0 "release initiale save the date"
#   ./push.sh v1.1.0 "ajout logo partenaire X + photo Y"
#
# Prerequisites:
#   - git configured with user.name and user.email
#   - authenticated push access to WMH-Project/neptune-assets
#     (via gh auth login, SSH key, or HTTPS credential helper)
#   - working tree clean-ish (script will show status before committing)
#
# What it does:
#   1. validates tag format (vX.Y.Z)
#   2. refuses if tag already exists locally or remotely
#   3. shows git status + diff summary
#   4. confirms with user
#   5. git add -A, git commit, git push main
#   6. git tag -a <tag>, git push --tags
#   7. prints jsDelivr URLs to purge cache if needed

set -euo pipefail

# --- args -------------------------------------------------------------------

TAG="${1:-}"
MESSAGE="${2:-}"

if [[ -z "$TAG" ]]; then
  echo "usage: $0 <tag> [message]"
  echo "   ex: $0 v1.0.0 \"release initiale save the date\""
  exit 1
fi

if ! [[ "$TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "error: tag must match vX.Y.Z (got: $TAG)"
  exit 1
fi

if [[ -z "$MESSAGE" ]]; then
  MESSAGE="Release $TAG"
fi

# --- sanity checks ----------------------------------------------------------

if [[ ! -d .git ]]; then
  echo "error: not a git repository (.git/ not found)"
  exit 1
fi

REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [[ -z "$REMOTE_URL" ]]; then
  echo "error: no 'origin' remote configured"
  echo "  run: git remote add origin git@github.com:WMH-Project/neptune-assets.git"
  exit 1
fi

# tag collision check
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "error: tag $TAG already exists locally"
  exit 1
fi

if git ls-remote --tags origin "$TAG" | grep -q "$TAG"; then
  echo "error: tag $TAG already exists on remote"
  exit 1
fi

# --- summary ----------------------------------------------------------------

echo "==> Repository: $REMOTE_URL"
echo "==> Tag:        $TAG"
echo "==> Message:    $MESSAGE"
echo
echo "==> git status:"
git status --short
echo
echo "==> files that will be added:"
git add -A --dry-run | sed 's/^/    /'
echo

read -r -p "Proceed with commit, push, and tag? [y/N] " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
  echo "aborted."
  exit 0
fi

# --- commit + push ----------------------------------------------------------

git add -A

if git diff --cached --quiet; then
  echo "==> no changes to commit (tag only)"
else
  git commit -m "$MESSAGE"
fi

# push main (create branch if needed)
BRANCH=$(git rev-parse --abbrev-ref HEAD)
git push -u origin "$BRANCH"

# tag
git tag -a "$TAG" -m "$MESSAGE"
git push origin "$TAG"

# --- done -------------------------------------------------------------------

echo
echo "==> Released $TAG"
echo "==> jsDelivr base URL:"
echo "    https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@$TAG/"
echo
echo "==> to purge jsDelivr cache for a specific file (only if overwriting):"
echo "    curl https://purge.jsdelivr.net/gh/WMH-Project/neptune-assets@$TAG/<path>"
