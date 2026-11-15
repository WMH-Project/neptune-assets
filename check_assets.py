#!/usr/bin/env python3
"""Contrôle de ce qui va être publié sur le CDN, avant commit ou en CI.

    python3 check_assets.py                 # ce qui est indexé (git add) contre le dernier tag
    python3 check_assets.py --target HEAD   # le commit courant contre le dernier tag (CI)
    python3 check_assets.py --base <ref>    # autre point de comparaison

Bibliothèque standard seulement : tourne tel quel en CI et en session cloud.
Code de sortie 0 = publiable, 1 = au moins une erreur.

Ce qui est vérifié :
  1. poids total de l'arbre publié — jsDelivr refuse les fichiers neufs d'un tag
     dont l'arbre dépasse 50 Mo (403 « Package size exceeded ») ;
  2. poids de chaque fichier AJOUTÉ ou MODIFIÉ depuis la base (les fichiers
     historiques trop lourds sont tolérés tant qu'on n'y touche pas) ;
  3. emplacement, extension et nom des fichiers ajoutés ;
  4. aucune suppression, aucun renommage, aucune modification d'un visuel publié :
     le site et les emails déjà envoyés pointent ces chemins, et le CDN
     (cdn.mission-neptune.com) les sert sans numéro de version, en cache d'un jour.
     Une correction se publie sous un nouveau nom (hero-2.jpg), sauf dérogation
     du mainteneur (push.sh --allow-modify / --allow-delete).
"""
import argparse
import re
import subprocess
import sys

# --- Règles -------------------------------------------------------------------

# jsDelivr annonce « 50 MB » sans préciser l'unité : on se cale sur la lecture
# la plus stricte (50 000 000 octets) et on bloque 1 Mo avant.
TOTAL_BLOCK = 49_000_000
TOTAL_WARN = 48_000_000

FILE_MAX = 250 * 1024  # règle du dépôt : 250 Ko par image

# Dépassements assumés, à justifier ici même.
EXCEPTIONS = {
    # fac-similé de presse consulté au clic, illisible si compressé davantage
    "photos/newsletter/summer-wine/oped-liberation-full.jpg",
}

MEDIA_DIRS = {"photos", "logos", "graphics", "posters", "reports"}
MEDIA_EXT = {"jpg", "jpeg", "png", "webp", "svg", "gif", "avif"}
OTHER_DIRS = {"docs", "email-signatures", "word", ".github"}
ROOT_FILES = {
    ".gitignore", "ASSETS.md", "CHANGELOG.md", "CLAUDE.md", "LICENSE", "README.md",
    "check_assets.py", "netlify.toml", "optimize_images.py", "push.sh", "requirements.txt",
}
# Ne doivent jamais partir sur un dépôt public, où qu'ils soient.
FORBIDDEN_EXT = {
    "sql", "eml", "env", "key", "pem", "xlsx", "xls", "csv",
    "heic", "tif", "tiff", "psd", "zip", "mp4", "mov", "pdf",
}
MEDIA_NAME = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def ko(n):
    return f"{n / 1024:.0f} Ko"


def mo(n):
    return f"{n / 1_000_000:.2f} Mo"


def tree_sizes(treeish):
    """{chemin: taille en octets} pour tous les fichiers d'un arbre git."""
    sizes = {}
    for entry in git("ls-tree", "-r", "-l", "-z", treeish).split("\0"):
        if not entry:
            continue
        meta, path = entry.split("\t", 1)
        size = meta.split()[3]
        sizes[path] = int(size) if size != "-" else 0  # « - » = sous-module
    return sizes


def changes(base, target):
    """[(statut, chemin)] entre deux arbres, sans détection de renommage."""
    out = git("diff", "--no-renames", "--name-status", "-z", base, target).split("\0")
    return [(out[i], out[i + 1]) for i in range(0, len(out) - 1, 2)]


def check_added(path, errors):
    parts = path.split("/")
    name = parts[-1]
    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""

    if ".claude" in parts:
        errors.append(f"{path} : configuration locale de Claude, à ne pas publier")
        return
    if ext in FORBIDDEN_EXT or name.startswith(".env"):
        errors.append(f"{path} : type de fichier interdit sur ce dépôt public (.{ext or name})")
        return
    if len(parts) == 1:
        if name not in ROOT_FILES:
            errors.append(f"{path} : rien de nouveau à la racine — range-le dans un dossier")
        return
    top = parts[0]
    if top in OTHER_DIRS:
        return
    if top not in MEDIA_DIRS:
        errors.append(
            f"{path} : dossier « {top}/ » inconnu. Les visuels d'une newsletter vont "
            "dans photos/newsletter/<campagne>/"
        )
        return
    if name.endswith(".md"):  # crédits, notes
        return
    if ext not in MEDIA_EXT:
        errors.append(
            f"{path} : extension .{ext} non servie ici ({', '.join(sorted(MEDIA_EXT))})"
        )
    if not MEDIA_NAME.match(name):
        errors.append(
            f"{path} : nom de fichier en minuscules, sans espace ni accent "
            "(lettres, chiffres, tiret, point)"
        )


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--base", help="point de comparaison (défaut : dernier tag)")
    ap.add_argument("--target", help="arbre à contrôler (défaut : l'index, ce qui est « git add »)")
    ap.add_argument("--allow-delete", action="store_true",
                    help="tolérer suppressions et renommages (à réserver au mainteneur)")
    ap.add_argument("--allow-modify", action="store_true",
                    help="tolérer la modification d'un visuel publié (à réserver au mainteneur)")
    args = ap.parse_args()

    base = args.base or git("describe", "--tags", "--abbrev=0").strip()
    if args.target:
        target, label = args.target, args.target
    else:
        target, label = git("write-tree").strip(), "index (fichiers ajoutés par git add)"

    errors, warnings = [], []
    sizes = tree_sizes(target)
    total = sum(sizes.values())
    diff = changes(base, target)

    added = [p for s, p in diff if s == "A"]
    modified = [p for s, p in diff if s == "M"]
    deleted = [p for s, p in diff if s == "D"]

    for path in added:
        check_added(path, errors)
    for path in added + modified:
        size = sizes.get(path, 0)
        if size > FILE_MAX and path not in EXCEPTIONS and path.split("/")[0] in MEDIA_DIRS:
            errors.append(
                f"{path} : {ko(size)}, la limite est {ko(FILE_MAX)} — "
                "réduis ou recompresse l'image avant de publier"
            )
    for path in modified:
        if path.split("/")[0] in MEDIA_DIRS and not path.endswith(".md"):
            msg = (f"{path} : visuel déjà publié, modifié — publie la correction sous un "
                   "nouveau nom et pointe l'email dessus")
            (warnings if args.allow_modify else errors).append(msg)
    for path in deleted:
        msg = f"{path} : supprimé ou renommé — un chemin publié ne doit pas disparaître"
        (warnings if args.allow_delete else errors).append(msg)

    if total > TOTAL_BLOCK:
        errors.append(
            f"arbre de {mo(total)} : au-delà de {mo(TOTAL_BLOCK)}, jsDelivr refusera les "
            "nouveaux fichiers de ce tag (limite 50 Mo). Il faut alléger le dépôt d'abord."
        )
    elif total > TOTAL_WARN:
        warnings.append(f"arbre de {mo(total)} : il reste {mo(TOTAL_BLOCK - total)} avant blocage")

    delta = total - sum(tree_sizes(base).values())
    print(f"Contrôle : {label}  ←  base {base}")
    print(f"  fichiers : {len(added)} ajouté(s), {len(modified)} modifié(s), {len(deleted)} supprimé(s)")
    print(f"  arbre    : {mo(total)} ({delta / 1000:+.0f} Ko), "
          f"marge avant blocage {mo(TOTAL_BLOCK - total)}")
    for w in warnings:
        print(f"  ⚠ {w}")
    for e in errors:
        print(f"  ✗ {e}")
    if errors:
        print(f"\n✗ {len(errors)} erreur(s) — rien ne doit être publié en l'état.")
        return 1
    print("✓ publiable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
