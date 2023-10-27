Il existe quatre règles majeures à suivre pour obtenir un clean code : 

- 100% des tests doivent être verts
- Pas de redondance de code
- Utilisation de l’expressivité
- Respect du SPR

Faisons quelques rappels pour chacune de ces règles.

## 100% des tests sont verts

Le clean code établit comme principe qu’un système non testable est équivalent à un système non vérifiable, et par conséquent propice à trouver différents bugs et/ou problèmes. Les tests sont donc l’assurance d’un système vérifiable, et testable à tout moment du développement. Les tests permettent également de remanier ou refactorer le code tout en sachant à chaque fois si l’on a cassé quelque chose ou pas.

## Pas de redondance

La redondance de code est l’ennemi numéro 1 d’un code propre. Utilisez les fonctions et les classes au maximum pour éviter la redondance de code et les failles impliquées. Prenons un exemple : vous devez vérifier si une personne est majeure ou non au sein de votre code. Vous faites une simple comparaison “<= 18” dans votre code. Aux premiers abords, vous n’avez aucun besoin de positionner cette comparaison dans une fonction, parce que l’âge de la majorité (18 ans) ne changera vraisemblablement pas régulièrement, voire jamais. 

Or ce biais de pensée peut conduire à de la redondance de code et donc à des problèmes futurs. Si par exemple vous utilisez cette condition 4 fois au sein de votre code, et que votre application vient d’être vendue aux USA pour vérifier le droit de boire de l’alcool (âge légal 21 ans), alors vous devrez retrouver toutes vos comparaisons dans votre code, tandis que vous auriez pu simplement modifier une fonction…

Imaginez une condition de la sorte pour vérifier si une personne est majeure et à le droit de toucher des aides d’un pays. Si l’âge de la personne est de 150 ans, la condition sera respectée, et donc la personne en question pourra obtenir de l'aide. Sauf qu’à 150 ans, on est plus probablement mort qu’en capacité de toucher n’importe quelle aide… 

Aussi le fait de ne pas regrouper le code redondant peut mener à des manques de vérification ou à des problématiques majeures au sein d’un système, et il est primordial de le prendre en compte !

## Expressivité

Plus un code est expressif, plus il est généralement simple à comprendre. Cela concerne aussi bien les noms de variables, que de fonctions, classes, commentaires, etc… C’est une règle donc récurrente, mais qui reste au cœur du dispositif du clean code.

L’idée derrière est que plus le temps passe sur un projet, plus le code est compliqué à comprendre. Aussi, garder une expressivité forte permettra de réduire cet effet de bord et permettra de garder aussi longtemps que possible un code parfaitement compréhensible.

## SPR

Le principe de responsabilité unique (SPR - _Single Principle Responsibility_) est au centre de tout clean code. Il établit que chaque élément d’un code ne doit avoir qu’une et une seule responsabilité.

Le suivi de cette règle simplifie généralement la phase de test et favorise l’exhaustivité desdits tests. Par ailleurs, l’application de ce principe permet majoritairement de conserver chaque partie du système aussi petit que possible et donc contribue nettement à la simplification du code et de sa compréhension.