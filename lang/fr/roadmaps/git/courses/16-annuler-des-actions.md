## Annuler des actions

À tout moment, vous pouvez désirer annuler une de vos dernières actions. Il faut être très attentif car certaines de ces annulations sont définitives (elles ne peuvent pas être elles-mêmes annulées). C’est donc un des rares cas d’utilisation de Git où des erreurs de manipulation peuvent entraîner des pertes définitives de données.

Une des annulations les plus communes apparaît lorsqu’on valide une modification trop tôt en oubliant d’ajouter certains fichiers, ou si on se trompe dans le message de validation. Si vous souhaitez rectifier cette erreur, vous pouvez valider le complément de modification avec l’option **--amend** :

```bash
$ git commit --amend
```

Cette commande prend en compte la zone d’index et l’utilise pour le commit. Si aucune modification n’a été réalisée depuis la dernière validation (par exemple en lançant cette commande immédiatement après la dernière validation), alors l’instantané sera identique et la seule modification à introduire sera le message de validation.

L’éditeur de message de validation démarre, mais il contient déjà le message de la validation précédente. Vous pouvez éditer ce message normalement, mais il écrasera le message de la validation précédente.

Par exemple, si vous validez une version puis réalisez que vous avez oublié d’indexer les modifications d’un fichier que vous vouliez ajouter à ce commit, vous pouvez faire quelque chose comme ceci :

```bash
$ git commit -m 'validation initiale'
$ git add fichier_oublie
$ git commit --amend
```

Vous n’aurez au final qu’un unique commit, la seconde validation remplace le résultat de la première.
