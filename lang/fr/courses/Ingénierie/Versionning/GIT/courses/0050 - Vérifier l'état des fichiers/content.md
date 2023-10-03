Lorsque vous travaillez sur votre projet, il est important de comprendre que chaque fichier de votre copie de travail peut se trouver dans l'un des deux états : suivi ou non suivi.

Les fichiers **suivis** sont ceux qui étaient déjà présents dans la dernière version (commit). Ils peuvent être inchangés, modifiés ou indexés pour un futur commit. Tous les autres fichiers sont considérés comme **non suivis** cela signifie qu'ils ne faisaient pas partie de la dernière version et n'ont pas été inclus dans l'index (zone de staging).

Lorsque vous clonez un dépôt pour la première fois, tous les fichiers sont marqués comme **suivis** et **inchangés** car Git vient de les extraire et vous ne les avez pas encore modifiés.

Au fur et à mesure que vous modifiez des fichiers, Git les détecte comme **modifiés** car ils diffèrent de la version présente dans la dernière version. Vous pouvez ensuite les **indexer** en les ajoutant à la zone de staging, puis vous effectuez un commit pour enregistrer toutes les modifications indexées. Ce cycle se répète au fur et à mesure de l'évolution de votre projet.

L'outil principal pour déterminer l'état de vos fichiers dans Git est la commande ```git status```. Lorsque vous l'exécutez juste après avoir cloné un dépôt, vous obtenez une réponse semblable à ceci :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
rien à valider, la copie de travail est propre
```

Ce message indique que votre copie de travail est propre, ce qui signifie qu'aucun des fichiers suivis n'a été modifié depuis le dernier commit. Git n'a également détecté aucun fichier non suivi, sinon ils seraient répertoriés ici. Enfin, la commande vous indique sur quelle branche vous vous trouvez, pour l'instant, c'est généralement **master** ou **main** qui est la branche par défaut. Nous explorerons les branches dans un autre cours.

Supposons maintenant que vous souhaitiez ajouter un nouveau fichier au projet, par exemple, un fichier nommé LISEZMOI. Si ce fichier n'existait pas auparavant et que vous exécutez ```git status```, vous verrez votre fichier **non suivi** répertorié comme suit :

```bash
$ echo 'Mon Projet' > LISEZMOI
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)

        LISEZMOI

aucune modification ajoutée à la validation mais des fichiers non suivis sont présents (utilisez "git add" pour les suivre)
```

Vous remarquerez que le nouveau fichier LISEZMOI est répertorié comme **Fichiers non suivis** dans le rapport de statut. Cela signifie simplement que Git a détecté un fichier qui n'était pas présent dans le dernier commit. Git ne suit pas automatiquement les fichiers nouvellement créés, vous devez lui indiquer de les suivre explicitement. Cette approche empêche d'ajouter accidentellement des fichiers non désirés à votre suivi de version. 