## Déplacer des fichiers

Contrairement à d'autres systèmes de contrôle de version (VCS), Git ne suit pas explicitement les mouvements de fichiers. Lorsque vous renommez un fichier suivi par Git, aucune métadonnée indiquant le renommage n'est stockée par Git. Cependant, Git est suffisamment intelligent pour détecter ces renommages a posteriori.

Par conséquent, le fait que Git dispose d'une commande ```mv``` peut sembler trompeur. Si vous souhaitez renommer un fichier dans Git, vous pouvez simplement exécuter une commande telle que :

```bash
$ git mv nom_origine nom_cible
```

Et cela fonctionne. En fait, si vous exécutez une commande comme celle-ci et que vous examinez le résultat de ```git status```, vous constaterez que Git gère le renommage de fichier :

```bash
$ git mv LISEZMOI.txt LISEZMOI
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui seront validées :
  (utilisez "git reset HEAD <fichier>..." pour désindexer)

        renommé :         LISEZMOI.txt -> LISEZMOI
```

Cependant, cela équivaut à exécuter les commandes suivantes :

```bash
$ mv LISEZMOI.txt LISEZMOI
$ git rm LISEZMOI.txt
$ git add LISEZMOI
```

Git déduit implicitement qu'il s'agit d'un renommage, il n'a donc pas d'importance si vous renommez un fichier de cette manière ou en utilisant la commande ```mv```. La seule différence réelle est que ```git mv``` est une commande unique à saisir au lieu de trois, ce qui en fait une commande plus pratique. L'essentiel est que vous pouvez utiliser n'importe quel outil pour renommer un fichier, puis gérer les commandes ```add``` et ```rm``` ultérieurement, avant de valider les modifications.