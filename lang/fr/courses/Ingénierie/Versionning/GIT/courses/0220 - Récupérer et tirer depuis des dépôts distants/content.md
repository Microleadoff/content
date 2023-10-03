Pour obtenir les données des dépôts distants, comme vous venez de le voir, vous pouvez utiliser la commande suivante :

```bash
$ git fetch [nom-distant]
```

Cette commande communique avec le dépôt distant spécifié et récupère toutes les données de ce projet que vous n'avez pas déjà dans votre dépôt local. Après cette opération, vous aurez toutes les références aux branches contenues dans ce dépôt distant, que vous pourrez fusionner ou inspecter à tout moment.

Lorsque vous clonez un dépôt, le dépôt distant est automatiquement ajouté sous le nom ```origin```. Ainsi, git fetch origin récupère toutes les modifications qui ont été poussées vers ce dépôt distant depuis que vous l'avez cloné ou depuis la dernière fois que vous avez effectué une opération de récupération. Il est important de noter que la commande fetch récupère ces données dans votre dépôt local mais les stocke dans des branches distinctes. Elle ne fusionne pas automatiquement ces modifications avec votre travail en cours ni ne modifie votre copie de travail. Vous devez volontairement fusionner ces modifications distantes dans votre travail lorsque vous le souhaitez.

Si vous avez créé une branche pour suivre l'évolution d'une branche distante, vous pouvez utiliser la commande ```git pull```. Celle-ci récupère automatiquement les modifications d'une branche distante et les fusionne dans votre branche locale. Cette approche peut rendre votre flux de travail plus fluide, car par défaut, la commande git clone configure votre branche locale pour suivre la branche master du dépôt que vous avez cloné (si le dépôt distant a une branche master). En lançant ```git pull```, vous obtiendrez généralement les données depuis le serveur que vous avez initialement cloné et elles seront fusionnées automatiquement dans votre branche de travail actuelle.

```bash
$ git pull
```