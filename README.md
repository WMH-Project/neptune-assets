# neptune-assets

CDN versionné pour les assets graphiques de **Mission Neptune / Neptune Forum** — photos, logos, fonts — servis via [jsDelivr](https://www.jsdelivr.com/).

Mission Neptune est une initiative mondiale lancée à l'UNOC, sous le haut patronage du Président de la République française et en lien avec le Pacte européen pour l'Océan. Le **Neptune Forum — Les rêves du vivant** se tient du **6 au 8 juin 2026** au Muséum national d'Histoire naturelle, Jardin des Plantes, Paris.

Site officiel : [forum.mission-neptune.com](https://forum.mission-neptune.com)

## Usage

Les assets sont accessibles via jsDelivr à l'URL suivante, avec un tag de version obligatoire :

```
https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@<TAG>/<path>
```

**Exemple** :

```
https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.0.0/photos/save-the-date/clownfish-600.jpg
https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.0.0/logos/mission-neptune/mission-neptune-white.png
```

> ⚠️ **Ne jamais utiliser `@main`** en production (cache jsDelivr imprévisible de ~12h). Toujours référencer un tag versionné pour bénéficier du cache immuable.

Liste complète des URLs dans [`ASSETS.md`](ASSETS.md).

## Structure

```
neptune-assets/
├── logos/
│   ├── mission-neptune/        # Logos Mission Neptune (white, blue, vectorized)
│   ├── mnhn/                   # Logo Muséum national d'Histoire naturelle (partenaire hôte)
│   ├── fon/                    # Logos Focused on Nature (SVG black/white/color)
│   └── partners/
│       ├── founding/           # Founding Partners (8)
│       ├── institutional/      # Institutional Partners (3)
│       ├── knowledge/          # Knowledge Partners (17)
│       └── global-ocean/       # Global Ocean Partners (6)
├── photos/
│   └── save-the-date/          # Photos campagne Save the Date (faune marine)
│       ├── clownfish.jpg       (1200px, ~119 Ko, pleine rés.)
│       ├── clownfish-600.jpg   (600px, ~42 Ko, version email)
│       ├── tortue.jpg / -600.jpg
│       ├── dauphin.jpg / -600.jpg
│       └── algue.jpg   / -600.jpg
└── docs/
    ├── palette.md              # Palette Neptune (hex codes)
    └── CREDITS.md              # Crédits photos & logos (à compléter)
```

## Partenaires (34)

| Catégorie | Nombre |
|---|---|
| Founding | 8 |
| Institutional | 3 |
| Knowledge | 17 |
| Global Ocean | 6 |

Référentiel détaillé (statuts, URLs, contacts) : `../partners/neptune-forum-partners.xlsx` (hors repo, privé WMH).

## Règles de publication

1. **Toujours optimiser avant commit** : photos ≤ 250 Ko, JPG progressif. Version `-600.jpg` obligatoire pour tout visuel utilisé en email (largeur max 600 px).
2. **Tagger chaque release** : utiliser `./push.sh v1.x.y` (wrapper git add/commit/push/tag).
3. **Incrémenter la version** à chaque modification d'un asset déjà référencé dans un template en production.
4. **Ne jamais supprimer** un asset déjà publié dans un template en production — créer une nouvelle version.
5. **Pas de fichiers > 1 Mo** — utiliser un vrai CDN (Cloudflare R2) pour les gros fichiers.

## Versioning

- `v1.x.y` : campagne **Save the Date** (phase actuelle)
- `v2.x.y` : campagne **Invitations officielles + Agenda**
- `v3.x.y` : phase **Live event + Post-event**

## Licences

**All Rights Reserved** — voir [`LICENSE`](LICENSE).

- **Logos partenaires** : propriété de leurs détenteurs respectifs, utilisés avec autorisation dans le cadre exclusif de la communication Neptune Forum 2026.
- **Photographies** : crédits obligatoires dans tout support utilisant ces visuels (voir [`docs/CREDITS.md`](docs/CREDITS.md)).
- **Logos Mission Neptune et MNHN** : usage réservé à la communication officielle de l'événement.

Toute réutilisation hors du périmètre Mission Neptune / WMH Project nécessite une autorisation écrite.

## Contact

WMH Project — pôle Digital
team@mission-neptune.com
