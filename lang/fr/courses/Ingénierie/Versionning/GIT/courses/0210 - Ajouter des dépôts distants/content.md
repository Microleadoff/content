## Ajouter des dépôts distants

Pour ajouter un nouveau dépôt distant Git avec un nom court pour une référence facile, utilisez la commande ```git remote add [nom court] [URL]```. Voici un exemple :

```bash
$ git remote
origin
$ git remote add pb https://github.com/paulboone/ticgit
$ git remote -v
origin  https://github.com/schacon/ticgit (fetch)
origin  https://github.com/schacon/ticgit (push)
pb  https://github.com/paulboone/ticgit (fetch)
pb  https://github.com/paulboone/ticgit (push)
```

Maintenant, vous pouvez utiliser le mot-clé ```pb``` sur la ligne de commande au lieu de l'URL complète. Par exemple, si vous souhaitez récupérer toutes les informations que Paul a, mais que vous ne voulez pas encore les fusionner dans votre branche actuelle, vous pouvez utiliser git fetch ```pb``` :

```bash
$ git fetch pb
remote: Counting objects: 43, done.
remote: Compressing objects: 100% (36/36), done.
remote: Total 43 (delta 10), reused 31 (delta 5)
Dépaquetage des objets: 100% (43/43), fait.
Depuis https://github.com/paulboone/ticgit
 * [nouvelle branche] master     -> pb/master
 * [nouvelle branche] ticgit     -> pb/ticgit
```

La branche master de Paul est maintenant accessible localement sous le nom ```pb/master```. Vous pouvez la fusionner dans l'une de vos propres branches, ou vous pouvez extraire une branche localement si vous souhaitez l'inspecter plus en détail.
