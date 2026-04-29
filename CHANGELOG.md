# Changelog

Tous les changements notables de ce repo sont documentés ici. Format inspiré de [Keep a Changelog](https://keepachangelog.com/), versioning [SemVer](https://semver.org/).

## [v1.0.16] — 2026-04-29

### Ajouts

- `photos/expeditions/2021-08dom-80a0965-mike-v3-2.jpg` — cachalot escorté en surface, Dominique 2021-08, série DOM_80A0965 (« Mike »), 2000×1334 paysage (~1265 Ko). Crédit © Prince Hussain Aga Khan / Focused on Nature. Fournit l'arrière-plan plein-écran du hero `/the-forum` (paysage pleine largeur en remplacement de l'affiche). Le chemin est déjà référencé en production depuis le commit recette FBB du 2026-04-29 — cette release fournit le binaire manquant.

> Source : OneDrive WMH `04_Assets/Photos/JPG/2021-08DOM_80A0965_MIKE_V3 OK-2.jpg`. Renommé en kebab-case selon la convention du repo (lowercase, dashes, suffixe `-2` conservé pour la version retouchée).

## [v1.0.15] — 2026-04-28

### Ajouts

- `photos/initiatives/neptune-expeditions.jpg` — méduse rouge profonde sur fond noir avec lignes topologie (1410 Ko, portrait). Carte 01/04 du bloc « Quatre activités fondatrices » côté site mission-neptune.com → Neptune Expeditions.
- `photos/initiatives/neptune-fellows.jpg` — requin océanique escorté de poissons-pilote sur bleu vif, lignes topologie ambrées (1080 Ko, portrait). Carte 02/04 → Neptune Fellows.
- `photos/initiatives/neptune-forum.jpg` — silhouette de dauphin sous une trame topologique sur bleu clair (937 Ko, portrait). Carte 03/04 → Neptune Forum.
- `photos/initiatives/neptune-explorers-galleries.jpg` — duo de requins remora sur fond très sombre, lignes topologie iridescentes (947 Ko, portrait). Carte 04/04 → Neptune Explorers Galleries.

> Source : OneDrive WMH `_STD_WORK/Brand/Mission Neptune_4Initiatives-0X.jpg`. Layout éditorial signature de la marque (image4.jpeg du brief FBB) — chaque photo embarque déjà les lignes topologie + une zone négative top-left pour accueillir le numéro et le titre.

## [v1.0.14] — 2026-04-28

### Ajouts

- `photos/venues/neptune-dome.jpg` — photo du Dôme Neptune monté sur le parvis du Jardin des Plantes devant la Grande Galerie de l'Évolution (1600×873, ~202 Ko, source Mission Neptune avril 2026). Utilisée sur le bloc « Ocean Dreams – Stories of Hope » de la programmation publique.
- `photos/venues/verniquet.webp` — photo de l'amphithéâtre Verniquet en configuration colloque (676×450, ~38 Ko). Récupérée depuis `public/venues/` du site mission-neptune-website pour mutualisation. Utilisée sur le bloc « Cinéma des Explorateurs ».
- `photos/venues/grande-galerie.webp` — photo de la nef centrale de la Grande Galerie de l'Évolution avec la procession des animaux (599×275, ~284 Ko). Récupérée depuis `public/venues/` du site. Utilisée sur le bloc « Les Botos, esprits de l'Amazone ».

> Source : photos institutionnelles MNHN + photo terrain Mission Neptune. Les versions servies localement par mission-neptune-website peuvent désormais être remplacées par les URLs jsDelivr correspondantes.

## [v1.0.13] — 2026-04-28

### Ajouts

- `graphics/bathymetric/bathymetric-cluster.png` — variante haute résolution du cluster topographique central (3508×2480, ~2,4 Mo). Lignes en gris clair (~RGB 170/172/175) sur fond transparent — exploitable directement comme `<img>` à faible opacité, ou comme `mask-image` (alpha-only) pour une recoloration côté CSS. Remplace l'usage de `bathymetric-dense.png` (841×595) côté site mission-neptune.com pour les fonds de section plein-écran où la basse résolution se voyait pixelisée. Les autres fichiers `bathymetric-{corner,dense,basin}.png` restent en place pour les usages email/print et toute consommation pinned aux versions antérieures.

> Source : Final Guidelines April 2026 — section « Graphical Elements ». Lignes très fines : prévoir une opacité minimale de ~0.18 sur fond sombre (sinon invisible) et plafonnée à ~0.35 sur fond clair (sinon trop bruyant).

## [v1.0.12] — 2026-04-28

### Ajouts

- `logos/mission-neptune/mission-neptune-picto-white.png` — picto seul (3 vagues) en blanc sur fond transparent, 1080×1080. Fournit la marque sans wordmark pour les usages réduits (favicon, app-icon, social square). Servir composé sur fond foncé (recommandé : `#111F4A` surface-deep).
- `logos/mission-neptune-forum/mission-neptune-forum-rgb.png` — lockup officiel « Mission Neptune | Forum » en couleurs RGB, 2048×~1500 (extrait de `Mission Neptune_FORUM_Logo_RGB.ai`).
- `logos/mission-neptune-forum/mission-neptune-forum-bw.png` — même lockup en noir et blanc (extrait de `Mission Neptune_FORUM_Logo_Bnw_RGB.ai`).
- `posters/neptune-forum-2026.png` — affiche officielle Neptune Forum 2026 (« Les Rêves de l'Océan », du 6 au 8 juin 2026 au MNHN), 841×1190, ~1.2 Mo. Carries event lockup, dates, public schedule and partner row — utilisable tel quel comme vignette portrait sur la page Forum.

> Sources : OneDrive WMH `_STD_WORK/Brand/OPEN FILE/BRAND ELEMENTS/`. PNG dérivés des `.ai` originaux (à conserver côté Brand pour ré-exports vectoriels).

## [v1.0.11] — 2026-04-27

### Modifications

- `graphics/bathymetric/bathymetric-{corner,dense,basin}.png` — recomposed with a proper alpha channel (lines opaque, background transparent). The v1.0.10 export had alpha=255 everywhere which made the file unusable as a CSS `mask-image`. v1.0.11 fixes this so a single asset can be recolored downstream via `mask-image` + `background-color`. RGB stays at white (255,255,255) so luminance-mode fallback also works.

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
