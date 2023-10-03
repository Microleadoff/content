## Afficher les dépôts distants

Pour afficher la liste des serveurs distants enregistrés, vous pouvez utiliser la commande ```git remote```. Cette commande répertorie les noms des références distantes que vous avez configurées. Lorsque vous clonez un dépôt, vous verrez au moins une référence appelée ```origin```, qui est le nom par défaut donné par Git au serveur à partir duquel vous avez cloné. Voici comment vous pouvez l'utiliser :

```bash
$ git clone https://github.com/schacon/ticgit
Clonage dans 'ticgit'...
remote: Counting objects: 1857, done.
remote: Total 1857 (delta 0), reused 0 (delta 0)
Réception d'objets: 100% (1857/1857), 374.35 KiB | 243.00 KiB/s, fait.
Résolution des deltas: 100% (772/772), fait.
Vérification de la connectivité... fait.
$ cd ticgit
$ git remote
origin
```

Si vous souhaitez voir également les URLs associées à chaque référence distante, vous pouvez utiliser l'option ```-v``` (pour "verbose") de la commande git remote :

```bash
$ git remote -v
origin  https://github.com/schacon/ticgit (fetch)
origin  https://github.com/schacon/ticgit (push)
```

Si vous avez plusieurs dépôts distants configurés, cette commande affichera la liste de tous ces dépôts. Par exemple :

```bash
$ cd grit
$ git remote -v
bakkdoor  https://github.com/bakkdoor/grit (fetch)
bakkdoor  https://github.com/bakkdoor/grit (push)
cho45     https://github.com/cho45/grit (fetch)
cho45     https://github.com/cho45/grit (push)
defunkt   https://github.com/defunkt/grit (fetch)
defunkt   https://github.com/defunkt/grit (push)
koke      git://github.com/koke/grit.git (fetch)
koke      git://github.com/koke/grit.git (push)
origin    git@github.com:mojombo/grit.git (fetch)
origin    git@github.com:mojombo/grit.git (push)
```
Cette liste affiche les noms des dépôts distants et leurs URLs associées pour les opérations de récupération (fetch) et de poussée (push).
