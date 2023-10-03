Pour créer un dépôt Git, vous avez principalement deux options. La première consiste à prendre un projet ou un répertoire existant et à l'intégrer dans Git. La seconde consiste à effectuer un clonage (clone) d'un dépôt Git existant depuis un autre serveur.

### Initialisation d’un dépôt Git dans un répertoire existant

Si vous souhaitez commencer à utiliser Git pour suivre un projet existant, il vous suffit de vous placer dans le répertoire du projet et d'exécuter la commande suivante :

```bash
$ git init
```

Cela va créer un nouveau sous-répertoire appelé .git qui contiendra tous les fichiers nécessaires pour votre dépôt Git, c'est en quelque sorte un squelette de dépôt Git. À ce stade, aucun fichier n'est encore inclus dans la gestion de version.

Si vous souhaitez commencer à versionner des fichiers existants (plutôt qu'un répertoire vide), vous devrez probablement suivre ces fichiers et effectuer un premier commit. Vous pouvez accomplir cela en utilisant quelques commandes d'ajout (add) pour spécifier les fichiers que vous souhaitez suivre, suivies par une commande git commit :

```bash
$ git add *.c
$ git add LICENSE
$ git commit -m 'initial project version'
```

### Cloner un dépôt existant

Si vous souhaitez obtenir une copie d'un dépôt Git existant, par exemple, si vous souhaitez contribuer à un projet, la commande dont vous avez besoin s'appelle ```git clone```. Git récupère une copie de presque toutes les données disponibles sur le serveur. Il télécharge toutes les versions de tous les fichiers de l'historique du projet lorsque vous exécutez ```git clone```. En fait, si le disque du serveur venait à se corrompre, vous pourriez utiliser n'importe quel clone pour restaurer le serveur dans l'état où il était au moment du clonage.

Pour cloner un dépôt, utilisez la commande ```git clone [url]```. Par exemple, si vous souhaitez cloner la bibliothèque logicielle Git appelée **libgit2**, vous pouvez le faire de la manière suivante :

```bash
$ git clone https://github.com/libgit2/libgit2
```

Cela créera un répertoire appelé "libgit2", initialisera un répertoire .git à l'intérieur, téléchargera toutes les données du dépôt et extraira une copie de travail de la dernière version. Si vous explorez le nouveau répertoire "libgit2", vous y trouverez les fichiers du projet, prêts à être modifiés ou utilisés. Si vous souhaitez cloner le dépôt dans un répertoire portant un nom différent, vous pouvez spécifier le nom dans une option supplémentaire de la ligne de commande :

```bash
$ git clone https://github.com/libgit2/libgit2 monlibgit2
```

Cette commande accomplira la même chose que la précédente, mais le répertoire cible sera nommé "monlibgit2".

Git prend en charge différents protocoles de transfert. L'exemple précédent utilise le protocole ```https://```, mais vous pouvez également rencontrer ```git://``` ou ```utilisateur@serveur:/chemin.git```, qui utilise le protocole de transfert SSH.
