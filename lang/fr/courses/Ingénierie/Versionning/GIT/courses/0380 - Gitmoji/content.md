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
|🎨|:art:|Améliorer la structure / le format du code.|
|⚡️|:zap:|Améliorer les performances.|
|🔥|:fire:|Supprimer du code ou des fichiers.|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
|XXX|XXX|XXX|
