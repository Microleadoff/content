Que faire si vous réalisez que vous ne souhaitez pas conserver les modifications du fichier CONTRIBUTING.md ? Comment le réinitialiser facilement, le ramener à son état du dernier instantané (ou lors du clonage, ou dans l’état dans lequel vous l’avez obtenu dans votre copie de travail) ? Heureusement, ```git status``` vous indique comment procéder. Dans le résultat de la dernière commande, la zone de travail ressemble à ceci :

```bash
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git checkout -- <fichier>..." pour annuler les modifications dans la copie de travail)

        modifié :         CONTRIBUTING.md
```

Ce qui vous indique de façon explicite comment annuler des modifications que vous avez faites. Faisons comme indiqué :

```bash
$ git checkout -- CONTRIBUTING.md
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        renommé :         README.md -> README
```

Vous pouvez constater que les modifications ont bien été annulées.
