En complément des options de formatage de sortie, ```git log``` est pourvu de certaines options de limitation utiles, des options qui permettent de restreindre la liste à un sous-ensemble de commits. Vous avez déjà vu une de ces options, l’option `-2` qui ne montre que les deux derniers commits. En fait, on peut utiliser ```-<n>```, où n correspond au nombre de commits que l’on cherche à visualiser en partant des plus récents. En vérité, il est peu probable que vous utilisiez cette option, parce que Git injecte par défaut sa sortie dans un outil de pagination qui permet de la visualiser page à page.

Cependant, les options de limitation portant sur le temps, telles que ```--since``` (depuis) et ```--until``` (jusqu’à) sont très utiles. Par exemple, la commande suivante affiche la liste des commits des deux dernières semaines :

```bash
$ git log --since=2.weeks
```

Cette commande fonctionne avec de nombreux formats — vous pouvez indiquer une date spécifique (2008-01-05) ou une date relative au présent telle que "2 years 1 day 3 minutes ago".

Vous pouvez aussi restreindre la liste aux commits vérifiant certains critères de recherche. L’option ```--author``` permet de filtrer sur un auteur spécifique, et l’option ```--grep``` permet de chercher des mots clés dans les messages de validation. Notez que si vous spécifiez à la fois ```--author``` et ```--grep```, la commande retournera seulement des commits correspondant simultanément aux deux critères.

Si vous souhaitez spécifier plusieurs options ```--grep```, vous devez ajouter l’option ```--all-match```, car par défaut ces commandes retournent les commits vérifiant au moins un critère de recherche.

Un autre filtre vraiment utile est l’option ```-S``` qui prend une chaîne de caractères et ne retourne que les commits qui introduisent des modifications qui ajoutent ou retirent du texte comportant cette chaîne. Par exemple, si vous voulez trouver la dernière validation qui a ajouté ou retiré une référence à une fonction spécifique, vous pouvez lancer :

```bash
$ git log -S nom_de_fonction
```

La dernière option vraiment utile à ```git log``` est la spécification d’un chemin. Si un répertoire ou un nom de fichier est spécifié, le journal est limité aux commits qui ont introduit des modifications aux fichiers concernés. C’est toujours la dernière option de la commande, souvent précédée de deux tirets (--) pour séparer les chemins des options précédentes.

Le tableau Options pour limiter la sortie de ```git log``` récapitule les options que nous venons de voir ainsi que quelques autres pour référence.

Options pour limiter la sortie de ```git log``` :

| Option | Description |
| --- | --- |
| -(n) | N’affiche que les n derniers commits |
| --since, --after | Limite l’affichage aux commits réalisés après la date spécifiée |
| --until, --beforer | Limite l’affichage aux commits réalisés avant la date spécifiée |
| --author | Ne montre que les commits dont le champ auteur correspond à la chaîne passée en argument |
| --committer | Ne montre que les commits dont le champ validateur correspond à la chaîne passée en argument |
| --grep | Ne montre que les commits dont le message de validation contient la chaîne de caractères |
| -S | Ne montre que les commits dont les ajouts ou retraits contiennent la chaîne de caractères |
