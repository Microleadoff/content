## Créer une nouvelle branche

Pour créer une nouvelle branche, on utilise la commande ```git branch nom-de-la-branche```. Cette syntaxe va créer un nouveau pointeur vers le dernier commit effectué (le commit courant). A ce stade, vous allez donc avoir deux branches (deux pointeurs) vers le dernier commit : la branche master et la branche tout juste créée.

Créer une nouvelle branche :

```bash
$ git branch test
```

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-1-image-à-remplacer)

Pour déterminer quel pointeur vous utilisez, c’est-à-dire sur quelle branche vous vous trouvez, Git utilise un autre pointeur spécial appelé **HEAD**. **HEAD** pointe sur la branche master par défaut. Notez que la commande ```git branch``` permet de créer une nouvelle branche mais ne déplace pas HEAD.

Nous allons donc devoir déplacer explicitement HEAD pour indiquer à Git qu’on souhaite basculer sur une autre branche. On utilise pour cela la commande ```git checkout``` suivi du nom de la branche sur laquelle on souhaite basculer.

```bash
$ git checkout test
```

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-2-image-à-remplacer)

Note : On peut également utiliser ```git checkout -b``` pour créer une branche et basculer immédiatement dessus. Cela est l’équivalent d’utiliser ```git branch``` puis ```git checkout```.

HEAD pointe maintenant vers notre branche test. Si on effectue un nouveau commit, la branche test va avancer automatiquement tandis que master va toujours pointer sur le commit précédent. C’est en effet la branche sur laquelle on se situe lors d’un commit qui va pointer sur ce commit.

```bash
$ touch fichier ficher3.txt
$ git add fichier3.txt
$ git commit -m "nouveau fichier ajouté"
```

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-3-image-à-remplacer)