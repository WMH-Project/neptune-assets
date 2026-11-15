#!/usr/bin/env bash
# push.sh — publie une nouvelle version de neptune-assets (commit + tag sur main)
#
# Usage :
#   ./push.sh next   "visuels newsletter décembre" photos/newsletter/december-2026/
#   ./push.sh v1.5.0 "nouveau logo partenaire"     logos/partners/knowledge/x.png
#   ./push.sh next   "retouche d'un visuel existant"          # sans chemin : fichiers déjà suivis seulement
#   ... --yes                                                 # sans question (session sans clavier)
#   ... --allow-modify                                        # dérogation : remplacer un visuel déjà publié
#   ... --allow-delete                                        # dérogation : supprimer ou renommer un chemin publié
#
# Dérogations — réservées au mainteneur. Un visuel remplacé sous le même nom met
# jusqu'à 24 h à changer chez qui l'a déjà chargé (cache navigateur), et les proxys
# d'images des messageries (Gmail, Apple) gardent leur copie plus longtemps encore :
# pour un email déjà envoyé, préférer un nouveau nom de fichier.
#
# Ce que fait le script :
#   1. vérifie qu'on est sur main, à jour avec origin
#   2. « next » = dernier tag + 1 ; refuse un tag déjà pris
#   3. n'ajoute QUE les chemins passés en argument (jamais « git add -A ») ;
#      sans chemin, seulement les modifications de fichiers déjà suivis
#   4. lance check_assets.py (poids par image, poids total, emplacement) — bloquant
#   5. demande confirmation, puis commit + tag poussés ensemble
#   6. vérifie que jsDelivr sert bien les nouveaux fichiers
#
# Prérequis : git configuré, accès en écriture à WMH-Project/neptune-assets, python3.

set -euo pipefail

REPO="WMH-Project/neptune-assets"

# --- arguments --------------------------------------------------------------

YES=0
CHECK_FLAGS=()
MARKERS=""
ARGS=()
for a in "$@"; do
  case "$a" in
    --yes) YES=1 ;;
    --allow-modify|--allow-delete) CHECK_FLAGS+=("$a"); MARKERS="$MARKERS [${a#--}]" ;;
    *) ARGS+=("$a") ;;
  esac
done

TAG="${ARGS[0]:-}"
MESSAGE="${ARGS[1]:-}"
PATHS=("${ARGS[@]:2}")

if [[ -z "$TAG" ]]; then
  echo "usage: $0 <next|vX.Y.Z> \"message\" [chemin ...] [--yes] [--allow-modify] [--allow-delete]"
  echo "   ex: $0 next \"visuels newsletter décembre\" photos/newsletter/december-2026/"
  exit 1
fi

# --- garde-fous sur le dépôt ------------------------------------------------

cd "$(dirname "$0")"

if [[ ! -e .git ]]; then
  echo "erreur : pas un dépôt git"; exit 1
fi

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" != "main" ]]; then
  echo "erreur : on publie depuis main, pas depuis « $BRANCH »."
  echo "  Depuis une autre branche, ouvre une pull request : le tag se crée après la fusion."
  exit 1
fi

echo "==> synchronisation avec origin…"
git fetch --quiet --tags origin main
if [[ -n "$(git rev-list HEAD..origin/main)" ]]; then
  echo "erreur : main local est en retard sur origin/main."
  echo "  lance : git pull --ff-only"
  exit 1
fi

# --- tag --------------------------------------------------------------------

LAST=$(git tag -l 'v[0-9]*' --sort=-v:refname | head -1)
if [[ "$TAG" == "next" ]]; then
  if ! [[ "$LAST" =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
    echo "erreur : dernier tag illisible (« $LAST ») — passe un tag explicite"; exit 1
  fi
  TAG="v${BASH_REMATCH[1]}.${BASH_REMATCH[2]}.$((BASH_REMATCH[3] + 1))"
fi

if ! [[ "$TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "erreur : le tag doit être « next » ou de la forme vX.Y.Z (reçu : $TAG)"; exit 1
fi
if git rev-parse -q --verify "refs/tags/$TAG" >/dev/null; then
  echo "erreur : le tag $TAG existe déjà (dernier tag : $LAST) — utilise « next »"; exit 1
fi

[[ -z "$MESSAGE" ]] && MESSAGE="Release $TAG"
# La dérogation est tracée dans le message de commit : la CI la lit pour ne pas échouer.
MESSAGE="$MESSAGE$MARKERS"

# --- ajout ciblé ------------------------------------------------------------

if [[ ${#PATHS[@]} -gt 0 ]]; then
  git add -- "${PATHS[@]}"
else
  git add -u
fi

LEFT=$(git ls-files --others --exclude-standard --directory | sed 's/^/    /')
if [[ -n "$LEFT" ]]; then
  echo "==> non suivis, laissés de côté (passe leur chemin en argument pour les publier) :"
  echo "$LEFT"
fi

# --- contrôle bloquant ------------------------------------------------------

echo
if ! python3 check_assets.py ${CHECK_FLAGS[@]+"${CHECK_FLAGS[@]}"}; then
  echo
  echo "Publication annulée. Rien n'a été commité ; pour désindexer : git restore --staged ."
  exit 1
fi

# --- confirmation -----------------------------------------------------------

echo
echo "==> tag     : $TAG  (précédent : $LAST)"
echo "==> message : $MESSAGE"
echo "==> contenu :"
git diff --cached --stat | sed 's/^/    /'
echo

if [[ $YES -ne 1 ]]; then
  if [[ ! -t 0 ]]; then
    echo "Pas de clavier pour confirmer : relis la liste ci-dessus puis relance avec --yes."
    echo "(les fichiers restent indexés ; pour désindexer : git restore --staged .)"
    exit 1
  fi
  read -r -p "Publier ? [y/N] " confirm
  if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "annulé. (pour désindexer : git restore --staged .)"; exit 0
  fi
fi

# --- commit + tag, poussés ensemble -----------------------------------------

NEW_FILES=$(git diff --cached --name-only --diff-filter=AM)

if git diff --cached --quiet; then
  echo "==> rien à commiter (tag seul)"
else
  git commit -q -m "$MESSAGE"
fi
git tag -a "$TAG" -m "$MESSAGE"
# --atomic : la branche et le tag passent ensemble ou pas du tout.
git push --atomic origin main "$TAG"

# --- vérification jsDelivr --------------------------------------------------

BASE="https://cdn.jsdelivr.net/gh/$REPO@$TAG"
echo
echo "==> publié : $TAG"
echo "==> base   : $BASE/"

KO=0
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  code=$(curl -s -o /dev/null -w '%{http_code}' "$BASE/$f" || echo "000")
  if [[ "$code" != "200" ]]; then
    # 404 mis en cache avant propagation du tag, ou 403 de taille : purge puis 2e essai
    curl -s -o /dev/null "https://purge.jsdelivr.net/gh/$REPO@$TAG/$f" || true
    sleep 3
    code=$(curl -s -o /dev/null -w '%{http_code}' "$BASE/$f" || echo "000")
  fi
  if [[ "$code" == "200" ]]; then
    echo "    200  $f"
  else
    echo "    $code  $f   ← PAS SERVI"
    KO=1
  fi
done <<< "$NEW_FILES"

if [[ $KO -ne 0 ]]; then
  echo
  echo "⚠ Certains fichiers ne sont pas servis par jsDelivr. Ne pas envoyer d'email"
  echo "  qui les référence avant d'avoir un 200 (réessayer dans quelques minutes)."
  exit 2
fi
