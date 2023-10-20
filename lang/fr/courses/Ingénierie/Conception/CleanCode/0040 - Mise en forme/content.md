Souvenez-vous des trois caractéristiques principales d’un Clean Code : **expressif**, **évident**, et **sexy**. Et devinez quoi ? Le sex appeal d’un code est similaire à celui d’un humain : on juge d’abord l’apparence ! Il est donc important que l’aspect visuel de votre code donne envie de le lire, mais également qu’il respecte une certaine logique.

La mise en forme d’un code est la première communication existante entre plusieurs développeurs. Aussi, si une mauvaise communication peut souvent entraîner des échecs, il en va de même pour le code. Cette mise en forme se travaille selon deux axes différents : l’axe vertical, et l’axe horizontal.

## Axe vertical

L’axe vertical, comme son nom l’indique, représente l’aspect du fichier de haut en bas. Et concernant ce point, le premier facteur à prendre en considération est la longueur totale du fichier. Plus votre fichier sera long, moins il sera facile à appréhender. Faites donc attention à bien séparer votre code dans différents fichiers, chacun regroupant des intentions différentes.

Le second point consiste à raconter votre code, plutôt que de l’expliquer. Un code se raconte comme on raconte une histoire : d’abord on présente le contexte et les protagonistes, puis on pose la trame, qu’on déroule ensuite avant de conclure. La rédaction d’un fichier de code doit être similaire : Le code doit être expliqué dans l’ordre où il intervient. Si vous avez trois méthodes, une méthode A utilisant une méthode B, utilisant elle-même une méthode C, alors vous devez d’abord positionner la méthode A, puis la B, puis enfin la C. Ne présentez pas la méthode C avant de l’avoir contextualiser grâce à B, il en va de même pour B vis-à-vis de A !

Vous devez ensuite considérer l’espacement des différents concepts. Plus vos lignes seront rapprochées, plus le concept rattaché sera proche, à contrario plus les lignes seront éloignées, plus le concept sera lointain. Dans le cadre d’un bloc d’instructions, toutes les lignes du même bloc seront positionnées les unes à la suite des autres, sans séparation. A contrario, si vous devez séparer deux blocs d’instructions, alors une ligne vide sera insérée entre ceux-ci. De la sorte, vous obtenez visuellement un découpage des concepts et vous pouvez mieux segmenter la lecture de votre code pour encore faciliter sa compréhension.

Toujours dans l’esprit de distanciation, et en lien avec l’idée de raconter une histoire,  il est important d’éviter de trop nombreux aller-retours haut-bas dans la lecture de votre fichier afin de le comprendre.

Les variables sont souvent sujet à mauvaise interprétation lorsqu’elles sont mal positionnées. Leur contexte va donc influer selon si elles doivent être placées juste avant leur utilisation, ou bien au début d’un bloc. Il n’y à en réalité besoin de considérer que deux contextes ici : le contexte procédural et le contexte objet. Dans le premier cas, on considère que les variables doivent être déclarées au plus près de leur utilisation. Dans le second, il est d’usage de les déclarer au tout début de la classe.

En résumé succinct, il faut considérer l’affinité entre les différentes lignes de code que vous rédigez : plus l’affinité sera importante, plus les lignes de code doivent être proches. Plus l’affinité est faible, plus elles doivent être éloignées. Attention, il n’est pas pour autant question de séparer deux fonctions par 15 lignes vides si leur affinité n’est pas forte : c’est inutile…

## Axe horizontal

Le traitement de l’aspect visuel du code sur l’axe horizontal est bien plus discuté que pour l’aspect vertical. Pour comprendre cela, il faut remonter dans les années 1960 durant lesquelles IBM à mis au point les premières cartes perforées montrant les caractères avec les représentations binaires. Celles-ci s'étendaient sur 80 colonnes, et c’est partiellement de ce fait qu’aujourd’hui encore il est estimé qu’une ligne de code ne doit pas excéder 80 caractères. Par la suite, la majorité des ordinateurs qui sont apparus et ont commencé à être utilisés par le grand public disposaient d’un écran qui - lui aussi - n’affichait que 80 caractères par ligne. Comme vous vous en doutez déjà, les ordinateurs et écrans d’aujourd’hui permettent d’afficher un nombre de caractères bien plus grand (au moment où j’écris ces lignes, mon logiciel me permet de rédiger 290 caractères sur une seule ligne avec un logiciel standard…). Cette norme de 80 caractères à donc évoluée, et est passée pour certains à 100 ou encore 120 caractères. Certains standards de langages de programmation proposent en chiffres, certaines sociétés un autre… Retenez-donc que la norme standard de base est de 80 caractères par ligne, mais qu’on ne pourra pas vous en vouloir de figer à 100 ou 120 votre limite tant qu’elle reste cohérente avec votre projet et votre équipe.

Second point horizontal important : la séparation des opérateurs d’affectation (les symboles “=” dans la majorité des langages). Ceux-ci doivent impérativement être entourés d’espaces afin de les démarquer davantage des autres informations. Ici encore, cela induit un repère visuel démontrant une affectation de valeur.

Les fonctions et leurs arguments étant étroitement liés, il n’y a théoriquement pas d’intérêt à séparer le nom de la fonction de ses parenthèses par un espace. Cependant, pour des questions de lisibilité, il est plus pertinent de séparer les arguments par des espaces à l’intérieur des parenthèses.

Certaines personnes réalisent encore aujourd’hui (grâce à des plugins dont le monde se passerait bien…) des alignements horizontaux. Cette technique est à proscrire purement et simplement. Outre le fait de ne pas apporter de clarté particulière, elle peut s’avérer chronophage et casser le dynamisme de la lecture d’un code. Imaginez un livre où les mots seraient séparés d’un nombre aléatoire entre 1 et 10 espaces selon le nombre de caractères qui les composent. Nous n’aborderons pas non plus la question de la maintenance pour des raisons évidentes…

Le dernier point, et pas des moindres, concerne l’indentation ! Qu’est-ce que l’indentation ? C’est tout simplement le fait d’ajouter des espaces au début de chaque ligne. Une bonne indentation est primordiale, et si certains langages comme Python l’obligent car se basent dessus pour l’interprétation du code, il n’en est pas de même pour tous les autres langages. Ainsi il est extrêmement important d’indenter le code correctement pour séparer les différents blocs de code visuellement. Une bonne indentation est soit représentée par 2 ou 4 caractères d’espacement, soit par 1 caractère de tabulation (selon les préférences établies au sein de chaque équipe / entreprise). Je favorise à titre personnel les tabulations de 4 espaces. Chaque bloc de code n’étant contenu dans aucune autre bloc ne doit pas être indenté. Par contre, à chaque fois qu’un nouveau bloc est inséré au sein d’un bloc déjà existant, il est pertinent de rajouter un niveau d’indentation pour ainsi être informé de sa contenance visuellement. Voici un exemple permettant de mieux comprendre la chose : 

```
bloc 1 {
    bloc 2 { }

    bloc 3 {
        bloc 4 {}
    }
}
```

Dans l’exemple ci-dessus, le bloc 1 n’a pas de bloc “parent”. Il n’est donc pas indenté, que cela soit au niveau de l’ouverture, ou de la fermeture. Le bloc 2 est quant à lui intégré au bloc 1, il est donc indenté de 4 espaces afin de savoir visuellement à quel bloc il appartient.
Même chose pour le bloc 3, qui suit simplement le bloc 2 et est également contenu dans le bloc 1. Quant au bloc 4, celui-ci est contenu dans le bloc 3, on ajoute donc 4 espaces d’indentation au début de la ligne à l'indentation déjà existante afin de signifier son appartenance au bloc n°3.

**NB** : Pour les utilisateurs de VSCode, j’utilise à titre personnel un petit plugin du nom de “rainbow-indent” que m’a fait découvrir un étudiant, et que je trouve particulièrement efficace !

## Résumé

En résumé, il faut considérer l’ensemble des règles que nous vous avons présentées. Il faut cependant largement considérer ici que les règles à appliquer sont d’abord et avant tout celles fixées par votre équipe. Aussi, la maintenance se fera également par votre équipe, donc ne changez pas de règle si l’équipe entière ne l’a pas décidé.
