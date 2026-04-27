# Changelog

Tous les changements notables de ce repo sont documentés ici. Format inspiré de [Keep a Changelog](https://keepachangelog.com/), versioning [SemVer](https://semver.org/).

## [v1.0.10] — 2026-04-27

### Ajouts

- `graphics/bathymetric/bathymetric-corner.png` — cluster bas-gauche avec petite boucle fermée centrale, 50% top-right vide (102 Ko, 841×595).
- `graphics/bathymetric/bathymetric-dense.png` — carte topographique dense, layered, boucle concentrique top-left (117 Ko, 841×595).
- `graphics/bathymetric/bathymetric-basin.png` — grande dépression centrale entourée de contours sparse (84 Ko, 841×595).

> Source : Mission Neptune Final Guidelines April 2026, section « Graphical Elements » p.43. Trois compositions topographiques signature à appliquer uniquement sur fonds unis ou blancs (jamais sur photo). Lignes natives `#F8F8F8` — recoloration côté consommateur via `mask-image` CSS (blanc sur IKB/Gold, terracotta `#C29F80` sur Seafoam, IKB sur blanc).

## [v1.0.9] — 2026-04-25

### Ajouts

- `photos/expeditions/` — 40 photos sous-marines curatées issues des expéditions Focused on Nature 2014-2025. Couverture 18 lieux (Açores, Bahamas, Brésil, Costa Rica, Dominique, Égypte, Galápagos, Indonésie, Maldives, Mexique, Moorea, Philippines, Polynésie française, Raja Ampat, Sardaigne, Tahiti, Tonga, Imatra). Toutes en 2000×1333 minimum, 1-9 Mo par fichier, total 109 Mo.
- `photos/expeditions/CREDITS.md` — crédit unique applicable à tous les fichiers du dossier : © Prince Hussain Aga Khan / Focused on Nature.

> Sélection issue d'une bibliothèque source de 232 photos (416 Mo) hébergée sur SharePoint WMH. Pour ajouter d'autres photos en v1.0.10+, copier depuis `04_Assets/Photos/JPG` (OneDrive) avec lowercase + tirets URL-safe.

## [v1.0.8] — 2026-04-25

### Ajouts

- `photos/save-the-date/_full/algue.jpg` — version HD (2000×1333, 3.1 Mo)
- `photos/save-the-date/_full/clownfish.jpg` — version HD (2000×1334, 1.2 Mo)
- `photos/save-the-date/_full/dauphin.jpg` — version HD (2000×1333, 1.8 Mo)
- `photos/save-the-date/_full/tortue.jpg` — version HD (2000×1333, 1.2 Mo)

> Versions originales haute résolution des photos save-the-date, jusque-là conservées dans le repo privé `neptune-landing/assets/photos`. À utiliser pour les hero plein écran et tout fond `100vw` du site mission-neptune.com — les versions racine (1200×800) restent recommandées pour l'email et les vignettes (~120 Ko vs 1-3 Mo).

## [v1.0.7] — 2026-04-21

### Ajouts

- `logos/mission-neptune/mission-neptune-klein-blue.png` — wordmark Mission Neptune en Klein Blue (tight crop, 927×226)
- `logos/mission-neptune/mission-neptune-white-on-klein-blue.png` — wordmark blanc sur fond Klein Blue (1920×362)
- `logos/mission-neptune/mission-neptune-white-tight.png` — wordmark blanc (tight crop, 927×226)

> Nouvelle déclinaison Klein Blue de la charte Mission Neptune. Les versions existantes (`mission-neptune-blue.png`, `mission-neptune-white.png`) restent disponibles.

## [v1.0.6] — 2026-04-16

### Retraits

- `logos/partners/knowledge/avatar-alliance-foundation.jpg` — remplacé par la version PNG sur fond transparent `avatar-alliance-foundation-black.png` (ajoutée en v1.0.3)
- `logos/partners/global-ocean/high-seas-alliance.png` — partenaire retiré du Save the Date
- `logos/partners/global-ocean/deep-sea-conservation-coalition.jpg` — partenaire retiré du Save the Date

> Les URLs pinned sur `@v1.0.2` (templates emailing archivés) restent servies par jsDelivr depuis la version taggée et ne sont pas impactées.

## [v1.0.0] — 2026-04-10

Release initiale pour la campagne **Save the Date** du Neptune Forum 2026.

### Ajouts

- **Logos Mission Neptune** : versions `blue`, `white`, `vectorized` (PNG)
- **Logo Muséum national d'Histoire naturelle** : sceau `black` et `white` (PNG)
- **Logos Focused on Nature** : SVG multi-versions `black`, `white`, `color`
- **Logos partenaires (33)** :
  - Founding (8) : Ifremer, Institut océanographique de Monaco, Minderoo Foundation, University of Khorfakkan, VOTO, OceanX, Tsao Pao Chee Group, Focused on Nature
  - Institutional (3) : Gouvernement français, Commission européenne, UNESCO
  - Knowledge (17) : Avatar Alliance Foundation, CNRS, Monaco Explorations, GOOS, INPO, IRD, Invemar, CNR ISMAR, Jaywun, Mercator Ocean International, MBARI, NIOZ, NOC, Scripps, Sorbonne Université, Tara Océan Foundation, WHOI
  - Global Ocean (6) : DSCC, Institut Jacques Delors, High Seas Alliance, Mission Blue, Oceano Azul Foundation, Ocean & Climate Platform
- **Photos Save the Date** : 4 visuels faune marine (tortue, dauphin, clownfish, algue) en pleine résolution (~1200px) + version email 600px
- **Palette chromatique** Neptune (`docs/palette.md`)

### Infrastructure

- Repo public GitHub `WMH-Project/neptune-assets` servi via jsDelivr CDN
- Script `push.sh` pour workflow de publication versionnée
- Mapping complet des URLs jsDelivr dans `ASSETS.md`
