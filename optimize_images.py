#!/usr/bin/env python3
"""Allège les images du dépôt pour rester sous la limite jsDelivr (50 Mo par tag).

Règle du README : photos ≤ 250 Ko, JPG progressif, aucun fichier > 1 Mo. Ce script
l'applique aux JPG du dépôt qui la dépassent :

  1. le côté long est ramené à MAX_SIDE px s'il est plus grand ;
  2. ré-encodage JPEG progressif, qualité 82 puis décroissante (plancher Q_MIN) jusqu'à
     passer sous TARGET octets ;
  3. si le plancher ne suffit pas, le côté long descend par paliers (2000, 1800, 1600).

Les dimensions d'origine ne sont réduites que pour les fichiers > MAX_SIDE : les ratios
sont conservés, les chemins ne changent pas, le site n'a rien à modifier (next/image
ré-encode de toute façon à la largeur d'affichage). Les originaux restent dans l'historique
git et dans les tags précédents, que jsDelivr continue de servir.

    python3 optimize_images.py            # dry-run : liste ce qui changerait
    python3 optimize_images.py --apply    # écrit les fichiers
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
TARGET = 300_000          # octets — un peu au-dessus des 250 Ko du README pour les héros du site
MAX_SIDE = 2400           # px
Q_START, Q_MIN = 82, 70
STEPS = (2000, 1800, 1600)
APPLY = "--apply" in sys.argv

# Exception documentée (mission-neptune-Brevo/CLAUDE.md §4) : fac-similé de presse consulté
# au clic, illisible si compressé davantage. On n'y touche pas.
EXCLUS = {"photos/newsletter/summer-wine/oped-liberation-full.jpg"}

# Photos affichées en héros plein écran par le site (src/ de mission-neptune-website au
# 09/10/2026) : budget plus large pour ne pas les dégrader. Les autres photos d'expéditions
# sont une bibliothèque de candidats, non affichées.
HEROS = {
    "photos/expeditions/2016-05gal-uu8a8818-rec.jpg",
    "photos/expeditions/2017-05phi-j11a7756-2-forum.jpg",
    "photos/expeditions/2017-05phi-j11a9194-2-reveler-inconnu.jpg",
    "photos/expeditions/2019-04bah-6l1a6227-v4-rgb-hr-2-reves-ocean.jpg",
    "photos/expeditions/2021-07dom-80a5330-shl-v3-2.jpg",
    "photos/expeditions/2023-03raj-71a9984-shl-ok-2.jpg",
    "photos/expeditions/2023-11egy-0r8a7270-2.jpg",
    "photos/expeditions/2024-07egy-dive18-0r8a2667-2.jpg",
    "photos/expeditions/2025-08azor-day5-ex7a8618-rec-2.jpg",
    "photos/expeditions/2025-09pol-moor-day02-x7a0693-rec.jpg",
    "photos/expeditions/2025-09pol-moor-day04-x7a4646-rec.jpg",
    "photos/save-the-date/_full/clownfish.jpg",
}
HERO_TARGET, HERO_STEPS = 450_000, (2000,)


def encode(im, q):
    from io import BytesIO
    b = BytesIO()
    im.save(b, "JPEG", quality=q, optimize=True, progressive=True)
    return b.getvalue()


def shrink(path, target=TARGET, steps=STEPS):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    w0, h0 = im.size
    sides = [MAX_SIDE] + [s for s in steps if s < max(w0, h0)]
    for side in sides:
        cur = im
        if max(im.size) > side:
            r = side / max(im.size)
            cur = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        q = Q_START
        data = encode(cur, q)
        while len(data) > target and q > Q_MIN:
            q -= 3
            data = encode(cur, q)
        if len(data) <= target:
            return data, cur.size, q
    return data, cur.size, q        # au pire : plus petit palier, qualité plancher


avant = apres = 0
rows = []
for p in sorted(ROOT.rglob("*.jp*g")):
    if ".git" in p.parts:
        continue
    size = p.stat().st_size
    rel = p.relative_to(ROOT).as_posix()
    if size <= 250_000 or rel in EXCLUS:
        continue
    data, dims, q = shrink(p, HERO_TARGET, HERO_STEPS) if rel in HEROS else shrink(p)
    avant += size
    apres += len(data)
    rows.append((size, len(data), dims, q, p.relative_to(ROOT)))
    if APPLY:
        p.write_bytes(data)

for s, n, (w, h), q, rel in rows:
    print(f"{s/1024:7.0f} -> {n/1024:5.0f} Ko  {w}x{h}  q{q}  {rel}")
print(f"\n{len(rows)} JPG {'réécrits' if APPLY else 'concernés (dry-run)'} : "
      f"{avant/1048576:.1f} Mo -> {apres/1048576:.1f} Mo")
