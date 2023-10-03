Les deux sections suivantes démontrent comment bricoler les modifications dans votre zone d’index et votre zone de travail. Un point sympathique est que la commande permettant de connaître l’état de ces deux zones vous rappelle aussi comment annuler les modifications. Par exemple, supposons que vous avez modifié deux fichiers et voulez les valider comme deux modifications indépendantes, mais que vous avez tapé accidentellement ```git add``` et donc indexé les deux. Comment annuler l’indexation d’un des fichiers ? La commande ```git status``` vous le rappelle :

```bash
$ git add .
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

    renommé :   README.md -> README
    modifié :   CONTRIBUTING.md
```

Juste sous le texte « Modifications qui seront validées », elle vous indique d’utiliser ```git reset HEAD <fichier>``` pour désindexer un fichier. Utilisons donc ce conseil pour désindexer le fichier CONTRIBUTING.md :

```bash
$ git reset HEAD CONTRIBUTING.md
Modifications non indexées après reset :
M       CONTRIBUTING.md
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        renommé :         README.md -> README

Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git checkout -- <fichier>..." pour annuler les modifications dans la copie de travail)

        modifié :         CONTRIBUTING.md
```

La commande à taper peut sembler étrange mais elle fonctionne. Le fichier CONTRIBUTING.md est modifié mais de retour à l’état non indexé.
