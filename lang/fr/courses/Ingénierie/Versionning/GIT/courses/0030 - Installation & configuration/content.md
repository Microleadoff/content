## Installation

Avant de pouvoir commencer à utiliser Git, vous devez vous assurer qu'il est installé sur votre ordinateur. Même s'il est déjà installé, il est généralement recommandé d'utiliser la dernière version disponible. Vous avez plusieurs options pour l'installer : vous pouvez choisir de l'installer en tant que paquet ou à l'aide d'un programme d'installation, ou bien vous pouvez télécharger le code source et le compiler vous-même.

### Installation sur Windows

Il existe plusieurs façons d'installer Git sur un système Windows. L'application officielle de Git est disponible en téléchargement sur le site web de Git. Vous pouvez y accéder en vous rendant sur [http://git-scm.com/download/win](http://git-scm.com/download/win), et le téléchargement commencera automatiquement. Il est important de noter qu'il s'agit du projet appelé "Git for Windows" (également connu sous le nom de msysGit), qui est distinct du projet Git lui-même.

Une autre méthode simple pour installer Git est d'utiliser "Github for Windows". Cet installateur inclut une version en ligne de commande de Git ainsi qu'une interface graphique conviviale. Il est également compatible avec Powershell et configure automatiquement les paramètres de mise en cache des informations d'authentification et les réglages CRLF. Il est important de savoir que ces options sont très utiles. Vous pouvez télécharger Github for Windows depuis le site [http://windows.github.com](http://windows.github.com).

### Installation sur Mac

Il existe plusieurs méthodes pour installer Git sur un Mac, et l'une des plus simples consiste à installer les Xcode Command Line Tools. Si vous utilisez Mavericks (10.9) ou une version ultérieure, vous pouvez simplement essayer de lancer la commande 'git' dans le terminal. Si Git n'est pas déjà installé, il vous sera demandé de le faire.

Si vous préférez disposer d'une version plus récente, vous avez également la possibilité de l'installer à partir de l'installateur binaire. Un installateur Git spécifiquement conçu pour OS X est maintenu et disponible en téléchargement sur le site web de Git à l'adresse [http://git-scm.com/download/mac](http://git-scm.com/download/mac).

Vous pouvez aussi l’installer comme sous-partie de l’installation de GitHub pour Mac. Leur outil Git graphique a une option pour installer les outils en ligne de commande. Vous pouvez télécharger cet outil depuis le site web de GitHub pour Mac, à [http://mac.github.com](http://mac.github.com).

### Installation sur Linux

Si vous voulez installer les outils basiques de Git sur Linux via un installateur binaire, vous pouvez généralement le faire au moyen de l’outil de gestion de paquet fourni avec votre distribution. Sur Fedora, par exemple, vous pouvez utiliser dnf :

```bash
$ dnf install git-all
```

Sur une distribution basée sur Debian, telle que Ubuntu, essayer apt-get :

```bash
$ apt-get install git-all
```

Pour plus d’options, des instructions d’installation sur différentes versions Unix sont disponibles sur le site web de Git, à [http://git-scm.com/download/linux](https://git-scm.com/download/linux).

## Configuration

Après avoir installé Git, la première étape consiste à configurer votre nom et votre adresse e-mail. Ces informations sont essentielles car Git les utilise pour chaque validation (commit), et elles seront intégrées de manière permanente dans toutes les validations que vous effectuerez :

```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Il est important de noter que cette étape n'est nécessaire qu'une seule fois si vous utilisez l'option --global, car Git utilisera ces informations pour toutes vos opérations sur ce système. Si vous souhaitez spécifier un nom ou une adresse e-mail différents pour un projet particulier, vous pouvez exécuter ces commandes sans l'option --global lorsque vous êtes dans ce projet spécifique.

De nombreux outils graphiques vous guideront également lors de cette configuration la première fois que vous les utiliserez.

## Vérifier votre configuration

Si vous souhaitez vérifier les réglages de configuration que Git a enregistrés, vous pouvez utiliser la commande **git config --list** pour afficher la liste de tous les réglages que Git a recueillis jusqu'à présent :

```bash
$ git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
```

Il est possible que vous voyiez certains paramètres apparaître plusieurs fois, car Git peut lire les mêmes paramètres à partir de différents fichiers (comme /etc/gitconfig et ~/.gitconfig, par exemple). Dans ce cas, Git utilise la valeur la plus récente pour chaque paramètre.

Si vous souhaitez vérifier la valeur spécifique d'un paramètre particulier, vous pouvez le faire en utilisant la commande git config suivie du nom du paramètre :

```bash
$ git config user.name
John Doe
```
