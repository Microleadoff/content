Pour créer une nouvelle branche, on utilise la commande ```git branch nom-de-la-branche```. Cette syntaxe va créer un nouveau pointeur vers le dernier commit effectué (le commit courant). A ce stade, vous allez donc avoir deux branches (deux pointeurs) vers le dernier commit : la branche master et la branche tout juste créée.

Créer une nouvelle branche :

```bash
$ git branch test
```

![Représentation de la branche master et de la branche test qui pointent sur le dernier commit](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0270%20-%20Cr%C3%A9er%20une%20nouvelle%20branche/images/representation-de-la-branche-master-et-de-la-branche-test-qui-pointent-sur-le-dernier-commit.png)

Pour déterminer quel pointeur vous utilisez, c’est-à-dire sur quelle branche vous vous trouvez, Git utilise un autre pointeur spécial appelé **HEAD**. **HEAD** pointe sur la branche master par défaut. Notez que la commande ```git branch``` permet de créer une nouvelle branche mais ne déplace pas **HEAD**.

Nous allons donc devoir déplacer explicitement **HEAD** pour indiquer à Git qu’on souhaite basculer sur une autre branche. On utilise pour cela la commande ```git checkout``` suivi du nom de la branche sur laquelle on souhaite basculer.

```bash
$ git checkout test
```

![Représentation du déplacement de HEAD sur la branche test](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0270%20-%20Cr%C3%A9er%20une%20nouvelle%20branche/images/representation-du-deplacement-de-head-sur-la-branche-test.png)

Note : On peut également utiliser ```git checkout -b``` pour créer une branche et basculer immédiatement dessus. Cela est l’équivalent d’utiliser ```git branch``` puis ```git checkout```.

HEAD pointe maintenant vers notre branche test. Si on effectue un nouveau commit, la branche test va avancer automatiquement tandis que master va toujours pointer sur le commit précédent. C’est en effet la branche sur laquelle on se situe lors d’un commit qui va pointer sur ce commit.

```bash
$ touch fichier ficher3.txt
$ git add fichier3.txt
$ git commit -m "nouveau fichier ajouté"
```

![Représentation du nouveau commit sur la branche test, qui diverge maintenant de la branche master](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0270%20-%20Cr%C3%A9er%20une%20nouvelle%20branche/images/representation-du-nouveau-commit-sur-la-branche-test-qui-diverge-maintenant-de-la-branche-master.png)