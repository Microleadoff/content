La concurrence est souvent sujet à des problèmes lors du développement applicatif puisqu’elle engendre de nombreuses failles du fait même de la non synchronicité des actions. Elle est souvent assimilée au multi-threading bien qu’elle puisse être impliquée dans d’autres utilisations. Tout comme du code plus “simple”, elle implique cependant le respect de certaines règles pour pouvoir être qualifié de “clean code”. Notez par ailleurs que le respect de ces règles permet souvent de résoudre des bugs ou d'anticiper des bugs qui ne se sont pas encore présentés !

La première règle est qu’il est difficile d’écrire des programmes concurrents propres. Même avec la meilleure volonté du monde, vous n’obtiendrez ainsi pas forcément un code majestueux… La première règle en matière de concurrence est donc de se demander si les découplages effectués sont bien réalisés à bon escient ! Sont-ils réellement obligatoires ou pertinents ?

Il est donc important de rappeler quelques points : 
1. la concurrence n’améliore pas toujours les performances
2. la conception d’un programme est fortement impactée par la concurrence
3. la compréhension des problèmes liés à la concurrence est importante lorsqu’un travail est mené en environnement web ou conteneurisé

Le constat est donc simple : la concurrence implique obligatoirement un surcoût de développement et sa mise en œuvre est complexe. Les bogues ne sont majoritairement pas reproductibles et la correction de ceux-ci est souvent complexe.

Par conséquent, les bonnes pratiques induisant un clean code dans le cadre de la concurrence commencent à nouveau par le respect du SPR. Il est plus important que jamais dans le cadre du multi-threading et vous permettra de limiter au maximum les effets négatifs de votre code sur votre programme.

Il est ensuite fortement encouragé de décorréler le code propre à la concurrence du reste du code applicatif. Vous devrez dans le même esprit limiter la portée de vos données. Plus celles-ci seront accessibles, plus vous serez susceptible de créer des bugs ou des conflits liés à la concurrence.

Enfin, il est fortement recommandé de rendre chaque thread indépendant. Plus vous limiterez les interactions entre différents threads, plus vous limiterez le nombre de bugs potentiels.

En résumé, l’application du clean code à la concurrence consiste majoritairement en l’anticipation des problèmes, grâce au respect des quelques règles particulières énoncées ici, ainsi que de toutes celles déjà évoquées !
