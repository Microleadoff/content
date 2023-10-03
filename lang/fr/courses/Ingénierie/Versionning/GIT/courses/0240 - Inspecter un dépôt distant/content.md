## Inspecter un dépôt distant

Si vous souhaitez obtenir des informations détaillées sur un dépôt distant particulier, vous pouvez utiliser la commande ```git remote show [nom-distant]```. Par exemple, si vous exécutez cette commande avec le nom court origin, vous obtiendrez une sortie semblable à ceci :

```bash
$ git remote show origin
* distante origin
  URL: https://github.com/my-org/complex-project
  URL de rapatriement : https://github.com/my-org/complex-project
  URL push : https://github.com/my-org/complex-project
  Branche HEAD : master
  Branches distantes :
    master                           suivi
    dev-branch                       suivi
    markdown-strip                   suivi
    issue-43                         nouveau (le prochain rapatriement (fetch) stockera dans remotes/origin)
    issue-45                         nouveau (le prochain rapatriement (fetch) stockera dans remotes/origin)
    refs/remotes/origin/issue-11     dépassé (utilisez 'git remote prune' pour supprimer)
  Branches locales configurées pour 'git pull' :
    dev-branch fusionne avec la distante dev-branch
    master     fusionne avec la distante master
  Références locales configurées pour 'git push' :
    dev-branch                     pousse vers dev-branch        (à jour)
    markdown-strip                 pousse vers markdown-strip    (à jour)
    master                         pousse vers master            (à jour)
```

Cela affiche des informations telles que l'URL de rapatriement (fetch) et l'URL de pousse (push) du dépôt distant, la branche HEAD (branche par défaut) du dépôt distant, les branches distantes suivies, et les configurations pour les opérations git pull et git push.

Lorsque vous travaillez sur des projets Git plus complexes, la commande ```git remote show``` peut fournir une grande quantité d'informations utiles, notamment les branches locales configurées pour ```git pull``` et les références locales configurées pour ```git push```. Elle peut également indiquer les branches distantes qui n'ont pas encore été rapatriées, les branches distantes localement présentes mais supprimées sur le serveur, ainsi que les branches qui seront fusionnées lors de l'exécution de ```git pull```. Cette commande est très utile pour comprendre la configuration d'un dépôt distant et comment il interagit avec votre dépôt local.
