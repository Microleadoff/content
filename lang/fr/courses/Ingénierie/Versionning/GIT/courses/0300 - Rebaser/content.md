## Rebaser

Git offre deux méthodes pour intégrer le travail effectué sur une branche dans une autre : la fusion (merge) et le rebasage (rebase). Nous allons maintenant explorer le rebasage, examiner les distinctions entre la fusion et le rebasage, et déterminer dans quelles situations il est préférable d'utiliser l'une ou l'autre de ces opérations.

Reprenons notre exemple précédent avec nos deux branches divergentes.

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-7-image-à-remplacer)

Au lieu de procéder à une fusion à trois sources, nous avons la possibilité de réaliser un rebasage des modifications validées dans **commitN+1** sur notre branche **master**. Cette opération est accomplie à l'aide de la commande git rebase, qui permet de récupérer les modifications validées sur une branche et de les rejouer sur une autre.

Concrètement, Git commence par se baser sur le dernier commit commun aux deux branches (c'est-à-dire l'ancêtre commun le plus récent). Ensuite, il récupère les modifications effectuées sur la branche que nous souhaitons intégrer et les applique à la branche vers laquelle nous souhaitons rebaser notre travail, en respectant l'ordre chronologique de leur introduction.

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-8-image-à-remplacer)

Le résultat final obtenu avec un rebasage est similaire à celui d'une fusion, mais l'historique est plus linéaire et clair, car toutes les modifications apparaissent en série, même si elles ont été effectuées en parallèle. L'opération de rebasage rejoue les modifications d'une série de commits sur une autre branche dans l'ordre chronologique de leur création, tandis que la fusion combine les têtes de deux branches distinctes.

Cependant, il est essentiel de comprendre que le rebasage équivaut à supprimer des commits existants pour en créer de nouveaux qui ont un contenu similaire, mais qui sont distincts en tant qu'entités. Pour cette raison, il ne faut jamais rebaser des commits qui ont déjà été poussés sur un dépôt public.

Imaginons la situation suivante :

1. Vous poussez des commits sur un dépôt public.
2. D'autres personnes récupèrent ces commits et travaillent à partir d'eux.
3. Vous utilisez ensuite **git rebase** pour **réécrire** ces commits et les poussez à nouveau.

Dans ce scénario, des problèmes surviendront, car les personnes qui ont travaillé à partir des commits d'origine ne trouveront pas ces commits dans le projet lorsqu'elles souhaiteront récupérer les mises à jour. De plus, lorsqu'elles pousseront leurs propres modifications sur le dépôt public, les commits qui avaient été supprimés seront réintroduits, créant ainsi un historique de version très confus et potentiellement générant des conflits.
