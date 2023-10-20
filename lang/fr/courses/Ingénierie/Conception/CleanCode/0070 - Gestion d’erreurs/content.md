La gestion des erreurs mérite un cours à part entière en matière de clean code. Si une minorité de développeurs s’en servent aujourd’hui, il reste important pour celle-ci de comprendre comment les exploiter au mieux afin de rester fidèle aux pratiques de code propre.

La première règle de la gestion des erreurs est qu’elle ne doit pas masquer la lisibilité de la logique. Si tel est le cas, elle doit être employée différemment pour ne pas nuire au premier but du code propre : sa lisibilité et sa compréhensibilité.

Une fois ce constat établi, il devient nécessaire d’aborder la comparaison de la gestion d’erreurs à la gestion de logs ou de codes retours. Ces logs et ces codes retours sont en effet moins impactants que les exceptions, et il conviendra toujours de préférer l’utilisation des exceptions, qui sont plus complets et permettent une homogénéité supérieure dans la gestion des erreurs.

Chaque exception ainsi levée doit obligatoirement fournir un contexte afin de déterminer l'origine de l’emplacement de l’erreur. Ainsi une “trace” (souvent appelée “StackTrace”) doit être fournie si possible et les messages d’erreurs associés doivent prodiguer des informations utiles et sensées. Un message n’apportant pas d’information particulière n’a pas lieu d’être et peut mener à une mauvaise compréhension de l’erreur. Aussi soyez aussi attentif à vos messages d’erreurs qu’à votre manière de nommer des variables !

Faites ensuite attention à bien utiliser les bonnes classes d’exception. Chaque langage informatique dispose de ses propres classes d’exception pour leur traitement. Il existe souvent une classe générique, puis plusieurs classes spécifiques. Une bonne gestion d’exception doit être la plus précise possible, et donc utiliser les classes spécifiques lorsque c’est possible plutôt que de choisir la classe générique. Le principe (simple) résident derrière cette logique est qu’il est plus facile de comprendre une exception précise plutôt qu’une exception générique. Il est ainsi plus simple de résoudre un problème lorsque l’on sait d’où il provient !

Enfin, vous devez éviter au maximum d’utiliser les valeur “nulles” dans deux cas de figure : 

1. Les exceptions ne doivent jamais retourner de valeur “nulle” (à adapter en fonction du langage, ex : Null, None, etc…)
2. Évitez au maximum de passer des valeurs “nulles” en paramètre des fonctions.
