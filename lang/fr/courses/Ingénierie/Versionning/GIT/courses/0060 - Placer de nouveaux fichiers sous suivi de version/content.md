Pour commencer à suivre un nouveau fichier, vous devez utiliser la commande ```git add```. Dans le cas de votre fichier LISEZMOI, vous pouvez le faire en saisissant la commande suivante :

```bash
$ git add LISEZMOI
```

Si vous exécutez à nouveau la commande ```git status```, vous verrez que votre fichier LISEZMOI est désormais suivi et indexé :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        nouveau fichier : LISEZMOI
```

La présence du fichier LISEZMOI dans la section "Modifications qui seront validées" signifie qu'il est maintenant indexé. Cela signifie que si vous effectuez un commit à ce stade, la version du fichier telle qu'elle est au moment où vous avez exécuté git add sera enregistrée dans l'historique des versions.

Vous pouvez vous rappeler que lorsque vous avez initialement exécuté git init, vous avez ensuite utilisé git add pour commencer à suivre les fichiers de votre répertoire de travail. La commande git add accepte en argument un chemin vers un fichier ou un répertoire. Si vous spécifiez un répertoire, la commande ajoutera récursivement tous les fichiers présents dans ce répertoire au suivi de version.