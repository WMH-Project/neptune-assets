# Email Signatures — Mission Neptune

Signatures HTML pour Outlook (Windows, Mac, Web), Apple Mail et Gmail.

10 signatures = 5 collaborateurs × 2 variantes :

- **Forum** (bleue) — version événementielle, met en avant le Neptune Forum 6-8 juin 2026.
- **Permanente** (blanche) — version institutionnelle pour le reste de l'année.

Toutes les images sont servies par jsDelivr depuis ce repo (cache immuable, sub-100 ms partout dans le monde).

## Fichiers

```
email-signatures/
├── README.md              # Ce fichier
├── generate.py            # Script générateur (à relancer après ajout/modif personne)
├── preview.html           # Aperçu local des 8 signatures (chemins images relatifs)
├── images/
│   ├── forum-panel-left.jpg          # Panneau bleu gauche Forum (185×192 display)
│   ├── permanente-logo-left.png      # Logo MISSION NEPTUNE Permanente (140×34)
│   ├── permanente-reef-right.jpg     # Photo récif + bouton VOIR LE FILM (320×192)
│   ├── icon-phone.png                # Picto téléphone (11×11)
│   ├── icon-email.png                # Picto email (12×12)
│   └── play-icon.png                 # Picto play "VOIR LE FILM" Forum (14×14)
├── forum/
│   ├── adiceam.htm
│   ├── begards.htm
│   ├── kisseleva.htm
│   ├── lepivain.htm
│   └── stojilkovic.htm
└── permanente/
    ├── adiceam.htm
    ├── begards.htm
    ├── kisseleva.htm
    ├── lepivain.htm
    └── stojilkovic.htm
```

## Installation Outlook Windows

1. Télécharger le fichier `.htm` correspondant (par exemple `forum/adiceam.htm`).
2. Ouvrir le dossier `%APPDATA%\Microsoft\Signatures\` (taper ça dans la barre d'adresse de l'Explorateur).
3. Coller le fichier dans ce dossier en le renommant — par exemple `Neptune-Forum.htm`. Le nom du fichier devient le nom de la signature dans Outlook.
4. Dans Outlook : **Fichier → Options → Courrier → Signatures…** — votre nouvelle signature apparaît. L'affecter par défaut aux nouveaux messages et/ou aux réponses.

> Note : aucune image n'est stockée localement, tout est appelé depuis le CDN jsDelivr. Si le destinataire bloque les images distantes (rare mais possible en entreprise), il verra quand même les noms / fonctions / coordonnées en texte HTML.

## Installation Outlook Mac / Apple Mail

- **Outlook Mac** : Outlook → Préférences → Signatures → cliquer « + » → coller le contenu HTML.
- **Apple Mail** : Mail → Réglages → Signatures → glisser-déposer le `.htm` ou ouvrir le fichier dans un navigateur, sélectionner tout (⌘A), copier (⌘C), coller dans le champ signature.

## Installation Outlook Web (OWA)

1. Ouvrir le `.htm` dans un navigateur.
2. Sélectionner tout le contenu de la signature (⌘A / Ctrl+A).
3. Copier (⌘C / Ctrl+C).
4. Dans OWA : Paramètres → Courrier → Composer et répondre → coller dans le bloc « Signature ».

## URLs CDN

Toutes les URLs ci-dessous référencent le tag `v1.2.0`. Ne jamais utiliser `@main` en production (cf. règle repo).

### Signatures HTML (téléchargement direct)

| Collaborateur | Forum | Permanente |
|---|---|---|
| Ashok Adicéam | [forum/adiceam.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/forum/adiceam.htm) | [permanente/adiceam.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/permanente/adiceam.htm) |
| Jade Bégards | [forum/begards.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/forum/begards.htm) | [permanente/begards.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/permanente/begards.htm) |
| Daria Kisseleva | [forum/kisseleva.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/forum/kisseleva.htm) | [permanente/kisseleva.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/permanente/kisseleva.htm) |
| Anne-Sophie Le Pivain | [forum/lepivain.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/forum/lepivain.htm) | [permanente/lepivain.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/permanente/lepivain.htm) |
| Teodora Stojilkovic | [forum/stojilkovic.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/forum/stojilkovic.htm) | [permanente/stojilkovic.htm](https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/permanente/stojilkovic.htm) |

### Images (référencées automatiquement par les signatures)

- `https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/images/forum-panel-left.jpg`
- `https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/images/permanente-logo-left.png`
- `https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/images/permanente-reef-right.jpg`
- `https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/images/icon-phone.png`
- `https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/images/icon-email.png`
- `https://cdn.jsdelivr.net/gh/WMH-Project/neptune-assets@v1.2.0/email-signatures/images/play-icon.png`

## Liens présents dans les signatures

| Élément cliquable | Destination |
|---|---|
| Panneau-image gauche Forum | https://mission-neptune.com/fr/the-forum |
| Bloc « NEPTUNE FORUM » | https://mission-neptune.com/fr/the-forum |
| Bouton « VOIR LE FILM » (Forum + Permanente) | https://mission-neptune.com/fr/the-mission |
| Logo MISSION NEPTUNE (Permanente) | https://mission-neptune.com |
| www.mission-neptune.com | https://mission-neptune.com |
| Téléphone | `tel:+33XXXXXXXXX` (compose le numéro) |
| Email | `mailto:prenom.nom@mission-neptune.com` |

## Modifier une signature ou en ajouter une nouvelle

1. Éditer la liste `PEOPLE` dans `generate.py`.
2. Relancer `python3 generate.py [tag]` (le tag par défaut est `v1.1.0`).
3. Commit + tag avec `./push.sh v1.x.y` (incrément en mineure si nouvelle personne, en patch si simple correction).
4. Diffuser le nouveau lien CDN aux collaborateurs.

## Contraintes techniques Outlook Windows

Les fichiers `.htm` sont rendus par le moteur Word d'Outlook, qui ne supporte qu'un sous-ensemble très limité de CSS. Le template suit ces règles :

- Layout en `<table>` (jamais `<div>` flex/grid).
- Toutes les dimensions en pixels, en attributs HTML **et** en style inline.
- Polices web-safe uniquement (`Arial, Helvetica, sans-serif`).
- Couleurs en hexadécimal 6 caractères.
- Pas de feuille de style externe ni de `<style>` global complexe.
- Liens avec `text-decoration:none` et couleur en inline pour éviter le bleu/souligné auto.
- Images avec `width`/`height` HTML **et** CSS pour éviter le redimensionnement Outlook.
