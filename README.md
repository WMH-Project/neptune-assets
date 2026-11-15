# neptune-assets

CDN versionné pour les assets graphiques de **Mission Neptune / Neptune Forum** — photos, logos, fonts — servis par `cdn.mission-neptune.com`.

Mission Neptune est une initiative mondiale lancée à l'UNOC, sous le haut patronage du Président de la République française et en lien avec le Pacte européen pour l'Océan. Le **Neptune Forum — Les rêves du vivant** se tient du **6 au 8 juin 2026** au Muséum national d'Histoire naturelle, Jardin des Plantes, Paris.

Site officiel : [forum.mission-neptune.com](https://forum.mission-neptune.com)

## Usage

Les visuels sont servis par **`https://cdn.mission-neptune.com/<chemin>`**, un site Netlify qui
publie la branche `main` de ce dépôt (dossiers `photos/`, `logos/`, `graphics/`, `posters/`,
`reports/`), sans numéro de version :

```
https://cdn.mission-neptune.com/logos/mission-neptune/mission-neptune-white.png
https://cdn.mission-neptune.com/photos/newsletter/november-2026/x-pavilion-video.jpg
```

Jusqu'en novembre 2026 les visuels étaient servis par jsDelivr à un tag git
(`cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@vX.Y.Z/...`). Les emails déjà envoyés
gardent ces adresses : les tags existants ne doivent jamais être supprimés. Plus rien de
nouveau ne doit pointer jsDelivr (l'arbre dépasse sa limite de 50 Mo par tag).

Procédure et règles : [`CLAUDE.md`](CLAUDE.md).

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

1. **≤ 250 Ko par image**, noms en minuscules sans espace. `check_assets.py` le vérifie,
   en local et sur chaque pull request.
2. **Un fichier publié ne se modifie pas et ne se supprime pas** : une correction se
   publie sous un nouveau nom.
3. **N'ajouter que ses propres fichiers** (`git add <chemin>`), le dépôt est public.
4. Publication : pull request, ou `./push.sh next "message" <chemins>` pour le mainteneur.

## Licences

**All Rights Reserved** — voir [`LICENSE`](LICENSE).

- **Logos partenaires** : propriété de leurs détenteurs respectifs, utilisés avec autorisation dans le cadre exclusif de la communication Neptune Forum 2026.
- **Photographies** : crédits obligatoires dans tout support utilisant ces visuels (voir [`docs/CREDITS.md`](docs/CREDITS.md)).
- **Logos Mission Neptune et MNHN** : usage réservé à la communication officielle de l'événement.

Toute réutilisation hors du périmètre Mission Neptune / WMH Project nécessite une autorisation écrite.

## Contact

WMH Project — pôle Digital
team@mission-neptune.com
