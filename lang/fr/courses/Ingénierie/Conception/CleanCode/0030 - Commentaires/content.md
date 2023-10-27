Les commentaires, bien que théoriquement non interprétés, font pleinement partie des pratiques nécessaires à l’obtention d’un Clean Code. A titre personnel, j’aime à dire : “un bon commentaire est un commentaire inutile”. A toutes fins utiles, cette réplique n’est pas à prendre au pied de la lettre, mais reste néanmoins une bonne référence compte tenu de l’ensemble des attentions qu’ils impliquent.

La première étape d’un commentaire vise à s’assurer qu’il ne justifie pas un mauvais code. Mettre en commentaire des explications sur une variable ne vous dispense en rien de lui attribuer un nommage correct. Par contre, utiliser un commentaire pour apporter des informations supplémentaires non visibles instantanément est pertinent.

L’idée de base d’un commentaire est de permettre à n’importe quelle personne lisant votre code d’en faciliter sa compréhension. Ainsi, si une partie de votre code nécessite des explications spécifiques, alors l’utilisation des commentaires est requise. A contrario, si l’ensemble de votre code est lisible, clair, et compréhensible de tous, alors aucun commentaire n’est nécessaire. Rappeler cet état de fait peut sembler futile, mais c’est pourtant trop souvent qu’il est oublié lors de la rédaction de code…

Voici donc une liste non exhaustive des bons et mauvais commentaires, qui pourront vous servir de point de repère dans la réalisation de votre code.

## Les bons commentaires

Les commentaires légaux, c’est-à-dire ceux qui sont situés au début de fichier et ont pour vocation de transmettre des informations quant au copyright, à l'auteur ou à la licence d’un script, font partie des bons commentaires. J’ai attendu trop longtemps à titre personnel avant d’en rédiger de la sorte, c’est dommage. La plupart de ces commentaires permettent un semblant d’information et de traçabilité, notamment à propos de la possibilité ou non de la réexploitation d’un code.

Les commentaires informatifs, comme décrits précédemment, sont bien évidemment encouragés. Attention cependant à ne pas tomber dans l’excès : l’information doit être juste, pertinente, et limitée. Ne vous perdez pas dans la description des conséquences d’une mauvaise utilisation d’une constante ou autre. Contentez-vous d’y décrire ce qu’elle doit contenir comme information.

Un autre aspect parfois négligé sur l’utilisation des commentaires consiste en l'explication des intentions de l’auteur. En effet, à chaque problème, il existe une multitude de solutions, et autant de manières différentes de coder chacune de ces solutions. Aussi un choix d’algorithme ou de logique peut être commenté dans le code afin que les lecteurs suivants comprennent la ou les raisons de votre décision.

La clarification est bien évidemment un des objectifs premiers des commentaires. Dans cet esprit, beaucoup de codes ne sont pas suffisamment précis sur les paramètres et/ou arguments des fonctions ou méthodes qu’ils définissent et utilisent. De la sorte, il peut paraître certaines fois complexe de savoir comment utiliser une méthode ou une fonction sans aller constater son code source. Privilégiez donc les commentaires permettant d’indiquer de manière précise quels sont les arguments attendus !

Les commentaires peuvent également permettre d’avertir un lecteur des conséquences d’un changement de valeur. Le but n’est pas ici de s’éterniser sur le sujet ou d’y décrire précisément tous les tenants et aboutissants attendus, mais bien de prévenir d’une possible dangerosité. Dans le même registre, le commentaire peut servir à amplifier la transmission d’un point important au lecteur du code.

Enfin, les commentaires TODO font bien partie des bons commentaires, puisqu’ils permettent d’éviter des oublis. Attention cependant à ne pas oublier de traiter ces points… Les développeurs qui n’utilisent que rarement ce système ont souvent tendance à en oublier quelques-uns…

## Les mauvais commentaires

Il est important de retenir que les mauvais commentaires viennent toujours d’une bonne intention… Aussi voici quelques exemples de mauvais commentaires et de mauvaises pratiques : 

- **Ne parlez pas dans votre barbe** ! SI vous prenez le temps d’écrire un commentaire, prenez le temps de le rédiger correctement. Il doit rester sensé pour tout lecteur, faites donc également attention au contexte et aux explications ! Si le fait de rédiger un commentaire est une obligation imposée par votre hiérarchie ou votre client, c’est que vous êtes payé pour le faire, donc réalisez un travail respectueux !
- **Évitez les commentaires redondants**. Dire les choses une fois suffit amplement !
- **Attention à ne pas être trompeur**. Il arrive que certains commentaires ne soient pas suffisamment précis, ou mal contextualisés. Dans ce cas de figure, il se peut qu’un commentaire puisse induire en erreur le lecteur !
- **L’obligation de mettre en place des commentaires est parfois stupide**. S’ils n’ont pas pour vocation d’auto générer une documentation par la suite, alors il est très souvent stupide d’obliger à mettre des commentaires, même sur des fonctions ou méthodes parfaitement explicites…
- **Évitez les commentaires de journalisation**. S’ils étaient très pratiques il y a quelques années, ils sont aujourd’hui devenus obsolètes puisque c’est un des rôles principaux des outils de versionning.
- **Évitez les commentaires évidents, ou “parasites”**. Ne commentez pas un constructeur en stipulant qu’il s’agit du constructeur…
- **Abandonnez les marqueurs de positions**. Certains développeurs mettent en place des commentaires afin de se repérer dans un fichier, par exemple pour séparer des attributs et méthodes dans une classe. Ou encore dans des fichiers CSS afin de séparer le header, du body, du footer, etc… Ceci est une mauvaise pratique qui traduit souvent davantage un problème de découpage de fichiers plutôt qu’un réel intérêt de repérage.
- ***Localisez-les*** ! Un commentaire qui ne décrit pas un code qui lui est proche n’a pas d’intérêt !
- Certains développeurs rédigent leurs commentaires en HTML, ne faites jamais cela.
- **Trop d’information tue l’information.**
- Attention aux commentaires d’en-têtes de fonctions inutiles. Un bon nom de fonction est bien souvent suffisant…

Cette liste est, comme sa précédente, non exhaustive ! N’hésitez pas à la compléter par vous-même ou bien à nous soumettre des éléments supplémentaires afin que nous puissions la compléter !
