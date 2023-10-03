## Retirer et renommer des dépôts distants

Si vous souhaitez renommer une référence à un dépôt distant, vous pouvez utiliser la commande ```git remote rename``` pour modifier le nom court du dépôt distant. Par exemple, si vous souhaitez renommer pb en paul, vous pouvez le faire comme ceci :

```bash
$ git remote rename pb paul
$ git remote
origin
paul
```

Veuillez noter que cette opération renomme également les références des branches distantes associées. Par exemple, si vous aviez une branche distante pb/master, elle sera désormais appelée paul/master après le renommage.

Si vous avez besoin de retirer un dépôt distant pour quelque raison que ce soit, que ce soit parce que vous ne l'utilisez plus ou qu'il a été supprimé, vous pouvez utiliser la commande ```git remote rm```. Par exemple, pour retirer le dépôt distant nommé paul, vous pouvez faire ceci :

```bash
$ git remote rm paul
$ git remote
origin
```

Après cette opération, le dépôt distant **paul** ne sera plus répertorié parmi les dépôts distants associés à votre projet.
