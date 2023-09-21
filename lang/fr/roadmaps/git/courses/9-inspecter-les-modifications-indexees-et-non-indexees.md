## Inspecter les modifications indexées et non indexées

Lorsque la sortie de la commande **git status** ne fournit pas suffisamment de détails et que vous souhaitez non
seulement savoir quels fichiers ont été modifiés, mais également ce qui a été modifié dans ces fichiers, vous pouvez
utiliser la commande **git diff**. Cette commande sera examinée en détail plus tard, mais elle est généralement utilisée
pour répondre aux questions suivantes : qu'a-t-il été modifié mais pas encore indexé ? Quelles modifications ont été
indexées et sont prêtes à être validées ? Alors que **git status** offre des informations générales pour répondre à ces
questions, **git diff** affiche les lignes exactes qui ont été ajoutées, modifiées ou supprimées.

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

Pour voir ce qui a été modifié mais n'est pas encore indexé, exécutez simplement **git diff** sans autre argument :

```bash
$ git diff
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
index 8ebb991..643e24f 100644
--- a/CONTRIBUTING.md
+++ b/CONTRIBUTING.md
@@ -65,7 +65,8 @@ branch directly, things can get messy.
 Please include a nice description of your changes when you submit your PR;
 if we have to read the whole diff to figure out why you're contributing
 in the first place, you're less likely to get feedback and have your change
-merged in.
+merged in. Also, split your changes into comprehensive chunks if your patch is
+longer than a dozen lines.

 If you are starting to work on a particular area, feel free to submit a PR
 that highlights your work in progress (and note in the PR title that it's
```

Cette commande compare le contenu du répertoire de travail avec la zone d'index, vous montrant ainsi les modifications
non indexées.

Si vous souhaitez visualiser les modifications indexées qui seront incluses dans la prochaine validation, vous pouvez
utiliser **git diff --cached** ou **git diff --staged**.

```bash
$ git diff --staged
diff --git a/LISEZMOI b/LISEZMOI
new file mode 100644
index 0000000..1e17b0c
--- /dev/null
+++ b/LISEZMOI
@@ -0,0 +1 @@
+Mon Projet
```

Il est important de noter que **git diff** ne montre pas les modifications apportées depuis la dernière validation, mais
seulement les modifications qui ne sont pas encore indexées. Cela peut prêter à confusion, car si tous les fichiers
modifiés ont été indexés, **git diff** n'affichera aucune modification.
