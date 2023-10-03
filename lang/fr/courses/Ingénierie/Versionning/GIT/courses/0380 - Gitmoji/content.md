## Spécifications

Un message de commit suivant les spécifications gitmoji est composé des éléments suivants :

- **intention**: L'intention que vous souhaitez exprimer avec le commit, en utilisant un emoji de la liste. Soit au format ```:shortcode:```, soit au format unicode.
- **scope**: Une chaîne facultative qui ajoute des informations contextuelles sur le champ d'application de la modification.
- **message**: Une brève explication du changement.

```bash
<intention> [scope?][:?] <message>
```

### Examples

```bash
⚡️ Lazyload home screen images.
🐛 Fix `onClick` event handler
🔖 Bump version `1.2.0`
♻️ (components): Transform classes to hooks
📈 Add analytics to the dashboard
🌐 Support Japanese language
♿️ (account): Improve modals a11y
```

## Shortcode vs Unicode format

Vous remarquerez que lors de l'utilisation d'emojis dans les commits, il est possible d'utiliser soit le format shortcode, soit le format unicode.

La différence entre les deux est que l'unicode représente l'emoji lui-même tandis que le shortcode est une représentation textuelle de l'emoji qui sera convertie en caractère unicode lorsqu'elle sera affichée sur une plateforme Git, telle que GitHub, GitLab, etc.

Les deux approches sont tout à fait acceptables, vous pouvez choisir celle qui vous convient le mieux et qui vous met le plus à l'aise. Voyons les avantages et les inconvénients de chaque approche afin que vous puissiez prendre votre décision :

### Unicode

#### Pour ✅

- Il représente l'emoji réel et ne nécessite aucun système externe.
- Le ```git log``` est plus clair.
- Plus facile à taper.
- Prend moins de caractères dans le titre de l'engagement.

#### Contre ❌

- Il se peut que tous les terminaux et systèmes d'exploitation ne soient pas compatibles.

### Shortcode

#### Pour ✅

- Pris en charge partout car il s'agit d'une représentation textuelle de l'emoji.

#### Contre ❌

- Vous aurez besoin d'une plateforme / d'un système qui sait comment rendre correctement le shortcode.
- Des plateformes / systèmes différents peuvent utiliser des noms de shortcodes différents, par exemple : GitHub et GitLab présentent des différences.
- Prend plus de caractères du titre de l'engagement.

## Le tableau des intentions

| Unicode | Shortcode | Signification |
|-----|-----|-----|
|🎨|```:art:```|Améliorer la structure / le format du code.|
|⚡️|```:zap:```|Améliorer les performances.|
|🔥|```:fire:```|Supprimer du code ou des fichiers.|
|🐛|```:bug:```|Correction d'un bug.|
|🚑️|```:ambulance:```|Correctif critique.|
|✨|```:sparkles:```|Introduire de nouvelles fonctionnalités.|
|📝|```:memo:```|Ajouter ou mettre à jour la documentation.|
|🚀|```:rocket:```|Déployer des éléments.|
|💄|```:lipstick:```|Ajouter ou mettre à jour les fichiers d'interface utilisateur et de style.|
|🎉|```:tada:```|Commencer un projet.|
|✅|```:white_check_mark:```|Ajouter, mettre à jour ou passer des tests.|
|🔒️|```:lock:```|Corriger les problèmes de sécurité.|
|🔐|```:closed_lock_with_key:```|Add or update secrets.|
|🔖|```:bookmark:```|Étiquettes de version.|
|🚨|```:rotating_light:```|Correction des avertissements du compilateur / du linter.|
|🚧|```:construction:```|Travaux en cours.|
|💚|```:green_heart:```|Corriger le build du CI.|
|⬇️|```:arrow_down:```|Downgrade les dépendances.|
|⬆️|```:arrow_up:```|Upgrade les dépendances.|
|📌|```:pushpin:```|Attacher les dépendances à des versions spécifiques.|
|👷|```:construction_worker:```|Ajouter ou mettre à jour le système de construction CI.|
|📈|```:chart_with_upwards_trend:```|Ajouter ou mettre à jour le code d'analyse ou de suivi.|
|♻️|```:recycle:```|Refacto du code.|
|➕|```:heavy_plus_sign:```|Ajouter une dépendance.|
|➖|```:heavy_minus_sign:```|Supprimer une dépendance.|
|🔧|```:wrench:```|Ajouter ou mettre à jour des fichiers de configuration.|
|🔨|```:hammer:```|Ajouter ou mettre à jour des scripts de développement.|
|🌐|```:globe_with_meridians:```|Internationalisation et localisation.|
|✏️|```:pencil2:```|Corriger les fautes de frappe.|
|💩|```:poop:```|Écrire un mauvais code qui doit être amélioré.|
|⏪️|```:rewind:```|Revenir sur les modifications.|
|🔀|```:twisted_rightwards_arrows:```|Merge de branches.|
|📦️|```:package:```|Ajouter ou mettre à jour des fichiers compilés ou des paquets.|
|👽️|```:alien:```|Mise à jour du code suite à des modifications de l'API externe.|
|🚚|```:truck:```|Déplacer ou renommer des ressources (par exemple : fichiers, chemins, itinéraires).|
|📄|```:page_facing_up:```|Ajouter ou mettre à jour une licence.|
|💥|```:boom:```|Introduire des changements radicaux.|
|🍱|```:bento:```|Ajouter ou mettre à jour des assets.|
|♿️|```:wheelchair:```|Améliorer l'accessibilité.|
|💡|```:bulb:```|Ajouter ou mettre à jour des commentaires dans le code source.|
|🍻|```:beers:```|Écrire du code en état d'ébriété.|
|💬|```:speech_balloon:```|Ajouter ou mettre à jour du texte et des éléments littéraux.|
|🗃️|```:card_file_box:```|Effectuer des modifications liées à la base de données.|
|🔊|```:loud_sound:```|Ajouter ou mettre à jour les journaux.|
|🔇|```:mute:```|Supprimer les logs.|
|👥|```:busts_in_silhouette:```|Ajouter ou mettre à jour le(s) contributeur(s).|
|🚸|```:children_crossing:```|Améliorer l'expérience de l'utilisateur / l'utilisabilité.|
|🏗️|```:building_construction:```|Apporter des modifications architecturales.|
|📱|```:iphone:```|Travailler sur le responsive design.|
|🤡|```:clown_face:```|Mocker des choses.|
|🥚|```:egg:```|Ajouter ou mettre à jour un Easter Egg.|
|🙈|```:see_no_evil:```|Ajouter ou mettre à jour un fichier .gitignore.|
|📸|```:camera_flash:```|Ajouter ou mettre à jour des instantanés.|
|⚗️|```:alembic:```|Réaliser des expériences.|
|🔍️|```:mag:```|Améliorer le référencement.|
|🏷️|```:label:```|Ajouter ou mettre à jour des types.|
|🌱|```:seedling:```|Ajouter ou mettre à jour les fichiers de seed.|
|🚩|```:triangular_flag_on_post:```|Ajouter, mettre à jour ou supprimer des indicateurs de fonctionnalité.|
|🥅|```:goal_net:```|Erreurs de capture.|
|💫|```:dizzy:```|Ajouter ou mettre à jour des animations et des transitions.|
|🗑️|```:wastebasket:```|Déclasser le code qui a besoin d'être nettoyé.|
|🛂|```:passport_control:```|Travailler sur le code relatif à l'autorisation, aux rôles et aux permissions.|
|🩹|```:adhesive_bandage:```|Un simple correctif pour un problème non critique.|
|🧐|```:monocle_face:```|Exploration/inspection des données.|
|⚰️|```:coffin:```|Supprimer le code mort.|
|🧪|```:test_tube:```|Ajouter un test défaillant.|
|👔|```:necktie:```|Ajouter ou mettre à jour la logique d'entreprise.|
|🩺|```:stethoscope:```|Ajouter ou mettre à jour le contrôle de santé.|
|🧱|```:bricks:```|Changements liés à l'infrastructure.|
|🧑‍💻|```:technologist:```|Améliorer l'expérience des développeurs.|
|💸|```:money_with_wings:```|Ajouter des parrainages ou des infrastructures liées à l'argent.|
|🧵|```:thread:```|Ajouter ou mettre à jour le code relatif au multithreading ou à la concurrence.|
|🦺|```:safety_vest:```|Ajouter ou mettre à jour le code relatif à la validation.|
