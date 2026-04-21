# Changelog

Tous les changements notables de ce repo sont documentés ici. Format inspiré de [Keep a Changelog](https://keepachangelog.com/), versioning [SemVer](https://semver.org/).

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
