Pour supprimer un fichier de Git, vous devez d'abord le retirer des fichiers sous suivi de version (plus précisément, le désindexer dans la zone d'index), puis procéder à la validation. La commande ```git rm``` accomplit cette tâche, mais elle efface également le fichier de votre copie de travail de manière à ce qu'il ne réapparaisse pas comme un fichier non suivi lors de la prochaine validation.

Si vous supprimez simplement le fichier dans votre copie de travail, il apparaîtra sous la section **Modifications qui ne seront pas validées** (c'est-à-dire, non indexé) lorsque vous exécutez ```git status``` :

```bash
$ rm PROJECTS.md
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui ne seront pas validées :
  (utilisez "git add/rm <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git checkout -- <fichier>..." pour annuler les modifications dans la copie de travail)

        supprimé :        PROJECTS.md

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")
```

Ensuite, lorsque vous utilisez ```git rm```, la suppression du fichier est prise en compte dans la zone d'index :

```bash
$ git rm PROJECTS.md
rm 'PROJECTS.md'
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        supprimé :        PROJECTS.md
```

Lors de la prochaine validation, le fichier sera complètement supprimé et ne sera plus sous suivi de version. Si vous avez précédemment apporté des modifications et indexé le fichier, vous devrez utiliser l'option ```-f``` pour forcer sa suppression. Cela sert de mesure de sécurité pour éviter toute suppression accidentelle de données qui n'ont pas encore été enregistrées dans un instantané et qui seraient irrémédiablement perdues.

Une autre situation peut se produire lorsque vous souhaitez cesser de suivre la version d'un fichier tout en le conservant dans votre copie de travail. Cela peut être particulièrement utile si vous avez oublié d'inclure un modèle dans le fichier ```.gitignore``` et avez accidentellement indexé un fichier, comme un gros fichier journal ou une série d'archives de compilation .a. Pour réaliser cela, utilisez l'option ```--cached``` :

```bash
$ git rm --cached LISEZMOI
```

Vous pouvez spécifier des noms de fichiers, de répertoires ou des modèles de fichiers avec la commande ```git rm```. Cela signifie que vous pouvez exécuter des commandes telles que :

```bash
$ git rm log/\*.log
```

Veuillez noter l'utilisation du caractère d'échappement (\) devant *. C'est nécessaire car Git utilise sa propre expansion de noms de fichiers en plus de l'expansion du shell. Vous pouvez omettre ce caractère d'échappement sous Windows si vous utilisez le terminal système. Cette commande supprime tous les fichiers avec l'extension .log présents dans le répertoire log/. Vous pouvez également utiliser une commande telle que :

```bash
$ git rm \*~
```

Cette commande supprime tous les fichiers se terminant par ~.
