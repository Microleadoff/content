Pour revenir à la branche **master** dans Git, vous pouvez utiliser la commande ```git checkout master```. Cette commande permet de déplacer le pointeur HEAD sur la branche **master** et de restaurer votre répertoire de travail dans l'état du dernier commit auquel pointe la branche **master**. En d'autres termes, cela vous ramène à la version actuelle de la branche **master** de votre projet.

```bash
$ git checkout master
```

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-4-image-à-remplacer)

Lorsque vous modifiez le répertoire de travail et effectuez un nouveau commit sur une branche, cela crée effectivement un nouvel instantané qui représente l'état actuel du projet à ce stade précis. Si vous effectuez ces modifications sur une branche différente de **master**, par exemple **test**, les branches **master** et **test** vont en effet diverger. Cela signifie qu'elles pointeront vers des instantanés différents qui reflètent des états différents du projet.

Chaque branche dans Git conserve son propre historique de commits, ce qui permet aux branches de se développer indépendamment les unes des autres. Vous pouvez ensuite fusionner ces branches pour incorporer les modifications d'une branche dans une autre lorsque vous le souhaitez, ce qui permet de réunir les développements parallèles en une seule branche.

En résumé, lorsque vous effectuez des commits sur différentes branches, elles évoluent séparément et pointent vers des instantanés différents, créant ainsi une divergence entre les branches.

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-5-image-à-remplacer)
