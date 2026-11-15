# neptune-assets — visuels de Mission Neptune

Ce dépôt contient les images du site mission-neptune.com et des newsletters. Tout ce qui
est fusionné sur `main` est en ligne une à deux minutes plus tard sur
**`https://cdn.mission-neptune.com/<chemin du fichier>`** (site Netlify `neptune-assets-cdn`).
Le dépôt est **public**. Réponds en français.

## Ce qu'on fait ici

Presque toujours une seule chose : **ajouter les images d'une newsletter ou d'une page**.

1. Les images arrivent déjà préparées (≤ 250 Ko, noms en minuscules) depuis le dépôt
   `mission-neptune-Brevo` : `python3 build/newsletter.py images <dossier>`.
2. Les copier dans `photos/newsletter/<campagne>/` (ex. `photos/newsletter/december-2026/`).
   Portraits de profils speakers : `photos/speakers/<slug>.jpg`.
3. Vérifier : `python3 check_assets.py` après `git add <le dossier>`.
4. Ouvrir une **pull request**. Le contrôle « Contrôle des assets » doit être vert.
   Netlify ajoute une URL d'aperçu où regarder les images.
5. Après fusion, l'adresse d'une image est
   `https://cdn.mission-neptune.com/photos/newsletter/<campagne>/<fichier>`.

## Règles

- **N'ajouter que ses propres fichiers** : `git add <chemin précis>`, jamais `git add -A` ni
  `git add .`. Tout fichier oublié dans le dossier partirait sur un dépôt public.
- **Un fichier publié ne se modifie pas, ne se renomme pas, ne se supprime pas.** Le site et
  les emails déjà envoyés pointent son adresse. Une correction se publie sous un nouveau
  nom (`hero-2.jpg`) et on change le lien dans l'email. `check_assets.py` refuse le reste.
- **≤ 250 Ko par image**, extensions `jpg png webp svg gif avif`, noms en minuscules sans
  espace ni accent. PDF seulement dans `reports/`.
- **Jamais ici** : fichiers de contacts, exports, `.sql`, `.eml`, `.env`, originaux lourds,
  captures de conversations. Le dépôt est public.
- Ne pas toucher à `netlify.toml`, `.github/`, `check_assets.py`, `push.sh`,
  `email-signatures/`, `word/`, ni aux dossiers `logos/`, `graphics/`, `posters/` sans
  demande explicite du mainteneur (Gilles).
- Ne plus rien pointer vers `cdn.jsdelivr.net` : c'est l'ancien hébergement. Les tags git
  `v1.x.y` existants servent encore les emails déjà envoyés — **ne jamais supprimer un tag**.

## Si le contrôle refuse

Le message dit quoi corriger. Les cas courants : image trop lourde (la réduire avec
`newsletter.py images --largeur 1000`), nom avec majuscule ou espace, fichier rangé hors de
`photos/newsletter/<campagne>/`. Ne jamais contourner le contrôle : les options
`--allow-modify` et `--allow-delete` sont réservées au mainteneur.

## Pour le mainteneur

`./push.sh next "message" <chemins>` publie directement depuis `main` (contrôle, commit,
tag, vérification du CDN). Après une fusion de PR, `.github/workflows/release.yml` pose le
tag suivant et vérifie que le CDN sert les nouveaux fichiers.
