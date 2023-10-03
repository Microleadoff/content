## Indexer des fichiers modifiés

Modifier un fichier déjà sous suivi de version. Si vous apportez des modifications à un fichier suivi par Git, tel que "CONTRIBUTING.md", et que vous exécutez à nouveau la commande ```git status```, vous obtiendrez la sortie suivante :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        nouveau fichier : LISEZMOI

Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git checkout -- <fichier>..." pour annuler les modifications dans la copie de travail)

        modifié :         CONTRIBUTING.md
```

Le fichier "CONTRIBUTING.md" apparaît dans la section "Modifications qui ne seront pas validées", ce qui signifie qu'il a été modifié dans la copie de travail, mais qu'il n'a pas encore été indexé. Pour l'indexer, vous devez exécuter la commande ```git add```. ```git add``` est une commande polyvalente : elle peut être utilisée pour mettre un fichier sous suivi de version, indexer un fichier ou effectuer d'autres actions, telles que marquer des conflits de fusion comme résolus. Son sens est davantage "ajouter ce contenu pour la prochaine validation" que "ajouter ce contenu au projet".

Exécutons maintenant ```git add``` pour indexer le fichier "CONTRIBUTING.md", puis vérifions à nouveau l'état avec ```git status``` :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        nouveau fichier : LISEZMOI
        modifié :         CONTRIBUTING.md
```

Désormais, les deux fichiers sont indexés et seront inclus dans la prochaine validation. Supposons toutefois que vous souhaitiez apporter une autre petite modification au fichier "CONTRIBUTING.md" avant de le valider. Vous l'ouvrez à nouveau, effectuez la modification, et vous êtes prêt à valider. Cependant, si vous exécutez ```git status``` une dernière fois, vous obtenez ceci :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        nouveau fichier : LISEZMOI
        modifié :         CONTRIBUTING.md

Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git checkout -- <fichier>..." pour annuler les modifications dans la copie de travail)

        modifié :         CONTRIBUTING.md
```

Que s'est-il passé ? Désormais, "CONTRIBUTING.md" apparaît à la fois comme indexé et non indexé. En fait, Git indexe un fichier dans l'état où il se trouvait au moment où la commande "git add" a été exécutée. Si vous validez les modifications maintenant, la version de "CONTRIBUTING.md" qui sera incluse dans le commit sera celle qui existait au moment où la commande ```git add CONTRIBUTING.md``` a été exécutée, et non la version actuelle dans la copie de travail au moment où la commande ```git commit``` est lancée. Si le fichier est modifié après un ```git add```, vous devez réexécuter ```git add``` pour prendre en compte l'état actuel de la copie de travail :

```bash
$ git add CONTRIBUTING.md
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        nouveau fichier : LISEZMOI
        modifié :         CONTRIBUTING.md
```
