Une fois que vous avez configuré votre zone d'index comme vous le souhaitez, il est temps de valider vos modifications. N'oubliez pas que tout ce qui n'a pas encore été indexé, c'est-à-dire tous les fichiers que vous avez créés ou modifiés mais auxquels vous n'avez pas encore appliqué la commande ```git add``` depuis leur modification, ne fera pas partie de la prochaine validation. Ces fichiers resteront dans un état modifié sur votre disque.

Dans notre cas, lors de votre dernière utilisation de ```git status```, vous avez vérifié que tout était bien indexé, ce qui signifie que vous êtes prêt à valider vos modifications. La méthode la plus simple pour effectuer une validation est d'exécuter la commande ```git commit``` :

```bash
$ git commit
```

Cette action ouvre votre éditeur par défaut, qui est généralement défini par la variable d'environnement $EDITOR de votre shell (il s'agit généralement de vim ou Emacs, mais vous pouvez le spécifier spécifiquement pour Git en utilisant la commande ```git config --global core.editor```.

L'éditeur affiche le texte suivant :

```bash
# Veuillez saisir le message de validation pour vos modifications. Les lignes
# commençant par '#' seront ignorées, et un message vide annulera la validation.
# Sur la branche master
# Votre branche est à jour avec 'origin/master'.
#
# Modifications qui seront validées :
#       nouveau fichier : LISEZMOI
#       modifié :         CONTRIBUTING.md
#
```

Vous pouvez remarquer que le message de validation par défaut contient une ligne vide suivie en commentaire par le résultat de la commande ```git status```. Vous avez la possibilité d'effacer ces lignes de commentaire et de saisir votre propre message de validation, ou de les laisser en place pour vous aider à vous rappeler ce que vous êtes en train de valider. Cette option affiche le résultat du diff en commentaire dans l'éditeur, vous permettant de visualiser exactement ce qui a été modifié. Lorsque vous quittez l'éditeur après avoir sauvegardé le message, Git crée votre commit avec ce message de validation (en supprimant les commentaires et le diff).

Alternativement, vous pouvez spécifier votre message de validation directement en ligne avec la commande ```git commit``` en l'ajoutant après l'option ```-m```, comme ceci :

```bash
$ git commit -m "mon premier commit"
```

À présent, vous avez créé votre premier commit ! Vous pouvez remarquer que le commit vous fournit quelques informations sur lui-même : sur quelle branche vous avez validé (master), combien de fichiers ont été modifiés, et quelques statistiques sur les lignes ajoutées et supprimées dans ce commit.

Rappelez-vous que la validation enregistre ce que vous avez préparé dans la zone d'index. Tout ce que vous n'avez pas indexé reste en état modifié ; vous pouvez réaliser une nouvelle validation pour l'ajouter à l'historique. À chaque validation, vous enregistrez une nouvelle version du projet.
