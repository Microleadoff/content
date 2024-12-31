# Contenu de ./0010 - Site statique vs site dynamique/content.md

Les sites web se divisent en trois types différents : statiques et dynamiques. Les sites statiques sont ceux qui sont fixes et affichent le même contenu pour chaque utilisateur, généralement écrit exclusivement en HTML. Un site web dynamique, en revanche, est un site qui peut afficher un contenu différent et offrir une interaction avec l'utilisateur, en utilisant une programmation avancée et des bases de données en plus du HTML. Comme vous pouvez le constater, les sites web statiques sont plus faciles à créer, tandis que les sites web dynamiques demandent plus de travail.

Avant d'entrer dans les détails de chaque type de site web, vous devez comprendre comment l'Internet s'y prend pour fournir des sites web en premier lieu. La communication Internet implique un serveur et un navigateur web.

Pour établir une connexion entre les deux, un ensemble de règles appelé Hypertext Transfer Protocol (HTTP) est utilisé. En termes simples, le navigateur web transmet une demande HTTP au serveur, qui lui répond par une réponse HTTP accompagnée de la page web demandée en HTML.

## Site statique

Les sites web statiques comportent généralement un nombre fixe de pages avec une mise en page spécifique. Lorsque la page s'exécute sur un navigateur, le contenu est littéralement statique et ne change pas en réponse aux actions de l'utilisateur. Un site web statique est généralement créé avec du HTML et du CSS

Si vous avez besoin d'un site web de moins de trois pages, opter pour un site web statique est le bon choix. Sa création ne demande pas autant de temps et d'efforts que celle d'un site dynamique. Si les pages de votre site doivent avoir un aspect différent, le code HTML peut facilement être dupliqué sur chacune de ces pages, avec les modifications nécessaires.

Même si le site web affiche la même chose, sans détails de navigation complexes, les sites web statiques ne doivent pas nécessairement contenir uniquement du texte. En fait, vous pouvez utiliser divers éléments multimédias et des vidéos. Un site web HTML peut être magnifique, mais le code source de la page ne changera pas, quelles que soient les actions effectuées par l'utilisateur.

## Site dynamique

Par rapport aux sites web statiques, qui sont purement informatifs, un site web dynamique est plus fonctionnel. Il permet aux utilisateurs d'interagir avec les informations figurant sur la page. Bien sûr, cela nécessite d'utiliser plus que le simple code HTML.

Les sites web statiques n'utilisent que du code HTML et CSS côté client, tandis que les sites web dynamiques reposent sur des langages de script côté client et côté serveur, tels que JavaScript, PHP ou ASP. Lorsqu'un utilisateur accède à un site web dynamique, le site peut être modifié grâce à un code exécuté dans le navigateur et/ou sur le serveur. Le résultat final est le même que celui d'un site web statique : une page HTML affichée sur le navigateur web.

Pour générer du contenu dynamique, ces sites web utilisent une combinaison de scripts côté serveur et côté client. Le script côté client fait référence au code qui est exécuté par le navigateur, généralement avec JavaScript. Quant au script côté serveur, il s'agit du code exécuté par le serveur (avant que le contenu ne soit envoyé au navigateur de l'utilisateur).

# Contenu de ./0020 - Installation d'un serveur local/content.md

Lors du développement d'un site Web, le concepteur doit être en mesure de voir ses pages Web de la même manière que l'utilisateur final. Parfois, le simple fait de cliquer sur vos fichiers HTML et de les visualiser dans le navigateur Web est suffisant, mais si vous voulez tester du contenu dynamique, vous devrez configurer un serveur Web local. Cette opération est assez simple et peut être réalisée facilement sous Windows, macOS et Linux. Il existe de nombreux types de serveurs Web, mais nous utilisons Apache dans ce tutoriel, car il s'agit du serveur le plus courant, très facile à configurer et compatible avec tous les principaux systèmes d'exploitation.

## Installation sous Windows

Téléchargez la version Windows de XAMPP sur le site officiel <a href="https://www.apachefriends.org/index.html" title="téléchargement d'apache" target="_blank">https://www.apachefriends.org/index.html</a> et commencez l'installation. Suivez les instructions de l'installateur.

## Installation sous Linux

Apache a été conçu pour les systèmes d'exploitation de type Unix. Linux fait partie de cette catégorie, et l'installation et la configuration d'un serveur web Apache peuvent se faire en une seule étape.

Nous traiterons ici de la ligne de commande. La plupart des distributions populaires vous permettent d'installer Apache sans le compiler à partir des sources en utilisant une simple commande.

**Pour Debian, Ubuntu :**

``` 
sudo apt install apache2
```

**Pour CentOS :**

```
sudo dnf install httpd
```

"127.0.0.1" ou "localhost" dans votre navigateur web permet de voir la page par défaut de Apache.
Les fichiers sont à mettre dans ce dossier ```cd /var/www/html```.

## Installation sous macOS

L'avantage de macOS est qu'Apache y est installé par défaut. Tout ce que vous avez à faire est de l'activer.

Dans le Finder, allez dans "Applications -> Utilitaires", puis double-cliquez sur Terminal pour l'ouvrir.

```
sudo apachectl start
```

"127.0.0.1" ou "localhost" dans votre navigateur web permet de voir la page par défaut de Apache.

Les fichiers sont à mettre dans ce dossier ```cd /Library/WebServer/Documents/```.

# Contenu de ./0030 - Où mettre du PHP dans un fichier ?/content.md

Le PHP est un langage de programmation informatique. Tout comme les autres, il est nécessaire de créer des fichiers qui vont contenir le code réalisé afin qu’il puisse ensuite être interprété par une machine. Les fichiers contenants du PHP doivent posséder l’extension ```.php``` afin de signifier leurs types aux ordinateurs, de telle sorte à ce que ceux-ci puissent les interpréter.

Une fois l’extension définie, il faut délimiter le code à interpréter au sein d’un fichier PHP. Pour cela, il faut placer l’ensemble du code PHP entre la balise ouvrante <code>&lt;?php</code> et la balise fermante <code>?&gt;</code>. Tout le code situé au milieu de ces deux balises sera supposé être du PHP et donc interprété comme tel par la machine.

Il faut ici noter deux notions importantes :

- Un fichier PHP ne contient pas obligatoirement uniquement du PHP. Il peut par exemple contenir du HTML, ou bien encore du CSS. Il ne faut donc pas être étonné de trouver du code “étranger” au sein d’un fichier PHP. Il n’est d’ailleurs pas rare de transformer un fichier HTML en PHP lorsque l’on souhaite ajouter du PHP au sein d’un fichier HTML existant. Pour ce faire, il suffit de changer l’extension du fichier de ```.html``` à ```.php```.
- Il est possible d’intégrer plusieurs balises ouvrantes et fermantes au sein d’un seul et même fichier PHP. La seule règle concernant ce point réside dans le fait de bien respecter l’ordre d’utilisation de celles-ci : Toute balise ouverte doit être fermée avant d’en ouvrir une autre !

Il reste néanmoins possible de réaliser des fichiers en PHP uniquement. Dans ce cadre-là, il arrive qu’il ne faille pas mettre de balise fermante en fin de fichier, mais uniquement une balise ouvrante au début de celui-ci. La règle de l’extension en ```.php``` reste inchangée.

En développant en PHP, et en fonction des projets à concevoir, il est possible que le code à rédiger soit bien trop important pour n’être contenu que dans un seul et même fichier. Il faut donc bien noter qu’il est convenable de créer autant de fichiers PHP que souhaité.

# Contenu de ./0040 - Utiliser les variables/content.md

## Qu’est-ce qu’une variable ?

Une *“variable”* est une sorte de conteneur qui permet de stocker une information. Elle peut stocker un nombre, un texte, une date, une heure, ou bien tous types d’informations existants en programmation. 

Les variables sont souvent amenées à évoluer dans le temps, au fur et à mesure de l’exécution du code par la machine. Ainsi, une variable peut changer de valeur autant de fois souhaité au cours du script, tout aussi bien qu’elle peut garder une seule et même valeur tout du long de l’exécution du programme.

Les variables ont cependant une durée de vie : elles sont automatiquement supprimées à la fin de l’exécution du script dans lequel elles sont utilisées.

## À quoi sert une variable ?

Les variables représentent à elles seules les bases de la programmation, et ce sont grâce à elles que vous allez pouvoir mettre en place votre logique au sein d’un script. La première utilisation qu’un développeur est amené à faire lors de son apprentissage concerne la manipulation de données.

Imaginons par exemple un programme demandant un nombre à un utilisateur et lui renvoyant ensuite la valeur du carré de ce nombre. Voici un exemple d’algorithme simple en 3 étapes qui pourrait être utilisé pour un tel script : 

1. demande de saisie d’un nombre à l’utilisateur
2. réalisation du calcul
3. affichage du résultat du calcul à l’utilisateur

Lors de l’étape (2), le calcul en lui-même est simple : il suffit de multiplier le nombre par lui-même. La difficulté ici réside dans le fait que lors de l’écriture du programme, le nombre saisi par l’utilisateur n’est pas connu. Ainsi, il n’est pas possible de prévoir un calcul à l’aide de nombres. Par exemple, nous ne pouvons pas faire “2*2” sans savoir si le nombre qu’aura choisi l’utilisateur est bien “2”. Idem, il n'est pas possible de prévoir des calculs pour tous les nombres existants.

C’est donc ce genre de problèmes et questionnements que les variables vont nous permettre de résoudre. Nous allons pouvoir déclarer une variable (que nous appellerons *“nombre”* pour l’exemple), et ainsi transformer les étapes de l’algorithme précédent de la sorte : 

1. demande de saisie d’un nombre à l’utilisateur et **stockage de ce nombre dans la variable “*nombre*”**
2. réalisation du calcul : “**nombre * nombre**”
3. affichage du résultat du calcul à l’utilisateur

De cette manière, et grâce à l’utilisation des variables, nous allons donc pouvoir commencer à mettre en place une logique, avec des données inconnues stockées dans des variables.

Les variables vont également nous permettre de faire passer certaines valeurs d’une page d’un site web à une autre. De la même façon que pour l’exemple de calcul ci-dessus, nous pourrons stocker des valeurs au sein de variables, puis les “envoyer” vers d’autres pages web, de telle sorte à faire transiter des informations d’une page à une autre. Nous pourrions illustrer ce fait par exemple avec la réalisation d’un formulaire de connexion. L’utilisateur renseigne son adresse mail ainsi que son mot de passe, et ceux-ci sont ensuite transmis à une autre page qui va se charger de faire la vérification des éléments.

Dans le cadre d’un développement web en PHP, les variables peuvent aussi vous permettre de dynamiser l’apparence de votre site internet. Vous pourrez par exemple créer une variable “*couleur*”, qui pourra changer selon certaines conditions que vous aurez définies, et indiquer à votre site web d’afficher telle ou telle partie de votre site selon la couleur définie dans votre variable.

## Les variables dans du code PHP

### Règles de nommage

Tout comme chaque langage de programmation, il existe de nombreuses normes, règles et conventions en PHP, et les variables en font pleinement  partie. Voici donc quelques règles de base :

- En PHP, la déclaration d’une variable doit toujours s’effectuer avec le symbole ```$``` qui précède le **nom** de la variable. Par exemple : ```$name```.
- Le premier caractère suivant le symbole du dollar ```$``` doit être obligatoirement **une lettre ou un underscore**. Par exemple : ```$_var``` ou ```$var```.
- Le nom de la variable ne doit pas contenir de caractères spéciaux à l’exception de tirets. Sont autorisés les tirets ```-```, les underscores ```_```, et les lettres et chiffres.
- Les noms des variables sont dits “sensibles à la casse”, c'est-à-dire qu’une variable ne dispose que d’un nom, et si un des caractères composants ce nom est en majuscule, alors il devra l’être également pour la réutilisation de cette variable. Notez par exemple que ```$variable``` et ```$variAble``` sont deux noms de variables distinctes, et par conséquent que l’utilisation de ceux-ci entraînera l’utilisation de 2 variables obligatoirement (et non une seule).
- Certains noms de variables sont réservés, par exemple les variables appelées “Superglobales” que nous apprendrons à utiliser plus tard.
- En PHP, le nommage des variables doit être effectué selon le principe du camelCase.

### Utilisation

#### Déclaration et stockage de variable

Comme vu précédemment, pour déclarer une variable, il faut commencer par le symbole ```$```, puis y accoler le nom souhaité. De la sorte, si l’on souhaite créer une variable qui s’appelle “variable”, et qui contient le mot “Bonjour”, alors il faudra faire de la sorte : 

```php
$variable = "Bonjour";
```

Si on souhaite créer une variable “nombre”, et lui affecter la valeur “0” (zéro), alors il faudra faire : 

```php
$nombre = 0;
```

#### Affichage de variable

Il existe deux différentes méthodes afin d’afficher une variable en PHP. En effet, ce dernier nous livre deux fonctions : ```echo()``` et ```print()```

Reprenons les mêmes exemples qu’au-dessus, si l’on souhaite créer une variable qui s’appelle “variable”, et qui contient le mot “Bonjour”, et ensuite afficher le contenu de cette variable, il sera possible de faire : 

```php
# déclaration de la variable et affectation de la
# valeur "Bonjour"
$variable = "Bonjour"

# méthode 1
print($variable)

# méthode 2
echo($variable)
```

# Contenu de ./0050 -  L'opérateur d'assignation/content.md

L’opération d’assignation est le signe ```=```. Contrairement à ce que l’on peut penser, ce signe ne veut pas dire “égale à”, il signifie que l’opérande de gauche est affectée par la valeur de l’expression de droite qui est située après le signe ```=```.

Exemple :

```php
<?php
$a = ($b = 2) + 3;
// $a est maintenant égal à 5, et $b vaut 2.
```

Il est également possible d’assigner simplement une valeur, afin de la réutiliser par la suite : 

```php
<?php
$maVariable = "Hello World !";
// $maVariable peut être modifiée par la suite, ou bien utilisée simplement pour afficher son contenu.
```

Chaque affectation de valeur remplacera la précédente, de telle sorte que : 

```php
<?php
$a = 3;
// $a vaut 3
$a = 4;
// $a vaut 4;
```

# Contenu de ./0060 - Utiliser les constantes/content.md

Une constante est un conteneur qui permet de stocker une ou plusieurs informations. Elle est similaire aux variables dans le sens où n’importe quel type de donnée peut être stocké, et que ce stockage est temporaire puisque la constante disparaît à la fin de l’exécution du script.

La différence majeure entre une constante et une variable réside dans le fait que la première n’est pas modifiable une fois définie. C'est-à-dire qu’il est possible de se servir de sa valeur, de ce qu’elle contient, mais pas de modifier son contenu une fois défini.

Lors de l’apprentissage de la programmation, il n’est pas rare de se poser la question de l’intérêt des constantes, pourquoi donc utiliser autre chose qu’une variable ?

La réponse est souvent simple : il n’est pas obligatoire de s’en servir. Cependant, attention, même si l’utilisation des constantes reste optionnelle, elles permettent d’apporter de la sémantique et de la clarté dans le code. En effet, les valeurs des constantes n’étant pas modifiables en cours de script, l’utilisation de celles-ci survient généralement pour définir les différents paramètres des scripts et applications. En procédant de la sorte, il est possible d’un simple regard sur le code de déterminer si une variable est utilisée pour un algorithme précis, ou bien si une constante est utilisée de manière globale.

## Les constantes au sein du PHP

### Règles de nommage

Il existe quelques règles de nommage de vos constantes. Elles sont simples :

- Pas d’utilisation du symbole du dollar ```$``` - qui est réservé aux variables
- Pas de caractères spéciaux
- Tout doit être écrit en majuscule. Si plusieurs mots sont nécessaires pour nommer les constantes, il faut les séparer par le symbole “underscore” ```_```.

### Déclaration d’une constante

Il existe différentes façons de déclarer des constantes. La première méthode est d’utiliser “define” : 

```php
# déclaration d'une constante nommée "NOM", en lui affectant la valeur 
# "Microlead" :
define("NOM", "Microlead");
```

Une deuxième méthode est d’utiliser le mot-clé “const” juste avant de définir le nom de la constante. L’affectation de la valeur se fait alors de la même manière qu’une variable : 

```php
# déclaration d'une constante nommée "NOM", en lui affectant la valeur 
# "Microlead" :
const NOM = "Microlead";
```

### Affichage de la valeur d’une constante

Tout comme pour la déclaration, il existe différentes manières d’utiliser ou d’afficher la valeur d’une constante. La première est tout simplement d’utiliser le ```echo```, comme pour les variables, la deuxième est d’utiliser la fonction ```constant()``` : 

```php
# déclaration d'une constante nommée "NOM", en lui affectant la valeur 
# "Microlead" :
const NOM = "Microlead";

# Affichage de la valeur avec le "echo"
echo(NOM);
# affichera donc "Microlead"

# Affichage avec la fonction "constant()"
constant("NOM");
# affichera également "Microlead"
```

### Vérifier l’existence d’une constante

La fonction ```defined()``` de PHP permet de vérifier l’existence d’une constante par rapport à son nom. Voici un exemple :

```php
# déclaration d'une constante nommée "NOM", en lui affectant la valeur 
# "Microlead" :
const NOM = "Microlead";

# Vérification de la constante "NOM" :
defined("NOM");
# la ligne du dessus renverra "vrai"

# Vérification de la constante "MICROLEAD" :
defined("MICROLEAD");
# la ligne du dessus renverra "faux", car aucune constante "MICROLEAD" 
# n'a été déclarée.
```

# Contenu de ./0070 - Les chaînes de caractères/content.md

En informatique, est appelée chaîne de caractères une séquence de caractères. En d’autres termes, il s’agit d’un mot ou d’un texte. Une chaîne de caractères est un type de données et est plus communément appelée par sa traduction anglaise, *string*. 

Une chaîne de caractères peut aussi ne rien contenir. Il s’agira, auquel cas, d’une chaîne vide. 

## Qu’est-ce qu’une chaîne de caractères ?

- Séquence de caractères (du texte)
- Traduit en anglais par “string”
- Est un type de données
- Peut contenir aucun caractère, c’est ce qu’on appelle une chaîne vide.

## Les chaînes de caractères dans du code PHP

Comme pour le langage JavaScript, les guillemets simples et doubles sont utilisables en PHP pour entourer une chaîne de caractères. 

Le langage PHP fait la différence entre ces deux types de guillemets.

### Les guillemets simples 

Les guillemets simples (‘’) sont utilisables en PHP. C’est d’ailleurs le type de guillemets le plus communément utilisé pour entourer une chaîne de caractères. 

Exemple :

```php
echo('Ceci est une chaîne de caractères');
```

Lorsqu’une apostrophe doit être utilisée au sein d’une chaîne entourée de guillemets simples, il est nécessaire d’échapper l’apostrophe avec un antislash, afin que le navigateur ne confonde pas l’apostrophe avec un guillemet de fin de chaîne.

Exemple :

```php
echo('J\'utilise une chaîne de caractères’);
```

Cet exemple retourne bien la phrase : **J’utilise une chaîne de caractères**.

De même, si un antislash doit être utilisé comme caractère au sein d’une string, il doit également être échappé avec un antislash.

Exemple :

```php
echo('Les fichiers se trouvent sur le disque C:\\');
```

Cet exemple donne le résultat suivant : **‘Les fichiers se trouvent sur le disque C:\’**

### Les guillemets doubles

Les guillemets doublent peuvent également être utilisés pour entourer une chaîne de caractères. L’avantage est que s’il y a besoin d’utiliser des caractères spéciaux tels qu’une apostrophe, il n’y aura pas besoin de l’échapper.

Exemple :

```php
echo("J'utilise une chaîne de caractères");
```

L’utilisation des guillemets double rend moins compliqué l’affichage du contenu d’un variable. En effet, il n’y a pas besoin d’utiliser la concaténation. 

Exemple :

```php
$var = "test";
echo("Ceci est un ${var}.");
```

L’exemple ci-dessus retourne bien la phrase **Ceci est un test**. Le contenu de la variable ```$var``` a donc été affiché correctement. 

Ce type de guillemets, comme évoqué dans l’introduction de ce point, rend aussi possible l’interprétation des caractères spéciaux tels que le ```\n```.

Exemple :

```php
echo("Ceci est une\nchaîne de caractères");
```

Voici ce que retourne cet exemple :

```
Ceci est une
chaîne de caractères
```

### Concaténation

Qu’il s’agisse de guillemets simples ou doubles, le langage PHP permet la concaténation des strings. Cela est par exemple utile pour l’affichage du contenu d’une variable.

Exemple :

```php
$var = "test";
echo("Ceci est un deuxième " . $var);
```

Cet exemple retourne bien la phrase “**Ceci est un deuxième test**”.


# Contenu de ./0080 -  Les nombres/content.md

Les nombres sont composés d’un ou plusieurs chiffres allant de 0 à 9. Un nombre peut être entier ou à virgule. En informatique, un nombre à virgule est appelé un nombre flottant ou *float*, en anglais. 

## Les nombres dans du code PHP

En PHP, il existe principalement deux types de nombres : les nombres entiers (ou *integer*, en anglais), et les nombres décimaux, également appelés flottants (ou *float* en anglais).

### Les nombres entiers

Les nombres entiers sont des nombres n’ayant pas de virgules. En anglais, ils sont appelés *integer*, et sont, dans les différents langages informatiques existants, raccourcis sous le nom de **int**.

Par exemple, le nombre 20 est considéré comme un **int** par PHP.

### Les nombres décimaux

Les nombres à virgules, appelés par leur nom anglais *float* représentent tous les nombres décimaux existants. 

Par exemple, 20.6 est un float.

__Remarque__ : En PHP, comme pour beaucoup d’autres langages, lorsqu’un nombre décimal est écrit, le point est utilisé comme virgule. Ainsi, 20.6 est reconnu par PHP, tandis que 20,6 ne l’est pas.

### Conversions

Il y a des situations dans lesquelles un **int** a besoin d’être converti en **float**, et inversement. Le langage PHP permet cela en mettant à disposition les deux fonctions suivantes : 

- ```intval()``` : cette fonction prend en paramètre le nombre décimal à convertir en nombre entier et retourne le résultat de la conversion
- ```floatval()``` : prend en paramètre le nombre entier à convertir en **float** et retourne le résultat de la conversion

Exemple :

``` php
intval(45.1); // Retourne 45
floatval(124); // Retourne 124.0
```

# Contenu de ./0090 - La constante NULL/content.md

Il est recommandé de toujours initialiser une variable lors de sa déclaration. Cela évite des erreurs ou des résultats inattendus dus au fait qu’une valeur au hasard a été attribuée à la variable par la mémoire de l’ordinateur. 

Seulement voilà, se pose le problème suivant : comment faire si une variable doit être déclarée, mais que sa valeur n’est pas connue de suite par le programme - principalement parce que c’est une valeur fournie par l’utilisateur ?

C’est justement pour résoudre ce problème que la constante **NULL** entre en jeu. **NULL**, en fait, représente la valeur 0 - ou null. Cette valeur **ne peut pas être modifiée** (ce qui est le principe fondamental d’une constante). 

Ainsi, en PHP, **NULL** est passé en valeur à une variable lors de sa déclaration, lorsque la vraie valeur n’est pas connue par avance. 

Exemple :

```php
$variable = NULL;
```

# Contenu de ./0100 - Les booléens/content.md

Un booléen est un type de donnée qui peut avoir seulement deux états : soit vrai (la valeur anglaise **true** est utilisée), soit faux (la valeur anglaise **false** est utilisée).

Avec les booléens, **true** vaut 1, tandis que **false** vaut 0.

## Les booléens dans du code PHP

### Les variables

Il est possible de créer des variables de type booléens. Pour ce faire, il suffit de passer la valeur **true** ou **false** à ces variables.

Exemple :

``` php
$var1 = true;
$var2 = false;
```

### Les conditions

Les conditions **if**, **else if**, ou encore **else** retournent, d’une manière ou d’une autre, toutes un booléen, car leur but est de tester si une condition est vraie ou fausse. 

Exemple :

``` php
$var1 = true;
if($var1 == true){
    echo("Oui");
}else{
    echo("Non");
}
```

L’exemple ci-dessus retourne oui, puisque ```$var1``` vaut **true**.

# Contenu de ./0110 - Les commentaires/content.md

Les commentaires sont en programmation un moyen de laisser des explications ou des informations dans votre code. La particularité du commentaire est qu’il n’est pas utilisé de la même manière que le reste de votre code étant donné que la machine ne l’interprète pas. La cible d’un commentaire est donc le développeur ou le lecteur d’un code.

Les commentaires sont souvent sujets à débats, surtout durant les premiers pas en développement, et il n’est pas rare d’entendre différentes phrases sur le sujet : 

- “Quel est l’intérêt ? C’est mon code, je le connais !”
- “Trop de lignes à écrire, mon code est moins lisible”
- “Pourquoi écrire des choses inutiles pour l’ordinateur ?”

En réalité, il existe autant d’interrogations qu’il existe de mauvaises explications… Les commentaires doivent faire partie intégrante du code. L’idée ici n’est pas de commenter la moindre ligne écrite, mais bien de rajouter des notes, explications ou informations sur telle ou telle partie de code. Le fait qu’ils semblent parfois inutiles est souvent lié au fait qu’il est rédigé par le créateur même du code, et donc que celui-ci sait ce qu’il contient et ce qu’il fait. Cependant, si une autre personne est amenée à modifier ce code, alors peut-être que celle-ci ne comprendra pas correctement ce que fait le code, ni même la logique appliquée. Par ailleurs, travailler sur un code complexe et devoir le modifier 6 mois plus tard entraîne généralement des problèmes, même au développeur ayant rédigé le code initial. Il n’est en effet pas rare dans ces conditions que les détails du code initial aient été oubliés, ce qui entraîne indéniablement une complexification des modifications à apporter.

Il faut ainsi garder en tête qu’un code professionnel est généralement apparenté à un code bien commenté. C’est d’ailleurs pourquoi certaines “normes” de codages incluent obligatoirement l’utilisation de commentaires, et PHP ne fait pas exception à cette règle…

De manière générale, le code écrit doit être rédigé en anglais, les commentaires également. C’est une convention internationale et la majorité des entreprises suivent ce chemin. Ainsi est recommandé de prendre rapidement l’habitude d’écrire l’ensemble de vos commentaires en anglais, afin de gagner en rapidité de travail par la suite.

Les commentaires peuvent par ailleurs servir à générer automatiquement des documentations de code. Ce n’est pas le moindre des arguments pour vous encourager à les utiliser, mais cela implique néanmoins de se conformer à une certaine nomenclature dans leur écriture. Il existe plusieurs outils permettant de générer des documentations à partir de commentaires, l’un des plus utilisés en PHP est “PHP Documentor”.

## Insérer des commentaires en PHP

Il existe deux moyens d’écrire des commentaires dans du code PHP. L’un permet de n’en écrire que sur une seule ligne, alors que l’autre vous permet d’en écrire sur plusieurs lignes.

### Sur une seule ligne

Deux symboles permettent de déclarer un commentaire sur une ligne : le “dièse” aussi appelé “hashtag” (**#**), ou bien le “double slash” (**//**).

À partir du moment où l’un de ces symboles est utilisé, alors la suite de la ligne est considérée comme étant un commentaire. Par exemple :

``` php
// Ceci est un commentaire sur une ligne complète
mais ici ce n'est plus un commentaire
echo('coucou'); // et ici encore un commentaire qui ne sera pas interprété

# Ceci est également un commentaire sur une ligne
echo('au revoir'); # et un dernier commentaire non interprété.
```

Quelques explications détaillées sur l'exemple ci-dessus : 

- **ligne 1** : La ligne est un commentaire, car débute par “ **//** “.
- **ligne 2** : La ligne ne commence ni par “ **//** “ ni par “ **#** “. PHP ne prendra donc pas cette ligne pour un commentaire et créera une erreur, parce qu'il va essayer d’interpréter la phrase comme du code.
- **ligne 3** : le commentaire commence à partir du symbole “ **//** “. Tout ce qui est placé avant va ainsi être interprété : la page affichera ici “coucou” à l’écran.
- **ligne 4** : La ligne est un commentaire, car débute par “ **#** “.
- **ligne 5** : Le commentaire commence par le symbole “ **#** “. Tout ce qui est placé avant va ainsi être interprété : la page affichera ici “au revoir”.

### Sur plusieurs lignes

Les commentaires écrivent sur plusieurs lignes commencent par les symboles “ /* “ (slash étoile), et se terminent par le symbole “ */ “ (étoile slash). Voici un exemple de commentaire sur plusieurs lignes : 

``` php
/*
Ceci est 
un commentaire
sur plusieurs
lignes
*/
```

Dans l’ensemble du code présenté ci-dessus, aucune ligne ne sera interprétée par PHP étant donné que tout est placé entre les symboles de début et de fin de commentaire multiligne.

#### Astuce

Il peut, certaines fois, arriver de vouloir supprimer une partie d’un code. Une astuce consiste à commenter ce code grâce aux commentaires plutôt que de l’effacer. Vous pourrez de la sorte aisément revenir en arrière si besoin. Attention tout de même à ne pas laisser de code commenté une fois finalisé : il est important de garder un code propre et professionnel, et donc de supprimer tout code inutile et non fonctionnel régulièrement.

# Contenu de ./0120 - Les opérateurs/content.md

Les opérateurs sont utilisés pour effectuer des opérations sur les variables et les valeurs.

Le langage PHP répartit les opérateurs dans les groupes suivants :

- Opérateurs arithmétiques
- Opérateurs d'assignation
- Opérateurs de comparaison
- Opérateurs d'incrémentation/décrémentation
- Opérateurs logiques
- Opérateurs de chaîne de caractères
- Opérateurs de tableaux

## Opérateurs arithmétiques

Les opérateurs arithmétiques sont utilisés avec des valeurs numériques pour effectuer des opérations, comme l'addition, la soustraction, la multiplication, etc.

## Opérateurs d'affectation

Les opérateurs d'affectation sont utilisés avec des valeurs numériques pour écrire une valeur dans une variable.

## Opérateurs de comparaison

Les opérateurs de comparaison sont utilisés pour comparer deux valeurs.

## Opérateurs d'incrémentation / décrémentation

Les opérateurs de décrémentation sont utilisés pour décrémenter la valeur d'une variable et les opérateurs d'incrémentation sont utilisés pour incrémenter la valeur d'une variable.

## Opérateurs logiques

Les opérateurs logiques sont utilisés pour combiner des déclarations conditionnelles.

## Opérateurs de chaînes de caractères

Le langage PHP possède deux opérateurs spécialement conçus pour les chaînes de caractères.

## Opérateurs de tableaux

Les opérateurs de tableaux sont utilisés pour comparer des tableaux.

# Contenu de ./0130 - PSR - Introduction/content.md

PSR est l’acronyme anglais de *PHP Standard Recommendation* (Bonnes pratiques de programmation en PHP). Il en existe à ce jour 20, qui présentent chacune des recommandations sur des sujets génériques aussi bien que spécifiques en lien avec le développement PHP.

L'ensemble de ces recommandations sont rédigées par un groupe qui s'appelle le PHP-FIG (PHP Framework Interop Group). Ils étudient ainsi l'ensemble des propositions qui peuvent être réalisées par n'importe quel développeur.

Chaque PSR concerne donc un sujet spécifique ou générique et énonce des règles. Celles-ci ne sont pas obligatoires, mais optionnelles. Il est ainsi fortement recommandé de suivre du mieux possible l'ensemble de ces règles de telle sorte à ce que tous les développeurs PHP respectent les mêmes conventions de développement et donc par extension à simplifier la compréhension et la maintenabilité des scripts.

Chaque recommandation PSR est maintenue à jour régulièrement et leurs états sont disponibles sur le site de php-fig.org. À ce jour, 13 recommandations PSR sont acceptées, c’est-à-dire validées par PHP-fig et donc à suivre. Deux sont en brouillon, et ainsi, leurs contenus peuvent encore changer avant une validation définitive. Trois sont abandonnées et deux sont dépréciées.

## Liste des PSR par catégorie et état

Voici la liste de l’ensemble des PSR ayant été créés depuis les débuts de PHP-fig. Vous trouverez également l’état actuel de chaque PSR afin de savoir s’il est à prendre en compte ou non.

| **Numéro** | **Titre** | **État** |
| --- | --- | --- |
| 0 | Autoloading Standard | Déprécié |
| 1 | Basic Coding Standard | Accepté |
| 2 | Coding Style Guide | Déprécié |
| 3 | Logger Interface | Accepté |
| 4 | Autoloading Standard | Accepté |
| 5 | PHPDoc Standard | Brouillon |
| 6 | Caching Interface | Accepté |
| 7 | HTTP Message Interface | Accepté |
| 8 | Huggable Interface | Abandonné |
| 9 | Security Advisories | Abandonné |
| 10 | Security Reporting Process | Abandonné |
| 11 | Container Interface | Accepté |
| 12 | Extended Coding Style Guide | Accepté |
| 13 | Hypermedia Links | Accepté |
| 14 | Event Dispatcher | Accepté |
| 15 | HTTP Handlers | Accepté |
| 16 | Simple Cache | Accepté |
| 17 | HTTP Factories | Accepté |
| 18 | HTTP Client | Accepté |
| 19 | PHPDoc Tags | Brouillon |


# Contenu de ./0140 - PSR 01 - Basic Coding Standard/content.md

Le PSR 01, “Basic Coding Standard” (fr: *norme de codage de base*), a pour but de définir des règles génériques de base sur la manière de coder un script ou un programme en PHP. Ces règles concernent des généralités, des normes concernant l’architecture de dossiers et de fichiers, des normes d’encodage, ou encore des normes liées à la programmation orientée objet.

## Généralités

le PSR 01 énonce en premier lieu des généralités qu’il conviendra de respecter en toutes circonstances : 

- Les fichiers PHP doivent **impérativement** et **uniquement** utiliser les balises ```<?php``` et ```<?=```. Aucune autre possibilité ne doit être utilisée.
- Les fichiers PHP ne doivent être encodés qu’en **UTF-8 sans BOM**. Aucun autre encodage n’est autorisé dans le cadre d’une conformité PSR 01.
- Les fichiers doivent autant que possible soit déclarer des symboles (classes, fonctions, constantes…),  soit provoquer des effets secondaires (affichages divers, modifications des paramètres, etc.), mais **pas les deux**. Nous développerons davantage ce point au titre 3.
- Les namespaces et les classes doivent obligatoirement suivre le PSR d’autoloading (PSR 04)
- Les noms de classe doivent obligatoirement être déclarés en “**StudlyCaps**”. C’est-à-dire que tous les mots qui composent le nom doivent être collés, et chacun doit commencer par une majuscule.
- Les constantes de classe doivent obligatoirement être déclarées entièrement en majuscule. Si son nom est composé de plusieurs mots, alors ils devront être séparés par des “**underscore**” (**_**).
- Les noms de méthodes doivent obligatoirement être déclarés en “**camelCase**”. Cette convention d’écriture consiste en l’écriture de tous les mots, sans espace (entièrement attachés), avec les premières lettres de chaque mot en majuscule à l’exception du premier.

## Les effets secondaires

Les fichiers doivent autant que possible soit déclarer des symboles (classes, fonctions, constantes…),  soit provoquer des effets secondaires (affichages divers, modifications des paramètres, etc.), mais **pas les deux**.

Le terme “effet secondaire” fait référence à l’exécution d’une logique qui n’est pas directement liée à la déclaration d’une classe, d’une fonction, d’une constante (etc.). Ainsi, tout effet secondaire ne doit pas - dans la mesure du possible - être présent dans les mêmes fichiers que les déclarations effectuées.

Les “effets secondaires” peuvent par exemple être (liste non exhaustive) : 

- une génération de contenu
- une utilisation explicite de “**require**” ou “**include**”
- une connexion à un service externe
- une modification des fichiers de configuration
- une émission d’erreur ou d’exception
- une modification de variable globale ou statique
- une lecture ou une écriture de fichier
- ...

Voici un exemple d’un fichier contenant des effets secondaires, ainsi qu’une déclaration :

```php
<?php
// modification d'un paramètre : effet secondaire
ini_set('error_reporting', ALL);

// inclusion d'un fichier : effet secondaire
include("file.php");

// génération d'un affichage : effet secondaire
echo("<html>\n");

// déclaration
function foo()
{
    // contenu de la fonction
}
```

Dans l’exemple ci-dessus, la déclaration ne fait pas partie des “effets secondaires”. Ainsi, sa présence entraîne une non-conformité à la PSR 01. Si cette fonction ```foo()``` était enlevée, alors la conformité PSR 01 serait validée.

Voici à présent un exemple de code ne contenant que des déclarations, et donc sans effets secondaires : 

```php
<?php

// déclaration d'une fonction
function foo()
{
    // contenu de la fonction
}

// la condition de déclaration d'une fonction n'est pas
// un effet secondaire
if (!function_exists('bar'))
{
    function bar()
    {
        // contenu de la fonction
    }
}
```

## Les namespaces et noms de classes

Les namespaces et les classes doivent impérativement suivre la PSR 04 “autoloading”. Ceci incluant :

- Chaque classe doit être dans un fichier homonyme
- Chaque classe doit être dans un namespace d’au moins 1 niveau
- Les noms de classe doivent être déclarés en “StudlyCaps”

Attention, la déclaration des namespaces dépend de la version PHP utilisée. À partir de la version 5.3 (et suivantes), les namespaces doivent être déclarés de manière formelle : 

```php
<?php


// formal namespace example PHP >= 5.3
namespace Vendor\Model;

class Foo
{
    // class code here
}
```

Concernant les versions antérieures à PHP 5.3 (à partir de la 5.2), les namespaces n’existants pas, il faut dans la mesure du possible nommer les classes en préfixant leur nom de leur chemin, en séparant chaque niveau par un “underscore” :

```php
<?php

// class name declaration PHP <= 5.2
class Vendor_Model_Foo
{
    // class code here
}
```

## Les constantes de classe, propriétés et méthodes

### Constantes de classe

Les constantes de classe doivent impérativement être déclarées entièrement en majuscule en séparant chaque mot par des underscores ( _ ).

```php
<?php

namespace Vendor\Model;

class Foo
{
    const VERSION = "1.0";
    const DATE_APPROVED = "01/01/2020";
}
```

### Propriétés

Contrairement aux idées reçues, la PSR 01 ne définit aucun formalisme particulier concernant le nommage des propriétés au sein d’une classe. Cependant, trois formalismes sont évoqués :

- Le **StudlyCaps**
- Le **camelCase**
- Le **snake_case**

Si la majorité des développeurs s’accordent aujourd’hui pour favoriser le camelCase, la PSR 01 indique uniquement qu’il devrait à minima être instauré un seul formalisme en fonction d’un scope (le plus large étant le mieux). Par exemple, l’utilisation du **camelCase** dans l’ensemble d’un namespace, à défaut dans l’ensemble d’une classe, à défaut dans une méthode.

### Méthodes

La PSR 01 se termine sur les méthodes, en spécifiant que leurs noms doivent impérativement être déclarés en **camelCase**.

# Contenu de ./0150 - Les tableaux/content.md

## Qu’est-ce qu’un tableau ?

Un tableau, aussi appelé “*Array*”, est une structure de données. Il peut contenir zéro, une, ou plusieurs informations de n’importe quel type (nombre, texte, date, etc…). Il peut être organisé ou non, contenir lui-même d’autres tableaux et est dynamique tout comme l’est une variable. Son contenu peut donc évoluer au fur et à mesure de l’avancement de l’interprétation d’un script. Afin de pouvoir récupérer, créer, modifier ou supprimer des données spécifiques à l’intérieur de ceux-ci, les tableaux incluent des “**indices**”.

La compréhension d’un tableau en PHP s'apparente à la compréhension d’un tableau Excel. Pour distinguer les cases d’un tableau Excel, il faut s’appuyer sur ses coordonnées (A1, A2, A3, A4, etc.). Les “**indices**” sont de ce fait l’équivalent en PHP de ce que sont les coordonnées dans Excel.

## Les tableaux dans du code PHP

### Déclaration

Un tableau est un élément qui est contenu dans une variable. Pour le déclarer, il faut ainsi  commencer par définir une variable, puis lui affecter la valeur d’un tableau vide. Il existe 2 manières différentes de déclarer un tableau vide : 

```php
# méthode 1
$tableau : array();
```

```php
# méthode 2
$tableau = [ ];
```

Il est également possible de directement déclarer un tableau en lui affectant des valeurs. Il n’y a à ce jour plus de réelle règle quant à la nécessité de déclarer un tableau vide avant de lui insérer des valeurs plutôt que de déclarer un nouveau tableau avec les valeurs directement. Notez toutefois qu’aux débuts du développement, on ne pouvait pas se servir d’un élément non déclaré préalablement. La manière de déclarer un tableau (avec ou sans données) dépendra donc vraisemblablement des développeurs avec lesquels vous serez amenés à travailler.

Il existe plusieurs types de tableaux en PHP, et il est important de bien les connaître et les différencier pour les exploités du mieux possible par la suite.

### Tableau à index numérique

Le tableau à index numérique est le plus basique de tous les tableaux. Il consiste uniquement en une suite de valeurs, chacune d’entre elles séparée par une virgule. Comme expliqué en introduction et comme l’indique le titre de cette partie, chaque tableau à index numérique dispose d’un ou plusieurs index permettant d’identifier les valeurs contenues. Les index sont ici des nombres, qui commencent à 0 (zéro), et qui s’incrémentent de 1 à chaque nouvelle valeur du tableau.

Attention, la première case d’un tableau porte l’index “0”, et non “1”. Ce qui veut dire que la première valeur d’un tableau se situe à l’index “0”, la deuxième valeur se situe à l’index “1”, et la troisième valeur se situe à l’index “2”. Ceci est souvent problématique chez les néophytes et entraîne de nombreuses erreurs !

#### Déclaration

Pour déclarer un tableau à index numérique en insérant des valeurs lors de sa création, il faut procéder comme expliqué ci-dessus, en ajoutant l’ensemble de vos valeurs entre les parenthèses qui suivent “*array*”, en les séparant par des virgules. Voici un exemple :

```php
# $tableau représente le nom de la variable qui contient le tableau.

# array() permet de définir un tableau

# 'val1', 'val2', 'val3'  sont les valeurs qui constituent le 
# contenu du tableau
$tableau = array('val1', 'val2', 'val3');
```

Il est également possible d’utiliser la deuxième méthode de déclaration d’un tableau : 

```php
# $tableau représente le nom de la variable qui contient le tableau.

# les crochets permettent de définir un tableau

# 'val1', 'val2', 'val3'  sont les valeurs qui constituent le contenu du 
# tableau
$tableau = ['val1', 'val2', 'val3'];
```

#### Ajout d’une valeur à la fin du tableau

Il n’existe ici encore pas qu’une seule manière d’ajouter une valeur à un tableau à index numérique. Il est possible de procéder comme suit : 

```php
# déclaration d'un tableau initial
$tableau = array('val1', 'val2', 'val3');

# ajout d'une valeur à la fin du tableau
$tableau[] = 'val4';
```

Une autre solution peut être d’utiliser une fonction fournie par PHP pour les tableaux : ```append()``` :

```php
# déclaration d'un tableau initial
$tableau = array('val1', 'val2', 'val3');

# ajout d'une valeur à la fin du tableau
$tableau->append('val4');
```

#### Modification d’un index précis

Dans le cadre de l’utilisation de tableaux en PHP, il est courant de devoir modifier des valeurs à des index précis du tableau. En reprenant l’exemple du tableau ci-dessus : ```$tableau = array('val1', 'val2', 'val3');``` et pour modifier la valeur de la deuxième case, alors il faut modifier l’index “1” comme suit : 

```php
# création du tableau initial
$tableau = array('val1', 'val2', 'val3');

# modification de la deuxième case.

# Les index commençant par "0", la deuxième case correspond donc à 
# l'index "1".

# il faut donc préciser l'affectation d'une valeur à cet index : 
$tableau[1] = 'val4';

# le tableau vaudra maintenant : 
# array('val1', 'val4', 'val3');
```

Attention, si jamais l’index choisi n’existe pas, alors il sera créé et la valeur désirée y sera affectée.

#### Récupération et affichage d’un élément du tableau

Afin de pouvoir exploiter l’ensemble des informations stockées dans un tableau, il faut pouvoir accéder à chacune de ses cases. Tout comme pour la modification d’une case, il est nécessaire de se servir de l’index de la case. Par exemple, pour afficher la dernière case du tableau suivant : 

```php
# création du tableau initial
$tableau = array('val1', 'val2', 'val3');

# Le tableau contient 3 cases, le dernier index est donc le "2"
# Utilisation de "echo()" pour l'affichage :

echo($tableau[2]);
# affichera : "val3"
```

#### Supprimer un élément d’un tableau

Pour supprimer un élément, il existe la fonction PHP “**unset()**”. Pour l’utiliser, il faut lui stipuler l’élément du tableau à supprimer en utilisant ici encore son indice. Par exemple, pour supprimer la première case d’un tableau :

```php
# création du tableau initial
$tableau = array('val1', 'val2', 'val3');

# suppression de la première case
# suppression donc de l'indice "0" (zéro)
unset($tableau[0]);
```

### Tableau associatif

Un tableau associatif est semblable à un tableau à index numérique, à ceci près que l’index n’est pas forcément numérique, et qu’il peut être défini par d’autres types que le type numérique. Cette organisation d’information est appelée une paire de “clé - valeur”. La clé joue le rôle d’index, tandis que la valeur représente l’élément qui y est lié.

En y réfléchissant davantage, il s’avère qu’un tableau à index numérique s’apparente également à un tableau associatif : la seule différence est que la clé utilisée dans le système de “clé - valeur” est gérée automatiquement par PHP et est numérique.

#### Déclaration d’un tableau avec des valeurs

La déclaration est assez similaire à un tableau à index numérique. Il faut créer une variable de la même manière, utiliser la méthode “**array()**” et séparer les “cases” par des virgules. La différence ici va se situer sur ce qu’il faut spécifier entre les parenthèses de “**array()**”. Pour symboliser un système de “clé - valeur”, il faut utiliser le symbole de la double flèche “**=>**”. À gauche de celle-ci est placée la clé, tandis que la valeur est disposée à sa droite. Voici un exemple de déclaration de tableau associatif :

```php
# Création d'un tableau associatif
$tableau = array(
    1 => "Hello World",
    "name" => "microlead",
    "useful" => True
);
```

Prenons le temps d’expliquer chacune des lignes : 

- ligne 0 : Commentaire simple.
- ligne 1 : Déclaration de la variable “*tableau*” et affectation d’un tableau
- ligne 2 : Affectation de la première paire “clé-valeur” au tableau. La clé est “**1**” (nombre entier), et la valeur est “**Hello World**” (chaine de caractère).
- ligne 3 : deuxième paire, la clé est “**name**” (chaine de caractère) et la valeur est “**microlead**” (chaine de caractère).
- ligne 4 : troisième paire, la clé est “**usefull**” (chaine de caractère) et la valeur est “**True**” (booléen)
- ligne 5 : Fin de déclaration du tableau

A noter qu’il est également possible d’utiliser la notation avec crochets pour créer le même tableau que présenté ci-dessus : 

```php
# Création d'un tableau associatif
$tableau = [
    1 => "Hello World",
    "name" => "microlead",
    "useful" => True
];
```

#### Ajout / Modification d’une valeur

Le principe est le même que pour les tableaux à index numérique. Pour ajouter ou modifier une valeur dans un tableau associatif, il faut spécifier l’index souhaité, puis lui affecter la valeur désirée. Par exemple : 

```php
# Ajout / modification d'une valeur dans un tableau associatif
$tableau["nouvelle_cle"] = "nouvelle valeur"
```

Dans cet exemple, si une clé “**nouvelle_cle**” est déjà existante dans le tableau ```$tableau```, alors la valeur “**nouvelle valeur**” va remplacer l’existante. L’ancienne valeur sera donc écrasée.

A contrario, si cette clé “**nouvelle_cle**” n’existe pas dans le tableau, alors elle va être créée et la valeur “**nouvelle valeur**” affectée. Il en résultera l’ajout d’une case au tableau.

#### Récupération et affichage d’un élément du tableau

Le principe de récupération d’un élément du tableau est ici aussi basé sur son index. Dans le contexte d’un tableau associatif, il est nécessaire de bien connaître la structure du tableau contenant l’élément qu’il faut afficher.

Si le tableau dispose d’une paire de “*clé-valeur*” spécifique, dont il faut afficher la “*valeur*”, il sera nécessaire d’appeler le tableau en passant entre crochets la “*clé*” associée. Par exemple : 

```php
# Création d'un tableau associatif
$tableau = array(
    1 => "Hello World",
    "name" => "microlead",
    "useful" => True
);

# Récupération de la valeur "Hello World" :
$tableau[1];

# Récupération de la valeur "microlead" :
$tableau["name"];

# Récupération de la valeur "True" :
$tableau["useful"];
```

#### Suppression d’un élément

La suppression d’un élément s’effectue ici encore de la même manière que pour les tableaux à index numérique à ceci près que l’index correspond à la “clé” pour chaque paire de “clé-valeur”. L’utilisation de la fonction ```unset()``` est donc toujours préconisée, en lui passant entre les parenthèses le tableau et en lui spécifiant la clé souhaitée : 

```php
# Création d'un tableau associatif
$tableau = array(
    1 => "Hello World",
    "name" => "microlead",
    "useful" => True
);

# suppression de l'index "name" et de la valeur associée :
unset($tableau[1]);

# suppression de l'index "usefull" et de la valeur associée :
unset($tableau["useful"]);
```

À l'issue de la suppression des deux index “**1**” et “**usefull**”, le tableau ne contiendra donc plus qu’une paire de “clé-valeur” : ```“name” => “microlead”```.

# Contenu de ./0160 - Les fonctions mathématiques/content.md

Comme beaucoup d’autres langages de programmation, le langage PHP met à disposition des développeurs toute une série de fonctions natives permettant d’effectuer des calculs mathématiques plus ou moins complexes. En PHP, ces fonctions sont assez similaires à celles proposées par le langage JavaScript.

Ces fonctions s’utilisent aussi bien avec les nombres de type **int**, que ceux de type **float**. 

## Fonctions mathématiques basiques

### La fonction abs()

Cette fonction prend en paramètre un chiffre ou un nombre et en retourne sa valeur absolue. 

Exemple :

```php
// Retourne 6
abs(6);
// Retourne 8
abs(-8);
```

### La fonction ceil()

Cette fonction prend en valeur un float et en retourne l’entier supérieur.

Exemple :

```php
// Retourne 7
ceil(6.9);
// Retourne 524
ceil(523.4);
```

### La fonction floor()

Cette fonction - signifiant littéralement *sol* en français - prend en paramètre un nombre décimal et en retourne l’arrondi inférieur.

Exemple :

```php
// Retourne 9
floor(9.8);
// Retourne 76
floor(76,5);
```

### La fonction round()

Cette fonction retourne le nombre arrondi le plus proche. Il prend en paramètre un float. En second paramètre, optionnel, cette fonction le nombre de chiffres après la virgule.

En second paramètre, ```round()``` accepte un chiffre négatif. Si tel est le cas, le nombre sera arrondi comme prévu et la fonction ajoutera, après la virgule, le nombre de 0 précisé en second paramètre, grâce au nombre négatif.

Exemple :

```php
// Retourne 3
round(2.5);
// Retourne 1.37
round(1.36931, 2);
// Retourne 532
round(532.32, 0);
// Retourne 65.254600
round(65.254532, -2);
```

### La fonction pow()

Cette fonction prend 2 arguments et retourne le premier argument à la puissance de l’argument 2.

Exemple :

```php
// Retourne 1
pow(0, 0);
// Retourne 256
pow(2, 8);
```

### La fonction max()

Cette fonction prend en paramètres une liste de nombres et en retourne le nombre le plus grand. 

Exemple :

```php
// Retourne 1502
max(1, 1502, 8, 952, 20);
```

### La fonction min()

Comme pour la fonction précédente, celle-ci prend également en paramètre une liste de nombres, mais en retourne le plus petit de la liste. 

Exemple :

```php
// Retourne 1
min(1, 1502, 8, 952, 20);
```

### La fonction log()

Cette fonction prend en paramètre un chiffre ou un nombre et en retourne le logarithme naturel.

Exemple :

```php
// Retourne 0.69314718055995
log(2);
```

### La fonction exp()

Cette fonction reçoit en paramètre un chiffre ou un nombre et en retourne l’exponentiel. 

Exemple :

```php
// Retourne 7.3890560989307
exp(2);
```

### La fonction sqrt()

Cette fonction retourne la racine carrée du nombre passé en paramètre.

Exemple :

```php
// Retourne 1.41421356237
sqrt(2);
```

### La fonction mt_rand()

Cette fonction ne reçoit pas forcément d’arguments. Si elle est utilisée comme telle, ```rand()``` retourne simplement un nombre aléatoire. 

Il est cependant possible de passer 2 paramètres à la fonction : le nombre minimum et le nombre maximum - dans cet ordre - entre lequel la fonction doit retourner le nombre aléatoire.

Exemple :

```php
// Retourne, ici, 59632214521
mt_rand();
// Retourne, ici, 9
mt_rand(0, 10);
```

### La fonction pi()

Cette fonction ne reçoit rien en paramètre et retourne la valeur du nombre Pi.

Exemple :

```php
// Retourne 3,14159265359
pi();
```

# Contenu de ./0170 -  Les opérateurs arithmétiques en PHP/content.md

En PHP, comme avec beaucoup d’autres langages informatiques, il est possible de faire des calculs. Le langage PHP comprend les quatre opérations arithmétiques de bases (addition, soustraction, multiplication et division), mais également des opérations plus avancées : division avec reste (modulo) et puissances (exposant). Le langage PHP peut aussi calculer l’opposé d’un chiffre (négation). 

## L’addition

En PHP, il est possible d’additionner des valeurs entre elles. Pour cela, il suffit d’utiliser le signe (appelé opérateur) ```+```. 

Exemple : 

```php
<?php
#Création des variables
$a = 3;
$b = 3;
# Addition des deux variables
$resultat = $a + $b;

# Ici, echo affiche “6”
echo($resultat);
?>
```

Dans l’exemple ci-dessus, les variables ```$a``` et ```$b``` sont créées et contiennent toutes deux le chiffre 3. Ensuite, dans la variable ```$resultat```, ```$a``` et ```$b``` sont additionnés. Enfin, echo affichera le résultat de l’opération ```$a + $b```, contenu dans ```$resultat``` : 6.

## La soustraction

De même qu’il est possible d’additionner deux valeurs entre elles, en PHP, il est par ailleurs possible d’obtenir la différence entre deux valeurs. Pour obtenir ce résultat, il faut utiliser le signe ```-```.

Exemple :

```php
<?php
#Création des deux variables
$a = 3;
$b = 2;

#Soustraction des deux variables
$resultat = $a - $b;

# Ici, $resultat contient le résultat de $a-$b, donc 1
echo($resultat);
?>
```

Le variable ```$a``` est créée et initialisée avec le chiffre 3 ; la variable ```$b``` est initialisée avec le chiffre 2. 

Ici, la variable ```$resultat``` contient le résultat de l’opération ```$a - $b``` (3-2), c'est-à-dire 1. 

Dans l’exemple ci-dessus, ```echo``` va donc afficher “1”.

## La multiplication

Avec le langage PHP, il est également possible d’obtenir un produit. Pour réaliser cela, il suffit d’utiliser le signe ```*``` (étoile).

Exemple :

```php
<?php
$a = 5;
$b = 2;

$resultat = $a * $b;

echo($resultat);
?>
```

Dans l’exemple ci-dessus, les variables ```$a``` et ```$b``` sont initialisées avec les valeurs suivantes : 5 et 2.

Dans ```$resultat```, les deux variables sont multipliées l’une avec l’autre. La variable ```$resultat``` contient le résultat de la multiplication 5*2, donc 10.

```Echo``` affiche 10.

## La division

L’opérateur suivant permet d’obtenir le **quotient** de deux valeurs. Pour faire une division, en PHP, il faut utiliser le signe ```/``` (slash).

```php
<?php
$a = 6;
$b = 3;

$resultat = $a / $b;

echo($resultat);
?>
```

Comme dans les exemples précédents, les variables ```$a``` et ```$b``` sont initialisées avec 6 et 3. Ensuite, dans la variable ```$resultat```, ```$a``` est divisée par ```$b```. La variable ```$resultat``` contenant le résultat de cette opération, ```echo``` retourne donc “2”.

*Remarque : L’opérateur de division retourne un chiffre à virgule, sauf si les deux valeurs de l’opération sont des nombres entiers et que leur division est exacte - cela signifie que la division a pour reste 0. Dans ce cas, l’opérateur ```/``` retourne un nombre entier.*

En plus de ces quatre opérations de base, le langage PHP permet également de faire des opérations plus avancées : le modulo et l’exposant.

## Le modulo

Le modulo est une opération particulière en ceci qu’elle retourne le **reste** d’une division. Il est important de comprendre que cet opérateur **ne retourne pas** le quotient d’une division mais le reste. 

Afin de faire une opération modulo, il suffit d’utiliser le signe ```%```.

Exemple :

```php
<?php
$a = 8;
$b = 5;

# Calcul du RESTE de la division 8/5
$resultat = $a % $b;

/* Ici echo affichera 3, car $resultat contient le RESTE et non le quotient de la division */
echo($resultat);
?>
```

Dans cet exemple, les variables ```$a``` et ```$b``` sont initialisées avec les valeurs 8 et 5. Dans la variable ```$resultat``` est calculé le reste de la division entre ```$a``` et ```$b```. Ainsi, au lieu d’afficher “1,6” qui sera le quotient de la division 8/5, ```echo``` affichera la valeur contenue dans la variable ```$resultat```, à savoir le reste de la division 8/5, soit “3”.

**Remarque** : Le résultat d’une opération modulo a forcément le même signe que le premier opérateur. Ainsi si ```$a``` est négatif, le résultat de l’opération sera, par conséquent, lui aussi négatif.

## L’exposant

Avec le langage PHP, il est également possible de retourner le résultat d’un chiffre élevé à la puissance d’un autre. 

Pour rappel, en mathématiques, la puissance d’un nombre (ou exposant) est le résultat de la multiplication d’un nombre avec lui-même. Par exemple, 2^5 signifie que 2 est multiplié cinq fois par lui-même. Ainsi 2^5 = 2*2*2*2*2 = 32.

Pour effectuer une opération de puissance en PHP, il faut utiliser le signe suivant : ```**```.

Exemple : 

```php
<?php
$a = 2;
$b = 10;

# Multiplie 2 dix fois par lui-même
$resultat = $a ** $b;

# Affiche "1024"
echo($resultat);
?>
```

Dans cet exemple, le chiffre contenu dans la variable ```$a``` (2) est élevé à la puissance du chiffre contenu dans la variable ```$b``` (10). La variable ```$resultat``` stocke le résultat de la multiplication de 2^10 (2 puissance 10). Ici, 2 est donc multiplié 10 fois par lui-même. Par conséquent ```echo``` affiche “1024”.

## La négation

Le PHP permet également de calculer l’opposé d’un chiffre. 

En arithmétiques, l’opposé d’un nombre a est l’unique nombre qui, ajouté à a, donne zéro. 

Pour calculer l’opposé d’un nombre en PHP, il faut utiliser l’opérateur ```+``` devant le nom de la variable. 

Exemple :

```php
<?php
$a = 2;

/* Pour trouver l'opposé du chiffre 2, il suffit d'ajouter l'opérateur "+" devant la variable $a */
$resultat = +$a;

# Affiche -2, car 2-2 = 0;
echo($resultat);
?>
```

Dans l’exemple ci-dessus, la variable ```$a``` est initialisée avec le chiffre 2. Dans ```$resultat``` est stocké le résultat de l’opération ```+$a```, calculant le chiffre opposé à 2. ```Echo``` affiche donc le contenu de ```$resultat```, soit -2, car il est l’unique chiffre qui, ajouté à 2, donne 0.

## Résumé des opérateurs

Voici un tableau récapitulatif des différents opérateurs arithmétiques en PHP, leurs noms et le résultat qu’ils retournent :

| **Opérateur** | **Nom** | **Résultat** |
| --- | --- | --- |
| ```+``` | Addition | Retourne le résultat de l’addition de deux valeurs |
| ```-``` | Soustraction | Retourne le résultat de la soustraction de deux valeurs |
| ```*``` | Multiplication | Retourne le résultat du produit de deux valeurs |
| ```/``` | Division | Retourne le **quotient** de la division de deux valeurs |
| ```%``` | Modulo | Retourne le **reste** de la division de deux valeurs |
| ```**``` | Exponentielle | Élève un chiffre à la puissance d’un autre |
| ```+$a``` | Négation | Retourne le chiffre opposé |

# Contenu de ./0180 - Les opérateurs de chaînes de caractères/content.md

Les 2 opérateurs de chaînes de caractères (*string*) sont :

- ```.``` : cet opérateur retourne la concaténation de ces deux arguments,
- ```.=``` : cet opérateur et l’opérateur d’affectation concaténant.

Exemple :

``` php
<?php
$a = "Prénom : ";
$b = $a . "Elon"; 

$a = "Nom : ";
$a .= "Musk"; 
?>
```

Dans cet exemple, la variable ```$b``` contient “**Prénom : Elon**” et la variable ```$a``` contient “**Nom : Musk**”.

Exemple 2 :

``` php
<?php
$nom = "Besos";
$prenom = "Jeff";
$a = "Prénom : " . $prenom . " et nom : " . $nom;
?>
```

Dans cet exemple, la variable ```$a``` contient “**Prénom : Jeff et nom : Besos**”.

# Contenu de ./0190 - Les opérateurs combinés/content.md

Les opérateurs combinés permettent d’utiliser la valeur d’une variable dans une expression et d’affecter le résultat de cette expression à cette variable.

Liste des opérateurs combinés et de leurs équivalents :

- ```$a += expression```, est équivalent à, ```$a = $a + expression``` 
- ```$a -= expression```, est équivalent à, ```$a = $a - expression```
- ```$a *= expression```, est équivalent à, ```$a = $a * expression```
- ```$a /= expression```, est équivalent à, ```$a = $a / expression```
- ```$a %= expression```, est équivalent à, ```$a = $a % expression```
- ```$a .= expression```, est équivalent à, ```$a = $a . expression```

Exemple :

```php
<?php
$a = 2;
$a += 10; 
// affecte la valeur 12 à la variable $a ce qui correspond à l’expression '$a = $a + 10'
$b = "Bonjour ";
$b .= "Martin";  
// affecte la valeur "Bonjour Martin" à la variable $b ce qui correspond à l’expression $b = $b . " Martin"
?>
```

# Contenu de ./0200 - L'incrémentation vs la décrémentation/content.md

Parfois, il est nécessaire d’ajouter ou d’enlever 1 à un nombre. C’est le cas lorsque qu’un compteur est créé, par exemple. Dans un tel cas, il est nécessaire de pouvoir incrémenter ou décrémenter un nombre. 

Incrémenter signifie ajouter 1 à un nombre ; tandis que décrémenter signifie : ôter 1 à un nombre.

## Incrémentation

Il existe deux moyens d’incrémenter un nombre

### ++$a

```$a``` représente la variable à incrémenter et le double plus (```++```) est le signe d’incrémentation en PHP. 

Incrémenter un nombre en utilisant l’écriture ```++$a``` ajoute 1 au nombre **puis** le retourne.

Exemple :

```php
$a = 0;
# retourne 1
echo(++$a;)
# retourne 1
echo($a);
```

### $a++

Cette manière d’incrémenter un nombre fait l’exact contraire de la manière détaillée au point précédent. En d’autres termes, ici, le nombre est d’abord retourné, **puis** 1 est ajouté.

Exemple :

```php
$a = 0;
# retourne 0
echo($a++);
# retourne 1
echo($a);
```

## Décrémentation

La décrémentation permet d’enlever 1 au nombre. Comme pour l’incrémentation, il existe, en PHP, deux façons de décrémenter un nombre, qui sont les mêmes que pour l’incrémentation.

### $a--

Cette manière de décrémenter enlève 1 au nombre puis le retourne.

Exemple :

```php
$a = 10;
# retourne 9
echo($a--);
# retourne 9
echo($a);
```

### --$a

Cette manière de décrémenter retourne le nombre **puis** enlève 1.

Exemple :

```php
$a = 10;
# retourne 10
echo(--$a);
# retourne 9
echo($a);
```


# Contenu de ./0210 - La priorité d'exécution des opérateurs/content.md

La priorité des opérateurs est l’ordre dans lequel les valeurs dans un script vont s'exécuter. Exemple, l’expression 2 + 8 * 3, le résultat est 26 et non 30, car comme en mathématique la multiplication à une priorité supérieur par rapport à une addition. Dans l’exemple ci-dessus, si on utilise des parenthèses la priorité va être forcé. Exemple, (2 + 8) *3 cette fois-ci le résultat est 30 et non 26.

Les opérateurs, dont la priorité est égale, qui ne sont pas associatifs, ne peuvent pas être utilisés entre eux. Exemple, 2 < 3 > 2 n’est pas autorisée en PHP, à l'inverse 2 <= 2 == 2 est autorisée, l’opérateur == a une précédence inférieur que l’opérateur <=.

L’utilisation des parenthèses dans une expression même si elles ne sont pas obligatoires peuvent permettre d’avoir une meilleure compréhension du code.

Exemple 1. Associativité :

```php
<?php
// (3 * 3) % 5 = 4
$a = 3 * 3 % 5;
// (true ? 0 : true) ? 1 : 2 = 2
$a = true ? 0 : true ? 1 : 2;

$a = 1;
$b = 2;
// $a = ($b += 3) -> $a = 5, $b = 5
$a = $b += 3;
?>
```

La priorité et l’association de l’opérateur ne déterminent que la façon dont les expressions sont regroupées. Dans cet exemple, les parenthèses permettent de définir la priorité d’exécution d’une expression.

Exemple 2. Ordre non défini

```php
<?php
$a = 5;
// affiche 6 ou 7
echo($a + $a++);
?>
```

# Contenu de ./0220 - Les opérateurs de comparaison/content.md

Les opérateurs de comparaisons sont, comme leurs noms l'indiquent, des moyens de comparer différentes valeurs. Il en existe différents, mais ils ont pour points communs de toujours renvoyer “vrai” ou “faux” selon les comparaisons effectuées. Ils sont très souvent utilisés dans des conditions et permettent de définir les actions à mener en fonction des valeurs comparées.

## Les différents opérateurs

### L’opérateur “==” - “égal”

Cet opérateur de comparaison permet d’établir un lien d’égalité entre deux valeurs. Ainsi si la première valeur est égale à la deuxième, alors l’opérateur retourne “vrai”. Dans le cas contraire, il renvoie “faux”. Cet opérateur ne compare QUE les valeurs, et pas les types, de telle sorte que le nombre “1” et le caractère “1” (donc en tant que texte) sont considérés égaux. Par exemple :

```php
echo( 1 == 2 );
# renvoie Faux, car les valeurs ne sont pas identiques

echo( 2 == 2 );
# renvoie Vrai, car les valeurs sont identiques

echo( 2 == "2" );
# renvoie Vrai, car les valeurs sont identiques - même si les types ne 
# ne sont pas les mêmes
```

### L’opérateur “===“ - “strictement égal”

Cet opérateur permet comme le précédent d'établir un lien d'égalité entre deux valeurs. Cependant, celui-ci compare non seulement les deux valeurs, mais également leurs types. De la sorte, le nombre “1” et le caractère “1” ne seront pas considérés comme égaux, puisque l’un est un nombre, tandis que l’autre est un caractère.

```php
echo( 1 === 2 );
# renvoie Faux, car les valeurs ne sont pas identiques


echo( 2 === 2 );
# renvoie Vrai, car les valeurs et les types sont identiques

echo( 2 === "2" );
# renvoie Faux, car même si les valeurs sont identiques, les types ne le sont pas
```

### L’opérateur “!=” - “différent”

Cet opérateur de comparaison vérifie que les valeurs testées soient bien différentes. Ici, seules les valeurs sont prises en compte, et non leur type.

```php
echo( 1 != 2 );
# renvoie Vrai, car les valeurs ne sont pas identiques

echo( 2 != 2 );
# renvoie Faux, car les valeurs sont identiques

echo( 2 != "2" );
# renvoie Faux, car les valeurs sont identiques - même si les types ne 
# ne sont pas les mêmes
```

### L’opérateur “!==” - “strictement différent”

Cet opérateur de comparaison est similaire au précédent, à ceci près qu’il teste les valeurs ainsi que les types, sur le même schéma que l’opérateur “ === ”.

```php
echo( 1 !== 2 );
# renvoie Vrai, car les valeurs ne sont pas identiques

echo( 2 !== 2 );
# renvoie Faux, car les valeurs sont identiques et leur type également

echo( 2 !== "2" );
# renvoie Vrai, car les valeurs sont identiques, mais pas leur type
```

### L’opérateur “<” - “strictement inférieur”

C’est l’opérateur traditionnellement appelé “strictement inférieur à”, issu des notations mathématiques. Il permet de vérifier que la première valeur (placée à gauche du symbole), soit bien inférieure à la seconde (placée à droite du symbole). Attention, le “strictement” est ici important puisque si les deux valeurs comparées sont identiques, alors l’une ne sera pas strictement inférieure à l’autre et la comparaison retournera “faux”.

De même, pour comparer si une valeur est strictement inférieure à une autre, il faut que les deux valeurs soient du même type, ou bien au moins que PHP soit à même de comparer les deux valeurs. De la sorte, si un nombre est comparé  à un caractère, une erreur est retournée. Par contre, si un nombre entier est comparé à un nombre à virgule, alors la comparaison pourra bien s’effectuer puisque les deux valeurs testées sont bien des nombres.

```php
echo( 1 < 2 );
# renvoie Vrai, car 1 est bien strictement inférieur à 2

echo( 2 < 2 );
# renvoie Faux, car les deux valeurs sont identiques

echo( 2 < "3" );
# renvoie une erreur puisque la comparaison concerne un nombre et un 
# caractère

echo( 1,1 < 5 );
# renvoie Vrai, car PHP sait comparer des nombres à virgule avec des 
# nombres entiers
```

### L’opérateur “<=” - “inférieur ou égal”

Cet opérateur est le même que le précédent, à ceci près qu’il va prendre en compte l’égalité entre les deux valeurs. Ainsi si les deux valeurs sont égales, alors “vrai” sera retourné.

```php
echo( 1 <= 2 );
# renvoie Vrai, car 1 est bien inférieur ou égal à 2

echo( 2 <= 2 );
# renvoie Vrai, car les deux valeurs sont égales

echo( 2 <= "3" );
# renvoie une erreur puisque la comparaison concerne un nombre et un 
# caractère

echo( 1,1 <= 5 );
# renvoie Vrai, car PHP sait comparer des nombres à virgule avec des 
# nombres entiers
```

### L’opérateur “>” - “strictement supérieur”

Il est l’exact opposé de l’opérateur “strictement inférieur” (<). Ainsi il renvoie vrai si la première valeur (à gauche du symbole) est strictement supérieure à la seconde (à droite du symbole). Les mêmes restrictions s’appliquent quant aux valeurs égales (qui renvoient donc faux), et à la comparaison d’un nombre et d’un caractère (qui renvoie une erreur).

```php
echo( 2 > 1 );
# renvoie Vrai, car 1 est bien strictement supérieur à 2

echo( 2 > 2 );
# renvoie Faux, car les deux valeurs sont identiques

echo( 2 > "3" );
# renvoie une erreur puisque la comparaison concerne un nombre et un 
# caractère

echo( 5 > 1,1 );
# renvoie Vrai, car PHP sait comparer des nombres à virgule avec des 
# nombres entiers
```

### L’opérateur “>=” - “supérieur ou égal”

Cet opérateur est le même que le précédent, à ceci près qu’il prend en compte l’égalité entre les deux valeurs. Ainsi, si les deux valeurs sont égales, alors il renvoie “vrai”.

```php
echo( 2 >= 1 );
# renvoie Vrai, car 1 est bien strictement supérieur à 2

echo( 2 >= 2 );
# renvoie Vrai, car les deux valeurs sont identiques

echo( 2 >= "3" );
# renvoie une erreur puisque la comparaison concerne un nombre et un 
# caractère

echo( 5 >= 1,1 );
# renvoie Vrai, car PHP sait comparer des nombres à virgule avec des 
# nombres entiers
```

# Contenu de ./0230 - Les opérateurs logiques/content.md

Les opérateurs logiques sont un moyen d’enchaîner les opérateurs de comparaisons. De la même manière qu’en mathématiques, ils disposent chacun d’une priorité d’exécution. À l’image de certains opérateurs mathématiques comme la multiplication ou la division qui sont prioritaires face à des additions ou soustractions, les opérateurs logiques informatiques induisent des règles similaires qui leur sont propres.

## L’opérateur “et”

L’opérateur “**et**” permet de tester si plusieurs comparaisons sont vraies ou fausses. Cet opérateur suis la logique suivante : 

- “vrai” **et** “vrai” donnent un résultat “vrai”
- “vrai **et** “faux” donnent un résultat “faux”
- “faux” **et** “faux donnent un résultat “faux”

Il peut être symbolisé de deux façons différentes en PHP : soit par le symbole “**&&**”, soit par le mot-clé “**AND**”. Ces deux représentations sont presque équivalentes, à ceci près que le symbole “**&&**” disposera d’une priorité d’exécution plus élevée que le mot-clé “**AND**”.

Par ailleurs, l’utilisation de cet opérateur logique n'entraîne pas obligatoirement la vérification de toutes les comparaisons effectuées. En effet, si l’une d’entre elles est fausse, alors le retour sera obligatoirement faux. Ceci évitant à PHP d’opérer des comparaisons, et donc des calculs, pour rien.

```php
# Déclaration de deux variables afin de tester nos opérateurs logiques
$a = 0;
$b = 1;

# comparaison logique de "$a" et "$b"
echo( $a == 0 AND $b == 1 );
# Lors de la vérification de cet opérateur logique, PHP commencera par 
# vérifier la première # condition, "$a == 0". Le résultat étant vrai, 
# on pourrait schématiser l'opération comme suit :

# echo( vrai AND $b == 1 );

# Comme la première condition est vraie, alors PHP va vérifier la seconde condition "$b == 1".

# Étant donné que celle-ci est également vraie, alors on arrive à la 
# comparaison suivante : 

# echo( vrai AND vrai );

# ainsi en se référant aux logiques de cet opérateur, on arrive à un 
# résultat qui sera "vrai"

# seconde comparaison logique de "$a" et "$b"
echo( $a == 1 AND $b == 1 );
# PHP commencera ici par tester la première comparaison "$a == 1". 
# Celle-ci est fausse étant donné que "$a" est égal à zéro. Ainsi PHP ne 
# ne prendra pas la peine de vérifier la deuxième comparaison et
# renverra directement "faux" sur cette comparaison logique.

# troisième comparaison logique de "$a" et "$b"
echo( $a == 0 AND $b == 2 );
# La première comparaison "$a == 0" renverra "vrai". On obtiendra alors la transformation 
# suivante : 
# echo( vrai AND $b == 2 );
# La seconde comparaison "$b == 2" renverra "faux". La logique appliquée 
# de l'opérateur "AND" renverra donc “faux”.
```

Il est important de noter que dans tous les exemples présentés ci-dessus, le mot-clé “**AND**” est utilisé. Celui-ci aurait pu être remplacé par le double symbole “**&&**” sans qu’aucun changement ne s’opère et les résultats auraient été identiques.

## L’opérateur “ou”

L’opérateur “ou” permet de tester si au moins une des comparaisons effectuées est vraie ou fausse. Cet opérateur suis la logique suivante : 

- “vrai” **ou** “vrai” renvoie “vrai”
- “vrai” **ou** “faux” renvoie “vrai”
- “faux” **ou** “faux” renvoie “faux”

Cet opérateur renvoie ainsi “vrai” tant que l’un des éléments comparés est également “vrai”. Il est représenté de deux manières : avec le mot-clé “**OR**” ou bien avec le double symbole “**||**”.

A contrario de l’opérateur “et”, l’opérateur “ou” renverra vrai, même si une seule des conditions comparées est vraie. Ainsi PHP testera chacune des comparaisons à tour de rôle jusqu’à obtenir un résultat de comparaison “vrai”, ou bien renverra “faux” si aucune n’est trouvée.

```php
# Déclaration de deux variables afin de tester nos opérateurs logiques
$a = 0;
$b = 1;

# comparaison logique de "$a" ou "$b"
echo( $a == 0 OR $b == 1 );
# Lors de la vérification de cet opérateur logique, PHP commencera par 
# vérifier la première # condition, "$a == 0". Le résultat étant vrai, 
# PHP ne testera pas la seconde comparaison, il retournera directement 
#"vrai".

# seconde comparaison logique de "$a" ou "$b"
echo( $a == 1 OR $b == 1 );
# PHP commencera ici par tester la première comparaison "$a == 1". 
# Celle-ci est fausse 
# Étant donné que "$a" est égal à zéro. Ainsi PHP va tester la prochaine 
# comparaison afin 
# de déterminer si au moins une est vraie : 
# "$b == 1" étant vrai, alors la comparaison logique renverra "vrai"

# troisième comparaison logique de "$a" ou "$b"
echo( $a == 1 OR $b == 2 );
# La première comparaison "$a == 1" renverra "faux". PHP testera donc la 
# comparaison 
# suivante "$b == 2". Celle-ci étant "fausse" également, alors la 
# comparaison logique renverra la valeur "faux".
```

À noter ici aussi que le mot-clé utilisé pour ces exemples est le “**OR**”. Celui-ci pourrait être remplacé par le double symbole “**||**” sans qu’aucun changement n’apparaisse.

## L’opérateur “ou exclusif”

L’opérateur “ou exclusif” permet de tester si une des comparaisons effectuées est vraie ou fausse, mais que les deux soient différentes ! Ainsi l’opérateur plus communément appelé par son mot-clé “**XOR**” suit la logique suivante : 

- “vrai” **XOR** “vrai” renvoie “faux”
- “vrai” **XOR** “faux” renvoie “vrai”
- “faux” **XOR** “faux” renvoie “faux”

Le principe d’utilisation de cet opérateur logique est donc de déterminer si deux comparaisons ont des résultats semblables ou non.

```php
# Déclaration de deux variables afin de tester nos opérateurs logiques
$a = 0;
$b = 1;

# premier test du "XOR"
echo( $a == 0 XOR $b == 1 );
# La première comparaison "$a == 0" est vraie. La seconde comparaison 
# "$b == 1" l'est également. Ainsi en suivant la logique de l'opérateur, 
# un résultat "faux" sera renvoyé.

# second test du "XOR"
echo( $a == 3 XOR $b == 1 );
# La première comparaison "$a == 3" est vraie. La seconde comparaison 
# "$b == 1" est fausse. En suivant la logique de l'opérateur "XOR", un 
# résultat "vrai" sera donc renvoyé.
```

## L’opérateur “NON”

L’opérateur “NON” est un opérateur de négation. Il s’exprime avec un point d’exclamation (!) et permet de tester l’inverse d’un état. Il présente ainsi la logique suivante : 

- **NON** “vrai” renverra “faux”
- **NON** “faux” renverra “vrai”

```php
# Déclaration d'une variable "$a" ayant pour valeur "0"
$a = 0;
$b = 1;

# Premier test avec l'opérateur "NON"
echo( !$a == 1 );
# L'exécution de la ligne ci-dessus, entraînera le test de la 
# comparaison "$a == 1". Cette comparaison est "fausse". Ainsi l'inverse 
# de la comparaison exercée par l'opérateur logique "NON" renverra 
# "vrai"

# Deuxième test
echo( !$b == 1 );
# De la même manière que dans le premier exemple, la première 
# comparaison effectuée sera "$b == 1", qui est donc "vraie". Ainsi 
# l'inverse de la comparaison étant testée du fait de l'opérateur 
# logique "NON" ( ! ), le résultat retourné sera "faux"
```

# Contenu de ./0240 - L'opérateur NULL Coalescing/content.md

Cet opérateur est disponible depuis la version 7.0 de PHP. Il a la même capacité que la fonction ```inset()``` et renvoie la variable spécifiée si elle existe, sinon c’est la valeur précisée après les deux points d’interrogation (**??**) qui est renvoyée.

De plus, cet opérateur peut être utilisé plusieurs fois de suite. 

## Utilisation

Les différents exemples ci-dessous permettent d’illustrer l’utilisateur de cet opérateur :

```php
$variable = NULL;
$seconde_variable = $variable ?? "Hello"; // Retourne Hello

$variable = "Voiture";
$seconde_variable = $variable ?? "Camion"; // Retourne Voiture

$variable = NULL;
$seconde_variable = "Pomme";
$variable_finale = $variable ?? $seconde_variable ?? "Fraise"; // Retourne Pomme
```

# Contenu de ./0250 - Condition - IF/content.md

Les conditions font partie des logiques “standard” de l’ensemble des langages de programmation. Elles permettent de définir s’il faut exécuter ou non une ou plusieurs lignes de code.

Ainsi la déclaration d’une condition créera un “bloc” de ligne(s) de code, qui ne sera exécuté que si la condition est “vraie”. Si celle-ci se révèle fausse, alors le bloc ne sera tout simplement pas exécuté.

L’ensemble des conditions est exprimé à l’aide d’opérateurs. C’est donc grâce à ces derniers que PHP pourra déterminer si la condition est vraie ou fausse, et donc par extension exécuter le code concerné ou non.

## Utilisation

### La condition “si” - IF

Le “si” est la base immuable de toute condition. Elle se représente en PHP à l’aide du mot clé “ **if** ”. La condition doit alors être exprimée entre parenthèses “ **( )** ” tout de suite après le premier mot-clé. Enfin, le bloc de code à exécuter si la condition est vraie doit être écrit entre accolades “ **{ }** “, elles-mêmes placées à la suite des parenthèses.

Prenons deux exemples afin de mieux comprendre la logique :

```php
# Déclaration d'une variable "$a", et attribution de la valeur "0"
$a = 0;

# Déclaration de la condition. Ici on teste que la valeur de "$a" soit
# strictement égale à "0".
if ($a == 0) {
	# Début du bloc à exécuter si la condition est vraie.
	echo("vrai");
}
```

Dans l’exemple ci-dessus, la condition vérifiée est vraie. Ainsi les instructions présentent dans le bloc qui suit, entre accolades, sera exécuté. De la sorte, PHP affichera “**vrai**”.

```php
# Déclaration d'une variable "$a", et attribution de la valeur "0"
$a = 0;

# Déclaration de la condition. Ici on teste que la valeur de "$a" soit
# strictement égale à "1".
if ($a == 1) {
	# Début du bloc à exécuter si la condition est vraie.
	echo("vrai");
}
```

Dans l’exemple ci-dessus, PHP va tester que la valeur de ```$a``` soit bien strictement égale à “1”. Or ```$a``` est égal à zéro et la condition nous renverra donc un résultat “faux”. Ainsi l’ensemble du code présent dans le bloc corrélé à la condition ne sera pas exécuté. La condition n’étant pas remplie, alors PHP ne rentrera pas dans le bloc et passera tout de suite à l’exécution de la suite du code, à savoir la fin du script dans le cas présenté.

### La condition “sinon” - ELSE

Les conditions “si” peuvent également comporter une partie “sinon”. Celle-ci se verra exécutée si la condition initiale décrite dans le bloc "if'' n'est pas remplie. Elle s’exprime grâce au mot-clé “else”, traduction littérale de “sinon” en anglais. 

Contrairement au “if”, il n’y a pas de condition à passer dans le “else” entre parenthèses, cependant il faut tout de même spécifier des accolades tout de suite après le mot clé afin d’y spécifier le code à exécuter si la condition initiale n’est pas remplie. Le “else” est optionnel, et il n’est nullement obligatoire de s’en servir.

```php
# Déclaration d'une variable "$a", et attribution de la valeur "0"
$a = 0;

# Déclaration de la condition. Ici on teste que la valeur de "$a" soit
# strictement égale à "1".
if ($a == 1) {
	# Début du bloc à exécuter si la condition est vraie.
	echo("vrai");
} else {
    # Bloc à exécuter si la condition n'est pas vraie.
    echo("false");
}
```

Dans l’exemple ci-dessus, nous déclarons une variable ```$a``` qui prend pour valeur zéro. Le bloc “if” vérifie ici que la valeur de ```$a``` est égale à 1, or ce n’est pas le cas. Ainsi, c'est le bloc “else” qui sera exécuté et le code affichera “false” en conséquence.

Prenons un deuxième exemple : 

```php
# Déclaration d'une variable "$a", et attribution de la valeur "0"
$a = 1;

# Déclaration de la condition. Ici on teste que la valeur de "$a" soit
# strictement égale à "1".
if ($a == 1) {
	# Début du bloc à exécuter si la condition est vraie.
	echo("vrai");
} else {
    # Bloc à exécuter si la condition n'est pas vraie.
    echo("false");
}
```

L’exemple ci-dessus est similaire au précédent, à ceci près que la valeur de “$a” est cette fois déclarée à “1”. Aussi lorsque PHP va exécuter le code, il va commencer par créer la variable “$a” et lui affecter la valeur “1”. 

PHP va ensuite vérifier la condition “if”, et donc trouver que cette condition est vraie. Ainsi il va afficher “vrai”, mais il n'exécutera pas le code dans le “else”. En effet, partant du principe que la condition exprimée dans le “si” est vraie, alors il n’aura aucun besoin d’exécuter le code dans le bloc “sinon”. De la sorte, il n’affichera pas “false”.

### ELSE IF

Il existe une alternative au “si” et au “sinon” : le “sinon si”. Celle-ci va permettre de tester d’autres conditions avant de passer au “else”, et va ainsi permettre de déterminer différentes actions à réaliser en fonction de plusieurs valeurs.

Le “sinon si” se traduit littéralement en anglais par “else if”. Aussi ce sont les deux mot-clés qu’il faut employer si l’on souhaite s’en servir. Tout comme pour le “if”, il conviendra ici de passer une condition à tester entre parenthèses. Tout comme pour le “else”, le “else if” n’est pas obligatoire.

```php
# Déclaration d'une variable "$a", et attribution de la valeur "0"
$a = 0;

# Déclaration de la condition. Ici on teste que la valeur de "$a" soit
# strictement égale à "1".
if ($a == 1) {
	# Début du bloc à exécuter si la condition est vraie.
	echo("a vaut 1");
} else if ($a == 0) {
    # Bloc à exécuter si $a vaut zéro.
    echo("a vaut zéro");
} else {
    # Bloc à exécuter si la condition n'est pas vraie.
    echo("a ne vaut ni un, ni zéro");
}
```

En exécutant le code ci-dessus, PHP commencera par créer la variable ```$a```, et lui affecter la valeur zéro. Il va ensuite arriver sur la condition “if” et vérifiera que la valeur de ```$a``` est bien égale à “1”. Ceci n’étant pas vrai, il n’exécutera pas le code présent dans le bloc “if”. PHP va donc continuer son exécution du code et arrivera à la condition “sinon si” où il vérifiera que ```$a``` est bien égale à zéro. Cette condition étant vraie, alors il exécutera le code à l’intérieur de ce bloc “else if” et affichera “a vaut zéro”.

Étant donné qu’un bloc de la condition aura été exécuté, alors PHP ne poursuivra pas son exécution des autres blocs de cette condition. Ainsi il n’exécutera pas le code présent dans le bloc “else”.

## Conclusion

L’utilisation des conditions est relativement simple en PHP. Les principales difficultés que vous rencontrerez seront de savoir quoi vérifier, et grâce à quel opérateur.

Il faut ici bien retenir deux points : 

- Une condition est constituée de plusieurs blocs. Lors de l’exécution du code, PHP traitera les blocs dans l’ordre d’écriture. Dès lors qu’un des blocs est exécuté, PHP considérera que la condition est terminée, et ne poursuivra donc pas l’exécution des blocs suivants
- Il est possible de faire autant de blocs que l’on souhaite. Le premier est obligatoirement un “if”. Vous pouvez ensuite mettre zéro ou plusieurs blocs “else if” en fonction de vos besoins. Vous pouvez enfin ajouter à la fin un bloc “else” qui sera exécuté si aucun des blocs précédents (dans la même condition) ne sont exécutés.

Par ailleurs, il est important de noter que dans une condition “if-else” (sans “else if”), il est souvent possible de ne pas utiliser le “else”. Voici un exemple :

```php
$a = 0;
$b = 0;
if ( $a == 0 ) {
    $b = 4
} else {
    $b = 3;
}
```

L’exemple ci-dessus montre un algorithme simple : 

- ```$a``` et ```$b``` sont deux variables initialisées chacune avec la valeur zéro
- si ```$a``` est égale à zéro, alors on passe la valeur de ```$b``` à “4”
- sinon on passe la valeur de ```$b``` à 3.

Il est possible d’écrire cette même condition sans le “else”, juste en changeant d’approche :

```php
$a = 0;
$b = 3;
if ( $a == 0 ) {
    $b = 4
}
```

L’idée est ici de définir la valeur de ```$b``` à 3 dès le début (ce qui était présent dans le bloc “else” de la condition du premier exemple. De la sorte, lorsque PHP va exécuter la condition, il ne changera la valeur de ```$b``` que si ```$a``` est égale à zéro. Dans l’autre cas de figure, alors il ne changera pas la valeur de ```$b``` puisque celui-ci aura déjà été déclaré avec la valeur qu’il aurait dû obtenir dans le bloc “else” de la condition précédente.

# Contenu de ./0260 - Les opérateurs pour tableaux/content.md

En PHP, il existe de nombreux opérateurs qui fonctionnent sur plus d'un tableau, pour obtenir l'union de deux tableaux, pour vérifier l'identité, l'égalité, etc.

Les différents opérateurs pour les tableaux sont :

- ```$a + $b``` : type “Union”, fusionne ```$a``` et ```$b```,
- ```$a == $b``` : type "Égalité", renvoi vrai (true) si ```$a``` et ```$b``` ont les mêmes paires de valeurs,
- ```$a === $b``` : type “Identique”, renvoi vrai (true) si ```$a``` et ```$b``` ont les mêmes paires de valeurs et dans le même ordre et du même type,
- ```$a != $b``` : type “Inégalité”, renvoi vrai (true) si ```$a``` n’est pas égal à ```$b```,
- ```$a <> $b``` : type “Inégalité”, renvoi vrai (true) si ```$a``` n’est pas égal à ```$b```,
- ```$a !== $b``` : type “Non-identique”, renvoi vrai (true) si ```$a``` n’est pas identique a ```$b```.

Exemple 1 :

```php
<?php
$a = array("a" => "abricot", "b" => "cerises");
$b = array("a" =>"poire", "b" => "banane", "c" => "orange");

$c = $a + $b; // type “Union”
var_dump($c);

$c = $b + $a; // type “Union”
var_dump($c);
?>
```

Dans cet exemple, le premier ```var_dump()``` renvoi :

```php
array(3) {
    ["a"] => string(7) "abricot"
    ["b"] => string(7) "cerises"
    ["c"] => string(6) "orange"
}
```

Le second ```var_dump()``` renvoi :

```php
array(3) {
    ["a"] => string(5) "poire"
    ["b"] => string(6) "banane"
    ["c"] => string(6) "orange"
}
```

Exemple 2 :

```php
<?php
$a = array("fraise", "ananas");
$b = array(1 => "ananas", "0" => "fraise");

var_dump($a == $b);
var_dump($a === $b); 
?>
```

Dans cet exemple, le premier ```var_dump()``` renvoi vrai “true” et le deuxième ```var_dump()``` renvoi faux “false”.

# Contenu de ./0270 - Boucle FOR/content.md

La boucle for de PHP peut être utilisée pour parcourir un ensemble de codes pendant un nombre de fois spécifié.

Elle doit être utilisée si le nombre d’itérations est connu, sinon utiliser la boucle while.

## Syntaxe

```php
for(initialization; condition; increment/decrement){ 
    //code à exécuter 
}
```

## Exemple

```php
for($n=1;$n<=10;$n++){ 
    echo("$n<br/>"); 
}
```

Dans cet exemple, le résultat renvoyé est :

```php
1
2
3
4
5
6
7
8
9
10
```

## Boucle For imbriqué

On peut utiliser une boucle for à l’intérieur d’une autre en PHP, on l’appelle boucle for **imbriquée**. En cas de boucle for interne ou imbriquée, la boucle for imbriquée est exécutée intégralement pour une boucle for externe. Si la boucle for externe doit être exécutée 3 fois et la boucle for interne 3 fois, la boucle for interne sera exécutée 9 fois (3 fois pour la première boucle externe, 3 fois pour la 2ᵉ boucle externe et 3 fois pour la 3ᵉ boucle externe).

### Exemple

```php
for($i=1;$i<=3;$i++){ 
    for($j=1;$j<=3;$j++){ 
        echo("$i   $j<br/>");
    } 
}
```

Dans cet exemple, le résultat renvoyé est :

```php
1  1
1  2
1  3
2  1
2  2
2  3
3  1
3  2
3  3
```

# Contenu de ./0280 - Boucle WHILE/content.md

La boucle While de PHP peut être utilisée pour parcourir un ensemble de code comme pour une boucle.

Elle est utilisée si le nombre d’itérations n’est pas connu.

syntaxe :

```php
while(condition){ 
    //code à exécuter 
}
```

autre syntaxe :

```php
while(condition): 
    //code à exécuter 
endwhile;
```

exemple :

```php
$n=1; 
while($n<=10){ 
    echo("$n<br/>");
    $n++; 
}
```

Dans cet exemple, le résultat renvoyé est :

```php
1
2
3
4
5
6
7
8
9
10
```

autre exemple :

```php
$n=1; 
while($n<=10): 
    echo("$n<br/>");
    $n++; 
endwhile;
```

Dans cet exemple, le résultat renvoyé est :

```php
1
2
3
4
5
6
7
8
9
10
```

## Boucle WHILE imbriqué

On peut utiliser la boucle while dans une autre boucle while en PHP, on l’appelle imbriquée.

En cas de boucle While interne ou imbriquée, la boucle While imbriquée est exécutée intégralement pour une boucle While externe. Si la boucle While externe doit être exécutée 3 fois et imbriquée 3 fois, la boucle While imbriquée sera exécutée 9 fois (3 fois pour la 1ère boucle externe, 3 fois pour la 2ᵉ boucle externe et 3 fois pour la 3ᵉ boucle externe).

exemple :

```php
$i=1; 
while($i<=3){ 
    $j=1; 
    while($j<=3){ 
        echo("$i   $j<br/>");
        $j++; 
    } 
    $i++;
}
```

Dans cet exemple, le résultat renvoyé est :

```php
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

# Contenu de ./0290 - Boucle FOREACH/content.md

La boucle FOREACH de PHP est une fonction native qui boucle un morceau de code pour chaque clé/valeur d'un tableau jusqu'à ce qu'elle atteigne le dernier élément du tableau. Elle ne fonctionne uniquement sur un tableau, donc elle ne fonctionne pas avec des expressions ou tout autre type de valeurs d'une variable autre que des tableaux.

Voici la syntaxe d'une boucle FOREACH :

```php
foreach( $array as $var ){ 
    //code à exécuter
}
```

La principale différence entre l'instruction FOREACH et les boucles WHILE ou FOR est la suivante : les boucles WHILE et FOR continuent jusqu'à ce qu'une condition soit remplie. En revanche, la boucle FOREACH continuera jusqu'à ce qu'elle ait parcouru tous les éléments d'un tableau.

Pour chaque boucle, la valeur de la clé actuelle du tableau est affectée à $value et le pointeur du tableau est déplacé en interne vers la clé suivante jusqu'à ce que la dernière clé soit atteinte.

Voici un exemple simple qui illustre le fonctionnement de l'instruction FOREACH :

```php
$season = array("été","printemps","hiver","automne"); 
foreach( $season as $value ){ 
    echo("La saison est: $value<br />");
}
```

Dans cet exemple, le résultat renvoyé est :

```php
La saison est été
La saison est printemps
La saison est hiver
La saison est automne
```

# Contenu de ./0300 - Include et require/content.md

L'instruction ```include()``` ou ```require()``` prend tout le texte/code/balisage existant dans le fichier spécifié et le copie dans le fichier qui utilise l'instruction ```include()``` ou ```require()```. L'inclusion de fichiers est très utile lorsque vous souhaitez inclure le même PHP, HTML ou texte sur plusieurs pages d'un site Web.

Il est possible d'insérer le contenu d'un fichier PHP dans un autre fichier PHP (avant que le serveur ne l'exécute), avec l'instruction include ou require.

Les instructions include et require sont identiques, sauf en cas d'échec :

- ```require()``` : produira une erreur fatale (E_COMPILE_ERROR) et arrêtera le script
- ```include()``` : ne produira qu'un avertissement (E_WARNING) et le script continuera

Donc, si vous voulez que l'exécution se poursuive et montre aux utilisateurs la sortie, même si le fichier d'inclusion est manquant, utilisez l'instruction include. Sinon, dans le cas de FrameWork, CMS ou d'un codage d'application PHP complexe, utilisez toujours l'instruction require pour inclure un fichier clé dans le flux d'exécution. Cela aidera à éviter de compromettre la sécurité et l'intégrité de votre application, juste au cas où un fichier clé serait accidentellement manquant.

L'inclusion de fichiers permet d'économiser beaucoup de travail. Cela signifie que vous pouvez créer un en-tête, un pied de page ou un fichier de menu standard pour toutes vos pages Web. Ensuite, lorsque l'en-tête doit être mis à jour, vous ne pouvez mettre à jour que le fichier d'inclusion d'en-tête.

## Syntaxe

```php
include('filename');

require('filename');
```

## Include

### Exemples

Supposons que nous ayons un fichier de pied de page standard appelé "footer.php", qui ressemble à ceci :

```php
<?php
    echo("<p>Copyright &copy; " . date("Y") . " Microlead.fr</p>");
?>
```

Pour inclure le fichier de pied de page dans une page, utilisez l'instruction ```include()``` :

```php
<html>
<body>

    <h1>Bienvenue sur mon site.</h1>
    <p>Un peu de texte.</p>
    <p>Encore plus de texte.</p>

    <?php include('footer.php';) ?>

</body>
</html>
```

Supposons que nous ayons un fichier de menu standard appelé "menu.php":

```php
<?php
echo('<a href="/">Accueil</a> -
<a href="/html/index.php">HTML</a> -
<a href="/css/index.php">CSS</a> -
<a href="/js/index.php">JavaScript</a> -
<a href="/php/index.php">PHP</a>');
?>
```

Toutes les pages du site Web doivent utiliser ce fichier de menu. Voici comment cela peut être fait (nous utilisons un élément ```<div>``` pour que le menu puisse facilement être stylisé avec CSS plus tard):

```php
<html>
<body>

    <div class="menu">
        <?php include 'menu.php'; ?>
    </div>

    <h1>Bienvenue sur mon site.</h1>
    <p>Un peu de texte.</p>
    <p>Encore plus de texte.</p>

</body>
</html>
```

## Require vs include

L'instruction ```require()``` est également utilisée pour inclure un fichier dans le code PHP.

Cependant, il y a une grande différence entre ```include()``` et ```require()``` ; lorsqu'un fichier est inclus avec l'instruction include et que PHP ne le trouve pas, le script continuera à s'exécuter, exemple :

```php
<html>
<body>

    <h1>Bienvenue sur mon site.</h1>
    <?php 
        include('noFileExists.php');
        echo("J’ai une $car $color.");
    ?>

</body>
</html>
```

Si nous faisons le même exemple en utilisant l'instruction require, l'instruction echo ne sera pas exécutée car l'exécution du script meurt après que l'instruction require ait renvoyé une erreur fatale :

```php
<html>
<body>

    <h1>Bienvenue sur mon site.</h1>
    <?php
        require('noFileExists.php');
        echo("J’ai une $car $color.");
    ?>

</body>
</html>
```

# Contenu de ./0310 - Superglobales - Introduction/content.md

Les variables superglobales en PHP sont des variables globales prédéfinies. Les variables globales sont des variables de portée globale, ce qui signifie qu'elles peuvent être utilisées partout où cela est nécessaire - elles n'ont pas besoin d'être déclarées, ni d'être marquées comme globales dans les fonctions. Toutes les variables superglobales sont écrites en majuscules, comme ```$_GLOBALS```.

## Liste des variables superglobales

Toutes les variables superglobales agissent comme des tableaux associatifs qui utilisent une valeur de chaîne comme clé pour accéder aux valeurs. Voici la liste des variables superglobales en PHP :

- ```$_GLOBALS``` est la variable superglobale qui stocke toutes les variables globales définies par l'utilisateur. Les noms des variables globales agissent comme des clés pour accéder à leurs valeurs.
- ```$_SERVER``` contient des données sur les en-têtes, les scripts et les chemins. Les clés des valeurs de ce tableau sont prédéfinies.
- ```$_REQUEST``` stocke les données saisies sous la forme de HTTP POST, GET et Cookies. Les clés de ce tableau sont définies dans les requêtes HTTP.
- ```$_POST``` stocke les données saisies sous la forme de demandes POST. Les clés de ce tableau sont définies dans la demande HTTP POST.
- ```$_GET``` contient des données saisies sous la forme de requêtes GET. Les clés de ce tableau sont définies dans la requête HTTP GET.
- ```$_FILES``` est un tableau associatif bidimensionnel qui contient une liste de fichiers téléchargés vers le script à l'aide de la méthode POST. Les clés de ce tableau sont les noms des champs qui ont téléchargé les fichiers et les données auxquelles on accède. Par exemple, ```$_FILES[fileUploaded][name]``` permet d'accéder au nom du fichier téléchargé à partir du champ fileUploaded.
- ```$_COOKIES``` conserve les données saisies via les cookies HTTP. Les clés de ce tableau sont définies lorsque les cookies sont définis.
- ```$_SESSION``` contient les variables de session. Les variables de session sont accessibles sur plusieurs pages. Les clés de ce tableau sont définies par les utilisateurs lorsqu'ils définissent les variables de session.
- ```$_ENV``` contient des informations sur l'environnement dans lequel PHP est exécuté. Les clés des valeurs de ce tableau sont prédéfinies.

# Contenu de ./0320 - PSR 03 - Logger Interface/content.md

Ce document décrit une interface commune pour la journalisation des bibliothèques.

L'objectif principal est de permettre aux bibliothèques de recevoir un objet ```Psr\Log\LoggerInterface``` et d'y écrire des logs de manière simple et universelle.

Les frameworks et les CMS qui ont des besoins personnalisés **peuvent** étendre l'interface pour leur propre usage, mais **doivent** rester compatibles avec ce document. Cela garantit que les bibliothèques tierces qu'une application utilise peuvent écrire dans les journaux d'application centralisés.

## Caractéristiques

### Notion de base

- Le LoggerInterface propose huit méthodes pour écrire des rapports aux huit niveaux de la RFC 5424 (debug, info, notice, warning, error, critical, alert, emergency).
- Une neuvième méthode, le log, accepte un niveau de log comme premier argument. L'appel de cette méthode avec une des constantes de niveau log DOIT avoir le même résultat que l'appel de la méthode spécifique au niveau. L'appel de cette méthode avec un niveau non défini par cette spécification DOIT lancer un Psr\Log\InvalidArgumentException si l'implémentation ne connaît pas le niveau. Les utilisateurs NE DOIVENT PAS utiliser un niveau spécifique sans être sûrs que l'implémentation actuelle le supporte.

### Message

- Chaque méthode accepte une chaîne de caractères comme message ou un objet avec une méthode ```__toString()```. Les implémenteurs PEUVENT avoir un traitement spécial pour les objets passés. Si ce n'est pas le cas, les implémenteurs DOIVENT le transformer en une chaîne de caractères.
- Le message PEUT contenir des caractères de remplacement que les implémenteurs PEUVENT remplacer par des valeurs du tableau de contexte.

Les noms de remplacement DOIVENT correspondre aux clés dans le tableau de contexte.

Les noms de remplacement DOIVENT être délimités par une seule accolade ouvrante { et une seule accolade fermante }. Il NE DOIT PAS y avoir d'espace entre les délimiteurs et le nom de remplacement.

Les noms de remplacement DOIVENT être composés uniquement des caractères A-Z, a-z, 0-9, du trait de soulignement _ et des points… L'utilisation d'autres caractères est réservée aux modifications futures de la spécification des noms de remplacement.

Les implémenteurs PEUVENT utiliser les caractères de remplissage pour mettre en œuvre diverses stratégies et traduire les logs pour l'affichage. Les utilisateurs NE DEVRAIENT PAS pré-échapper les valeurs des caractères de remplacement, car ils ne peuvent pas savoir dans quel contexte les données seront affichées.

Voici un exemple de mise en œuvre de l'interpolation des caractères de remplacement, fourni à titre de référence uniquement :

``` php
<?php

/**
 * Interpole les valeurs de contexte dans les messages de     
 * remplacement.
 */
function interpolate($message, array $context = array())
{
    // construit un tableau de remplacement avec des crochets autour des clés de contexte
    $replace = array();
    foreach ($context as $key => $val) {
        // vérifie que la valeur peut être exprimée en chaîne de caractères
        if (!is_array($val) && (!is_object($val) || method_exists($val, '__toString'))) {
            $replace['{' . $key . '}'] = $val;
        }
    }

    // interpole les valeurs de remplacement dans le message et le retour
    return strtr($message, $replace);
}

// un message avec les noms de remplacement délimités par des accolades
$message = "Utilisateur {username} créé";

// un tableau contextuel de noms de remplacement => valeurs de remplacement
$context = array('username' => 'bolivar');

// écrit "Utilisateur bolivar créé"
echo(interpolate($message, $context));
```

### Contexte

Chaque méthode accepte un tableau comme données de contexte. Celui-ci est destiné à contenir toute information étrangère qui ne s'inscrit mal dans une chaîne. Le tableau peut contenir n'importe quoi. Les implémenteurs DOIVENT s'assurer qu'ils traitent les données contextuelles avec autant d'indulgence que possible. Une valeur donnée dans le contexte NE DOIT PAS lancer d'exception ni provoquer d'erreur PHP ou encore d'avertissement.

Si un objet Exception est passé dans les données de contexte, il DOIT être dans la clé "exception". La journalisation des exceptions est un modèle courant et cela permet aux implémenteurs d'extraire une trace des exceptions lorsque le backend de journalisation le supporte. Les implémenteurs DOIVENT toujours vérifier que la clé "exception" est bien une Exception avant de l'utiliser en tant que telle, car elle PEUT contenir n'importe quoi.

### Classe d'assistants et interfaces

- La classe ```Psr\Log\AbstractLogger``` vous permet d'implémenter très facilement l'interface de journalisation en l'étendant et en implémentant la méthode de journalisation générique. Les huit autres méthodes lui transmettent le message et le contexte.
- De même, l'utilisation de la classe ```Psr\Log\LoggerTrait``` nécessite seulement l'implémentation de la méthode de journalisation générique. Notez que puisque les traits ne peuvent pas implémenter les interfaces, dans ce cas, vous devez constamment implémenter ```LoggerInterface```.
- Le ```Psr\Log\NNLogger``` est fourni avec l'interface. Il PEUT être utilisé par les utilisateurs de l'interface pour fournir une implémentation de repli "trou noir" si aucun logger ne leur est fourni. Cependant, la journalisation conditionnelle peut être une meilleure approche si la création de données contextuelles est coûteuse.
- La ```Psr\Log\LoggerAwareInterface``` ne contient qu'une méthode ```setLogger(LoggerInterface $logger)``` et peut être utilisée par les frameworks pour connecter automatiquement des instances arbitraires avec un logger.
- Le trait ```Psr\Log\LoggerAwareTrait``` peut être utilisé pour implémenter facilement l'interface équivalente dans n'importe quelle classe. Il vous donne accès à ```$this->logger```.
- La classe ```Psr\Log\LogLevel``` contient des constantes pour les huit niveaux de journalisation.

## Paquet

Les interfaces et les classes décrites ainsi que les classes d'exception correspondantes et une suite de tests pour vérifier votre implémentation sont fournies dans le cadre du paquet ```psr/log```.

## Psr\Log\LoggerInterface

``` php
<?php

namespace Psr\Log;

/**
 * Décrit une instance de logger.
 *
 * Le message DOIT être une chaîne ou un objet implémentant 
 * __toString().
 *
 * Le message PEUT contenir des espaces réservés dans le formulaire :    
 * {foo} où foo sera remplacé par les données de contexte dans la clé 
 * "foo".
 *
 * Le tableau de contexte peut contenir des données arbitraires, la
 * seule hypothèse qui peut être faite par les implémenteurs est que si 
 * une instance d'Exception est donnée pour produire une trace, elle 
 * DOIT être dans une clé nommée "exception".
 *
 * Voir 
https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logg
er-interface.md
 * pour la spécification complète de l'interface.
 */
interface LoggerInterface
{
    /**
     * Le système est inutilisable.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function emergency($message, array $context = array());

    /**
     * Des mesures doivent être prises immédiatement.
     *
     * Exemple : Tout le site web est hors service, la base de données 
     * est indisponible, etc. Cela devrait déclencher les alertes SMS et 
     * vous réveiller.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function alert($message, array $context = array());

    /**
     * Conditions critiques.
     *
     * Exemple : Composante de la demande indisponible, exception 
     * inattendue.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function critical($message, array $context = array());

    /**
     * Les erreurs d'exécution qui ne nécessite pas de mesures 
     * immédiates, mais qui devraient généralement être enregistrées et 
     * surveillées.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function error($message, array $context = array());

    /**
     * Des événements exceptionnels qui ne sont pas des erreurs.
     *
     * Exemple : Utilisation d'API dépréciées, mauvaise utilisation 
     * d'une API, choses indésirables qui ne sont pas nécessairement 
     * mauvaises.
     *
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function warning($message, array $context = array());

    /**
     * Des événements normaux, mais significatifs.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function notice($message, array $context = array());

    /**
     * Événements intéressants.
     *
     * Exemple : L'utilisateur se connecte, les journaux SQL.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function info($message, array $context = array());

    /**
     * Informations détaillées sur le débogage.
     *
     * @param string $message
     * @param array $context
     * @return void
     */
    public function debug($message, array $context = array());

    /**
     * Des journaux avec un niveau arbitraire.
     *
     * @param mixed $level
     * @param string $message
     * @param array $context
     * @return void
     */
    public function log($level, $message, array $context = array());
}
```

## Psr\Log\LoggerAwareInterface

``` php
<?php

namespace Psr\Log;

/**
 * Décrit une instance compatible avec le logger.
 */
interface LoggerAwareInterface
{
    /**
     * Définit une instance de logger sur l'objet.
     *
     * @param LoggerInterface $logger
     * @return void
     */
    public function setLogger(LoggerInterface $logger);
}
```

## Psr\Log\LogLevel

``` php
<?php

namespace Psr\Log;

/**
 * Décrit les niveaux de journalisation.
 */
class LogLevel
{
    const EMERGENCY = 'emergency';
    const ALERT     = 'alert';
    const CRITICAL  = 'critical';
    const ERROR     = 'error';
    const WARNING   = 'warning';
    const NOTICE    = 'notice';
    const INFO      = 'info';
    const DEBUG     = 'debug';
}
```

# Contenu de ./0330 - PSR 04 - Autoloading Standard/content.md

Ce PSR décrit une spécification pour l'auto-chargement de classes à partir de chemins de fichiers. Il est entièrement interopérable et peut être utilisé en complément de toute autre spécification d'auto-chargement, y compris le PSR-0. Ce PSR décrit également où placer les fichiers qui seront autochargés conformément à la spécification.

## Caractéristiques

1. Le terme "classe" fait référence aux classes, interfaces, traits et autres structures similaires.
2. Un nom de classe doit avoir la forme suivante : ```\<NamespaceName>(\<SubNamespaceNames>)*\<ClassName>```
    1. Le nom de classe DOIT avoir un dossier (namespace) de premier niveau, aussi appelé "vendor namespace".
    2. Le nom de classe PEUT avoir un ou plusieurs sous-dossiers (subnamespace).
    3. Le nom de classe DOIT avoir un dossier de classe terminale.
    4. Les traits de soulignement n'ont aucune signification particulière dans aucune partie du nom de classe.
    5. Les caractères alphabétiques dans le nom de classe PEUVENT être une combinaison de minuscules et de majuscules.
    6. Tous les noms de classe DOIVENT être référencés en tenant compte de la sensibilité de la casse.
3. Lors du chargement d'un fichier qui correspond à un nom de classe...
    1. Une série consécutive d'un ou plusieurs dossiers et de sous-dossier, sans inclure le séparateur de dossier,  dans le nom de classe correspond à, au moins, un "répertoire de base".
    2. Les noms des sous-dossiers consécutifs après un préfixe de dossier correspondent à un sous-répertoire dans un "répertoire de base", dans lequel les séparateurs de nom représentent des séparateurs de répertoire. Le nom du sous-répertoire DOIT correspondre à la casse des noms des sous-dossiers.
    3. Le nom de la classe terminale correspond à un nom de fichier se terminant par .php. Le nom du fichier DOIT correspondre à la casse du nom de la classe terminale.
4. Les implémentations d'auto-chargeurs NE DOIVENT PAS lancer d'exceptions, NE DOIVENT PAS soulever d'erreurs de quelque niveau que ce soit, et NE DOIVENT PAS renvoyer de valeur.

## Exemples

Le tableau ci-dessous indique le chemin de fichier correspondant pour un nom de classe, un préfixe d'un dossier et un répertoire de base donnés.

| **Nom de la classe** | **Préfixe du dossier** | **Répertoire de base** | **Résultat du chemin** |
| --- | --- | --- | --- |
| ```\Acme\Log\Writer\File_Writer``` | ```Acme\Log\Writer``` | ```./acme-log-writer/lib/``` | ```./acme-log-writer/lib/File_Writer.php``` |
| ```\Aura\Web\Response\Status``` | ```Aura\Web``` | ```/path/to/aura-web/src/``` | ```/path/to/aura-web/src/Response/Status.php``` |
| ```\Symfony\Core\Request``` | ```Symfony\Core``` | ```./vendor/Symfony/Core/``` | ```./vendor/Symfony/Core/Request.php``` |
| ```\Zend\Acl``` | ```Zend``` | ```/usr/includes/Zend/``` | ```/usr/includes/Zend/Acl.php``` |

# Contenu de ./0340 - PSR 12 - Extended Coding Style Guide/content.md

L’objectif du PSR 12 est d’étendre et remplacer le PSR 2, le guide de style de codage exige le respect du PSR 1, la norme de codage de base. Comme le PSR 2, cette spécification permet de réduire les frictions cognitives lors de la numérisation du code de différents auteurs. Le PSR 12 vise à fournir une manière définie que les outils de style de codage peuvent mettre en œuvre, les projets peuvent déclarer leur adhésion et les développeurs peuvent facilement s’identifier entre différents projets. Lorsque plusieurs développeurs collaborent sur plusieurs projets, il est utile de définir un ensemble de directives à utiliser pour ces projets. Ainsi, l'intérêt de ce PSR n’est pas dans les règles de style, mais dans le partage de ces règles.

En résumé, le PSR 12 cherche à clarifier le contenu du PSR 2 dans un contexte plus moderne avec de nouvelles fonctionnalités disponibles.

Exemple :

```php
<?php

declare(strict_types=1);

namespace Vendor\Package;

use Vendor\Package\{ClassA as A, ClassB, ClassC as C};
use Vendor\Package\SomeNamespace\ClassD as D;

use function Vendor\Package\{functionA, functionB, functionC};

use const Vendor\Package\{ConstantA, ConstantB, ConstantC};

class Foo extends Bar implements FooInterface
{
    public function sampleFunction(int $a, int $b = null): array
    {
        if ($a === $b) {
            bar();
        } elseif ($a > $b) {
            $foo->bar($arg1);
        } else {
            BazClass::bar($arg2, $arg3);
        }
    }

    final public static function bar()
    {
        // méthode
    }
}
?>
```

## Norme de codage de base

Le code doit suivre les règles décrites dans le PSR-1. Le terme “StudlyCaps” dans le PSR-1 doit être interprété comme PascalCase où la première lettre de chaque mot est en majuscule. y compris la toute première lettre

## Les fichiers

Tous les fichiers en PHP doivent utiliser uniquement la fin de ligne Unix LF (linefeed). Tous les fichiers PHP doivent se terminer par une ligne non vide, terminée par un seul LF. La balise ```?>``` de fermeture doit être omise des fichiers contenant seulement du PHP.

## Les Lignes

Il ne doit pas y avoir de limite stricte sur la longueur de la ligne. La limite souple sur la longueur de ligne doit être de 120 caractères. Les lignes ne devraient pas dépasser 80 caractères ; les lignes plus longues devraient être divisées en plusieurs lignes suivantes de 80 caractères chacune au maximum. Il ne doit pas y avoir d'espace à la fin des lignes. Des lignes vierges peuvent être ajoutées pour améliorer la lisibilité et pour indiquer les blocs de code associés, sauf là où cela est explicitement interdit. Il ne doit pas y avoir plus d'une instruction par ligne.

## Les Indentations

Le code DOIT utiliser un retrait de 4 espaces pour chaque niveau de retrait et NE DOIT PAS utiliser de tabulations pour le retrait.

## Les mots-clés et types

Tous les mots-clés et types doivent être en minuscules. Tous les nouveaux types et mots-clés ajoutés aux futures versions de PHP doivent être en minuscules.

La forme courte des mots-clés de type doit être utilisée, c'est "bool"-à dire au lieu de boolean, “int” au lieu de “integer”, etc.

## Les déclarations de déclarations, espace de noms et déclarations d’importation

L'en-tête d'un fichier PHP peut être constitué de plusieurs blocs différents. S'il est présent, chacun des blocs ci-dessous doit être séparé par une seule ligne vierge, et ne doit pas contenir de ligne vierge. Chaque bloc doit être dans l'ordre indiqué ci-dessous, bien que les blocs qui ne sont pas pertinents puissent être omis.

- Balise ```<?php``` d'ouverture.
- Docblock au niveau du fichier.
- Une ou plusieurs déclarations.
- La déclaration d'espace de noms du fichier.
- Une ou plusieurs “useinstructions” d'importation basée sur les classes.
- Une ou plusieurs “useinstructions” d'importation basée sur des fonctions.
- Une ou plusieurs “useinstructions” d'importation basée sur des constantes.
- Le reste du code dans le fichier.

Lorsqu'un fichier contient un mélange de HTML et de PHP, l'une des sections ci-dessus peut toujours être utilisée. Si c'est le cas, ils doivent être présents en haut du fichier, même si le reste du code consiste en une balise PHP de fermeture puis en un mélange de HTML et de PHP.

Lorsque la balise d'ouverture ```<?php``` est sur la première ligne du fichier, elle doit être sur sa propre ligne sans aucune autre instruction, à moins qu'il ne s'agisse d'un fichier contenant un balisage en dehors des balises d'ouverture et de fermeture PHP.

Les instructions d'importation ne doivent jamais commencer par une barre oblique inverse, car elles doivent toujours être pleinement qualifiées.

Exemple :

```php
<?php

/**
 * Ce fichier contient un exemple de coding styles.
 */

declare(strict_types=1);

namespace Vendor\Package;

use Vendor\Package\{ClassA as A, ClassB, ClassC as C};
use Vendor\Package\SomeNamespace\ClassD as D;
use Vendor\Package\AnotherNamespace\ClassE as E;

use function Vendor\Package\{functionA, functionB, functionC};
use function Another\Vendor\functionD;

use const Vendor\Package\{CONSTANT_A, CONSTANT_B, CONSTANT_C};
use const Another\Vendor\CONSTANT_D;

/**
 * FooBar est un exemple de classe
 */
class FooBar
{
    // ... PHP code ...
}
```

Les espaces de noms composés avec une profondeur de plus de deux ne doivent pas être utilisés. Par conséquent, la profondeur de composition maximale autorisée est la suivante :

Exemple :

```php
<?php

use Vendor\Package\SomeNamespace\{
    SubnamespaceOne\ClassA,
    SubnamespaceOne\ClassB,
    SubnamespaceTwo\ClassY,
    ClassZ,
};
```

Et ce qui suit ne serait pas autorisé :

Exemple :

```php
<?php

use Vendor\Package\SomeNamespace\{
    SubnamespaceOne\AnotherNamespace\ClassA,
    SubnamespaceOne\ClassB,
    ClassZ,
};
```

Lorsque vous souhaitez déclarer des types stricts dans des fichiers contenant un balisage en dehors des balises d'ouverture et de fermeture PHP, la déclaration doit être sur la première ligne du fichier et inclure une balise PHP d'ouverture, la déclaration des types stricts et la balise de fermeture.

Exemple :

```php
<?php declare(strict_types=1) ?>
<html>
<body>
    <?php
        // ... PHP code ...
    ?>
</body>
</html>
```

Les déclarations de déclaration ne doivent contenir aucun espace et doivent être exactement ```declare(strict_types=1)``` (avec un point-virgule facultatif de fin).

Les déclarations de bloc sont autorisées et doivent être formatées comme ci-dessous. Notez la position des accolades et l'espacement :

```php
declare(ticks=1) {
    // code
}
```

## Les classes, propriété et méthodes

Le terme « classe » fait référence à toutes les classes, interfaces et traits.

Aucune accolade fermante ne doit être suivie d'un commentaire ou d'une déclaration sur la même ligne.

Lors de l'instanciation d'une nouvelle classe, les parenthèses doivent toujours être présentes même lorsqu'il n'y a pas d'arguments passés au constructeur.

```php
new Foo();
```

## Extends et implements

Les mots clés “extends” et “implements” doivent être déclarés sur la même ligne que le nom de la classe. L'accolade ouvrante pour la classe doit aller sur sa propre ligne ; l'accolade fermante de la classe doit aller sur la ligne suivante après le corps. Les accolades ouvrantes doivent être sur leur propre ligne et ne doivent pas être précédées ou suivies d'une ligne vide. Les accolades fermantes doivent être sur leur propre ligne et ne doivent pas être précédées d'une ligne vide.

Exemple :

```php
<?php

namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements \ArrayAccess, \Countable
{
    // constants, properties, methods
}
```

Les listes de “implements” et, dans le cas des interfaces, “extends” peuvent être réparties sur plusieurs lignes, où chaque ligne suivante est indentée une fois. Ce faisant, le premier élément de la liste doit être sur la ligne suivante, et il doit n'y avoir qu'une seule interface par ligne.

```php
<?php

namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements
    \ArrayAccess,
    \Countable,
    \Serializable
{
    // constants, properties, methods
}
```

## Utilisation des traits

Le mot-clé ```use``` utilisé à l'intérieur des classes pour implémenter les traits doit être déclaré sur la ligne suivante après l'accolade ouvrante.

Exemple :

```php
<?php

namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;
}
```

Chaque trait individuel importé dans une classe doit être inclus une par ligne et chaque inclusion doit avoir sa propre déclaration d'importation.

```php
<?php

namespace Vendor\Package;

use Vendor\Package\FirstTrait;
use Vendor\Package\SecondTrait;
use Vendor\Package\ThirdTrait;

class ClassName
{
    use FirstTrait;
    use SecondTrait;
    use ThirdTrait;
}
```

Lorsque la classe n'a rien après l'instruction use, l'accolade fermante de classe doit être sur la ligne suivante après l'instruction use.

```php
<?php

namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;
}
```

Sinon, il doit avoir une ligne vide après l'instruction use.

```php
<?php

namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;

    private $property;
```

Lorsque vous utilisez les opérateurs “insteadof” et “as” ils doivent être utilisés comme suit en tenant compte de l'indentation, de l'espacement et des nouvelles lignes.

```php
<?php

class Talker
{
    use A;
    use B {
        A::smallTalk insteadof B;
    }
    use C {
        B::bigTalk insteadof C;
        C::mediumTalk as FooBar;
    }
}
```

## Les propriétés et constantes

La visibilité doit être déclarée sur toutes les propriétés. La visibilité doit être déclarée sur toutes les constantes si la version minimale de PHP de votre projet prend en charge les visibilités constantes (PHP 7.1 ou version ultérieure). Le mot-clé “var” ne doit pas être utilisé pour déclarer une propriété. Il ne doit pas y avoir plus d'une propriété déclarée par instruction. Les noms de propriété ne doivent pas être précédés d'un seul trait de soulignement pour indiquer une visibilité protégée ou privée. C'est-à-dire qu'un préfixe de soulignement n'a explicitement aucune signification. Il doit y avoir un espace entre la déclaration de type et le nom de la propriété. Une déclaration de propriété ressemble à ce qui suit :

```php
<?php

namespace Vendor\Package;

class ClassName
{
    public $foo = null;
    public static int $bar = 0;
}
```

## Les méthodes et fonctions

La visibilité doit être déclarée sur toutes les méthodes. Les noms de méthode ne doivent pas être précédés d'un seul trait de soulignement pour indiquer une visibilité protégée ou privée. C'est-à-dire qu'un préfixe de soulignement n'a explicitement aucune signification.

Les noms de méthode et de fonction ne doivent pas être déclarés avec un espace après le nom de la méthode. L'accolade ouvrante doit aller sur sa propre ligne et l'accolade fermante doit aller sur la ligne suivante après le corps. Il ne doit pas y avoir d'espace après la parenthèse ouvrante, et il ne doit pas y avoir d'espace avant la parenthèse fermante.

Une déclaration de méthode ressemble à ce qui suit. Notez l'emplacement des parenthèses, des virgules, des espaces et des accolades :

```php
<?php

namespace Vendor\Package;

class ClassName
{
    public function fooBarBaz($arg1, &$arg2, $arg3 = [])
    {
        // method body
    }
}
```

Une déclaration de fonction ressemble à ce qui suit. Notez l'emplacement des parenthèses, des virgules, des espaces et des accolades :

```php
<?php

function fooBarBaz($arg1, &$arg2, $arg3 = [])
{
    // function body
}
```

## Les arguments de méthode et de fonction

Dans la liste des arguments, il ne doit pas y avoir d'espace avant chaque virgule, et il doit y avoir un espace après chaque virgule.

Les arguments de méthode et de fonction avec des valeurs par défaut doivent aller à la fin de la liste d'arguments.

Exemple :

```php
<?php

namespace Vendor\Package;

class ClassName
{
    public function foo(int $arg1, &$arg2, $arg3 = [])
    {
        // method body
    }
}
```

Les listes d'arguments peuvent être divisées sur plusieurs lignes, où chaque ligne suivante est indentée une fois. Ce faisant, le premier élément de la liste doit être sur la ligne suivante, et il doit n'y avoir qu'un seul argument par ligne.

Lorsque la liste d'arguments est divisée sur plusieurs lignes, la parenthèse fermante et l'accolade ouvrante doivent être placées ensemble sur leur propre ligne avec un espace entre elles.

```php
<?php

namespace Vendor\Package;

class ClassName
{
    public function aVeryLongMethodName(
        ClassTypeHint $arg1,
        &$arg2,
        array $arg3 = []
    ) {
        // method body
    }
}
```

Lorsque vous avez une déclaration de type de retour présente, il doit y avoir un espace après les deux points suivis de la déclaration de type. Les deux points et la déclaration doivent être sur la même ligne que la parenthèse fermante de la liste d'arguments sans espace entre les deux caractères.

```php
<?php

declare(strict_types=1);

namespace Vendor\Package;

class ReturnTypeVariations
{
    public function functionName(int $arg1, $arg2): string
    {
        return 'foo';
    }

    public function anotherFunction(
        string $foo,
        string $bar,
        int $baz
    ): string {
        return 'foo';
    }
}
```

Dans les déclarations de type nullable, il ne doivent pas y avoir d'espace entre le point d'interrogation et le type.

```php
<?php

declare(strict_types=1);

namespace Vendor\Package;

class ReturnTypeVariations
{
    public function functionName(?string $arg1, ?int &$arg2): ?string
    {
        return 'foo';
    }
}
```

Lorsque vous utilisez l'opérateur de référence “&” avant un argument, il ne doit pas y avoir d'espace après celui-ci, comme dans l'exemple précédent.
Il ne doit pas y avoir d'espace entre l'opérateur variadique à trois points et le nom de l'argument :

```php
public function process(string $algorithm, ...$parts)
{
    // code
}
```

Lors de la combinaison de l'opérateur de référence et de l'opérateur variadique à trois points, il ne doit pas  y avoir d'espace entre les deux :

```php
public function process(string $algorithm, &...$parts)
{
    // code
}
```

## Abstract, final et static

Lorsqu'elles sont présentes, les déclarations ```abstract``` et ```final``` doivent précéder la déclaration de visibilité.

Lorsqu'elle est présente, la déclaration ```static``` doit venir après la déclaration de visibilité.

```php
<?php

namespace Vendor\Package;

abstract class ClassName
{
    protected static $foo;

    abstract protected function zim();

    final public static function bar()
    {
        // method body
    }
}
```

## Les appels de méthode et de fonction

Lors d'un appel de méthode ou de fonction, il ne doit pas y avoir d'espace entre le nom de la méthode ou de la fonction et la parenthèse ouvrante, il ne doit pas y avoir d'espace après la parenthèse ouvrante, et il ne doit pas y avoir d'espace avant la parenthèse fermante. Dans la liste des arguments, il ne doit pas y avoir d'espace avant chaque virgule, et il doit y avoir un espace après chaque virgule.

Exemple :

```php
<?php

bar();
$foo->bar($arg1);
Foo::bar($arg2, $arg3);
```

Les listes d'arguments peuvent être divisées sur plusieurs lignes, où chaque ligne suivante est indentée une fois. Ce faisant, le premier élément de la liste doit être sur la ligne suivante, et il doit n'y avoir qu'un seul argument par ligne. Un seul argument divisé sur plusieurs lignes (comme cela pourrait être le cas avec une fonction ou un tableau anonyme) ne constitue pas une division de la liste d'arguments elle-même.

```php
<?php

$foo->bar(
    $longArgument,
    $longerArgument,
    $muchLongerArgument
);

<?php

somefunction($foo, $bar, [
  // ...
], $baz);

$app->get('/hello/{name}', function ($name) use ($app) {
    return 'Hello ' . $app->escape($name);
});
```

## Les structures de contrôle

Les règles générales de style pour les structures de contrôle sont les suivantes :

- Il doit y avoir un espace après le mot-clé de la structure de contrôle
- Il ne doit pas  y avoir d'espace après la parenthèse ouvrante
- Il ne doit pas y avoir d'espace avant la parenthèse fermante
- Il doit y avoir un espace entre la parenthèse fermante et l'accolade ouvrante
- Le corps de la structure doit être indenté une fois
- Le corps doit être sur la ligne suivante après l'accolade d'ouverture
- L'accolade fermante doit être sur la ligne suivante après le corps

Le corps de chaque structure doit être entouré d'accolades. Cela standardise l'apparence des structures et réduit la probabilité d'introduire des erreurs lorsque de nouvelles lignes sont ajoutées au corps.

## If, elseif, else

Une structure “if” ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades ; et que “else” et “elseif” sont sur la même ligne que l'accolade de fermeture du corps plus tôt.

Exemple :

```php
<?php

if ($expr1) {
    // if body
} elseif ($expr2) {
    // elseif body
} else {
    // else body;
}
```

Le mot-clé ```elseif``` devrait être utilisé à la place de ```else if``` pour que tous les mots-clés de contrôle ressemblent à des mots simples.

Les expressions entre parenthèses peuvent être réparties sur plusieurs lignes, chaque ligne suivante étant indentée au moins une fois. Ce faisant, la première condition doit être sur la ligne suivante. La parenthèse fermante et l'accolade ouvrante doivent être placées ensemble sur leur propre ligne avec un espace entre elles. Les opérateurs booléens entre les conditions doivent toujours être au début ou à la fin de la ligne, pas un mélange des deux.

```php
<?php

if (
    $expr1
    && $expr2
) {
    // if body
} elseif (
    $expr3
    && $expr4
) {
    // elseif body
}
```

## Switch, case

Une structure ```switch``` ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades. La déclaration ```case``` doit être indentée une fois de ```switch```, et le mot - clé (ou d'autres mots-clés de fin) ```break``` doit être indenté au même niveau que le ```case``` corps. Il doit y avoir un commentaire tel que ```// no “break”``` lorsque la chute est intentionnelle.

Exemple :

```php
<?php

switch ($expr) {
    case 0:
        echo 'First case, with a break';
        break;
    case 1:
        echo 'Second case, which falls through';
        // no break
    case 2:
    case 3:
    case 4:
        echo 'Third case, return instead of break';
        return;
    default:
        echo 'Default case';
        break;
}
```

Les expressions entre parenthèses peuvent être réparties sur plusieurs lignes, chaque ligne suivante étant indentée au moins une fois. Ce faisant, la première condition doit être sur la ligne suivante. La parenthèse fermante et l'accolade ouvrante doivent être placées ensemble sur leur propre ligne avec un espace entre elles. Les opérateurs booléens entre les conditions doivent toujours être au début ou à la fin de la ligne, pas un mélange des deux.

```php
<?php

switch (
    $expr1
    && $expr2
) {
    // structure body
}
```

## While, do while

Une déclaration ```while``` ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades.

Exemple :

```php
<?php

while ($expr) {
    // code
}
```

Les expressions entre parenthèses peuvent être réparties sur plusieurs lignes, chaque ligne suivante étant indentée au moins une fois. Ce faisant, la première condition doit être sur la ligne suivante. La parenthèse fermante et l'accolade ouvrante doivent être placées ensemble sur leur propre ligne avec un espace entre elles. Les opérateurs booléens entre les conditions doivent toujours être au début ou à la fin de la ligne, pas un mélange des deux.

```php
<?php

while (
    $expr1
    && $expr2
) {
    // code
}
```

De même, une déclaration ```do while``` ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades.

```php
<?php

do {
    // code
} while ($expr);
```

Les expressions entre parenthèses peuvent être réparties sur plusieurs lignes, chaque ligne suivante étant indentée au moins une fois. Ce faisant, la première condition doit être sur la ligne suivante. Les opérateurs booléens entre les conditions doivent toujours être au début ou à la fin de la ligne, pas un mélange des deux.

```php
<?php

do {
    //code
} while (
    $expr1
    && $expr2
);
```

## For

Une déclaration ```for``` ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades.

Exemple :

```php
<?php

for ($i = 0; $i < 10; $i++) {
    // code
} 
```

Les expressions entre parenthèses peuvent être réparties sur plusieurs lignes, chaque ligne suivante étant indentée au moins une fois. Ce faisant, la première expression doit être sur la ligne suivante. La parenthèse fermante et l'accolade ouvrante doivent être placées ensemble sur leur propre ligne avec un espace entre elles.

```php
<?php

for (
    $i = 0;
    $i < 10;
    $i++
) {
    // code
}
```

## Foreach

Une déclaration ```foreach``` ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades.

Exemple :

```php
<?php

foreach ($iterable as $key => $value) {
    // code
}
```

## Try, catch, finally

Un bloc ```try-catch-finally``` ressemble à ce qui suit. Notez le placement des parenthèses, des espaces et des accolades.

Exemple :

```php
<?php

try {
    // try code
} catch (FirstThrowableType $e) {
    // catch code
} catch (OtherThrowableType | AnotherThrowableType $e) {
    // catch code
} finally {
    // finally code
}
```

## Les opérateurs

Les règles de style pour les opérateurs sont regroupées par arité (le nombre d'opérandes qu'elles prennent). Lorsque l'espace est autorisé autour d'un opérateur, plusieurs espaces peuvent être utilisés à des fins de lisibilité. Tous les opérateurs non décrits ici ne sont pas définis.

### Les opérateurs unaires

Les opérateurs d'incrémentation/décrémentation ne doivent pas avoir d'espace entre l'opérateur et l'opérande.

```php
$i++;
++$j;
```

Les opérateurs de transtypage ne doivent pas avoir d'espace entre les parenthèses :

```php
$intValue = (int) $input;
```

### Les opérateurs binaires

Tous les opérateurs binaires arithmétiques, de comparaison, d'affectation, au niveau du bit, logiques, de chaîne et de type doivent être précédés et suivis d'au moins un espace :

```php
if ($a === $b) {
    $foo = $bar ?? $a ?? $b;
} elseif ($a > $b) {
    $foo = $a + $b * $c;
}
```

### Les opérateurs ternaires

L'opérateur conditionnel, également connu simplement sous le nom d'opérateur ternaire, doit être précédé et suivi d'au moins un espace autour des caractères “?” et “:” :

```php
$variable = $foo ? 'foo' : 'bar';
```

Lorsque l'opérande du milieu de l'opérateur conditionnel est omis, l'opérateur doit suivre les mêmes règles de style que les autres opérateurs de comparaison binaire :

```php
$variable = $foo ?: 'bar';
```

## Les fermetures

Les fermetures doivent être déclarées avec un espace après le mot - clé ```function```, et un espace avant et après le mot - clé ```use```. L'accolade ouvrante doit aller sur la même ligne et l'accolade fermante doit aller sur la ligne suivante après le corps. Il ne doit pas y avoir d'espace après la parenthèse ouvrante de la liste d'arguments ou de la liste de variables, et il ne doit pas y avoir d'espace avant la parenthèse fermante de la liste d'arguments ou de la liste de variables. Dans la liste des arguments et la liste des variables, il ne doit pas y avoir d'espace avant chaque virgule, et il doit y avoir un espace après chaque virgule.

Les arguments de fermeture avec les valeurs par défaut doivent aller à la fin de la liste des arguments. Si un type de retour est présent, il doit suivre les mêmes règles qu'avec les fonctions et méthodes normales ; si le mot-clé ```use``` est présent, les deux points doivent suivre la liste des parenthèses fermantes sans espace entre les deux caractères.

Une déclaration de clôture ressemble à ce qui suit. Notez l'emplacement des parenthèses, des virgules, des espaces et des accolades :

```php
<?php

$closureWithArgs = function ($arg1, $arg2) {
    // code
};

$closureWithArgsAndVars = function ($arg1, $arg2) use ($var1, $var2) {
    // code
};

$closureWithArgsVarsAndReturn = function ($arg1, $arg2) use ($var1, $var2): bool {
    // code
};
```

Les listes d'arguments et les listes de variables peuvent être divisées sur plusieurs lignes, où chaque ligne suivante est indentée une fois. Ce faisant, le premier élément de la liste doit être sur la ligne suivante, et il doit n'y avoir qu'un seul argument ou variable par ligne. Lorsque la liste de fin (qu'il s'agisse d'arguments ou de variables) est divisée sur plusieurs lignes, la parenthèse fermante et l'accolade ouvrante doivent être placées ensemble sur leur propre ligne avec un espace entre elles. Voici des exemples de fermetures avec et sans listes d'arguments et de listes de variables réparties sur plusieurs lignes.

```php
<?php

$longArgs_noVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) {
   // code
};

$noArgs_longVars = function () use (
    $longVar1,
    $longer Var2,
    $muchLongerVar3
) {
   // code
};

$longArgs_longVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
   // code
};

$longArgs_shortVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) use ($var1) {
   // code
};

$shortArgs_longVars = function ($arg) use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
   // code
};
```

Notez que les règles de formatage s'appliquent également lorsque la fermeture est utilisée directement dans un appel de fonction ou de méthode en tant qu'argument.

```php
<?php

$foo->bar(
    $arg1,
    function ($arg2) use ($var1) {
        // code
    },
    $arg3
);
```

## Les classes anonymes

Les classes anonymes doivent suivre les mêmes directives et principes que les fermetures de la section ci-dessus.

```php
<?php

$instance = new class {};
```

L'accolade ouvrante peut être sur la même ligne que le mot - clé “class” tant que la liste des interfaces “implements” n'est pas bouclée. Si la liste des interfaces s'enroule, l'accolade doit être placée sur la ligne suivant immédiatement la dernière interface.

Exemple :

```php
<?php

$instance = new class extends \Foo implements \HandleableInterface {
    // Class code
};

$instance = new class extends \Foo implements
    \ArrayAccess,
    \Countable,
    \Serializable
{
    // Class code
};
```

# Contenu de ./0350 - L'opérateur de contrôle d'erreur/content.md

L’opérateur de contrôle d’erreur est le symbole ```@```. Quand cet opérateur est ajouté en préfixe d’une expression, les diagnostics d’erreurs qui peuvent être générés par cette expression seront ignorés.

Si ```set_error_handler()``` est défini comme gestionnaire d’erreur personnalisé, alors il sera quand même appelé même si le diagnostic a été ignoré. Le gestionnaire d’erreur personnalisé doit appeler ```error_reporting()``` et vérifier que l’opérateur ```@``` est utilisé.

exemple :

```php
<?php
function my_error_handler($err_no, $err_msg, $filename, $linenum) {
    if (!(error_reporting() & $err_no)) {
        // Ignoré
        return false;
    }
}
?>
```

Les messages d’erreurs générés par l’expression sont disponibles dans l’élément “message” du tableau retourné par la fonction ```error_get_last()```. Le résultat de la fonction change à chaque erreur.

exemple :

```php
<?php
/* Erreur voulu (ce fichier n'existe pas): */
$mon_fichier = @file ('non_persistent_file') or
    die ("Impossible d'ouvrir le fichier : L'erreur est : '" . error_get_last()['message'] . "'");
?>
```

L’opérateur ```@``` ne fonctionne qu’avec les expressions (exemples : devant les variables, les appels de fonctions, etc), il ne fonctionne pas devant les définitions de fonctions ou de classes, ou de structure conditionnelle (exemples : if, foreach,...).

# Contenu de ./0360 - Condition - SWITCH/content.md

La boucle ```switch``` permet d’économiser du code, car elle évite au développeur d’écrire plusieurs répétitions de ```else if```. Cependant, cette boucle est l’équivalent de plusieurs instructions ```if``` et permet de comparer une variable avec plusieurs possibilités de valeurs différentes et d’exécuter du code correspondant à une valeur précise. 

## Utilisation

### Syntaxe

La boucle ```switch``` s’écrit de la manière suivante :

```php
switch(variable) {
    case 1: 
    // Code à exécuter
    break;

    case 2:
    // Code à exécuter
    break;

    default :
    // Code à exécuter
}
```

#### case

Le mot-clé ```case``` permet de préciser une valeur. En d’autres termes, ```case 1``` signifie “**si la valeur de la variable est 1**”, alors il faut exécuter le code qui suit. Il passe ensuite au ```case``` suivant.

#### break

Ce mot-clé permet de sortir de la boucle lorsque la valeur du ```case``` correspond à celle de la variable. Le programme exécute le code et quitte la boucle. 

L’oubli d’un ```break``` aura pour conséquence de faire passer le programme au case suivant, quand bien même la valeur correspond à celle de la variable. 

*Remarque : Le ```break``` est inutile pour la dernière instruction de la boucle, car le programme sortira de la boucle quoi qu’il arrive.*

#### default

Ce mot-clé permet d’exécuter un morceau de code “par défaut” si aucune des valeurs ne correspond à celle de la variable. 

De manière générale, pour des raisons de logique et de lisibilité du code, le bloc ```default``` est placé comme dernière instruction dans la boucle ; cependant, il sera exécuté correctement même s’il est placé en premier.

## Exemples

Ci-dessous, quelques exemples afin d’illustrer l’utilisation de la boucle ```switch``` :

```php
$variable = "Voiture"
switch ($variable) {
    case "Camion":
        echo("$variable est un camion.");
    break;
    case "Voiture":
        echo("$variable est une voiture.");
    break;
} // Retourne "$variable est une voiture."

$variable = "Tomate"
switch ($variable) {
case "Courgette":
    echo("$variable est une courgette.");
break;
case "Carotte":
    echo("$variable est une carotte.");
break;
case "Champignon":
    echo("$variable est un champignon.");
break;
case "Tomate":
    echo("$variable est une tomate.");
break;
case "Radis":
    echo("$variable est un radis.");
break;
} // Retourne $variable est une tomate.
```

# Contenu de ./0370 - Ternaire/content.md

Les conditions ternaires permettent l’exécution d’une partie d’un code. Bien qu’un tant soit peu difficiles à comprendre au début, et pas forcément très lisibles au premier rapport, le principal avantage d’une condition ternaire est de raccourcir certaines instructions if.

## Utilisation

L’utilité principale d’une condition ternaire est d’économiser des lignes de codes - et, par conséquent, de gagner du temps - en raccourcissant au maximum l’écriture d’une condition ```if```.

### Syntaxe

Voici comment s’écrit une condition ```if``` traditionnelle :

```php
if({IF}) {
    $var = {IF};
} else {
    $var = 1;
}
```

Cette condition if est parfaitement lisible, mais un peu longue à écrire pour le peu d’instructions qu’elle a à exécuter.

Ainsi est-il possible de raccourcir cette condition en utilisant l’écriture ternaire, dont voici la syntaxe :

```php
$var = {IF} ? {THEN} : {ELSE};
```

Depuis la version 5.3 de PHP, il est possible de raccourcir davantage cette écriture :

```php
$var = {IF} ?: {ELSE};
```

## Exemple

Ci-dessous, un exemple utilisant d’abord une condition ```if```, puis l’écriture **ternaire**, puis l’écriture ternaire de la version 5.3 de PHP :

### En utilisant l’instruction IF

```php
$variable = "Camion";
if($variable == "Voiture") {
    $seconde_variable = $variable;
} else {
    $seconde_variable = "Avion";
}
// Retourne Avion
```

### Écriture ternaire

```php
$variable = "Camion";
$seconde_variable = $variable == "Voiture" ? $variable : "Avion";
// Retourne Avion
```

### Écriture ternaire avec la version 5.3 de PHP

```php
$variable = "Camion";
$seconde_variable = $variable == "Voiture" ?: "Avion";
// Retourne Avion
```

# Contenu de ./0380 - Syntaxes alternatives/content.md

PHP propose une syntaxe alternative pour certaines de ses structures de contrôle : ```if```, ```while```, ```for```, ```foreach```, et ```switch```. Dans chaque cas, la forme de base de la syntaxe alternative est de changer l'accolade d'ouverture par un deux-points (:) et l'accolade de fermeture par ```endif;```, ```endwhile;```, ```endfor;```, ```endforeach;```, ou ```endswitch;```.

## Utilisations

### IF / ELSE / ELSEIF

``` php
<?php
if ($condition):
    do_something();
elseif ($another_condition):
    do_something_else();
else:
    do_something_different();
endif;
?>

<?php if ($condition): ?>
    <p>Do something in HTML</p>
<?php elseif ($another_condition): ?>
    <p>Do something else in HTML</p>
<?php else: ?>
    <p>Do something different in HTML</p>
<?php endif; ?>
```

### SWITCH

``` php
<?php
switch ($condition):
    case $value:
        do_something();
        break;
    default:
        do_something_else();
        break;
endswitch;
?>

<?php switch ($condition): ?>
    <?php case $value: ?>
        <p>Do something in HTML</p>
        <?php break; ?>
    <?php default: ?>
        <p>Do something else in HTML</p>
        <?php break; ?>
<?php endswitch; ?>
```

### FOR

``` php
<?php
for ($i = 0; $i < 10; $i++):
    do_something($i);
endfor;
?>

<?php for ($i = 0; $i < 10; $i++): ?>
    <p>Do something in HTML with <?php echo $i; ?></p>
<?php endfor; ?>
```

### WHILE

``` php
<?php
while ($condition):
    do_something();
endwhile;
?>

<?php while ($condition): ?>
    <p>Do something in HTML</p>
<?php endwhile; ?>
```

### FOREACH

``` php
<?php
foreach ($collection as $item):
    do_something($item);
endforeach;
?>

<?php foreach ($collection as $item): ?>
    <p>Do something in HTML with <?php echo $item; ?></p>
<?php endforeach; ?>
```

# Contenu de ./0390 - Fonctions/content.md

La vraie puissance de PHP vient de ses fonctions. PHP a plus de 1000 fonctions intégrées, et en plus vous pouvez créer vos propres fonctions personnalisées.

## Fonctions intégrées

PHP a plus de 1000 fonctions intégrées qui peuvent être appelées directement, à partir d'un script, pour effectuer une tâche spécifique.

Veuillez consulter notre référence PHP pour un aperçu complet des fonctions intégrées de PHP.

Lien : <a href="https://www.php.net/manual/fr/indexes.functions.php" title="référenciel complet des fonctions en PHP" target="_blank">https://www.php.net/manual/fr/indexes.functions.php</a>

## Fonctions définies par l’utilisateur

Outre les fonctions PHP intégrées, il est possible de créer vos propres fonctions.

- Une fonction est un bloc d'instructions qui peut être utilisé à plusieurs reprises dans un programme.
- Une fonction ne s'exécutera pas automatiquement lors du chargement d'une page.
- Une fonction sera exécutée par un appel à la fonction.

## Créer une fonction définie par l’utilisateur

Une déclaration de fonction définie par l'utilisateur commence par le mot ```function``` :

syntaxe :

```php
function functionName() {
  // code
}
```

exemple :

```php
<?php
function writeMsg() {
  echo("Hello world!");
}

writeMsg(); // appel de la fonction
?>
```

## Arguments de fonction

Les informations peuvent être transmises aux fonctions via des arguments. Un argument est comme une variable.

Les arguments sont spécifiés après le nom de la fonction, à l'intérieur des parenthèses. Vous pouvez ajouter autant d'arguments que vous le souhaitez, séparez-les simplement par une virgule.

L'exemple suivant a une fonction avec un argument (```$fname```). Lorsque la fonction ```familyName()``` est appelée, nous passons également un nom (par exemple Marie), et le nom est utilisé à l'intérieur de la fonction, qui génère plusieurs prénoms différents, mais un nom de famille égal :

```php
<?php
function familyName($fname) {
    echo("$fname Dupont.<br>");
}

familyName("Marie");
familyName("Pierre");
familyName("Paul");
familyName("Louis");
familyName("Emma");
?>
```

L'exemple suivant a une fonction avec deux arguments ($fname et $year) :

```php
<?php
function familyName($fname, $year) {
    echo("$fname Dupont. Né en $year <br>");
}

familyName("Marie", "1975");
familyName("Pierre", "1978");
familyName("Louis", "1983");
?>
```

## Arguments par référence

En PHP, les arguments sont généralement transmis par valeur, ce qui signifie qu'une copie de la valeur est utilisée dans la fonction et que la variable qui a été transmise à la fonction ne peut pas être modifiée.

Lorsqu'un argument de fonction est passé par référence, les modifications apportées à l'argument modifient également la variable qui a été transmise. Pour transformer un argument de fonction en référence, l'opérateur & est utilisé :

```php
<?php
function add_five(&$value) {
  $value += 5;
}

$num = 2;
add_five($num);
echo($num);
?>
```

## Argument par défaut 

L'exemple suivant montre comment utiliser un paramètre par défaut. Si nous appelons la fonction ```setHeight()``` sans arguments, elle prend la valeur par défaut comme argument :

```php
<?php 
declare(strict_types=1);
function setHeight(int $minheight = 50) {
  echo("The height is : $minheight <br>");
}

setHeight(350);
setHeight();
setHeight(135);
setHeight(80);
?>
```

## Typer les fonctions

Dans l'exemple ci-dessus, notez que nous n'avons pas eu à dire à PHP quel type de données est la variable.

PHP associe automatiquement un type de données à la variable, en fonction de sa valeur. Étant donné que les types de données ne sont pas définis au sens strict, vous pouvez faire des choses comme ajouter une chaîne à un entier sans provoquer d'erreur.

En PHP 7, les déclarations de type ont été ajoutées. Cela nous donne la possibilité de spécifier le type de données attendu lors de la déclaration d'une fonction, et en ajoutant la déclaration strict, cela générera une "Erreur fatale" si le type de données ne correspond pas.

Dans l'exemple suivant, nous essayons d'envoyer à la fois un nombre et une chaîne à la fonction sans utiliser ```strict``` :

exemple :

```php
<?php
function addNumbers(int $a, int $b) {
  return $a + $b;
}
echo(addNumbers(5, "5 days"));
?>
```

Pour spécifier, ```strict``` nous devons définir ```declare(strict_types=1)```. Cela doit être sur la toute première ligne du fichier PHP.

Dans l'exemple suivant, nous essayons d'envoyer à la fois un nombre et une chaîne à la fonction, mais ici nous avons ajouté la ```strict``` déclaration strict :

```php
<?php declare(strict_types=1);

function addNumbers(int $a, int $b) {
  return $a + $b;
}
echo(addNumbers(5, "5 days"));
?>
```

## Déclaration du type de retour

PHP 7 prend également en charge les déclarations de type pour l'instruction ```return```. Comme avec la déclaration de type pour les arguments de fonction, en activant l'exigence stricte, une "erreur fatale" sera générée en cas de non-concordance de type.

Pour déclarer un type pour le retour de la fonction, ajoutez deux points (:) et le type juste avant l'accolade ouvrante ( {) lors de la déclaration de la fonction.

Dans l'exemple suivant, nous spécifions le type de retour ```float``` pour la fonction :

```php
<?php declare(strict_types=1); 
function addNumbers(float $a, float $b) : float {
  return $a + $b;
}
echo(addNumbers(1.2, 5.2));
?>
```

# Contenu de ./0400 - Superglobales - $GLOBALS/content.md

La superglobale ```$GLOBALS``` est utilisée pour créer une variable qui sera accessible depuis n’importe quel script PHP. PHP par défaut dans un tableau appelé ```$GLOBALS[index]```. L’index est simplement le nom de la variable.

Exemple :

``` php
<?php
$a = 75;
$b = 25;

function somme() {
  $GLOBALS['c'] = $GLOBALS['a'] + $GLOBALS['b'];
}

somme();
echo($c);
?>
```

Dans cet exemple, ```$c``` est une variable présente dans le tableau ```$GLOBALS```, elle est donc accessible depuis l'extérieur de la fonction.

# Contenu de ./0410 - Superglobales - $_SERVER/content.md

La superglobale ```$_SERVER``` est une variable qui contient des informations sur les en-têtes, les chemins et les emplacements des fichiers.

Exemple :

``` php
<?php
echo($_SERVER['SCRIPT_NAME']);
echo($_SERVER['HTTP_USER_AGENT']);
echo($_SERVER['SERVER_NAME']);
echo($_SERVER['PHP_SELF']);
echo($_SERVER['HTTP_HOST']);
?> 
```

La liste ci-dessus répertorie les éléments pouvant être intégrés à ```$_SERVER``` :

- ```$_SERVER[‘PHP_SELF’]``` : renvoie le nom du fichier en cours d’exécution,
- ```$_SERVER[‘GATEWAY_INTERFACE’]``` : renvoie l’interface commune que le serveur utilise,
- ```$_SERVER[‘SERVER_ADDR’]``` : renvoie l’adresse IP du serveur hôte,
- ```$_SERVER[‘SERVER_NAME’]``` : renvoie le nom du serveur hôte,
- ```$_SERVER[‘SERVER_PROTOCOL’]``` : renvoie le nom et la révision du protocole d’information,
- ```$_SERVER[‘REQUEST_METHOD’]``` : renvoie la méthode de requête utilisée pour accéder à la page,
- ```$_SERVER[‘REQUEST_TIME’]``` : renvoie la date du début de la requête,
- ```$_SERVER[‘QUERY_STRING’]``` : renvoie la chaîne de requête de la page,
- ```$_SERVER[‘HTTP_ACCEPT’]``` : renvoie l’en-tête Accept de la requête en cours,
- ```$_SERVER[‘HTTP_ACCEPT_CHARSET’]``` : renvoie l’en-tête Accept_Charset de la requête actuelle,
- ```$_SERVER[‘HTTP_HOST’]``` : renvoie l’en-tête Host de la requête actuelle,
- ```$_SERVER[‘HTTP_REFERER’]``` : renvoie l’URL complète de la page actuelle,
- ```$_SERVER[‘HTTPS’]``` : renvoie un boolean (true) si le script est interrogé via un protocole HTTP sécurisé, 
- ```$_SERVER[‘REMOTE_ADDR’]``` : renvoie l’adresse IP à partir de laquelle l’utilisateur consulte la page actuelle,
- ```$_SERVER[‘REMOTE_HOST’]``` : renvoie le nom d’hôte à partir duquel l’utilisateur affiche la page actuelle,
- ```$_SERVER[‘REMOTE_PORT’]``` : renvoie le port utilisé sur la machine de l’utilisateur pour communiquer avec le serveur,
- ```$_SERVER['SCRIPT_FILENAME']``` : renvoie le chemin d'accès absolu du script en cours d’exécution,
- ```$_SERVER['SERVER_ADMIN’']``` : renvoie la valeur donnée à la directive SERVER_ADMIN dans le fichier de configuration du serveur,
- ```$_SERVER[‘SERVER_PORT’]``` : renvoie le port sur la machine serveur utilisé par le serveur pour la communication (exemple: port 80),
- ```$_SERVER[‘SERVER_SIGNATURE’]``` : renvoie la version du serveur et le nom d’hôte virtuelle qui sont ajoutés aux pages générées par le serveur,
- ```$_SERVER['PATH_TRANSLATED']``` : renvoie le chemin basé sur le système de fichiers vers le script actuel,
- ```$_SERVER[‘SCRIPT_NAME’]``` : renvoie le chemin du script actuel,
- ```$_SERVER[‘SCRIPT_URI’]``` : renvoie l’uri de la page en cours.

# Contenu de ./0420 - Superglobales - $_GET/content.md

La superglobale ```$_GET``` est une variable qui est utilisée pour récupérer des données d’un formulaire HTML soumis avec une méthode get, de plus par défaut un formulaire est en méthode get. ```$_GET``` permet aussi de récupérer des informations contenues dans l’URL.

Exemple :

``` html
<a href="get.php?theme=js&route=microlead.fr">Test méthode get</a>
```

Si l’utilisateur clique sur le lien, les paramètres ```theme``` et ```route``` sont envoyés à ```get.php```, on peut donc récupérer ces valeurs avec ```$_GET```.

``` php
<?php
echo("theme " . $_GET['theme'] . "+" . $_GET['route']);
?>
```

Ce code nous renvoie :

``` php
theme js + microlead.fr
```

# Contenu de ./0430 - Superglobales - $_POST/content.md

La superglobale ```$_POST``` est une variable qui est utilisée pour récupérer les données provenant d’un formulaire HTML qui a été soumis avec la ```method=”post”```. ```$_POST``` est également utilisé pour passer des variables.

``` php
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Prénom: <input type="text" name="name">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // récupérer les données fournies par le formulaire
  $prenom = $_POST['name'];
  if (empty($name)) {
    echo("Le champ prénom est vide");
  } else {
    echo($prenom);
  }
}
?>
```

Dans cet exemple, on y retrouve un formulaire avec un champ prénom et un bouton de soumission. Lorsqu’un utilisateur soumet le formulaire les données du formulaire sont envoyées au fichier lui-même, ceci est précisé dans l’attribut ```action``` de la balise ```<form>``` grâce à la superglobale ```$_SERVER[‘PHP_SELF’]``` qui retourne le fichier actuel. Une fois le formulaire soumis avec la ```method=”post”```, on vérifie si le champ prénom est vide. Si le champ est vide, on renvoie un message “Le champ prénom est vide” sinon, on renvoie la valeur contenue dans le champ.


# Contenu de ./0440 - Superglobales - $_FILES/content.md

La superglobale ```$_FILES``` est une variable qui est utilisée pour le téléchargement de fichier via HTTP. ```$_FILES``` est un tableau associatif des valeurs téléchargées via le protocole HTTP et à la ```method=”post”```. ```$HTTP_POST_FILES``` contient les mêmes informations, mais il ne s'agit pas d’une superglobale. PHP traite ```$_FILES``` et ```$HTTP_POST_FILES``` comme des variables différentes.

Exemple :

```php
<?php
if(isset($_FILES['image']))
{ 
     $dossier = 'upload/';
     $fichier = basename($_FILES['image']['name']);
	 //on utilise la fonction move_uploaded_file() 
     if(move_uploaded_file($_FILES['image']['tmp_name'], $dossier . $fichier))
	 //Si la fonction renvoie TRUE
     {
          echo('Upload effectué avec succès !');
     }
     else 
	 //Sinon, la fonction renvoie FALSE
     {
          echo('Echec de l\'upload !');
     }
}
?>
```

Il ne faut pas mettre ce script en ligne, car un utilisateur pourrait vouloir supprimer la base de données à la place d’effectuer un upload. Il faudra donc sécuriser le script avant de l’utiliser.

# Contenu de ./0450 - Superglobales - $_COOKIE/content.md

La superglobale ```$_COOKIE``` stocke les variables transmises au script actuel avec la requête HTTP sous la forme de cookies. ```$HTTP_COOKIE_VARS``` contient également les mêmes informations, mais n'est pas une superglobale, et est désormais obsolète.

## Qu'est-ce qu'un cookie ?

Les cookies sont des fichiers texte stockés par un serveur sur l'ordinateur du client et ils sont conservés à des fins de suivi. PHP supporte de manière transparente les cookies HTTP. Les cookies sont généralement placés dans un en-tête HTTP. JavaScript peut aussi définir un cookie directement sur un navigateur.

Le script du serveur envoie un ensemble de cookies au navigateur. Il stocke ces informations sur la machine locale pour une utilisation ultérieure. La prochaine fois que le navigateur enverra une requête au serveur web, il enverra ces informations de cookies au serveur et le serveur utilisera ces informations pour identifier l'utilisateur.

PHP contient la fonction ```setcookie``` pour créer un objet cookie qui sera envoyé au client avec la réponse HTTP.

## setcookie

### Syntaxe

```php
setcookie(nom, valeur, expiration, chemin, domaine, sécurité);
```

### Paramètres

- **Nom** : nom du cookie stocké.
- **Valeur** : définit la valeur de la variable nommée.
- **Expiration** : spécifie un temps futur en secondes depuis le 1er janvier 1970 00:00:00 GMT.
- **Chemin** : répertoires pour lesquels le cookie est valide.
- **Domaine** : spécifie le nom de domaine dans les très grands domaines.
- **Sécurité** : 1 pour HTTPS. Par défaut, 0 pour le HTTP normal.

### Exemple

```php
<?php        

//on définit un nouveau cookie prenom
setcookie('prenom','lucie', time()+3600);   
//on affiche le contenu du cookie
echo $_COOKIE['prenom'];

?>
```

### Réponse

Le navigateur affichera le résultat suivant :

```php
lucie
```

Pour supprimer le cookie, définissez le cookie avec une date qui a déjà expiré.

# Contenu de ./0460 - Superglobales - $_SESSION/content.md

La superglobale ```$_SESSION``` est un tableau associatif qui contient toutes les variables de session. ```$_SESSION``` permet de sauvegarder des données liées à une connexion utilisateur, c’est comme une petite base de données qui ne dure que le temps d’une navigation (déconnexion, fermeture d'onglet, …).

Exemple :

```php
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

// prenom est une variable de session dans $_SESSION
$_SESSION['prenom'] = 'Marc';
?>

<p>Hello <?php echo $_SESSION['prenom']; ?> !</p>
```

Dans cet exemple, on commence d’abord par lancer la session grâce à la fonction ```session_start()```, ensuite on définit une variable de session “prenom“. Maintenant le paragraphe renvoie “Hello Marc !”.

# Contenu de ./0470 - Superglobales - $_REQUEST/content.md

La superglobale ```$_REQUEST``` est une variable qui est utilisée pour récupérer les données provenant d’un formulaire HTML qui a été soumis.

Exemple :

```php
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Prenom: <input type="text" name="name">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // récupérer les données fournis par le formulaire
  $prenom = $_REQUEST['name'];
  if (empty($name)) {
    echo("Le champ prénom est vide");
  } else {
    echo($prenom);
  }
}
?>
```

Dans cet exemple, on y retrouve un formulaire avec un champ prénom et un bouton de soumission. Lorsqu’un utilisateur soumet le formulaire les données du formulaire sont envoyées au fichier lui-même, ceci est précisé dans l’attribut ```action``` de la balise ```<form>``` grâce à la superglobale ```$_SERVER[‘PHP_SELF’]``` qui retourne le fichier actuel. Une fois le formulaire soumis, on vérifie si le champ prénom est vide. Si le champ est vide, on renvoie un message “Le champ prénom est vide” sinon, on renvoie la valeur contenue dans le champ.

# Contenu de ./0480 - Superglobales - $_ENV/content.md

```$_ENV``` est une autre superglobale en PHP. Elle stocke les variables d'environnement disponibles pour le script courant. ```$HTTP_ENV_VARS``` contient également les mêmes informations, mais ce n'est pas une superglobale, et elle est maintenant obsolète.

Les variables d'environnement sont importées dans l'espace de noms global. La plupart de ces variables sont fournies par le shell sous lequel le parseur PHP est exécuté. Par conséquent, la liste des variables d'environnement peut être différente sur différentes plateformes.

Ce tableau inclut par ailleurs les variables CGI dans le cas où PHP est exécuté en tant que module serveur ou processeur CGI.

## getenv

La bibliothèque PHP possède la fonction ```getenv()``` pour récupérer la liste de toutes les variables d'environnement ou la valeur d'une variable d'environnement spécifique.

Le script suivant affiche les valeurs de toutes les variables d'environnement disponibles :

``` php
<?php
$arr=getenv();
foreach ($arr as $key=>$val) {
    echo("$key=>$val");
}
?>
```

Pour obtenir la valeur d'une variable spécifique, utilisez son nom comme argument pour la fonction ```getenv()```.

### Exemple

``` php
<?php
echo("Chemin : " . getenv("PATH"));
?>
```

### Réponse

``` php
Chemin : /usr/bin:/bin
```

## putenv

PHP dispose également de la fonction ```putenv()``` pour créer une nouvelle variable d'environnement. La variable d'environnement n'existera que pour la durée de la requête en cours.

La modification de la valeur de certaines variables d'environnement doit être évitée. Par défaut, les utilisateurs ne pourront définir que les variables d'environnement qui commencent par ```PHP_``` (par exemple, ```PHP_FOO=BAR```).

La directive ```safe_mode_protected_env_vars``` du php.ini contient une liste de variables d'environnement délimitées par des virgules, que l'utilisateur final ne pourra pas modifier en utilisant putenv().

### Exemple

``` php
<?php
putenv("PHP_TEMPUSER=INVITE");
echo("Utilisateur temporaire : " . getenv("PHP_TEMPUSER"));
?>
```

### Réponse

Le navigateur affichera le résultat suivant :

``` php
Utilisateur temporaire : INVITE
```

# Contenu de ./0490 - PSR 06 - Caching Interface/content.md

La mise en cache est un moyen courant d'améliorer les performances de tout projet, ce qui fait des bibliothèques d'implémentation l'une des caractéristiques les plus courantes de nombreux frameworks et bibliothèques. Cela a conduit à une situation où de nombreuses bibliothèques utilisent leurs propres bibliothèques d'implémentation, avec différents niveaux de fonctionnalité. Ces différences obligent les développeurs à apprendre à utiliser plusieurs systèmes qui peuvent ou non fournir les fonctionnalités dont ils ont besoin. En outre, les développeurs de bibliothèques d'implémentation sont eux-mêmes confrontés à un choix entre la prise en charge d'un nombre limité de frameworks ou la création d'un grand nombre de classes d'adaptateurs.

Une interface commune pour les systèmes de mise en cache résoudra ces problèmes. Les développeurs de bibliothèques et de frameworks peuvent compter sur le fait que les systèmes de mise en cache fonctionnent comme ils l'espèrent, tandis que les développeurs de systèmes de mise en cache n'auront à mettre en œuvre qu'un seul ensemble d'interfaces plutôt qu'un assortiment complet d'adaptateurs.

## Objectif

L'objectif de ce PSR est de permettre aux développeurs de créer des bibliothèques compatibles avec le cache qui peuvent être intégrées dans des cadres et des systèmes existants sans qu'il soit nécessaire de procéder à un développement personnalisé.

## Définitions

- **Bibliothèque d'appel** - La bibliothèque ou le code qui a réellement besoin des services de cache. Cette bibliothèque utilisera les services de cache qui implémentent les interfaces de cette norme, mais n'aura autrement aucune connaissance de l'implémentation de ces services de cache.
- **Bibliothèque d'implémentation** - Cette bibliothèque est responsable de l'implémentation de cette norme afin de fournir des services de mise en cache à toute bibliothèque d'appel. La bibliothèque d'implémentation doit fournir des classes qui implémentent les interfaces Cache\CacheItemPoolInterface et Cache\CacheItemInterface. Les bibliothèques d'implémentation doivent au minimum prendre en charge la fonctionnalité TTL décrite ci-dessous avec une précision de granularité de l'ordre de la seconde.
- **TTL (The Time To Live)** - Le temps de vie d'un objet est le temps qui s'écoule entre le moment où cet objet est stocké et celui où il est considéré comme périmé. Le TTL est normalement défini par un entier représentant le temps en secondes, ou un objet DateInterval.
- **Expiration** - Le moment réel où un article est prêt à être périmé. Elle est généralement calculée en ajoutant le TTL à l'heure à laquelle un objet est stocké, mais peut également être explicitement définie avec l'objet DateTime. Un objet avec un TTL de 300 secondes stocké à 1:30:00 aura une expiration à 1:35:00. Les bibliothèques d'application peuvent faire expirer un article avant l'heure d'expiration demandée, mais doivent traiter un article comme expiré une fois que l'heure d'expiration est atteinte. Si une bibliothèque appelante demande qu'un document soit enregistré mais ne spécifie pas d'heure d'expiration, ou spécifie une heure d'expiration nulle ou TTL, une bibliothèque d'implémentation peut utiliser une durée par défaut configurée. Si aucune durée par défaut n'a été définie, la bibliothèque d'implémentation doit l'interpréter comme une demande de mise en cache de l'élément pour toujours, ou aussi longtemps que l'implémentation sous-jacente le permet.
- **Clé** - Une chaîne d'au moins un caractère qui identifie de manière unique un élément mis en cache. Les bibliothèques d'implémentation doivent prendre en charge les clés composées des caractères A-Z, a-z, 0-9, _, et . dans n'importe quel ordre en codage UTF-8 et d'une longueur maximale de 64 caractères. Les bibliothèques d'implémentation peuvent prendre en charge des caractères et des codages supplémentaires ou des longueurs plus importantes, mais doivent au moins prendre en charge ce minimum. Les bibliothèques sont responsables de leur propre échappement des chaînes de caractères clés selon le cas, mais doivent être en mesure de renvoyer la chaîne de caractères originale non modifiée. Les caractères suivants sont réservés aux extensions futures et ne doivent pas être pris en charge par les bibliothèques d'implémentation : {}()/\@:
- **Succès** - Un succès de cache se produit lorsqu'une bibliothèque appelante demande un article par clé et qu'une valeur correspondante est trouvée pour cette clé, et que cette valeur n'a pas expiré, et que la valeur n'est pas invalide pour une autre raison. Les bibliothèques appelantes doivent s'assurer de vérifier isHit() sur tous les appels à get().
- **Échec** - Un échec de cache est l'opposé d'un succès de cache. Un échec de cache se produit lorsqu'une bibliothèque appelante demande un élément par clé et que cette valeur n'a pas été trouvée pour cette clé, ou que la valeur a été trouvée, mais a expiré, ou que la valeur est invalide pour une autre raison. Une valeur expirée doit toujours être considérée comme un échec de cache.
- **Différé** - Une sauvegarde différée du cache indique qu'un élément du cache ne peut pas être persisté immédiatement par le groupe. Un objet du groupe peut retarder la persistance d'un élément de cache différé afin de tirer parti des opérations de groupage prises en charge par certains moteurs de stockage. Un groupe doit s'assurer que tout élément de cache différé est finalement persisté et que les données ne sont pas perdues, et peut les persister avant qu'une bibliothèque appelante ne demande qu'ils soient maintenus. Lorsqu'une bibliothèque appelante invoque la méthode commit(), tous les éléments différés en suspens doivent être maintenus. Une bibliothèque d'implémentation peut utiliser n'importe quelle logique appropriée pour déterminer quand persister les éléments différés, comme un destructeur d'objets, la persistance de tous les éléments lors de la sauvegarde, une vérification du délai d'attente ou du nombre maximum d'éléments ou toute autre logique appropriée. Les demandes pour un élément de cache qui a été reporté doivent obligatoirement renvoyer l'élément reporté, mais pas encore conservé.

## Données

Les bibliothèques implémentées doivent prendre en charge tous les types de données PHP sérialisables, y compris :

- **Chaînes** - Chaînes de caractères de taille arbitraire dans tout encodage compatible avec PHP.
- **Entiers** - Tous les entiers de toute taille pris en charge par PHP, jusqu'à 64 bits.
- **Nombre décimal** - Toutes les valeurs en nombre décimal.
- **Booléen** - Vrai et faux.
- **Null** - La valeur nulle.
- **Tableaux** - Tableaux indexés, associatifs et multidimensionnels de longueur arbitraire.
- **Objet** - Tout objet qui supporte la sérialisation et la désérialisation sans perte de manière que ```$o == unserialize(serialize($o))```. Les objets peuvent utiliser l'interface sérialisable de PHP, les méthodes magiques ```__sleep()``` ou ```__wakeup()```, ou des fonctionnalités similaires du langage si nécessaire.

Toutes les données transmises à la bibliothèque d'implémentation doivent être renvoyées exactement comme elles ont été transmises. Cela inclut le type de variable. C'est-à-dire que c'est une erreur de renvoyer (string) 5 si (int) 5 était la valeur sauvegardée. Les bibliothèques d'implémentation peuvent utiliser les fonctions ```serialize()``` et ```unserialize()``` de PHP en interne mais ne sont pas obligées de le faire. La compatibilité avec ces fonctions est simplement utilisée comme référence pour les valeurs d'objets acceptables.

S'il n'est pas possible de renvoyer la valeur exacte enregistrée pour une raison quelconque, les bibliothèques d'implémentation doivent répondre par un échec de cache plutôt que par des données corrompues.

## Concepts clés

### Groupe

Le Groupe représente une collection d'objets dans un système de mise en cache. Le groupe est un dépôt logique de tous les éléments qu'il contient. Tous les objets pouvant être mis en cache sont récupérés dans le groupe en tant qu'objet Item et toute interaction avec l'univers entier des objets mis en cache se fait par le biais du groupe.

### Éléments

Un élément représente une seule paire clé/valeur au sein d'un groupe. La clé est le principal identifiant unique d'un élément et doit être immuable. La valeur peut être modifiée à tout moment.

## Traitement des erreurs

Bien que la mise en cache soit souvent un élément important des performances des applications, elle ne devrait jamais être un élément critique de la fonctionnalité des applications. Ainsi, une erreur dans un système de cache ne doit pas entraîner l'échec d'une application. Pour cette raison, les bibliothèques de mise en œuvre ne doivent pas lancer d'exceptions autres que celles définies par l'interface, et doivent piéger toute erreur ou exception déclenchée par un magasin de données sous-jacent et ne pas leur permettre de faire des bulles.

Une bibliothèque d'implémentation devrait enregistrer ces erreurs ou les signaler à un administrateur, le cas échéant.

Si une bibliothèque appelante demande qu'un ou plusieurs éléments soient supprimés, ou qu'un groupe soit effacé, cela ne doit pas être considéré comme une condition d'erreur si la clé spécifiée n'existe pas. La postcondition est la même (la clé n'existe pas ou le groupe est vide), il n'y a donc pas de condition d'erreur.

## Interfaces

### CacheItemInterface

CacheItemInterface définit un élément à l'intérieur d'un système de cache. Chaque objet Item doit être associé à une clé spécifique, qui peut être définie en fonction du système d'implémentation et est généralement transmise par l'objet ```Cache\CacheItemPoolInterface```.

L'objet ```Cache\CacheItemInterface``` encapsule le stockage et la récupération des éléments du cache. Chaque ```Cache\CacheItemInterface``` est généré par un objet ```Cache\CacheItemPoolInterface```, qui est responsable de toute configuration requise ainsi que de l'association de l'objet à une clé unique. Les objets ```Cache\CacheItemInterface``` doivent être capables de stocker et de récupérer tout type de valeur PHP définie dans la section Données du présent document.

Les bibliothèques appelantes ne doivent pas instancier les objets Item eux-mêmes. Ils ne peuvent être demandés à un objet Pool que par la méthode ```getItem()```. Les bibliothèques appelantes ne doivent pas supposer qu'un élément créé par une bibliothèque d'implémentation est compatible avec un groupe d'une autre bibliothèque d'implémentation.

```php
<?php

namespace Psr\Cache;

/**
 * CacheItemInterface définit une interface permettant d'interagir avec des objets à l'intérieur d'un cache.
 */
interface CacheItemInterface
{
    /**
     * Renvoie la clé de l'élément de cache actuel.
     *
     * La clé est chargée par la bibliothèque d'implémentation, mais doit être disponible pour les appelants de niveau supérieur en cas de besoin.
     *
     * @return string
     *   La chaîne de la clé pour cet élément de la cache.
     */
    public function getKey();

    /**
     * Récupère la valeur de l'objet dans le cache associé à la clé de cet objet.
     *
     * La valeur retournée doit être identique à la valeur stockée à l'origine par set().
     *
     * Si isHit() renvoie false, cette méthode doit obligatoirement renvoyer null. Notez que null est une valeur légitime mise en cache, donc la méthode isHit() devrait être utilisée pour différencier la valeur "null a été trouvée" et "aucune valeur n'a été trouvée".
     *
     * @return mixed
     *   La valeur correspondant à la clé de cet élément de cache ou nulle si elle n'est pas trouvée.
     */
    public function get();

    /**
     * Confirme si la recherche d'éléments dans la mémoire cache a abouti à un résultat dans la mémoire cache.
     *
     * Note : Cette méthode ne doit pas avoir de condition préalable entre l'appel de isHit() et l'appel de get().
     *
     * @return bool
     *   Vrai si la demande a abouti à un résultat de cache. Faux dans le cas contraire.
     */
    public function isHit();

    /**
     * Définit la valeur représentée par cet élément de cache.
     *
     * L'argument $value peut être n'importe quel élément qui peut être sérialisé par PHP, bien que la méthode de sérialisation soit laissée à la bibliothèque d'implémentation.
     *
     * @param mixed $value
     *   La valeur sérialisable à stocker.
     *
     * @return static
     *   L'objet invoqué.
     */
    public function set($value);

    /**
     * Définit le délai d'expiration de cet élément.
     *
     * @param \DateTimeInterface|null $expiration
     *   Le moment après lequel le point doit être considéré comme expiré. Si la valeur null est passée explicitement, une valeur par défaut peut être utilisée. Si aucune valeur n'est définie, la valeur doit être stockée de manière permanente ou aussi longtemps que l'implémentation le permet.
     *
     * @return static
     *   L'objet appelé.
     */
    public function expiresAt($expiration);

    /**
     * Définit le délai d'expiration de cet élément.
     *
     * @param int|\DateInterval|null $time
     *   La période de temps à partir du présent après laquelle le point doit être considéré comme expiré. Un paramètre entier est compris comme étant le temps en secondes jusqu'à l'expiration. Si la valeur null est passée explicitement, une valeur par défaut peut être utilisée. Si aucune valeur n'est définie, la valeur doit être stockée de manière permanente ou aussi longtemps que l'implémentation le permet.
     *
     * @return static
     *   L'objet appelé.
     */
    public function expiresAfter($time);

}
```

### CacheItemPoolInterface

L'objectif principal de ```Cache\CacheItemPoolInterface``` est d'accepter une clé de la bibliothèque appelante et de renvoyer l'objet ```Cache\CacheItemInterface``` associé. C'est également le principal point d'interaction avec l'ensemble de la collection de caches. Toute la configuration et l'initialisation du groupe est laissée à une bibliothèque d'implémentation.

```php
<?php

namespace Psr\Cache;

/**
 * CacheItemPoolInterface génère des objets CacheItemInterface.
 */
interface CacheItemPoolInterface
{
    /**
     * Retourne un élément de cache représentant la clé spécifiée.
     *
     * Cette méthode doit toujours renvoyer un objet CacheItemInterface, même en cas d'absence de cache. Elle ne doit pas renvoyer un objet null.
     *
     * @param string $key
     *   La clé permettant de retourner l'élément de cache correspondant.
     *
     * @throws InvalidArgumentException
     *   Si la chaîne de caractères $key n'est pas une valeur légale, une \Psr\Cache\InvalidArgumentException doit être envoyée.
     *
     * @return CacheItemInterface
     *   L'élément de cache correspondant.
     */
    public function getItem($key);

    /**
     * Renvoie un ensemble d'éléments de la mémoire cache qui peut être parcouru.
     *
     * @param string[] $keys
     *   Un tableau indexé de clés des éléments à retrouver.
     *
     * @throws InvalidArgumentException
     *   Si l'une des clés en $keys n'a pas de valeur légale, une \Psr\Cache\InvalidArgumentException doit être envoyée.
     *
     * @return array|\Traversable
     *   Une collection d'élément de cache traversable dont les clés de cache de chaque élément sont saisies. Un élément du cache sera retourné pour chaque clé, même si cette clé n'est pas trouvée. Toutefois, si aucune clé n'est spécifiée, un élément de cache vide doit être renvoyé à la place.
     */
    public function getItems(array $keys = array());

    /**
     * Confirme si le cache contient l'élément de cache spécifié.
     *
     * Note : Cette méthode peut éviter de récupérer la valeur mise en cache pour des raisons de performance.
     * Cela pourrait entraîner une situation de concurrence avec CacheItemInterface::get(). Pour éviter une telle situation, utilisez plutôt CacheItemInterface::isHit().
     *
     * @param string $key
     *   La clé qui permet de vérifier l'existence.
     *
     * @throws InvalidArgumentException
     *   Si la chaîne de caractères $key n'est pas une valeur légale, une \Psr\Cache\InvalidArgumentException doit être envoyée.
     *
     * @return bool
     *   Vrai si l'objet existe dans le cache, faux dans le cas contraire.
     */
    public function hasItem($key);

    /**
     * Supprime tous les éléments du groupe.
     *
     * @return bool
     *   C'est vrai si le groupe a été nettoyé avec succès. Faux s'il y a eu une erreur.
     */
    public function clear();

    /**
     * Retire l'élément du groupe.
     *
     * @param string $key
     *   La clé à effacer.
     *
     * @throws InvalidArgumentException
     *   Si la chaîne de caractères $key n'est pas une valeur légale, une \Psr\Cache\InvalidArgumentException doit être envoyée.
     *
     * @return bool
     *   Vrai si l'objet a été retiré avec succès. Faux s'il y a eu une erreur.
     */
    public function deleteItem($key);

    /**
     * Retire plusieurs éléments du groupe.
     *
     * @param string[] $keys
     *   Un ensemble de clés qui doivent être retirées du groupe.
     *
     * @throws InvalidArgumentException
     *   Si l'une des clés en $keys n'a pas de valeur légale, une \Psr\Cache\InvalidArgumentException doit être envoyée.
     *
     * @return bool
     *   Vrai si les objets ont été retirés avec succès. Faux s'il y a eu une erreur.
     */
    public function deleteItems(array $keys);

    /**
     * Conserve immédiatement un élément de la cache.
     *
     * @param CacheItemInterface $item
     *   L'élément de cache à sauvegarder.
     *
     * @return bool
     *   Vrai si l'objet a été conservé avec succès. Faux s'il y a eu une erreur.
     */
    public function save(CacheItemInterface $item);

    /**
     * Définit un élément de cache qui sera conservé plus tard.
     *
     * @param CacheItemInterface $item
     *   L'élément de cache à sauvegarder.
     *
     * @return bool
     *   Faux si l'élément ne peut pas être mis en file d'attente ou si un engagement a été tenté et a échoué. Vrai dans le cas contraire.
     */
    public function saveDeferred(CacheItemInterface $item);

    /**
     * Conserve tous les éléments de cache reportés.
     *
     * @return bool
     *   Vrai si tous les objets qui n'ont pas encore été conservés ont été sauvegardés avec succès ou s'il n'y en a pas eu. Faux dans le cas contraire.
     */
    public function commit();
}
```

### CacheException

Cette interface d'exception est destinée à être utilisée lorsque des erreurs critiques se produisent, mais sans s'y limiter la configuration du cache comme la connexion à un serveur de cache ou des informations d'identification non valides fournies.

Toute exception lancée par une bibliothèque d'implémentation doit implémenter cette interface.

```php
<?php

namespace Psr\Cache;

/**
 * Interface d'exception pour toutes les exceptions lancées par une bibliothèque d'implémentation.
 */
interface CacheException
{
}
```

### InvalidArgumentException

```php
<?php

namespace Psr\Cache;

/**
 * Interface d'exception pour les arguments de cache non valables.
 *
 * Chaque fois qu'un argument non valide est passé dans une méthode, il doit lancer une classe d'exception qui implémente Psr\Cache\InvalidArgumentException.
 */
interface InvalidArgumentException extends CacheException
{
}
```

# Contenu de ./0500 - PSR 13 - Hypermedia Links/content.md

Les liens hypermédias deviennent une partie de plus en plus importante du Web, à la fois dans les contextes HTML et dans divers contextes de format API. Cependant, il n'y a pas de format hypermédia commun unique, ni de manière commune de représenter les liens entre les formats.

Cette spécification vise à fournir aux développeurs PHP une manière simple et courante de représenter un lien hypermédia indépendamment du format de sérialisation utilisé. Cela permet à son tour à un système de sérialiser une réponse avec des liens hypermédias dans un ou plusieurs formats de fil indépendamment du processus de décision de ces liens.

## Les liens de base

Un Lien Hypermédia se compose, au minimum :

- Un URI représentant la ressource cible référencée.
- Une relation définissant la relation entre la ressource cible et la source. Divers autres attributs du lien peuvent exister, selon le format utilisé. Comme les attributs supplémentaires ne sont pas bien standardisés ou universels, cette spécification ne cherche pas à les standardiser. Aux fins de la présente spécification, les définitions suivantes s'appliquent.
- Objet d'implémentation - Un objet qui implémente l'une des interfaces définies par cette spécification.
- Sérialiseur - Une bibliothèque ou un autre système qui prend un ou plusieurs objets Link et en produit une représentation sérialisée dans un format défini.

## Les attributs

Tous les liens peuvent inclure zéro ou plusieurs attributs supplémentaires au-delà de l'URI et de la relation. Il n'y a pas de registre formel des valeurs autorisées ici, et la validité des valeurs dépend du contexte et souvent d'un format de sérialisation particulier. Les valeurs couramment prises en charge incluent 'hreflang', 'title' et 'type'. Les sérialiseurs peuvent omettre des attributs sur un objet lien si cela est requis par le format de sérialisation. Cependant, les sérialiseurs devraient coder tous les attributs fournis possibles afin de permettre l'extension d'utilisateur à moins que cela ne soit empêché par la définition d'un format de sérialisation. Certains attributs (généralement “hreflang”) peuvent apparaître plusieurs fois dans leur contexte. Par conséquent, une valeur d'attribut PEUT être un tableau de valeurs plutôt qu'une simple valeur. Les sérialiseurs peuvent coder ce tableau dans le format approprié au format sérialisé (comme une liste séparée par des espaces, une liste séparée par des virgules, etc.). Si un attribut donné n'est pas autorisé à avoir plusieurs valeurs dans un contexte particulier, les sérialiseurs doivent utiliser la première valeur fournie et ignorer toutes les valeurs suivantes. Si une valeur d'attribut est boolean “true”, les sérialiseurs peuvent utiliser des formes abrégées si cela est approprié et pris en charge par un format de sérialisation. Par exemple, HTML permet aux attributs de n'avoir aucune valeur lorsque la présence de l'attribut a une signification booléenne. Cette règle s'applique si et seulement si l'attribut est boolean “true”, pas pour toute autre valeur "véridique" en PHP telle que l'entier 1. Si une valeur d'attribut est boolean “false”, les sérialiseurs devraient omettre entièrement l'attribut à moins que cela ne change la signification sémantique du résultat. Cette règle s'applique si et seulement si l'attribut est boolean “false”, pas pour toute autre valeur "false" en PHP telle que l'entier 0.

## Les relations

Les relations de lien sont définies sous forme de chaînes et sont soit un simple mot-clé dans le cas d'une relation définie publiquement, soit un URI absolu dans le cas d'une relation privée. Dans le cas où un mot clé simple est utilisé, il devrait correspondre à celui du registre IANA. Facultativement, le registre microformats.org peut être utilisé, mais cela peut ne pas être valide dans tous les contextes. Une relation qui n'est pas définie dans l'un des registres ci-dessus ou dans un registre public similaire est considérée comme « privée », c'est-à-dire spécifique à une application ou à un cas d'utilisation particulier. De telles relations doivent utiliser un URI absolu.

## Les modèles de liens

La RFC 6570 définit un format pour les modèles d'URI, autrement dit un modèle pour un URI qui doit être rempli avec les valeurs fournies par un outil client. Certains formats hypermédias prennent en charge les liens modélisés tandis que d'autres ne le font pas, et peuvent avoir une manière spéciale d'indiquer qu'un lien est un modèle. Un sérialiseur pour un format qui ne prend pas en charge les modèles d'URI doit ignorer tous les liens modélisés qu'il rencontre.

## Les fournisseurs évolutifs

Dans certains cas, un fournisseur de liens peut avoir besoin de pouvoir ajouter des liens supplémentaires. Dans d'autres, un fournisseur de liens est nécessairement en lecture seule, avec des liens dérivés au moment de l'exécution d'une autre source de données. Pour cette raison, les fournisseurs modifiables sont une interface secondaire qui peut éventuellement être implémentée.

En outre, certains objets Fournisseur de liaison, tels que les objets Réponse PSR-7, sont par conception immuables. Cela signifie que les méthodes pour y ajouter des liens sur place seraient incompatibles. Par conséquent, la “EvolvableLinkProviderInterface” méthode unique de ' nécessite qu'un nouvel objet soit renvoyé, identique à l'original, mais avec un objet Link supplémentaire inclus.

## Les objets de liaison évolutifs

Les objets de lien sont dans la plupart des cas des objets de valeur. En tant que tel, leur permettre d'évoluer de la même manière que les objets de valeur PSR-7 est une option utile. Pour cette raison, une “EvolvableLinkInterface” supplémentaire est incluse qui fournit des méthodes pour produire de nouvelles instances d'objet avec un seul changement. Le même modèle est utilisé par PSR-7 et, grâce au comportement de copie sur écriture de PHP, il est toujours efficace en termes de CPU et de mémoire.

Cependant, il n'existe pas de méthode évolutive pour les valeurs modélisées, car la valeur modélisée d'un lien est basée exclusivement sur la valeur href. Il ne doit pas  être défini indépendamment, mais dérivé du fait que la valeur href est ou non un modèle de lien RFC 6570.

## Les interfaces

“LinkInterface” :

```php
<?php

namespace Psr\Link;

interface LinkInterface
{
    /**
     * @return string
     */
    public function getHref();

    /**
     * @return bool
     */
    public function isTemplated();

    /**
     * @return string[]
     */
    public function getRels();

    /**
     * @return array
     */
    public function getAttributes();
}
```

“EvolvableLinkInterface” :

```php
<?php

namespace Psr\Link;

interface EvolvableLinkInterface extends LinkInterface
{
    /**
     * @param string $href
     * @return static
     */
    public function withHref($href);

    /**
     * @param string $rel
     * @return static
     */
    public function withRel($rel);

    /**
     * @param string $rel
     * @return static
     */
    public function withoutRel($rel);

    /**
     * @param string $attribute
     * @param string $value
     * @return static
     */
    public function withAttribute($attribute, $value);

    /**
     * @param string $attribute
     * @return static
     */
    public function withoutAttribute($attribute);
}
```

“LinkProviderInterface” :

```php
<?php

namespace Psr\Link;

interface LinkProviderInterface
{
    /**
     * @return LinkInterface[]|\Traversable
     */
    public function getLinks();

    /**
     * @return LinkInterface[]|\Traversable
     */
    public function getLinksByRel($rel);
}
```

“EvolvableLinkProviderInterface” :

```php
<?php

namespace Psr\Link;

interface EvolvableLinkProviderInterface extends LinkProviderInterface
{
    /**
     * @param LinkInterface $link
     * @return static
     */
    public function withLink(LinkInterface $link);

    /**
     * @param LinkInterface $link
     * @return static
     */
    public function withoutLink(LinkInterface $link);
}
```

# Contenu de ./0510 - Les classes/content.md

Une classe est un modèle pour les objets et un objet est une instance de classe.

## Cas de POO

Supposons que nous ayons une classe nommée Fruit. Un fruit peut avoir des propriétés telles que le nom, la couleur, le poids, etc. Nous pouvons définir des variables telles que ```$name```, ```$color``` et ```$weight``` pour contenir les valeurs de ces propriétés.

Lorsque les objets individuels (pomme, banane, etc.) sont créés, ils héritent de toutes les propriétés et comportements de la classe, mais chaque objet aura des valeurs différentes pour les propriétés.

## Définir une classe

Une classe est définie en utilisant le mot-clé ```class```, suivi du nom de la classe et d'une paire d'accolades (```{}```). Toutes ses propriétés et méthodes vont à l'intérieur des accolades.

syntaxe :

```php
<?php
class Fruit {
  // code 
}
?>
```

Ci-dessous, nous déclarons une classe nommée "Fruit" composée de deux propriétés (```$name``` et ```$color```) et de deux méthodes ```set_name()``` et ```get_name()``` pour définir et obtenir la propriété ```$name``` :

```php
<?php
class Fruit {
  // Propriétés
  public $name;
  public $color;

  // Méthodes
  function set_name($name) {
    $this->name = $name;
  }
  function get_name() {
    return $this->name;
  }
}
?>
```

## Définir des objets

Nous pouvons créer plusieurs objets à partir d'une classe. Chaque objet possède toutes les propriétés et méthodes définies dans la classe, mais elles auront des valeurs de propriété différentes.

Les objets d'une classe sont créés à l'aide du mot-clé ```new```.

Dans l'exemple ci-dessous, ```$apple``` et ```$banana``` sont des instances de la classe ```Fruit``` :

```php
<?php
class Fruit {
  // Properties
  public $name;
  public $color;

  // Methods
  function set_name($name) {
    $this->name = $name;
  }
  function get_name() {
    return $this->name;
  }
}

$apple = new Fruit();
$banana = new Fruit();
$apple->set_name('Apple');
$banana->set_name('Banana');

echo($apple->get_name());
echo("<br>");
echo($banana->get_name());
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
Apple
Banana
```

## Le mot clé this

Le mot-clé ```$this``` fait référence à l'objet courant et n'est disponible qu'à l'intérieur des méthodes.

exemple :

```php
<?php
class Fruit {
  public $name;
}
$apple = new Fruit();
?>
```

Alors, où pouvons-nous changer la valeur de la propriété” $name” ? Il y a deux manières :

1 - Dans la classe (en ajoutant une méthode ```set_name()``` et en utilisant ```$this```) :

```php
<?php
class Fruit {
  public $name;
  function set_name($name) {
	$this->name = $name;
  }
}
$apple = new Fruit();
$apple->set_name("Apple");

echo($apple->name);
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
Apple
```

2 - En dehors de la classe (en modifiant directement la valeur de la propriété) :

```php
<?php
class Fruit {
  public $name;
}
$apple = new Fruit();
$apple->name = "Apple";

echo($apple->name);
?>
```

Dans cet exemple, le résultat renvoyé est :

```
Apple
```

## Instance of

Vous pouvez utiliser le mot-clé ```instanceof``` pour vérifier si un objet appartient à une classe spécifique :

```php
<?php
$apple = new Fruit();
var_dump($apple instanceof Fruit);
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
bool(true);
```

# Contenu de ./0520 - Les opérateurs de types/content.md

Les opérateurs de types sont utilisés pour déterminer si une variable est un objet instancié d’une certaine classe. Pour réaliser cela on utilise ```instanceof```.

Exemple 1. instanceof avec des classes :

```php
<?php
class MaClasse
{
}
class CeciNestPasMaClasse
{
}
$a = new MaClasse;

var_dump($a instanceof MaClasse);
var_dump($a instanceof CeciNestPassMaClasse);
?>
```

Dans cet exemple, le premier ```var_dump()``` renvoi vrai (true) alors que le second ```var_dump()``` renvoi faux (false).

Exemple 2. instanceof avec des classes héritées :

```php
<?php
class ClassParent
{
}
class MaClass extends ParentClass
{
}
$a = new MaClass;

var_dump($a instanceof MaClass);
var_dump($a instanceof ClassParent);
?>
```

Dans cet exemple, le premier ```var_dump()``` renvoi vrai (true) et le second ```var_dump()``` renvoi vrai (true) aussi.

Exemple 3. instanceof pour vérifier que l’objet n’est pas une instance de la classe :

```php
<?php
class MaClass
{
}
$a = new MaClass;
var_dump(!($a instanceof stdClass));
?>
```

Dans cet exemple, le ```var_dump()``` renvoi vrai (true).

Exemple 4. instanceof pour une interface :

```php
<?php
interface MonInterface
{
}
class MaClass implements MonInterface
{
}
$a = new MaClass;

var_dump($a instanceof MaClass);
var_dump($a instanceof MonInterface);
?>
```

Dans cet exemple, les deux ```var_dump()``` renvoient vrai (true).

Exemple 5 : instanceof pour d’autres types :

```php
<?php
$a = 1;
$b = NULL;
var_dump($a instanceof stdClass);
var_dump($b instanceof stdClass);
var_dump(FALSE instanceof stdClass);
?>
```

L’exemple du dessus donne le résultat suivant :

```php
bool(false)
bool(false)
bool(false)
PHP Fatal error:  instanceof expects an object instance, constant given
```

# Contenu de ./0530 - Encapsulation/content.md

Avant de comprendre le concept d'**encapsulation**, il est important de comprendre le concept de **spécificateur d'accès**. Les spécificateurs d'accès définissent le type d'accès des membres (propriétés et méthodes) de la classe et il existe trois types de spécificateurs d'accès en PHP.

- ```public``` : les membres de la classe sont accessibles de partout. C'est aussi le spécificateur d'accès par défaut.
- ```protected``` : les membres de la classe sont accessibles à l'intérieur de la classe et par les classes dérivées.
- ```private``` : les membres de la classe ne sont accessibles QUE dans la classe.

## Exemple

Dans l'exemple ci-dessous, une classe appelée *person* est créée et possède une propriété privée appelée name. Lorsqu'on accède à cette propriété dans le programme, une exception est levée car il s'agit d'une propriété privée à laquelle on ne peut accéder en dehors de la classe dans laquelle elle est définie.

```php
<?php
class person {
  private $name = "John";
};

$p1 = new person();
echo($p1->name);
?>
```

La réponse du code ci-dessus sera :

```php
PHP Fatal error:  Uncaught Error: Cannot access private property person::$name
```

## Encapsulation

L'**encapsulation** est un processus consistant à lier les propriétés et les méthodes dans une seule unité appelée classe. Elle a pour but d'empêcher l'accès direct aux propriétés et n'est disponible que par le biais des méthodes de la classe. L'encapsulation des données a conduit à l'important concept de dissimulation des données dans la programmation orientée objet, également connu sous le nom d'**abstraction des données**. L'abstraction de données est un mécanisme qui permet de n'exposer que les interfaces et de cacher les détails de la mise en œuvre à l'utilisateur.

Étapes de l'encapsulation des données :

- Déclarez chaque propriété privée.
- Créez une méthode publique set pour chaque propriété afin de définir les valeurs des propriétés.
- Créez une méthode publique get pour chaque propriété afin de récupérer les valeurs des propriétés.

Dans l'exemple ci-dessous, des méthodes publiques set et get sont créées pour accéder aux propriétés privées nom et âge de la classe *person*.

```php
<?php
class person {
  private $Name;
  private $Age;
  // méthode pour définir la valeur du nom
  public function setName($name) {
    $this->Name = $name;
  }
  // méthode pour récupérer la valeur du nom
  public function getName() {
    return $this->Name;
  }
  // méthode pour définir la valeur de âge
  public function setAge($age) {
    $this->Age = $age;
  }
  // méthode pour récupérer la valeur de âge
  public function getAge() {
    return $this->Age;
  }
};

$p1 = new person();

// définir le nom et l'âge
$p1->setName("Patrick");
$p1->setAge(64);
// obtenir le nom et l'âge
echo($p1->getName()." a ".$p1->getAge()." ans.");
?>
```

La réponse du code ci-dessus sera :

```php
Patrick a 64 ans.
```

# Contenu de ./0540 - Opérateurs de résolution de portée/content.md

L'opérateur de résolution de portée (aussi appelé Paamayim Nekudotayim) ou, en termes plus simples, le symbole "double deux-points" (::), fournit un moyen d'accéder aux membres static ou constant, ainsi qu'aux propriétés ou méthodes surchargées d'une classe.

Lorsque vous référencez ces éléments en dehors de la définition de la classe, utilisez le nom de la classe.

Depuis PHP 5.3.0, il est possible de référencer une classe en utilisant une variable. La valeur de la variable ne peut être un mot-clé (e.g. self, parent et static).

Paamayim Nekudotayim pourrait au premier abord sembler être un choix étrange pour nommer un double deux-points. Cependant, au moment de l'écriture du Zend Engine 0.5 (qui faisait fonctionner PHP 3), c'est le nom qui a été choisi par l'équipe Zend. En fait, cela signifie un double deux-points en hébreu.

Exemple 1 : en dehors de la définition de la classe

```php
<?php
class MyClass {
	const CONST_VALUE = 'Une valeur constante';
}

$classname = 'MyClass';
// Depuis PHP 5.3.0
echo($classname::CONST_VALUE);

echo(MyClass::CONST_VALUE);
```

Trois mots-clés spéciaux, self, parent, et static sont utilisés pour accéder aux propriétés ou aux méthodes depuis la définition de la classe.

Exemple 2 : depuis la définition de la classe

```php
<?php
class OtherClass extends MyClass
{
	public static $my_static = 'variable statique';

	public static function doubleColon() {
		echo(parent::CONST_VALUE . "\n");
		echo(self::$my_static . "\n");
	}
}

$classname = 'OtherClass';
// Depuis PHP 5.3.0
echo($classname::doubleColon());

OtherClass::doubleColon();
?>
```

Lorsqu'une classe héritant d'une autre redéfinit une méthode de sa classe parente, PHP n'appellera pas la méthode de la classe parente. Il appartient à la méthode dérivée d'appeler la méthode d'origine en cas de besoin. Cela est également valable pour les définitions des constructeurs et destructeurs, la surcharge, et les définitions de méthodes magiques.

Exemple 3 : appel d’une méthode parent

```php
<?php
class MyClass
{
	protected function myFunc() {
		echo("MyClass::myFunc()\n");
	}
}

class OtherClass extends MyClass
{
	// Surcharge de la définition parente
	public function myFunc() {

		// Mais appel de la méthode parente
		parent::myFunc();
		echo("OtherClass::myFunc()\n");
	}
}

$class = new OtherClass();
$class->myFunc();
?>
```

# Contenu de ./0550 - L'héritage/content.md

L'héritage en POO c’est lorsqu'une classe dérive d'une autre classe.

La classe enfant héritera de toutes les propriétés et méthodes publiques et protégées de la classe parente. De plus, il peut avoir ses propres propriétés et méthodes.

Une classe héritée est définie à l'aide du mot-clé ```extends```.

exemple :

```php
<?php
class Fruit {
  public $name;
  public $color;
  public function __construct($name, $color) {
    $this->name = $name;
    $this->color = $color;
  }
  public function intro() {
    echo("The fruit is {$this->name} and the color is {$this->color}.");
  }
}

class Strawberry extends Fruit {
  public function message() {
    echo("Am I a fruit or a berry? ");
  }
}
$strawberry = new Strawberry("Strawberry", "red");
$strawberry->message();
$strawberry->intro();
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
Am I a fruit or a berry? The fruit is Strawberry and the color is red.
```

La classe Fraise est héritée de la classe Fruit.

Cela signifie que la classe Strawberry peut utiliser les propriétés publiques ```$name``` et ```$color``` ainsi que les méthodes publiques ```__construct()``` et ```intro()``` de la classe Fruit en raison de l'héritage.

La classe Strawberry a aussi sa propre méthode : ```message()```.

## Héritage et modificateur d’accès protégé

Les propriétés ```protected``` ou les méthodes sont accessibles au sein de la classe et par les classes dérivées de cette classe. 

exemple :

```php
<?php
class Fruit {
  public $name;
  public $color;
  public function __construct($name, $color) {
    $this->name = $name;
    $this->color = $color;
  }
  protected function intro() {
    echo("The fruit is {$this->name} and the color is {$this->color}.");
  }
}

class Strawberry extends Fruit {
  public function message() {
    echo("Am I a fruit or a berry? ");
  }
}

$strawberry = new Strawberry("Strawberry", "red"); 
$strawberry->message();
$strawberry->intro();
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
Am I a fruit or a berry?
```

Dans l'exemple ci-dessus, nous voyons que si nous essayons d'appeler une méthode ```protected``` (```intro()```) depuis l'extérieur de la classe, nous recevons une erreur. Les méthodes ```public``` fonctionnent bien !

## Remplacement des méthodes héritées

Les méthodes héritées peuvent être remplacées en définissant les méthodes (utiliser le même nom) dans la classe enfant.

L'exemple ci-dessous. Les méthodes ```__construct()``` et ```intro()``` de la classe enfant (Strawberry) remplaceront les méthodes ```__construct()``` et ```intro()``` de la classe parent (Fruit) :

```php
<?php
class Fruit {
  public $name;
  public $color;
  public function __construct($name, $color) {
    $this->name = $name;
    $this->color = $color;
  }
  public function intro() {
    echo("The fruit is {$this->name} and the color is {$this->color}.");
  }
}

class Strawberry extends Fruit {
  public $weight;
  public function __construct($name, $color, $weight) {
    $this->name = $name;
    $this->color = $color;
    $this->weight = $weight;
  }
  public function intro() {
    echo("The fruit is {$this->name}, the color is {$this->color}, and the weight is {$this->weight} gram.");
  }
}

$strawberry = new Strawberry("Strawberry", "red", 50);
$strawberry->intro();
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
The fruit is Strawberry, the color is red, and the weight is 50 gram.
```

## Le mot clé final

Le mot-clé ```final``` peut être utilisé pour empêcher l'héritage de classe ou pour empêcher la substitution de méthode.

L'exemple suivant montre comment empêcher l'héritage de classe :

```php
<?php
final class Fruit {
  // code
}

class Strawberry extends Fruit {
  // code
}
?>
```

L'exemple suivant montre comment empêcher le remplacement de méthode :

```php
<?php
class Fruit {
  final public function intro() {
    // code
  }
}

class Strawberry extends Fruit {
  public function intro() {
    // code
  }
}
?>
```

# Contenu de ./0560 - Exceptions/content.md

PHP a une gestion des exceptions similaire à ce qu'offrent les autres langages de programmation. Une exception peut être lancée ("throw") et attrapée ("catch") dans PHP. Le code devra être entouré d'un bloc “try” pour faciliter la saisie d'une exception potentielle. Chaque “try” doit avoir au moins un bloc “catch” ou “finally” correspondant.
Si une exception est lancée et que la portée courante de la fonction n'a pas de bloc “catch”, l'exception "remontera" la pile d'appel de la fonction appelante jusqu'à trouver un bloc “catch” correspondant. Tous les blocs “finally” rencontrés seront exécutés. Si la pile d'appels est déroulée jusqu'à la portée globale sans rencontrer de bloc “catch” correspondant, le programme sera terminé avec une erreur fatale sauf si un gestionnaire global d'exception a été défini.

L'objet lancé doit être une instance de la classe Exception ou d'une sous-classe de la classe Exception. Tenter de lancer un objet qui ne correspond pas à cela résulte en une erreur fatale émise par PHP.

À partir de PHP 8.0.0, le mot clé “throw” est une expression et peut être utilisé dans n'importe quel contexte d'expressions. Dans les versions antérieures, c'était une déclaration qui devait être sur sa propre ligne.

## Catch

Un bloc ```catch``` définit comment réagir à une exception qui a été lancée. Un bloc ```catch``` définit un ou plusieurs types d'exceptions ou erreurs qu'il peut gérer, et optionnellement une variable dans laquelle assigner l'exception. (Cette variable était requise dans les versions antérieures à PHP 8.0.0) Le premier bloc ```catch``` qu'une exception ou erreur lancée rencontre et qui correspond au type de l'objet lancé gérera l'objet.

Plusieurs blocs ```catch``` peuvent être utilisés pour attraper différentes classes d'exceptions. L'exécution normale (lorsque aucune exception n'est lancée dans le bloc ```try```) continue après le dernier bloc ```catch``` défini dans la séquence. Les exceptions peuvent être lancées (```throw```) ou relancées dans un bloc ```catch```. Sinon, l'exécution continuera après le bloc ```catch``` qui a été déclenché.

Lorsqu'une exception est lancée, le code suivant le traitement ne sera pas exécuté et PHP tentera de trouver le premier bloc ```catch``` correspondant. Si une exception n'est pas attrapée, une erreur fatale issue de PHP sera envoyée avec un message "Uncaught Exception ..." indiquant que l'exception n'a pu être attrapée à moins qu'un gestionnaire d'exceptions ne soit défini avec la fonction ```set_exception_handler()```.

À partir de PHP 7.1, un bloc ```catch``` peut spécifier plusieurs exceptions à l'aide du caractère pipe (```|```). Ceci est utile lorsque différentes exceptions de hiérarchies de classes différentes sont traitées de la même manière.

À partir de PHP 8.0.0, le nom de variables pour l'exception attrapée est optionnel. Si non spécifié, le bloc catch sera toujours exécuté, mais n'aura pas accès à l'objet lancé.

## Finally

Un bloc ```finally``` peut aussi être spécifié après des blocs ```catch```. Le code à l'intérieur du bloc ```finally``` sera toujours exécuté après les blocs ```try``` et ```catch```, indépendamment du fait qu'une exception a été lancée, avant de continuer l'exécution normale.
Une interaction notable est entre un bloc ```finally``` et une déclaration ```return```. Si une déclaration ```return``` est rencontrée à l'intérieur des blocs ```try``` ou ```catch```, le bloc ```finally``` sera quand même exécuté. De plus, la déclaration ```return``` est évaluée quand elle est rencontrée, mais le résultat sera retourné après que le bloc ```finally``` est exécuté. Additionnellement, si le bloc ```finally``` contient aussi une déclaration ```return``` la valeur du bloc ```finally``` est retournée.

## Global exception handler

Si une exception est autorisée à remonter jusqu'à la portée globale, elle peut être attrapée par un gestionnaire d'exceptions global s'il a été défini. La fonction ```set_exception_handler()``` peut définir une fonction qui sera appelée à la place d'un bloc ```catch``` si aucun autre bloc n'est invoqué. L'effet est essentiellement identique à entourer le programme entier dans un bloc ```try-catch``` avec cette fonction en tant que ```catch```.

## Exemples

Exemple 1 : Lancer une exception 

```php
<?php
function inverse($x) {
    if (!$x) {
        throw new Exception('Division par zéro.');
    }
    return 1/$x;
}

try {
    echo(inverse(5) . "\n");
    echo(inverse(0) . "\n");
} catch (Exception $e) {
    echo('Exception reçue : ',  $e->getMessage(), "\n");
}

// Continue execution
echo("Bonjour tout le monde !\n");
?>
```

L'exemple ci-dessus va afficher :

```php
0.2
Exception reçue : Division par zéro.
Bonjour tout le monde !
```

Exemple 2 : Gestion de l'exception avec un bloc finally

```php
<?php
function inverse($x) {
    if (!$x) {
        throw new Exception('Division par zéro.');
    }
    return 1/$x;
}

try {
    echo(inverse(5) . "\n");
} catch (Exception $e) {
    echo('Exception reçue : ',  $e->getMessage(), "\n");
} finally {
    echo("Première fin.\n");
}

try {
    echo(inverse(0) . "\n");
} catch (Exception $e) {
    echo('Exception reçue : ',  $e->getMessage(), "\n");
} finally {
    echo("Seconde fin.\n");
}

// On continue l'exécution
echo("Bonjour tout le monde !\n");
?>
```

L'exemple ci-dessus va afficher :

```php
0.2
Première fin.
Exception reçue : Division par zéro.
Seconde fin.
Bonjour tout le monde !
```

Exemple 3 : Interaction entre le bloc finally et return

```php
<?php

function test() {
    try {
        throw new Exception('foo');
    } catch (Exception $e) {
        return 'catch';
    } finally {
        return 'finally';
    }
}

echo(test());
?>
```

L'exemple ci-dessus va afficher :

```php
finally
```

Exemple 4 : Héritage d’une exception

```php
<?php

class MyException extends Exception { }

class Test {
    public function testing() {
        try {
            try {
                throw new MyException('foo!');
            } catch (MyException $e) {
                // on la relance
                throw $e;
            }
        } catch (Exception $e) {
            var_dump($e->getMessage());
        }
    }
}

$foo = new Test;
$foo->testing();

?>
```

L'exemple ci-dessus va afficher :

```php
string(4) "foo!"
```

Exemple 5 : Gestions des exceptions de capture multiple

```php
<?php

class MyException extends Exception { }

class MyOtherException extends Exception { }

class Test {
    public function testing() {
        try {
            throw new MyException();
        } catch (MyException | MyOtherException $e) {
            var_dump(get_class($e));
        }
    }
}

$foo = new Test;
$foo->testing();

?>
```

L'exemple ci-dessus va afficher :

```php
string(11) "MyException"
```

Exemple 6 : Omettre la variable attrapée (PHP 8.0.0 ou supérieur)

```php
<?php

class SpecificException extends Exception {}

function test() {
    throw new SpecificException('Oopsie');
}

try {
    test();
} catch (SpecificException) {
    print "A SpecificException was thrown, but we don't care about the details.";
}
?>
```

Exemple 7 : Throw en tant qu’expression (PHP 8.0.0 ou supérieur)

```php
<?php

class SpecificException extends Exception {}

function test() {
    do_something_risky() or throw new Exception('It did not work');
}

try {
    test();
} catch (Exception $e) {
    print $e->getMessage();
}
?>
```

# Contenu de ./0570 - Traits/content.md

Depuis PHP 5.4.0, PHP supporte une manière de réutiliser le code appelée Traits.
Les traits sont un mécanisme de réutilisation de code dans un langage à héritage simple tel que PHP. Un trait tente de réduire certaines limites de l'héritage simple, en autorisant le développeur à réutiliser un certain nombre de méthodes dans des classes indépendantes. La sémantique entre les classes et les traits réduit la complexité et évite les problèmes typiques de l'héritage multiple et des Mixins.

Un trait est semblable à une classe, mais il ne sert qu'à grouper des fonctionnalités d'une manière intéressante. Il n'est pas possible d'instancier un Trait en lui-même. C'est un ajout à l'héritage traditionnel, qui autorise la composition horizontale de comportements, c'est-à-dire l'utilisation de méthodes de classe sans besoin d'héritage.

exemple : 

```php
<?php
trait ezcReflectionReturnInfo {
	function getReturnType() { /*1*/ }
	function getReturnDescription() { /*2*/ }
}

class ezcReflectionMethod extends ReflectionMethod {
	use ezcReflectionReturnInfo;
	/* ... */
}

class ezcReflectionFunction extends ReflectionFunction {
	use ezcReflectionReturnInfo;
	/* ... */
}
?>
```

## Précédence

Une méthode héritée depuis une classe mère est écrasée par une méthode issue d'un Trait. L'ordre de précédence fait en sorte que les méthodes de la classe courante écrasent les méthodes issues d'un Trait, elles-mêmes surchargeant les méthodes héritées.

Exemple :

```php
<?php
class Base {
	public function sayHello() {
		echo('Hello ');
	}
}

trait SayWorld {
	public function sayHello() {
		parent::sayHello();
		echo('World!');
	}
}

class MyHelloWorld extends Base {
	use SayWorld;
}

$o = new MyHelloWorld();
$o->sayHello();
?>
```

```php
<?php
trait HelloWorld {
	public function sayHello() {
		echo('Hello World!');
	}
}

class TheWorldIsNotEnough {
	use HelloWorld;
	public function sayHello() {
		echo('Hello Universe!');
	}
}

$o = new TheWorldIsNotEnough();
$o->sayHello();
?>
```

```php
<?php
trait Hello {
	public function sayHello() {
		echo('Hello ');
	}
}
```

```php
trait World {
	public function sayWorld() {
		echo('World');
	}
}

class MyHelloWorld {
	use Hello, World;
	public function sayExclamationMark() {
		echo('!');
	}
}

$o = new MyHelloWorld();
$o->sayHello();
$o->sayWorld();
$o->sayExclamationMark();
?>
```

```php
<?php
trait A {
	public function smallTalk() {
		echo('a');
	}
	public function bigTalk() {
		echo('A');
	}
}

trait B {
	public function smallTalk() {
		echo('b');
	}
	public function bigTalk() {
		echo('B');
	}
}

class Talker {
	use A, B {
		B::smallTalk insteadof A;
		A::bigTalk insteadof B;
	}
}

class Aliased_Talker {
	use A, B {
		B::smallTalk insteadof A;
		A::bigTalk insteadof B;
		B::bigTalk as talk;
	}
}
?>
```

## Changer la visibilité des méthodes

En utilisant la syntaxe “as”, vous pouvez aussi ajuster la visibilité de la méthode dans la classe qui l'utilise.

Exemple :

```php
<?php
trait HelloWorld {
	public function sayHello() {
		echo('Hello World!');
	}
}

// Modification de la visibilité de la méthode sayHello
class MyClass1 {
	use HelloWorld { sayHello as protected; }
}

// Utilisation d'un alias lors de la modification de la visibilité
// La visibilité de la méthode sayHello n'est pas modifiée
class MyClass2 {
	use HelloWorld { sayHello as private myPrivateHello; }
}
?>
```

## Traits composés depuis d’autres traits

Tout comme les classes peuvent utiliser des traits, d'autres traits le peuvent aussi. Un trait peut donc utiliser d'autres traits et hériter de tout ou d'une partie de ceux-ci.

Exemple :

```php
<?php
trait Hello {
	public function sayHello() {
		echo('Hello ');
	}
}

trait World {
	public function sayWorld() {
		echo('World!');
	}
}

trait HelloWorld {
	use Hello, World;
}

class MyHelloWorld {
	use HelloWorld;
}

$o = new MyHelloWorld();
$o->sayHello();
$o->sayWorld();
?>
```

```php
<?php
trait Hello {
	public function sayHelloWorld() {
		echo('Hello'.$this->getWorld());
	}
	abstract public function getWorld();
}

class MyHelloWorld {
	private $world;
	use Hello;
	public function getWorld() {
		return $this->world;
	}
	public function setWorld($val) {
		$this->world = $val;
	}
}
?>
```

## Attributs statiques dans les traits

Des variables statiques peuvent être utilisées dans les méthodes d'un trait, mais ne peuvent être définies dans le trait. Les traits peuvent par contre déclarer des méthodes statiques pour la classe sous-jacente.

Exemple 1 :

```php
<?php
trait Counter {
	public function inc() {
		static $c = 0;
		$c = $c + 1;
		echo("$c\n");
	}
}

class C1 {
	use Counter;
}

class C2 {
	use Counter;
}

$o = new C1(); $o->inc(); // echo 1
$p = new C2(); $p->inc(); // echo 1
?>
```

Exemple 2 :

```php
<?php
trait StaticExample {
	public static function doSomething() {
		return 'Doing something';
	}
}

class Example {
	use StaticExample;
}

Example::doSomething();
?>
```

## Propriétés

Les traits peuvent aussi définir des propriétés.

Exemple 1 :

```php
<?php
trait PropertiesTrait {
	public $x = 1;
}

class PropertiesExample {
	use PropertiesTrait;
}

$example = new PropertiesExample;
$example->x;
?>
```

Si un trait définit une propriété, alors la classe ne peut pas définir une propriété du même nom ; sinon, une erreur sera levée. Il s'agira d'une erreur de type ```E_STRICT``` si la définition dans la classe est compatible (même visibilité et valeur initiale), et d'une erreur fatale dans les autres cas.

Exemple 2 :

```php
<?php
trait PropertiesTrait {
	public $same = true;
	public $different = false;
}

class PropertiesExample {
	use PropertiesTrait;
	public $same = true; // Strict Standards
	public $different = true; // Fatal error
}
?>
```

# Contenu de ./0580 - PDO/content.md

Le PHP Data Objects (PDO) définit une interface légère pour accéder aux bases de données en PHP. Il fournit une couche d'abstraction d'accès aux données pour travailler avec les bases de données en PHP. Il définit une API cohérente pour travailler avec différents systèmes de bases de données.

## Classes PHP PDO

Le PDO représente une connexion entre PHP et un serveur de base de données. La classe PDOStatement représente une instruction préparée et, après l'exécution de l'instruction, un ensemble de résultats associés. La classe ```PDOException``` représente une erreur soulevée par PDO.

## Base de données MySQL

Dans ce cours, nous travaillons avec une base de données MySQL. Voici le code permettant de créer la table dont nous nous servirons pendant ce cours. Si vous ne savez pas comment l'exploiter, référez vous aux cours de MySQL.

```sql
DROP TABLE IF EXISTS countries;
CREATE TABLE countries(id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255), population INT);

INSERT INTO countries(name, population) VALUES('China', 1382050000);
INSERT INTO countries(name, population) VALUES('India', 1313210000);
INSERT INTO countries(name, population) VALUES('USA', 324666000);
INSERT INTO countries(name, population) VALUES('Indonesia', 260581000);
INSERT INTO countries(name, population) VALUES('Brazil', 207221000);
INSERT INTO countries(name, population) VALUES('Pakistan', 196626000);
INSERT INTO countries(name, population) VALUES('Nigeria', 186988000);
INSERT INTO countries(name, population) VALUES('Bangladesh', 162099000);
INSERT INTO countries(name, population) VALUES('Nigeria', 186988000);
INSERT INTO countries(name, population) VALUES('Russia', 146838000);
INSERT INTO countries(name, population) VALUES('Japan', 126830000);
```

## PHP PDO query

La fonction PDO ```query()``` exécute une instruction SQL en un seul appel de fonction, et renvoie le jeu de résultats (s'il y en a) renvoyé par l'instruction.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);

$stm = $pdo->query("SELECT VERSION()");

$version = $stm->fetch();

echo($version[0] . PHP_EOL);
```

L'exemple renvoie la version de MySQL.

```php
$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";
```

Ces variables sont utilisées pour créer une chaîne de connexion à la base de données. Le ```$dsn``` est le nom de la source de données, qui contient les informations nécessaires pour se connecter à la base de données.

```php
$pdo = new PDO($dsn, $user, $passwd);
```

Un nouvel objet PDO est créé. Il passe au constructeur le nom de la source de données ainsi que le nom d'utilisateur et le mot de passe. La classe PDO représente une connexion entre PHP et un serveur de base de données.

```php
$stm = $pdo->query("SELECT VERSION()");
```

La méthode ```query()``` exécute une instruction SQL en un seul appel de fonction. Elle renvoie le jeu de résultats.

```php
$version = $stm->fetch();
```

La méthode ```fetch()``` de l'instruction PDO permet d'extraire la ligne suivante d'un ensemble de résultats. Dans notre cas, il s'agit d'une version de MySQL.

```php
echo($version[0] . PHP_EOL);
```

La variable ```$version``` est un tableau, il affiche sa première valeur.

## PHP PDO exec

La fonction PDO ```exec()``` exécute une instruction SQL et renvoie le nombre de lignes concernées.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);
$id = 12;
$nrows = $pdo->exec("DELETE FROM countries WHERE id IN (1, 2, 3)");
echo("La déclaration a supprimé $nrows lignes\n");
```

L'exemple de code supprime trois lignes. Il affiche le nombre de lignes concernées.

```php
$nrows = $pdo->exec("DELETE FROM countries WHERE id IN (1, 2, 3)");
```

Dans cette instruction SQL, les lignes avec les identifiants 1, 2 et 3 sont supprimées. Le nombre de lignes supprimées est stocké dans la variable ```$nrows```.

```php
echo("La déclaration a supprimé $nrows lignes\n");
```

Cela affiche le nombre de lignes supprimées.

## PHP PDO fetch

Le paramètre fetch contrôle la façon dont la ligne suivante sera retournée à l'appelant. Par exemple, ```PDO::FETCH_ASSOC``` renvoie un tableau indexé par le nom de la colonne, ```PDO::FETCH_NUM``` renvoie un tableau indexé par le numéro de la colonne, et ```PDO::FETCH_BOTH``` renvoie un tableau indexé à la fois par le nom et le numéro de la colonne indexée. Le style de récupération par défaut est ```PDO::FETCH_BOTH```.

```php
<?php
$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);
$stm = $pdo->query("SELECT * FROM countries");
$rows = $stm->fetchAll(PDO::FETCH_NUM);
foreach($rows as $row) {
    printf("$row[0] $row[1] $row[2]\n");
}
```

Dans cet exemple, le code affichera les données dans un tableau indexé.

```php
$stm = $pdo->query("SELECT * FROM countries");
```

Il sélectionne toutes les données du tableau des pays.

```php
$rows = $stm->fetchAll(PDO::FETCH_NUM);
```

Il passe le style ```PDO:FETCH_NUM``` à la méthode ```fetchAll()```.

```php
foreach($rows as $row) {
    printf("$row[0] $row[1] $row[2]\n");
}
```

Il parcourt le tableau ```$rows``` et affiche les champs. Les champs sont accessibles via les index du tableau.

## Liaison des paramètres PHP PDO

Les instructions SQL sont souvent construites de manière dynamique. Un utilisateur fournit une entrée et cette entrée est intégrée dans la déclaration. Nous devons être prudents chaque fois que nous traitons une entrée provenant d'un utilisateur. Cela a de sérieuses implications en matière de sécurité. La manière recommandée de construire dynamiquement des instructions SQL est d'utiliser la liaison des paramètres.

PDO contient les méthodes ```bindParam()``` et ```bindValue()``` pour créer des requêtes paramétrées.

PDO permet de lier des données à des points d'interrogation ou à des espaces nommés.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "root";
$passwd = "andrea";

$pdo = new PDO($dsn, $user, $passwd);

$id = 12;

$stm = $pdo->prepare("SELECT * FROM countries WHERE id = ?");
$stm->bindValue(1, $id);
$stm->execute();

$row = $stm->fetch(PDO::FETCH_ASSOC);

echo("Id: " . $row['id'] . PHP_EOL);
echo("Name: " . $row['name'] . PHP_EOL);
echo("Population: " . $row['population'] . PHP_EOL);
```

Dans l'exemple, nous utilisons bindValue() pour créer une requête paramétrée. Nous utilisons le point d'interrogation comme placeholder.

```php
$id = 12;
```

Disons que cette entrée provient d'un utilisateur.

```php
$stm = $pdo->prepare("SELECT * FROM countries WHERE id = ?");
$stm->bindValue(1, $id);
$stm->execute();
```

L'instruction select récupère une ligne spécifique du tableau. Nous lions la valeur avec ```bindValue()``` à un point d'interrogation.

Dans le second cas, nous utilisons ```bindParam()```.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);

$id = 12;

$stm = $pdo->prepare("SELECT * FROM countries WHERE id = :id");
$stm->bindParam(":id", $id, PDO::PARAM_INT);
$stm->execute();

$row = $stm->fetch(PDO::FETCH_ASSOC);

echo("Id : " . $row['id'] . PHP_EOL);
echo("Nom : " . $row['name'] . PHP_EOL);
echo("Population : " . $row['population'] . PHP_EOL);
```

L'exemple sélectionne et affiche une ligne spécifique.

```php
$stm = $pdo->prepare("SELECT * FROM countries WHERE id = :id");
$stm->bindParam(":id", $id, PDO::PARAM_INT);
$stm->execute();
```

Cette fois-ci, nous utilisons un placeholder nommé (:id) et bindParam().

## PHP PDO lastInsertId

La méthode PDO ```lastInsertId()``` renvoie l'identifiant de la dernière ligne insérée.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);

$sql = "CREATE TABLE words(id INT PRIMARY KEY AUTO_INCREMENT,
    word VARCHAR(255))";

$ret = $pdo->exec($sql);
$pdo->exec("INSERT INTO words(word) VALUES ('pen')");
$pdo->exec("INSERT INTO words(word) VALUES ('bum')");
$pdo->exec("INSERT INTO words(word) VALUES ('hum')");
$pdo->exec("INSERT INTO words(word) VALUES ('den')");

$rowid = $pdo->lastInsertId();

echo("L'ID de la dernière ligne insérée est : $rowid\n");
```

Dans l'exemple, nous créons une nouvelle table. Après la création de la table, nous trouvons le dernier Id inséré avec ```lastInsertId()```.

```
L'ID de la dernière ligne insérée est : 4
```

Voici la réponse.

```sql
mysql> select * from words;
+----+------+
| id | word |
+----+------+
|  1 | pen  |
|  2 | bum  |
|  3 | hum  |
|  4 | den  |
+----+------+
4 rows in set (0.01 sec)
```

Nous vérifions les données.

## Transactions PHP PDO

Une transaction est une unité atomique d'opérations de base de données sur les données d'une ou plusieurs bases de données. Les effets de toutes les instructions SQL dans une transaction peuvent être soit tous validés dans la base de données, soit tous annulés.

La fonction PDO ```beginTransaction()``` initie une nouvelle transaction. PDO ```commit()``` commet la transaction. Et PDO ```rollback()``` annule la transaction.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);

try {
    $pdo->beginTransaction();
    $stm = $pdo->exec("INSERT INTO countries(name, population) VALUES ('Iraq', 38274000)");
    $stm = $pdo->exec("INSERT INTO countries(name, population) VALUES ('Uganda', 37673800)");
    $pdo->commit();
} catch(Exception $e) {
    $pdo->rollback();
    throw $e;
}
```

Dans l'exemple, nous ajoutons deux nouveaux pays à la table de la base de données. Les instructions d'insertion sont placées dans une transaction : soit les deux insertions sont exécutées, soit aucune.

```php
} catch(Exception $e) {
    $pdo->rollback();
    throw $e;
}
```

En cas d'exception, nous annulons la transaction : aucune donnée n'est écrite dans la base de données. Nous lançons l'exception pour que le traitement des exceptions continue de la manière habituelle.

## PHP PDO obtention de métadonnées

Les métadonnées sont des informations sur les données d'une base de données. Les métadonnées contiennent des informations sur les tables et les colonnes dans lesquelles nous stockons les données. Le nombre de lignes qu'une instruction SQL affecte est une métadonnée. Le nombre de lignes et de colonnes renvoyées dans un jeu de résultats sont également des métadonnées.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);

$stm = $pdo->query("SELECT name, population FROM countries WHERE id=1");

$ncols = $stm->columnCount();

echo("Le jeu de résultats contient $ncols colonnes\n");
```

Dans l'exemple, il affiche le nombre de colonnes dans le jeu de résultats avec la méthode ```columnCount()```.

La méthode ```getAttribute()``` permet de récupérer un attribut de connexion à une base de données.

```php
<?php

$dsn = "mysql:host=localhost;dbname=mydb";
$user = "user12";
$passwd = "12user";

$pdo = new PDO($dsn, $user, $passwd);

$driver = $pdo->getAttribute(PDO::ATTR_DRIVER_NAME);
$server_version = $pdo->getAttribute(PDO::ATTR_SERVER_VERSION);
$autocommit_mode = $pdo->getAttribute(PDO::ATTR_AUTOCOMMIT);

echo("Driver: $driver\n");
echo("Server version: $server_version\n");
echo("Autocommit mode: $autocommit_mode\n");
```

Dans l'exemple, nous obtenons le nom du pilote, la version du serveur et le mode autocommit avec la méthode ```getAttribute()```.

Voici un exemple de réponse :

```sql
Driver: mysql
Server version: 5.7.22-0ubuntu0.16.04.1
Autocommit mode: 1
```

# Contenu de ./0590 - Les méthodes magiques/content.md

Les méthodes magiques sont des méthodes spéciales qui écrase l'action par défaut de PHP quand certaines actions sont réalisées sur un objet.

Les méthodes suivantes sont considérées magiques : 

- ```__construct()```
- ```__destruct()```
- ```__call()```
- ```__callStatic()```
- ```__get()```
- ```__set()```
- ```__isset()```
- ```__unset()```
- ```__sleep()```
- ```__wakeup()```
- ```__serialize()```
- ```__unserialize()```
- ```__toString()```
- ```__invoke()```
- ```__set_state()```
- ```__clone()```
- ```__debugInfo()```

## Exemple __construct()

```php
__construct(mixed ...$values = ""): void
```

PHP permet aux développeurs de déclarer des constructeurs pour les classes. Les classes qui possèdent une méthode constructeur appellent cette méthode à chaque création d'une nouvelle instance de l'objet, ce qui est intéressant pour toutes les initialisations dont l'objet a besoin avant d'être utilisé.

Exemple :

```php
<?php
class BaseClass {
    function __construct() {
        print("Dans le constructeur de BaseClass\n");
    }
}

class SubClass extends BaseClass {
    function __construct() {
        parent::__construct();
        print("Dans le constructeur de SubClass\n");
    }
}

class OtherSubClass extends BaseClass {
    // Constructeur hérité de BaseClass
}

// Dans le constructeur de BaseClass
$obj = new BaseClass();

// Dans le constructeur de BaseClass
// Dans le constructeur de SubClass
$obj = new SubClass();

// Dans le constructeur de BaseClass
$obj = new OtherSubClass();
?>
```

Exemple : arguments dans le constructeur

```php
<?php
class Point {
    protected int $x;
    protected int $y;

    public function __construct(int $x, int $y = 0) {
        $this->x = $x;
        $this->y = $y;
    }
}

$p1 = new Point(4, 5);
$p2 = new Point(4);
$p3 = new Point(y: 5, x: 4);
?>
```

## Exemple __destruct()

```php
__destruct(): void
```

PHP possède un concept de destructeur similaire à celui d'autres langages orientés objet, comme le C++. La méthode destructeur est appelée dès qu'il n'y a plus de référence sur un objet donné, ou dans n'importe quel ordre pendant la séquence d'arrêt.

Exemple :

```php
<?php

class MyDestructableClass 
{
    function __construct() {
        print("In constructor\n");
    }

    function __destruct() {
        print("Destroying " . __CLASS__ . "\n");
    }
}

$obj = new MyDestructableClass();
```

Tout comme le constructeur, le destructeur parent ne sera pas appelé implicitement par le moteur. Pour exécuter le destructeur parent, vous devez appeler explicitement la fonction ```parent::__destruct``` dans le corps du destructeur. Tout comme les constructeurs, une classe enfant peut hériter du destructeur du parent s'il n'en implémente pas un lui-même.

Le destructeur sera appelé même si l'exécution du script est stoppée en utilisant la fonction ```exit()```. Appeler la fonction ```exit()``` dans un destructeur empêchera l'exécution des routines d'arrêt restantes.

## Exemple __sleep() et __wakeup()

```php
public __sleep(): array
public __wakeup(): void
```

```serialize()``` vérifie si la classe a une méthode avec le nom magique ```__sleep()```. Si c'est le cas, cette méthode sera exécutée avant toute linéarisation. Elle peut nettoyer l'objet, et elle est supposée retourner un tableau avec les noms de toutes les variables de l'objet qui doivent être linéarisées. Si la méthode ne retourne rien, alors “null” sera linéarisé, et une alerte de type ```E_NOTICE``` sera émise.

Le but avoué de ```__sleep()``` est de valider des données en attente ou d'effectuer des opérations de nettoyage. De plus, cette fonction est utile si un objet très large n'a pas besoin d'être sauvegardé dans sa totalité.

Réciproquement, la fonction ```unserialize()``` vérifie la présence d'une méthode dont le nom est le nom magique ```__wakeup()```. Si elle est présente, cette fonction peut reconstruire toute ressource que l'objet pourrait posséder.

Le but avoué de ```__wakeup()``` est de rétablir toute connexion de base de données qui aurait été perdue durant la linéarisation et d'effectuer des tâches de réinitialisation.

Exemple :

```php
<?php
class Connection
{
    protected $link;
    private $dsn, $username, $password;

    public function __construct($dsn, $username, $password)
    {
        $this->dsn = $dsn;
        $this->username = $username;
        $this->password = $password;
        $this->connect();
    }

    private function connect()
    {
        $this->link = new PDO($this->dsn, $this->username, $this->password);
    }

    public function __sleep()
    {
        return array('dsn', 'username', 'password');
    }

    public function __wakeup()
    {
        $this->connect();
    }
}
?>
```

## Exemple __serialize() et __unserialize()

```php
public __serialize(): array
public __unserialize(array $data): void
```

```serialize()``` vérifie si la classe a une méthode avec le nom magique ```__serialize()```. Si c'est le cas, cette méthode sera exécutée avant toute linéarisation. Elle doit construire et retourner un tableau associatif de paire clé/valeur qui représente la forme linéarisée de l'objet. Si aucun tableau n'est retournée une TypeError sera lancée.

L'utilisation prévue de ```_serialize()``` est de définir une représentation arbitraire de l'objet pour le linéariser facilement. Les éléments du tableau peuvent correspondre aux propriétés de l'objet mais ceci n'est pas requis.

Inversement, ```unserialize()``` vérifie la présence d'une fonction avec le nom magique ```__unserialize()```. Si présent, cette fonction sera passé le tableau restauré qui a été retournée depuis ```__serialize()```. Il peut alors restaurer les propriétés de l'objet depuis ce tableau comme approprié.

Exemple :

```php
<?php
class Connection
{
    protected $link;
    private $dsn, $username, $password;

    public function __construct($dsn, $username, $password)
    {
        $this->dsn = $dsn;
        $this->username = $username;
        $this->password = $password;
        $this->connect();
    }

    private function connect()
    {
        $this->link = new PDO($this->dsn, $this->username, $this->password);
    }

    public function __serialize(): array
    {
        return [
            'dsn' => $this->dsn,
            'user' => $this->username,
            'pass' => $this->password,
        ];
    }

    public function __unserialize(array $data): void
    {
        $this->dsn = $data['dsn'];
        $this->username = $data['user'];
        $this->password = $data['pass'];

        $this->connect();
    }
}
?>
```

## Exemple __toString()

```php
public __toString(): string
```

La méthode ```__toString()``` détermine comment l'objet doit réagir lorsqu'il est traité comme une chaîne de caractères. 

Exemple :

```php
<?php
class ClasseTest
{
    public $foo;

    public function __construct($foo)
    {
        $this->foo = $foo;
    }

    public function __toString()
    {
        return $this->foo;
    }
}

$class = new ClasseTest('Bonjour');
echo $class;
?>
```

L'exemple ci-dessus va afficher : Bonjour

## Exemple __invoke()

```php
__invoke( ...$values): mixed
```

La méthode ```__invoke()``` est appelée lorsqu'un script tente d'appeler un objet comme une fonction.

Exemple :

```php
<?php
class CallableClass
{
    public function __invoke($x)
    {
        var_dump($x);
    }
}
$obj = new CallableClass();
$obj(5);
var_dump(is_callable($obj));
?>
```

L'exemple ci-dessus va afficher : ```int(5) bool(true)```

## Exemple __set_state()

```php
static __set_state(array $properties): object
```

Cette méthode statique est appelée pour les classes exportées par la fonction ```var_export()```.

Le seul paramètre de cette méthode est un tableau contenant les propriétés exportées sous la forme ```['property' => value, ...]```.

Exemple :

```php
class A
{
    public $var1;
    public $var2;

    public static function __set_state($an_array)
    {
        $obj = new A();
        $obj->var1 = $an_array['var1'];
        $obj->var2 = $an_array['var2'];
        return $obj;
    }
}

$a = new A();
$a->var1 = 5;
$a->var2 = 'foo';

$b = var_export($a, true);
var_dump($b);
eval('$c = ' . $b . ';');
var_dump($c);
?>
```

L’exemple ci-dessus va afficher :

```php
string(60) "A::__set_state(array(
    'var1' => 5,
    'var2' => 'foo',
))"
object(A)#2 (2) {
    ["var1"]=>
    int(5)
    ["var2"]=>
    string(3) "foo"
}
```

## Exemple __debugInfo()

```php
__debugInfo(): array
```

Cette méthode est appelée par ```var_dump()``` lors du traitement d'un objet pour récupérer les propriétés qui doivent être affichées. Si la méthode n'est pas définie dans un objet, alors toutes les propriétés publiques, protégées et privées seront affichées.

exemple :

```php
<?php
class C {
    private $prop;

    public function __construct($val) {
        $this->prop = $val;
    }

    public function __debugInfo() {
        return [
            'propSquared' => $this->prop ** 2,
        ];
    }
}

var_dump(new C(42));
?>
```

L’exemple ci-dessus va afficher :

```php
object(C)#1 (1) {
    ["propSquared"]=>
    int(1764)
}
```

## Exemple __call() et __callStatic()

```php
public __call(string $name, array $arguments): mixed
public static __callStatic(string $name, array $arguments): mixed
```

- ```__call()``` est appelée lorsque l'on invoque des méthodes inaccessibles dans un contexte objet.
- ```__callStatic()``` est lancée lorsque l'on invoque des méthodes inaccessibles dans un contexte statique.

L'argument ```$name``` est le nom de la méthode appelée. L'argument ```$arguments``` est un tableau contenant les paramètres passés à la méthode ```$name```.

Exemple :

```php
<?php
class MethodTest
{
    public function __call($name, $arguments)
    {
        // Note : la valeur de $name est sensible à la casse.
        echo("Appel de la méthode '$name' "
             . implode(', ', $arguments). "\n");
    }

    public static function __callStatic($name, $arguments)
    {
        // Note : la valeur de $name est sensible à la casse.
        echo("Appel de la méthode statique '$name' "
             . implode(', ', $arguments). "\n");
    }
}

$obj = new MethodTest;
$obj->runTest('dans un contexte objet');

MethodTest::runTest('dans un contexte static');
?>
```

L’exemple ci-dessus va afficher :

```php
Appel de la méthode 'runTest' dans un contexte objet
Appel de la méthode statique 'runTest' dans un contexte static
```

## Exemple __get(), __set(), __iseet() et __unset()

```php
public __set(string $name, mixed $value): void
public __get(string $name): mixed
public __isset(string $name): bool
public __unset(string $name): void
```

- ```__set()``` est sollicitée lors de l'écriture de données vers des propriétés inaccessibles (protégées ou privées) ou inexistantes.
- ```__get()``` est appelée pour lire des données depuis des propriétés inaccessibles (protégées ou privées) ou inexistantes.
- ```__isset()``` est sollicitée lorsque ```isset()``` ou ```empty()``` sont appelées sur des propriétés inaccessibles (protégées ou privées) ou inexistantes.
- ```__unset()``` est invoquée lorsque ```unset()``` est appelée sur des propriétés inaccessibles (protégées ou privées) ou inexistante.

L'argument ```$name``` est le nom de la propriété avec laquelle on interagit. L'argument ```$value``` de la méthode ```__set()``` spécifie la valeur à laquelle la propriété $name devrait être définie.

La surcharge de propriétés ne fonctionne que dans les contextes objets. Ces méthodes magiques ne seront pas lancées en contexte statique. Par conséquent, ces méthodes ne devraient pas être déclarées comme statiques. Un avertissement est levé si une des méthodes magiques est déclarée comme statique.

Exemple :

```php
<?php
class PropertyTest
{
    /**  Variable pour les données surchargées.  */
    private $data = array();

    /**  La surcharge n'est pas utilisée sur les propriétés déclarées.  */
    public $declared = 1;

    /**  La surcharge n'est lancée que lorsque l'on accède à cette propriété depuis l'extérieur de la classe.  */
    private $hidden = 2;

    public function __set($name, $value)
    {
        echo("Définition de '$name' à la valeur '$value'\n");
        $this->data[$name] = $value;
    }

    public function __get($name)
    {
        echo("Récupération de '$name'\n");
        if (array_key_exists($name, $this->data)) {
            return $this->data[$name];
        }

        $trace = debug_backtrace();
        trigger_error(
            'Propriété non-définie via __get() : ' . $name .
            ' dans ' . $trace[0]['file'] .
            ' à la ligne ' . $trace[0]['line'],
            E_USER_NOTICE);
        return null;
    }

    public function __isset($name)
    {
        echo("Est-ce que '$name' est défini ?\n");
        return isset($this->data[$name]);
    }

    public function __unset($name)
    {
        echo("Effacement de '$name'\n");
        unset($this->data[$name]);
    }

    /**  Ce n'est pas une méthode magique, nécessaire ici que pour l'exemple.  */
    public function getHidden()
    {
        return $this->hidden;
    }
}


echo("<pre>\n");

$obj = new PropertyTest;

$obj->a = 1;
echo($obj->a . "\n\n");

var_dump(isset($obj->a));
unset($obj->a);
var_dump(isset($obj->a));
echo("\n");

echo($obj->declared . "\n\n");

echo("Manipulons maintenant la propriété privée nommée 'hidden' :\n");
echo("'hidden' est visible depuis la classe, donc __get() n'est pas utilisée...\n");
echo($obj->getHidden() . "\n");
echo("'hidden' n'est pas visible en dehors de la classe, donc __get() est utilisée...\n");
echo($obj->hidden . "\n");
?>
```

L’exemple ci-dessus va afficher :

```php
Définition de 'a' à '1'
Récupération de 'a'
1

Est-ce que 'a' est défini ?
bool(true)
Effacement de 'a'
Est-ce que 'a' est défini ?
bool(false)

1

Manipulons maintenant la propriété privée nommée 'hidden' :
'hidden' est visible depuis la classe, donc __get() n'est pas utilisée...
2
'hidden' n'est pas visible en dehors de la classe, donc __get() est utilisée...
Récupération de 'hidden'


Notice: Propriété non définie via __get() : hidden dans <file> à la ligne 64 dans <file> à la ligne 28
```

## Exemple __clone()

Le fait de créer une copie d'un objet possédant exactement les mêmes propriétés n'est pas toujours le comportement que l'on souhaite. Un bon exemple pour illustrer le besoin d'un constructeur de copie : si vous avez un objet qui représente une fenêtre GTK et que l'objet contient la ressource représentant cette fenêtre GTK, lorsque vous créez une copie vous pouvez vouloir créer une nouvelle fenêtre avec les mêmes propriétés, mais que le nouvel objet contient une ressource représentant la nouvelle fenêtre.

Une copie d'objet est créée en utilisant le mot-clé ```clone``` (qui fait appel à la méthode ```__clone()``` de l'objet, si elle a été définie).

exemple :

```php
<?php

$copie_d_objet = clone($objet);

?>
```

Lorsqu'un objet est cloné, PHP effectue une copie superficielle de toutes les propriétés de l'objet. Toutes les propriétés qui sont des références à d'autres variables demeureront des références.

```php
__clone(): void
```

Une fois le clonage effectué, si une méthode ```__clone()``` est définie, la méthode ```__clone()``` du nouvel objet sera appelée, pour permettre à chaque propriété qui doit l'être d'être modifiée.

exemple :

```php
<?php
class SubObject 
{
    static $instances = 0;
    public $instance;

    public function __construct() {
        $this->instance = ++self::$instances;
    }

    public function __clone() {
        $this->instance = ++self::$instances;
    }
}

class MyCloneable 
{
    public $objet1;
    public $objet2;

    function __clone() 
    {    
        // Force la copie de this->object, sinon
        // il pointera vers le même objet.
        $this->object1 = clone $this->object1;
    }
}

$obj = new MyCloneable();

$obj->object1 = new SubObject();
$obj->object2 = new SubObject();

$obj2 = clone $obj;


print("Objet original :\n");
print_r($obj);

print("Objet cloné :\n");
print_r($obj2);

?>
```

L’exemple ci dessus va afficher :

```php
Object original :
MyCloneable Object
(
    [object1] => SubObject Object
        (
            [instance] => 1
        )

    [object2] => SubObject Object
        (
            [instance] => 2
        )

)
Object cloné :
MyCloneable Object
(
    [object1] => SubObject Object
        (
            [instance] => 3
        )

    [object2] => SubObject Object
        (
            [instance] => 2
        )
)
```

# Contenu de ./0600 - Objets et références/content.md

Un des piliers de la POO de PHP est le fait que les "objets sont passés par référence par défaut". Ce n'est pas complètement vrai. Cette section rectifie cette généralisation avec quelques exemples.

Une référence PHP est un alias, qui permet à deux variables différentes de représenter la même valeur. Dans PHP, une variable objet ne contient plus l'objet en lui-même comme valeur. Elle contient seulement un identifiant d'objet, qui permet aux accesseurs d'objets de trouver cet objet. Lorsque l'objet est utilisé comme argument, retourné par une fonction, ou assigné à une autre variable, les différentes variables ne sont pas des alias : elles contiennent des copies de l'identifiant, qui pointent sur le même objet.

exemple :

```php
<?php
class A {
    public $foo = 1;
}  

$a = new A;
// $a et $b sont des copies du même identifiant
// ($a) = ($b) = <id>
$b = $a;
$b->foo = 2;
echo($a->foo."\n");


$c = new A;
// $c et $d sont des références
// ($c,$d) = <id>
$d = &$c;

$d->foo = 2;
echo($c->foo."\n");


$e = new A;

function foo($obj) {
    // ($obj) = ($e) = <id>
    $obj->foo = 2;
}

foo($e);
echo($e->foo."\n");

?>
```

L'exemple ci-dessus va afficher :

```php
2
2
2
```

# Contenu de ./0610 - Comparaison d'objets/content.md

Depuis PHP 5, la comparaison d'objets est plus complexe qu'en PHP 4, et plus proche du comportement que l'on pourrait attendre d'un langage orienté objet (sans aller jusqu'à dire que PHP 5 en soit un).

Lors de l'utilisation de l'opérateur de comparaison (==), les objets sont comparés de manière simple, à savoir : deux objets sont égaux s'ils ont les mêmes attributs et valeurs, et qu'ils sont des instances de la même classe.

D'un autre côté, lors de l'utilisation de l'opérateur d'identité (===), les objets sont identiques uniquement s'ils font référence à la même instance de la même classe.

Exemple :

```php
<?php
function bool2str($bool)
{
	if ($bool === false) {
		return 'FALSE';
	} else {
		return 'TRUE';
	}
}

function compareObjects(&$o1, &$o2)
{
	echo('o1 == o2 : '.bool2str($o1 == $o2)."\n");
	echo('o1 != o2 : '.bool2str($o1 != $o2)."\n");
	echo('o1 === o2 : '.bool2str($o1 === $o2)."\n");
	echo('o1 !== o2 : '.bool2str($o1 !== $o2)."\n");
}

class Flag
{
	public $flag;

	function Flag($flag = true) {
		$this->flag = $flag;
	}
}

class OtherFlag
{
	public $flag;

	function OtherFlag($flag = true) {
		$this->flag = $flag;
	}
}

$o = new Flag();
$p = new Flag();
$q = $o;
$r = new OtherFlag();

echo("Deux instances de la même classe\n");
compareObjects($o, $p);

echo("\nDeux références sur le même objet\n");
compareObjects($o, $q);

echo("\nInstances de classes différentes\n");
compareObjects($o, $r);
?>
```

L'exemple ci-dessus va afficher :

```php
Deux instances de la même classe
o1 == o2 : TRUE
o1 != o2 : FALSE
o1 === o2 : FALSE
o1 !== o2 : TRUE

Deux références sur le même objet
o1 == o2 : TRUE
o1 != o2 : FALSE
o1 === o2 : TRUE
o1 !== o2 : FALSE

Instances de classes différentes
o1 == o2 : FALSE
o1 != o2 : TRUE
o1 === o2 : FALSE
o1 !== o2 : TRUE
```

# Contenu de ./0620 - Itération d'objets/content.md

Depuis PHP 5, il est possible d'itérer dans la liste de tous les éléments visibles d'un objet. L'itération peut être effectuée en utilisant la boucle foreach ainsi que l'interface iterator. Il existe également une interface IteratorAggregate en PHP, qui peut être utilisée dans ce but.

## Utilisation de la boucle foreach

### Exemple

```php
<?php
class myclass{
   private $var;
   protected $var1;
   public $x, $y, $z;
   public function __construct(){
      $this->var="private variable";
      $this->var1=TRUE;
      $this->x=100;
      $this->y=200;
      $this->z=300;
   }
   public function iterate(){
      foreach ($this as $key => $value) {
         print("$key => $value\n");
      }
   }
}
$obj = new myclass();
foreach($obj as $key => $value) {
   print("$key => $value\n");
}
echo("\n");
$obj->iterate();
?>
```

### Réponse

La réponse est la suivante :

```php
x => 100
y => 200
z => 300

var => private variable
var1 => 1
x => 100
y => 200
z => 300
```

## Utilisation de l'interface Iterator

Cette interface définit les méthodes abstraites suivantes qui seront implémentées dans l'exemple suivant :

```php
abstract public current ( void ) : mixed
abstract public key ( void ) : scalar
abstract public next ( void ) : void
abstract public rewind ( void ) : void
abstract public valid ( void ) : bool
```

- ```Iterator::current``` : Retourne l'élément courant
- ```Iterator::key``` : Retourne la clé de l'élément courant
- ```Iterator::next``` : Passer à l'élément suivant
- ```Iterator::rewind``` : Rembobine l’itérateur jusqu'au premier élément
- ```Iterator::valid``` : Vérifie si la position actuelle est valide

L'exemple suivant démontre l'itération d'objets en implémentant l'interface Iterator.

### Exemple

```php
<?php
class myclass implements Iterator{
   private $arr = array('a','b','c');
   public function rewind(){
      echo("rewinding\n");
      reset($this->arr);
   }
   public function current(){
      $var = current($this->arr);
      echo("current: $var\n");
      return $var;
   }
   public function key() {
      $var = key($this->arr);
      echo("key: $var\n");
      return $var;
   }
   public function next() {
      $var = next($this->arr);
      echo("next: $var\n");
      return $var;
   }
   public function valid(){
      $key = key($this->arr);
      $var = ($key !== NULL && $key !== FALSE);
      echo("valid: $var\n");
      return $var;
   }
}
$obj = new myclass();
foreach ($obj as $k => $v) {
   print("$k: $v\n");
}
?>
```

### Réponse

Le code ci-dessus produit le résultat suivant :

```php
rewinding
valid: 1
current: a
key: 0
0: a
next: b
valid: 1
current: b
key: 1
1: b
next: c
valid: 1
current: c
key: 2
2: c
next:
valid:
```

# Contenu de ./0630 - Interfaces/content.md

Les interfaces vous permettent de spécifier les méthodes qu'une classe doit implémenter.

Les interfaces facilitent l'utilisation d'une variété de classes différentes de la même manière. Lorsqu'une ou plusieurs classes utilisent la même interface, on parle de « polymorphisme ».

Les interfaces sont déclarées avec le mot-clé ```interface``` :

syntaxe :

```php
<?php
interface InterfaceName {
  public function someMethod1();
  public function someMethod2($name, $color);
  public function someMethod3() : string;
}
?>
```

## Interface vs Classes abstraites

L'interface est similaire aux classes abstraites. Les différences entre les interfaces et les classes abstraites sont :

- Les interfaces ne peuvent pas avoir de propriétés, tandis que les classes abstraites peuvent
- Toutes les méthodes d'interface doivent être publiques, tandis que les méthodes de classe abstraites sont publiques ou protégées
- Toutes les méthodes d'une interface sont abstraites, elles ne peuvent donc pas être implémentées dans le code et le mot-clé abstract n'est pas nécessaire
- Les classes peuvent implémenter une interface tout en héritant d'une autre classe en même temps

## Utilisation des interfaces

Pour implémenter une interface, une classe doit utiliser le “implements” mot - clé.
Une classe qui implémente une interface doit implémenter toutes les méthodes de l'interface.

Exemple :

```php
<?php
interface Animal {
  public function makeSound();
}

class Cat implements Animal {
  public function makeSound() {
    echo("Meow");
  }
}

$animal = new Cat();
$animal->makeSound();
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
Meow
```

A partir de l'exemple ci-dessus, disons que nous aimerions écrire un logiciel qui gère un groupe d'animaux. Il y a des actions que tous les animaux peuvent faire, mais chaque animal le fait à sa manière.

En utilisant des interfaces, nous pouvons écrire du code qui peut fonctionner pour tous les animaux même si chaque animal se comporte différemment :

```php
<?php
interface Animal {
  public function makeSound();
}

class Cat implements Animal {
  public function makeSound() {
    echo(" Meow ");
  }
}

class Dog implements Animal {
  public function makeSound() {
    echo(" Bark ");
  }
}

class Mouse implements Animal {
  public function makeSound() {
    echo(" Squeak ");
  }
}

$cat = new Cat();
$dog = new Dog();
$mouse = new Mouse();
$animals = array($cat, $dog, $mouse);

foreach($animals as $animal) {
  $animal->makeSound();
}
?>
```

Dans cet exemple, le résultat renvoyé est :

```php
Meow Bark Squeak
```

Chat, Chien et Souris sont toutes des classes qui implémentent l'interface Animal, ce qui signifie qu'elles sont toutes capables de faire un son en utilisant la ```makeSound()``` méthode. Pour cette raison, nous pouvons parcourir tous les animaux et leur dire de faire un son même si nous ne savons pas de quel type d'animal il s'agit.

Comme l'interface ne dit pas aux classes comment implémenter la méthode, chaque animal peut émettre un son à sa manière.

# Contenu de ./0640 - PSR 07 - HTTP Message Interface/content.md

Les messages HTTP sont à la base du développement Web. Les navigateurs Web et les clients HTTP tels que cURL créent des messages de requête HTTP qui sont envoyés à un serveur Web, qui fournit un message de réponse HTTP. Le code côté serveur reçoit un message de requête HTTP et renvoie un message de réponse HTTP.

Les messages HTTP sont généralement extraits du consommateur final, mais en tant que développeurs, nous avons généralement besoin de savoir comment ils sont structurés et comment y accéder ou les manipuler afin d'effectuer nos tâches, qu'il s'agisse de faire une demande à une API HTTP. , ou le traitement d'une demande entrante.

Chaque message de requête HTTP a une forme spécifique :

```http
POST /path HTTP/1.1
Host: example.com

foo=bar&baz=bat
```

La première ligne d'une requête est la « ligne de requête » et contient, dans l'ordre, la méthode de requête HTTP, la cible de la requête (généralement un URI absolu ou un chemin sur le serveur Web) et la version du protocole HTTP. Ceci est suivi d'un ou plusieurs en-têtes HTTP, d'une ligne vide et du corps du message.

Les messages de réponse HTTP ont une structure similaire :

```http
HTTP/1.1 200 OK
Content-Type: text/plain
```

La première ligne est la “ligne d'état” et contient, dans l'ordre, la version du protocole HTTP, le code d'état HTTP et une "phrase de raison", une description lisible par l'homme du code d'état. Comme le message de requête, il est ensuite suivi d'un ou plusieurs en-têtes HTTP, d'une ligne vide et du corps du message.

Les interfaces décrites dans ce document sont des abstractions autour des messages HTTP et des éléments qui les composent.

## Les messages

Un message HTTP est soit une requête d'un client à un serveur, soit une réponse d'un serveur à un client. Cette spécification définit les interfaces pour les messages HTTP ```Psr\Http\Message\RequestInterface``` et ```Psr\Http\Message\ResponseInterface``` respectivement.

Les deux ```Psr\Http\Message\RequestInterface``` et ```Psr\Http\Message\ResponseInterface``` étendent ```Psr\Http\Message\MessageInterface```. Bien que ```Psr\Http\Message\MessageInterface``` peuvent être implémentés directement, les implémenteurs doivent être implémenter ```Psr\Http\Message\RequestInterface``` et ```Psr\Http\Message\ResponseInterface```.

À partir de maintenant, l'espace de noms ```Psr\Http\Message``` sera omis lors de la référence à ces interfaces.

## Les en-têtes

Les messages HTTP incluent des noms de champs d'en-tête insensibles à la casse. Les en-têtes sont récupérés par nom à partir des classes implémentant le ```MessageInterface``` d'une manière insensible à la casse. Par exemple, la récupération de l'en-tête ```Foo``` renverra le même résultat que la récupération de l'en-tête ```Foo```. De même, la définition de l'en-tête ```Foo``` écrasera toute valeur d'en-tête précédemment définie.

exemple :

```php
$message = $message->withHeader('foo', 'bar');

echo($message->getHeaderLine('foo'));

echo($message->getHeaderLine('FOO'));

$message = $message->withHeader('fOO', 'baz');
echo($message->getHeaderLine('foo'));
```

Bien que les en-têtes puissent être récupérés sans tenir compte de la casse, la casse d'origine doit être préservée par la mise en œuvre, en particulier lorsqu'elle est récupérée avec ```getHeaders()```.

Les applications HTTP non conformes peuvent dépendre d'un certain cas, il est donc utile pour un utilisateur de pouvoir dicter la casse des en-têtes HTTP lors de la création d'une demande ou d'une réponse.

Afin de prendre en charge les en-têtes avec plusieurs valeurs tout en offrant la commodité de travailler avec des en-têtes sous forme de chaînes, les en-têtes peuvent être récupérés à partir d'une instance de a ```MessageInterface``` sous forme de tableau ou de chaîne. Utilisez la ```getHeaderLine()``` méthode pour récupérer une valeur d'en-tête sous forme de chaîne contenant toutes les valeurs d'en-tête d'un en-tête insensible à la casse par nom concaténé avec une virgule. Utilisez ```getHeader()``` pour récupérer un tableau de toutes les valeurs d'en-tête pour un en-tête particulier insensible à la casse par nom.

exemple :

```php
$message = $message
    ->withHeader('foo', 'bar')
    ->withAddedHeader('foo', 'baz');

$header = $message->getHeaderLine('foo');

$header = $message->getHeader('foo');
```

Remarque : toutes les valeurs d'en-tête ne peuvent pas être concaténées à l'aide d'une virgule (par exemple, ```Set-Cookie```). Lorsqu'ils travaillent avec de tels en-têtes, les consommateurs des classes basées sur ```MessageInterface``` devraient s'appuyer sur la méthode ```getHeader()``` pour récupérer ces en-têtes à valeurs multiples.

Dans les requêtes, l'en-tête reflète généralement le composant hôte de l'URI, ainsi que l'hôte utilisé lors de l'établissement de la connexion TCP. Cependant, la spécification HTTP permet à l'en-tête de différer de chacun des deux.

Pendant la construction, les mises en œuvre doivent tenter de définir l'en-tête à partir d'un URI fourni si aucun en-tête n'est fourni.

```RequestInterface::withUri()``` remplacera, par défaut, l'en-tête de la requête envoyée par un en-tête correspondant au composant hôte du fichier ```UriInterface```.

Vous pouvez choisir de conserver l'état d'origine de l'en-tête en passant ```true``` en deuxième argument (```$preserveHost```). Lorsque cet argument est défini à “true”, la demande renvoyée ne mettra pas à jour l'en-tête du message renvoyé, à moins que le message ne contient aucun en-tête.

Les messages HTTP se composent d'une ligne de départ, d'en-têtes et d'un corps. Le corps d'un message HTTP peut être très petit ou extrêmement grand. Tenter de représenter le corps d'un message sous forme de chaîne peut facilement consommer plus de mémoire que prévu, car le corps doit être entièrement stocké en mémoire. Tenter de stocker le corps d'une demande ou d'une réponse en mémoire empêcherait l'utilisation de cette implémentation de pouvoir travailler avec des corps de message volumineux. ```StreamInterface``` est utilisé afin de masquer les détails de l'implémentation lorsqu'un flux de données est lu ou écrit. Pour les situations où une chaîne serait une implémentation de messages appropriés, des flux intégrés tels que ```php://memory``` et ```php://temp``` peuvent être utilisés.

```StreamInterface``` expose plusieurs méthodes qui permettent de lire, d'écrire et de traverser efficacement les flux.

Les flux exposent leurs capacités à l'aide de trois méthodes : ```isReadable()```, ```isWritable()```, et ```isSeekable()```. Ces méthodes peuvent être utilisées par les collaborateurs du flux pour déterminer si un flux est capable de répondre à leurs besoins.

Chaque instance de flux aura différentes capacités : elle peut être en lecture seule, en écriture seule ou en lecture-écriture. Il peut également autoriser un accès aléatoire arbitraire (recherche vers l'avant ou l'arrière vers n'importe quel emplacement), ou uniquement un accès séquentiel (par exemple dans le cas d'un socket, d'un tuyau ou d'un flux basé sur un rappel).

Enfin, ```StreamInterface``` définit une ```__toString()``` méthode pour simplifier la récupération ou l'émission de tout le contenu du corps à la fois.

Contrairement aux interfaces de requête et de réponse, ```StreamInterface``` ne modélise pas l'immuabilité. Dans les situations où un flux PHP réel est encapsulé, l'immuabilité est impossible à appliquer, car tout code qui interagit avec la ressource peut potentiellement changer son état (y compris la position du curseur, le contenu, etc.). Notre recommandation est que les implémentations utilisent des flux en lecture seule pour les demandes côté serveur et les réponses côté client. Les consommateurs doivent être conscients du fait que l'instance de flux peut être modifiable et, en tant que telle, pourrait modifier l'état du message ; en cas de doute, créez une nouvelle instance de flux et attachez-la à un message pour appliquer l'état.

## Les cibles de requête et URI

Selon la RFC 7230, les messages de demande contiennent une « cible de demande » comme deuxième segment de la ligne de demande. La cible de la demande peut être l'une des formes suivantes :

- **origin-form**, qui se compose du chemin et, le cas échéant, de la chaîne de requête ; c'est ce qu'on appelle souvent une URL relative. Les messages tels qu'ils sont transmis sur TCP sont généralement de la forme d'origine ; les données de schéma et d'autorité ne sont généralement présentes que via les variables CGI.
- **absolute-form**, qui comprend le schéma, l'autorité (```[user-info@]host[:port]```, où les éléments entre crochets sont facultatifs), le chemin (le cas échéant), la chaîne de requête (le cas échéant) et le fragment ( si présent). Il s'agit souvent d'un URI absolu, et c'est le seul formulaire permettant de spécifier un URI tel que détaillé dans la RFC 3986. Ce formulaire est couramment utilisé lors des demandes de proxy HTTP.
- **author-form**, qui se compose uniquement de l'autorité. Ceci est généralement utilisé dans les requêtes CONNECT uniquement, pour établir une connexion entre un client HTTP et un serveur proxy.
- **asterisk-form**, qui se compose uniquement de la chaîne ```*```, et qui est utilisé avec la méthode OPTIONS pour déterminer les capacités générales d'un serveur Web.

En dehors de ces cibles de requête, il existe souvent une « URL effective » qui est distincte de la cible de la requête. L'URL effective n'est pas transmise dans un message HTTP, mais elle est utilisée pour déterminer le protocole (http / https), le port et le nom d'hôte pour effectuer la demande.

L'URL effective est représentée par” UriInterface”. “UriInterface” modélise les URI HTTP et HTTPS comme spécifié dans la RFC 3986 (le cas d'utilisation principal). L'interface fournit des méthodes pour interagir avec les différentes parties d'URI, ce qui évitera le besoin d'analyses répétées de l'URI. Il spécifie également une ```__toString()``` méthode pour convertir l'URI modélisé en sa représentation sous forme de chaîne.

Lors de la récupération de la cible de la requête avec ```getRequestTarget()```, cette méthode utilisera par défaut l'objet URI et ensuite il extrait tous les composants nécessaires pour construire la forme d'origine . Le formulaire d'origine est de loin la cible de requête la plus courante.

Si un utilisateur final souhaite utiliser l'une des trois autres formes, ou si l'utilisateur souhaite explicitement écraser la cible de la requête, il est possible de le faire avec ```withRequestTarget()```.

L'appel de cette méthode n'affecte pas l'URI, car il est renvoyé par ```getUri()```.

Par exemple, un utilisateur peut souhaiter envoyer une requête sous forme d'astérisque à un serveur :

```php
$request = $request
    ->withMethod('OPTIONS')
    ->withRequestTarget('*')
    ->withUri(new Uri('https://example.org/'));
```

Cet exemple peut finalement aboutir à une requête HTTP qui ressemble à ceci :

```http
OPTIONS * HTTP/1.1
```

Mais le client HTTP pourra utiliser l'URL effective (de “getUri()”), pour déterminer le protocole, le nom d'hôte et le port TCP.

Un client HTTP soit ignorer les valeurs de ```Uri::getPath()``` et ```Uri::getQuery()```, et utiliser à la place la valeur renvoyée par ```getRequestTarget()```, qui par défaut concaténera ces deux valeurs.

Les clients qui choisissent de ne pas implémenter 1 ou plusieurs des 4 formulaires cible de demande, doivent toujours utiliser ```getRequestTarget()```. Ces clients doivent rejeter les cibles de demande qu'ils ne prennent pas en charge, et ne doivent pas se rabattre sur les valeurs de ```getUri()```.

```RequestInterface``` fournit des méthodes pour récupérer la cible de requête ou créer une nouvelle instance avec la cible de requête fournie. Par défaut, si aucune requête-cible n'est spécifiquement composée dans l'instance, ```getRequestTarget()``` renverra la forme d'origine de l'URI composé (ou "/" si aucun URI n'est composé). ```withRequestTarget($requestTarget)``` crée une nouvelle instance avec la cible de demande spécifiée et permet ainsi aux développeurs de créer des messages de demande qui représentent les trois autres formes de cible de demande (forme absolue, forme d'autorité et forme astérisque). Lorsqu'elle est utilisée, l'instance d'URI composée peut toujours être utile, en particulier chez les clients, où elle peut être utilisée pour créer la connexion au serveur.

## Les requêtes côté serveur

```RequestInterface``` fournit la représentation générale d'un message de requête HTTP. Cependant, les demandes côté serveur nécessitent un traitement supplémentaire, en raison de la nature de l'environnement côté serveur. Le traitement côté serveur doit prendre en compte la Common Gateway Interface (CGI) et, plus précisément, l'abstraction et l'extension de CGI par PHP via ses API de serveur (SAPI). PHP a fourni une simplification autour du marshaling d'entrée via des superglobaux tels que :

- ```$_COOKIE```, qui désérialise et fournit un accès simplifié aux cookies HTTP.
- ```$_GET```, qui désérialise et fournit un accès simplifié aux arguments de chaîne de requête.
- ```$_POST```, qui désérialise et fournit un accès simplifié pour les paramètres codés en URL soumis via HTTP POST ; de manière générique, il peut être considéré comme le résultat de l'analyse du corps du message.
- ```$_FILES```, qui fournit des métadonnées sérialisées autour des téléchargements de fichiers.
- ```$_SERVER```, qui permet d'accéder aux variables d'environnement CGI/SAPI, qui incluent généralement la méthode de requête, le schéma de requête, l'URI de requête et les en-têtes.

```ServerRequestInterface``` s'étend ```RequestInterface``` pour fournir une abstraction autour de ces différents superglobaux. Cette pratique permet de réduire le couplage aux superglobales par les consommateurs et encourage et promeut la capacité de tester les consommateurs à la demande.

La demande du serveur fournit une propriété supplémentaire, "attributs", pour permettre aux consommateurs de décomposer et de faire correspondre la demande à des règles spécifiques à l'application (telles que la correspondance de chemin, la correspondance de schéma, la correspondance d'hôte, etc.). En tant que telle, la demande de serveur peut également fournir une messagerie entre plusieurs consommateurs de demande.

## Les fichiers téléchargés

```ServerRequestInterface``` spécifie une méthode pour récupérer une arborescence de fichiers de téléchargement dans une structure normalisée, avec chaque feuille une instance de ```UploadedFileInterface```.

Le ```$_FILES``` superglobal a des problèmes bien connus lorsqu'il traite des tableaux d'entrées de fichiers. Par exemple, si vous avez un formulaire qui soumet un tableau de fichiers - par exemple, le nom d'entrée "files", soumettre ```files[0]``` et ```files[1]``` - PHP le représentera comme :

```php
array(
    'files' => array(
        'name' => array(
            0 => 'file0.txt',
            1 => 'file1.html',
        ),
        'type' => array(
            0 => 'text/plain',
            1 => 'text/html',
        ),
    ),
)
```

Au lieu de l’attendu :

```php
array(
    'files' => array(
        0 => array(
            'name' => 'file0.txt',
            'type' => 'text/plain',
        ),
        1 => array(
            'name' => 'file1.html',
            'type' => 'text/html',
        ),
    ),
)
```

Le résultat est que les consommateurs ont besoin de connaître ces détails d'implémentation du langage et d'écrire du code pour collecter les données pour un téléchargement donné.

De plus, il existe des scénarios où ```$_FILES``` n'est pas renseigné lorsque des téléchargements de fichiers se produisent :

- Lorsque la méthode HTTP n'est pas “POST”.
- Lors des tests unitaires.
- Lorsque vous travaillez dans un environnement non SAPI, tel que ReactPHP.

Dans de tels cas, les données devront être ensemencées différemment. A titre d'exemples :

- Un processus peut analyser le corps du message pour découvrir les téléchargements de fichiers. Dans de tels cas, l'implémentation peut choisir de ne pas écrire les téléchargements de fichiers dans le système de fichiers, mais de les envelopper dans un flux afin de réduire la mémoire, les E/S et la surcharge de stockage.
- Dans les scénarios de test unitaire, les développeurs doivent être en mesure de stub et/ou de simuler les métadonnées de téléchargement de fichier afin de valider et de vérifier différents scénarios.

```getUploadedFiles()``` fournit la structure normalisée pour les consommateurs. Les implémentations devraient :

- Regroupez toutes les informations pour un téléchargement de fichier donné et utilisez-les pour remplir une ```Psr\Http\Message\UploadedFileInterface``` instance.
- Recréez la structure arborescente soumise, chaque feuille étant l' ```Psr\Http\Message\UploadedFileInterface``` instance appropriée pour l'emplacement donné dans l'arborescence.

L'arborescence référencée doit imiter la structure de nommage dans laquelle les fichiers ont été soumis.

Dans l'exemple le plus simple, il peut s'agir d'un seul élément de formulaire nommé soumis en tant que :

``` html
<input type="file" name="avatar" />
```

Dans ce cas, la structure dans ```$_FILES``` ressemblerait à :

```php
array(
    'avatar' => array(
        'tmp_name' => 'phpUxcOty',
        'name' => 'my-avatar.png',
        'size' => 90996,
        'type' => 'image/png',
        'error' => 0,
    ),
)
```

La forme normalisée renvoyée par ```getUploadedFiles()``` serait :

```php
array(
    'avatar' => /* UploadedFileInterface instance */
)
```

Dans le cas d'une entrée utilisant la notation matricielle pour le nom :

``` html
<input type="file" name="my-form[details][avatar]" />
```

```$_FILES``` finit par ressembler à ça :

```php
array (
    'my-form' => array (
        'name' => array (
            'details' => array (
                'avatar' => 'my-avatar.png',
            ),
        ),
        'type' => array (
            'details' => array (
                'avatar' => 'image/png',
            ),
        ),
        'tmp_name' => array (
            'details' => array (
                'avatar' => 'phpmFLrzD',
            ),
        ),
        'error' => array (
            'details' => array (
                'avatar' => 0,
            ),
        ),
        'size' => array (
            'details' => array (
                'avatar' => 90996,
            ),
        ),
    ),
)
```

Et l'arbre correspondant renvoyé par ```getUploadedFiles()``` devrait être :

```php
array(
    'my-form' => array(
        'details' => array(
            'avatar' => /* UploadedFileInterface instance */
        ),
    ),
)
```

Dans certains cas, vous pouvez spécifier un tableau de fichiers :

``` html
<input type="file" name="my-form[details][avatars][]" />
<input type="file" name="my-form[details][avatars][]" />
```

(Par exemple, les contrôles JavaScript peuvent générer des entrées de téléchargement de fichiers supplémentaires pour permettre le téléchargement de plusieurs fichiers à la fois.)

Dans un tel cas, l'implémentation de la spécification doit agréger toutes les informations relatives au fichier à l'index donné. La raison en est que ```$_FILES``` s'écarte de sa structure normale dans de tels cas :

```php
array (
    'my-form' => array (
        'name' => array (
            'details' => array (
                'avatars' => array (
                    0 => 'my-avatar.png',
                    1 => 'my-avatar2.png',
                    2 => 'my-avatar3.png',
                ),
            ),
        ),
        'type' => array (
            'details' => array (
                'avatars' => array (
                    0 => 'image/png',
                    1 => 'image/png',
                    2 => 'image/png',
                ),
            ),
        ),
        'tmp_name' => array (
            'details' => array (
                'avatars' => array (
                    0 => 'phpmFLrzD',
                    1 => 'phpV2pBil',
                    2 => 'php8RUG8v',
                ),
            ),
        ),
        'error' => array (
            'details' => array (
                'avatars' => array (
                    0 => 0,
                    1 => 0,
                    2 => 0,
                ),
            ),
        ),
        'size' => array (
            'details' => array (
                'avatars' => array (
                    0 => 90996,
                    1 => 90996,
                    3 => 90996,
                ),
            ),
        ),
    ),
)
```

Le ```$_FILES``` tableau ci-dessus correspond à la structure suivante telle que renvoyée par ```getUploadedFiles()``` :

```php
array(
    'my-form' => array(
        'details' => array(
            'avatars' => array(
                0 => /* UploadedFileInterface instance */,
                1 => /* UploadedFileInterface instance */,
                2 => /* UploadedFileInterface instance */,
            ),
        ),
    ),
)
```

Les consommateurs accéderont à l'index 1 du tableau imbriqué en utilisant :

```php
$request->getUploadedFiles()['my-form']['details']['avatars'][1];
```

Étant donné que les données des fichiers téléchargés sont dérivées (dérivées de ```$_FILES``` ou du corps de la requête), une méthode de mutateur, ```withUploadedFiles()```, est également présente dans l'interface, permettant la délégation de la normalisation à un autre processus.

Dans le cas des exemples originaux, la consommation ressemble à ce qui suit :

```php
$file0 = $request->getUploadedFiles()['files'][0];
$file1 = $request->getUploadedFiles()['files'][1];

printf(
    $file0->getClientFilename(),
    $file1->getClientFilename()
);
```

Cette proposition reconnaît également que les mises en œuvre peuvent fonctionner dans des environnements non SAPI. En tant que tel, “UploadedFileInterface” fournit des méthodes pour garantir que les opérations fonctionnent quel que soit l'environnement. En particulier :

- ```moveTo($targetPath)``` est fourni comme une alternative sûre et recommandée à l'appel ```move_uploaded_file()``` direct sur le fichier de téléchargement temporaire. Les implémentations détectent l'opération correcte à utiliser en fonction de l'environnement.
- ```getStream()``` retournera une instance de ```StreamInterface```. Dans les environnements non SAPI, une possibilité proposée est d'analyser les fichiers de téléchargement individuels dans des flux ```php://temp``` au lieu de directement dans des fichiers ; dans de tels cas, aucun fichier de téléchargement n'est présent. ```getStream()``` est donc garanti de fonctionner quel que soit l'environnement.

A titre d'exemple :

```php
$filename = sprintf(
    '%s.%s',
    create_uuid(),
    pathinfo($file0->getClientFilename(), PATHINFO_EXTENSION)
);
$file0->moveTo(DATA_DIR . '/' . $filename);

$stream = new Psr7StreamWrapper($file1->getStream());
stream_copy_to_stream($stream, $s3wrapper);
```

## Les interfaces

“MessageInterface” :

```php
<?php
namespace Psr\Http\Message;

interface MessageInterface
{
    /**
     * @return string
     */
    public function getProtocolVersion();

    /**
     * @param string
     * @return static
     */
    public function withProtocolVersion($version);

    /**
     * @return string[]
     */
    public function getHeaders();

    /**
     * @param string $name
     * @return bool
     */
    public function hasHeader($name);

    /**
     * @param string $name 
     * @return string[]
     */
    public function getHeader($name);

    /**
     * @param string $name 
     * @return string
     */
    public function getHeaderLine($name);

    /**
     * @param string $name
     * @param string|string[]
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withHeader($name, $value);

    /**
     * @param string $name
     * @param string|string[] 
     * @return static
     * @throws \InvalidArgumentException
     * @throws \InvalidArgumentException
     */
    public function withAddedHeader($name, $value);

    /**
     * @param string $name
     * @return static
     */
    public function withoutHeader($name);

    /**
     * @return StreamInterface Returns the body as a stream.
     */
    public function getBody();

    /**
     * @param StreamInterface $body Body.
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withBody(StreamInterface $body);
}
```

“RequestInterface” :

```php
<?php
namespace Psr\Http\Message;

interface RequestInterface extends MessageInterface
{
    /**
     * @return string
     */
    public function getRequestTarget();

    /**
     * @param mixed $requestTarget
     * @return static
     */
    public function withRequestTarget($requestTarget);

    /**
     * @return string
     */
    public function getMethod();

    /**
     * @param string $method
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withMethod($method);

    /**
     * @return UriInterface 
     */
    public function getUri();

    /**
     * @param UriInterface $uri
     * @param bool $preserveHost
     * @return static
     */
    public function withUri(UriInterface $uri, $preserveHost = false);
}
```

“ServerRequestInterface” :

```php
<?php
namespace Psr\Http\Message;

interface ServerRequestInterface extends RequestInterface
{
    /**
     * @return array
     */
    public function getServerParams();

    /**
     * @return array
     */
    public function getCookieParams();

    /**
     * @param array $cookies
     * @return static
     */
    public function withCookieParams(array $cookies);

    /**
     * @return array
     */
    public function getQueryParams();

    /**
     * @param array $query
     * @return static
     */
    public function withQueryParams(array $query);

    /**
     * @return array
     */
    public function getUploadedFiles();

    /**
     * @param array
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withUploadedFiles(array $uploadedFiles);

    /**
     * @return null|array|object
     */
    public function getParsedBody();

    /**
     * @param null|array|object
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withParsedBody($data);

    /**
     * @return mixed[] 
     */
    public function getAttributes();

    /**
     * @param string $name
     * @param mixed $default
     * @return mixed
     */
    public function getAttribute($name, $default = null);

    /**
     * @param string $name
     * @param mixed $value
     * @return static
     */
    public function withAttribute($name, $value);

    /**
     * @param string $name
     * @return static
     */
    public function withoutAttribute($name);
}
```

“ResponseInterface” :

```php
<?php
namespace Psr\Http\Message;

interface ResponseInterface extends MessageInterface
{
    /**
     * @return int
     */
    public function getStatusCode();

    /**
     * @param int $code
     * @param string $reasonPhrase
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withStatus($code, $reasonPhrase = '');

    /**
     * @return string
     */
    public function getReasonPhrase();
}
```

“StreamInterface” :

```php
<?php
namespace Psr\Http\Message;

interface StreamInterface
{
    /**
     * @return string
     */
    public function __toString();

    /**
     * @return void
     */
    public function close();

    /**
     * @return resource|null
     */
    public function detach();

    /**
     * @return int|null
     */
    public function getSize();

    /**
     * @return int
     * @throws \RuntimeException
     */
    public function tell();

    /**
     * @return bool
     */
    public function eof();

    /**
     * @return bool
     */
    public function isSeekable();

    /**
     * @param int $offset
     * @param int $whence
     * @throws \RuntimeException
     */
    public function seek($offset, $whence = SEEK_SET);

    /**
     * @throws \RuntimeException
     */
    public function rewind();

    /**
     * @return bool
     */
    public function isWritable();

    /**
     * @param string $string
     * @return int
     * @throws \RuntimeException
     */
    public function write($string);

    /**
     * @return bool
     */
    public function isReadable();

    /**
     * @param int $length
     * @return string
     * @throws \RuntimeException
     */
    public function read($length);

    /**
     * @return string
     * @throws \RuntimeException
     * @throws \RuntimeException 
     */
    public function getContents();

    /**
     * @param string $key
     * @return array|mixed|null
     */
    public function getMetadata($key = null);
}
```

“UriInterface” :

```php
<?php
namespace Psr\Http\Message;

interface UriInterface
{
    /**
     * @return string
     */
    public function getScheme();

    /**
     * @return string
     */
    public function getAuthority();

    /**
     * @return string
     */
    public function getUserInfo();

    /**
     * @return string
     */
    public function getHost();

    /**
     * @return null|int
     */
    public function getPort();

    /**
     * @return string
     */
    public function getPath();

    /**
     * @return string
     */
    public function getQuery();

    /**
     * @return string
     */
    public function getFragment();

    /**
     * @param string $scheme
     * @return static
     * @throws \InvalidArgumentException
     * @throws \InvalidArgumentException
     */
    public function withScheme($scheme);

    /**
     * @param string $user
     * @param null|string $password
     * @return static
     */
    public function withUserInfo($user, $password = null);

    /**
     * @param string $host
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withHost($host);

    /**
     * @param null|int $port
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withPort($port);

    /**
     * @param string $path
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withPath($path);

    /**
     * @param string $query
     * @return static
     * @throws \InvalidArgumentException
     */
    public function withQuery($query);

    /**
     * @param string $fragment
     * @return static 
     */
    public function withFragment($fragment);

    /**
     * @return string
     */
    public function __toString();
}
```

“UploadedFileInterface” :

```php
<?php
namespace Psr\Http\Message;

interface UploadedFileInterface
{
    /**
     * @return StreamInterface
     * @throws \RuntimeException
     * @throws \RuntimeException
     */
    public function getStream();

    /**
     * @param string $targetPath
     * @throws \InvalidArgumentException
     * @throws \RuntimeException 
     * @throws \RuntimeException
     */
    public function moveTo($targetPath);

    /**
     * @return int|null
     */
    public function getSize();

    /**
     * @return int
     */
    public function getError();

    /**
     * @return string|null
     */
    public function getClientFilename();

    /**
     * @return string|null
     */
    public function getClientMediaType();
}
```

# Contenu de ./0650 - PSR 11 - Container Interface/content.md

## Objectif du PSR 11

L’objectif du PSR 11 est de créer une interface commune pour les conteneurs d’injection de dépendances et de standardiser la façon dont les frameworks et les librairies l’utilisent. Le conteneur de dépendances est utilisé pour obtenir des objets en paramètre d’entrée d'une fonction.

L’```implementor``` dans ce cours doit être interprété comme quelque chose qui implémente le ```ContainerInterface``` dans une librairie ou framework. Les utilisateurs de conteneur d’injection de dépendances (DIC) sont appelés “user”.

## Identifiant d’entrée

Un identifiant d’entrée est une chaîne d’au moins 1 caractère qui identifie de manière unique un élément dans un conteneur. Un identifiant d’entrée est une chaîne opaque, donc les appelants ne devraient pas supposer que la structure de la chaîne porte une quelconque signification sémantique.

## Lecture d’un conteneur

Le ```Psr\Container\ContainerInterface``` expose 2 méthodes qui sont ```get``` et ```has```.

```get``` prend un identifiant d’entrée en paramètre, qui doit être une chaîne de caractère, ```get``` peut renvoyer n’importe quelle valeur ou lancer une ```NotFoundExeptionInterface``` si l'identifiant connu du conteneur fait 2 appels successifs à ```get``` avec le même identifiant, ce qui devrait retourner la même valeur. Cependant, selon l’```implementor``` conception et/ou la “user” configuration, des valeurs différentes peuvent être retournées, donc “user” ne doit pas compter sur l’obtention de la même valeur sur 2 appels successifs.

```has``` prend un identifiant d’entrée en paramètre, qui doit être une chaîne de caractère, ```has``` retourne “true” si l'identifiant d’entrée est connu de conteneur ou alors ```has``` renvoie “false” s’il ne l’est pas. Si ```has($id)``` renvoie false alors ```get($id)``` lance une ```NotFoundExceptionInterface```.

## Les exceptions

Les exceptions directement levées par le conteneur implémente le ```PSR\Container\ContainerExceptionInterface```. Un appel à la méthode ```get``` avec un identifiant existant doit lancer un ```Psr\Container\NotFoundExceptionInterface```.

## Les packages

Les interfaces et les classes ainsi que les exceptions sont fournies dans le cadre du package ```psr/container```. Les packages qui fournissent une implémentation de conteneur PSR doivent déclarer qu’ils fournissent des fichiers ```psr/container-implementation 1.0.0```.

## Les interfaces

Le ```Psr\Container\ContainerInterface``` :

```php
<?php
namespace Psr\Container;

/**
 * Décrit l’interface d’un container
 */
interface ContainerInterfaces
{
    /**
     * Recherche une entrée du container par son identifiant et la renvoie
     *
     * @param string $id Identifiant de l’entrée à rechercher
     *
     * @throws NotFoundExceptionInterface Aucune entrée trouvée
     * @throws ContainerExceptionInterface Erreur lors de la récupération de l’entrée
     *
     * @return mixed Entry.
     */
    public function get($id);

    /**
     * Returns true Si le container peut retourner une entrée pour l’identifiant donné
     * Returns false autrement
     *
     * `has($id)` retourne true ne signifie pas que `get($id)` ne lèvera pas d'exception
     * Cela signifie que `get($id)` ne lancera pas une `NotFoundExceptionInterface`.
     *
     * @param string $id Identifiant de l’entrée à rechercher
     *
     * @return bool
     */
    public function has($id);
}
?>
```

Le ```Psr\Container\ContainerExceptionInterface``` :

```php
<?php
namespace Psr\Container;

/**
 * Interface de base représentant une exception générique dans un container
 */
interface ContainerExceptionInterface
{
}
```

Le ```Psr\Container\NotFoundExceptionInterface``` :

```php
<?php
namespace Psr\Container;

/**
 * Aucune entrée n’a été trouvé dans le container
 */
interface NotFoundExceptionInterface extends ContainerExceptionInterface
{
}
```

# Contenu de ./0660 - Réfléxivité/content.md

Dans le développement de logiciels, le terme "réflexion" signifie qu'un programme connaît sa propre structure au moment de l'exécution et qu'il peut également la modifier. Cette capacité est également appelée "introspection". Dans le domaine PHP, Reflection est utilisé pour garantir la sécurité des types dans le code de programme.

## Exemple

Préparons une classe d'exemple simple :

```php
class Example {

	private $attribute1;

	protected $attribute2;

	public $attribute3;

	const PI = 3.1415;

	public function __construct() {
		$this->attribute1 = "Lorem ipsum";
		$this->attribute2 = 36;
		$this->attribute3 = 2 * self::PI;
	}


	public function getAttribute1() {
		return $this->attribute1;
	}
	
	public function setAttribute1($attribute1) {
		$this->attribute1 = $attribute1;
	}

	private function getAttribute2() {
		return $this->attribute2;
	}
	
}
```

Comme on peut le voir, cette classe d'exemple fournit quelques méthodes et attributs simples. Elle nous servira de point de départ dans les prochains exemples.

### Lister les méthodes d’un objet

Grâce à l'API Reflection, il est possible d'analyser les méthodes d’un objet depuis l'extérieur. Pour obtenir une liste complète des méthodes, ```Reflection()``` met à disposition la méthode statique ```getMethods()```.

```php
$reflection_class = new ReflectionClass("Example");

foreach ($reflection_class->getMethods() as $method) {
	echo($method->getName() . "\n"));
}
```

Le résultat est le suivant :

- ```__construct```
- ```getAttribute1```
- ```setAttribute1```
- ```getAttribute2```

La fonction ```ReflectionClass()``` n'attend comme paramètre que le nom complet de la classe à analyser (y compris le namespace, s'il existe). Pour rendre l'initialisation un peu plus agréable, on peut aussi utiliser directement la résolution du nom de classe de PHP :

```php
$reflection_class = new ReflectionClass( Example::class );
```

Outre les noms des méthodes, d'autres informations peuvent être lues :

```php
$reflection_class = new ReflectionClass( Example::class );

foreach ($reflection_class->getMethods() as $method) {
	echo($method->getName() . "\n");

	echo("Nombre de paramètres : " . $method->getNumberOfParameters() . "\n");
	echo("Est privé : " . ($method->isPrivate() ? 'Oui' : 'Non') . "\n\n");
}
```

Le résultat est le suivant :

- ```__construction```
    - Nombre de paramètres : 0
    - Est privé : Non
- ```getAttribute1```
    - Nombre de paramètres : 0
    - Est privé : Non
- ```setAttribute1```
    - Nombre de paramètres : 1
    - Est privé : Non
- ```getAttribute2```
    - Nombre de paramètres : 0
    - Est privé : Oui

### Lire les attributs

Le même comportement peut d'ailleurs être appliqué aux attributs. Au lieu de ```getMethods()```, on utilise simplement ```getProperties()```.

```php
$reflection_class = new ReflectionClass(Example::class);

foreach ($reflection_class->getProperties() as $property) {
    echo($property->getName() . "\n");

    echo("Est privé: " . ($property->isPrivate() ? 'Oui' : 'Non') . "\n\n");
}
```

Le résultat est ici comparable à celui des méthodes précédentes :

- ```attribut1```
    - Est privé : Oui
- ```attribut2```
    - Est privé : Non
- ```attribut3```
    - Est privé : Non

### Exécuter des méthodes à l'aide de Reflection

L'API de Reflection a d'ailleurs une particularité. Elle permet d'exécuter directement des méthodes privées, ce qui ne serait pas possible dans un contexte de programme normal.

```php
$object = new Example();

$reflection_object = new ReflectionObject($object);
$method = $reflection_object->getMethod("getAttribute1");

try {
	echo($method->invoke($object));
	
} catch (ReflectionException $e) {
	echo("Erreur !");
}
```

La chaîne de caractères "Lorem ipsum" est affichée. Cela est dû au fait que la méthode appelée ```getAttribute1()``` renvoie l'attribut ```attribute1```, qui a été initialisé avec cette chaîne dans le constructeur de la classe.

Comme on peut le voir, l'appel de cette méthode a fonctionné à merveille.

Essayons maintenant, dans l'étape suivante, d'appeler notre méthode privée ```getAttribute2()``` en indiquant dans ```getMethod()``` le nom de la méthode souhaitée :

```php
$object = new Example();

$reflection_object = new ReflectionObject($object);
$method = $reflection_object->getMethod("getAttribute2");

try {
	echo($method->invoke($object));
	
} catch (ReflectionException $e) {
	echo("Erreur !");
}
```

Le résultat est "Erreur !", comme défini dans notre gestion des exceptions. Comme prévu, cela est dû au fait que l'on ne peut pas accéder directement aux méthodes privées en dehors de la classe instanciée.

La méthode ```setAccessible()``` de l'API de Reflection est très utile dans ce cas.

```php
$object = new Example();

$reflection_object = new ReflectionObject($object);
$method = $reflection_object->getMethod("getAttribute2");

try {
	$method->setAccessible(true);
	echo($method->invoke($object));
	
} catch (ReflectionException $e) {
	echo("Erreur !");
}
```

Nous obtenons maintenant en sortie le nombre "36", tel que déclaré dans notre classe.

Avec ```setAccessible()```, le comportement privé de la méthode peut être désactivé pour la suite de son exécution.

Cependant, cela n'est pas très recommandé dans la pratique, car il y a généralement des raisons pour lesquelles certaines méthodes sont définies comme privées. Une utilisation possible de telles techniques pourrait par exemple être intéressante pour les tests unitaires.

## Autre exemple : objet d'entité avec remplissage automatique

Avec cet exemple, nous souhaitons vous montrer l'utilisation de l'API de Reflection dans la pratique. Pour illustrer cela, nous allons utiliser un objet d'entité, comme on le voit déjà dans de nombreux frameworks.

Pour cela, nous construisons d'abord un élément de base à partir duquel nous pouvons dériver nos entités individuelles. Nous partons du principe que chaque entité possède les attributs suivants (inspirés du framework Laravel) :

- id
- createdAt
- updatedAt
- deletedAt

```php
/**
 * Class BaseElement
 */
abstract class BaseElement {

	/**
	 * @var int $id
	 */
	private $id;

	/**
	 * @var \DateTime $createdAt
	 */
	private $createdAt;

	/**
	 * @var \DateTime $updatedAt
	 */
	private $updatedAt;

	/**
	 * @var \DateTime $deletedAt
	 */
	private $deletedAt;


	/**
	 * @var array
	 */
	private $_hidden = [ 'deleted_at' ];


	/**
	 * BaseElement constructor.
	 *
	 * @param array $data
	 */
	public function __construct( $data = null ) {
		
	}



	/**
	 * Returns the ID.
	 *
	 * @return int
	 */
	public function getId() {
		return $this->id;
	}


	/**
	 * Set the ID.
	 *
	 * @param int $id
	 */
	public function setId( int $id ) {
		$this->id = $id;
	}


	/**
	 * Returns the creation date.
	 *
	 * @return \DateTime
	 */
	public function getCreatedAt() {
		return $this->createdAt;
	}


	/**
	 * Set the creation date.
	 *
	 * @param \DateTime $createdAt
	 */
	public function setCreatedAt( $createdAt ) {
		$this->createdAt = $createdAt;
	}


	/**
	 * Returns the update date.
	 *
	 * @return \DateTime
	 */
	public function getUpdatedAt() {
		return $this->updatedAt;
	}


	/**
	 * Set the update date.
	 *
	 * @param \DateTime $updatedAt
	 */
	public function setUpdatedAt( $updatedAt ) {
		$this->updatedAt = $updatedAt;
	}


	/**
	 * Returns the delete date.
	 *
	 * @return \DateTime|null
	 */
	public function getDeletedAt() {
		return $this->deletedAt;
	}


	/**
	 * Set the delete date.
	 *
	 * @param \DateTime|null $deletedAt
	 */
	public function setDeletedAt( $deletedAt ) {
		$this->deletedAt = $deletedAt;
	}

}
```

### Mettre en œuvre le remplissage automatique

Nous avons maintenant une classe de base qui possède quatre attributs, avec les méthodes getter et setter correspondantes. Dans l'étape suivante, nous veillons à ce qu'un tableau de données puisse être transmis dans le constructeur, à l'aide duquel les méthodes Setter correspondantes seront automatiquement déterminées et exécutées.

Pour ce faire, nous écrivons deux classes Helper : l'une pour les opérations de chaînes de caractères concernant la conversion de et vers Camel-Case, et l'autre pour le Type-Casting :

```php
class StringHelper {

	/**
	 * Translates a camel case string into a string with
	 * underscores (e.g. firstName -> first_name)
	 *
	 * @param string $str String in camel case format
	 *
	 * @return string $str Translated into underscore format
	 */
	public static function fromCamelCase( $str ) {
		$str[0] = strtolower( $str[0] );
		$func   = create_function( '$c', 'return "_" . strtolower($c[1]);' );

		return preg_replace_callback( '/([A-Z])/', $func, $str );
	}

	/**
	 * Translates a string with underscores
	 * into camel case (e.g. first_name -> firstName)
	 *
	 * @param string $str String in underscore format
	 * @param bool $capitalise_first_char If true, capitalise the first char in $str
	 *
	 * @return string $str translated into camel caps
	 */
	public static function toCamelCase( $str, $capitalise_first_char = false ) {
		if ( $capitalise_first_char ) {
			$str[0] = strtoupper( $str[0] );
		}
		$func = create_function( '$c', 'return strtoupper($c[1]);' );

		return preg_replace_callback( '/_([a-z])/', $func, $str );
	}

}
```

```php
class IoHelper {

	/**
	 * Helper function for casting variables into desired types.
	 *
	 * @param $value
	 * @param string $type
	 *
	 * @return float|int|bool|string
	 */
	public static function castValue( $value, $type = 'string' ) {
		$type = strtolower($type);

		switch ( $type ) {
			case 'string':
				$value = (string) $value;
				break;
			case 'int':
			case 'integer':
				$value = (int) $value;
				break;
			case 'double':
				$value = (double) $value;
				break;
			case 'float':
				$value = (float) $value;
				break;
			case 'bool':
			case 'boolean':
				$value = (bool) $value;
				break;
			default:
				$value = $value;
		}

		return $value;
	}
}
```

Revenons maintenant à notre classe de base. Pour cela, nous étendons le constructeur comme suit :

```php
/**
 * BaseElement constructor.
 *
 * @param array $data
 */
public function __construct( $data = null ) {
	// check if fill data was provided
	if ( $data ) {

		// cast object into array if it's an object
		if ( is_object( $data ) ) {
			$data = (array) $data;
		}

		// iterate over data array
		foreach ( $data as $key => $value ) {

			// build up name for equivalent setter-function
			$setterFunction = 'set' . StringHelper::toCamelCase( $key, true );

			// check if desired setter-functions exists and if so, execute it
			if ( method_exists( $this, $setterFunction ) ) {

				// get reflection method
				$reflectionMethod = new \ReflectionMethod( $this, $setterFunction );

				// get parameters for reflection method
				$reflectionParameters = $reflectionMethod->getParameters();

				// check if desired parameter at position 0 exists
				if ( isset( $reflectionParameters[0] ) ) {

					// detect desired data type by reading doc-comments
					$type        = strtolower( (string) $reflectionParameters[0]->getType() );
					$castedValue = IoHelper::castValue( $value, $type );

					// call setter-function with casted parameter
					$this->$setterFunction( $castedValue );
				}

			}
		}
	}

}
```

Ce qui se passe ici est relativement simple à expliquer : on vérifie si un tableau de données a été transmis. Dans le cas d'une réponse positive, on vérifie alors s'il s'agit éventuellement d'un objet (comme ce serait par exemple le cas avec l'Eloquent-ORM de Laravel). Si c'est le cas, il est converti en un tableau. L'étape suivante consiste à itérer sur chaque attribut passé en paramètre à l'aide d'une boucle foreach de style key value. Comme l'index est toujours connu et qu'il doit représenter l'attribut concerné, nous supposons que la fonction Setter correspondante est nommée dans le style ```set<AttributName>```.

Si une telle méthode Setter existe réellement dans l'instance d'objet actuelle, nous l'instancions avec la ```ReflectionMethod()```. En théorie, il serait déjà possible de l'utiliser directement. Cependant, nous devons d'abord caster la valeur transmise de manière à ce qu'elle corresponde au type de données attendu de la méthode Setter correspondante.

Pour cela, il faut ensuite lire à l'aide de ```getParameters()``` quels paramètres peuvent être transmis à la méthode Setter concernée. Nous partons ici du principe que chacune de ces méthodes peut prendre en charge un seul paramètre, c'est-à-dire la valeur à définir. Si ce paramètre est défini, ```getType()``` renvoie le type de données attendu, qui a été défini dans les annotations PHP. Nous transmettons ensuite ce type de données cible à notre classe Helper et recevons en retour la variable castée correspondante.

Dans la dernière étape, nous appelons la méthode Setter par un accès régulier à celle-ci et lui transmettons comme paramètre la valeur castée précédemment. Nous avons ainsi implémenté notre fonctionnalité principale concernant l'auto-remplissage.

### Sortir les données

Pour accéder à l'intérieur de notre classe de base en utilisant la méthode getter correspondante, nous écrivons une petite méthode auxiliaire privée :

```php
/**
 * Tries to find an adequate Getter-function for the specified attribute key, and returns its value.
 *
 * @param $key
 *
 * @return null
 */
private function getElementByKey( $key ) {
	// build up name for equivalent setter-function
	$getterFunction = 'get' . StringHelper::toCamelCase( $key, true );

	// check if desired setter-functions exists and if so, execute it
	if ( method_exists( $this, $getterFunction ) ) {

		// get reflection method
		$reflectionMethod     = new \ReflectionMethod( $this, $getterFunction );
		$reflectionMethodName = $reflectionMethod->getName();

		return $this->$reflectionMethodName();
	}

	return null;
}
```

Nous pouvons lui transmettre comme paramètre le nom de l'attribut souhaité. De la même manière que pour la définition des valeurs, nous déterminons le nom de la méthode getter correspondante en supposant qu'elle a été définie sous la forme ```get<AttributName>```.

Si la méthode existe dans le contexte de l'objet actuel, elle est exécutée à l'aide de la fonction ```ReflectionMethod()``` et la valeur de l'attribut souhaité est renvoyée comme résultat.

Afin de permettre une sortie dynamique de tous les attributs, nous devons savoir quels attributs sont généralement disponibles dans la classe appelée, ainsi que dans la classe de base (en tant que classe parente). Pour cela, nous définissons une méthode appelée ```getDocument()```, qui fait exactement cela :

```php
/**
 * Build up the public exposed data array.
 *
 * @param bool $buildRelations
 *
 * @return array
 */
public function getDocument() {
	$reflectionClass = new \ReflectionClass( $this );
	$properties      = [];

	// determine properties of parent class from current context
	$this->buildPropertyArray( $reflectionClass->getParentClass()->getProperties(), $properties );

	// determine properties of current class
	$this->buildPropertyArray( $reflectionClass->getProperties(), $properties );

	// build up data array
	$data = [];
	foreach ( $properties as $property ) {
		if ( ! in_array( StringHelper::fromCamelCase( $property ), $this->_hidden ) ) {
			$data[ $property ] = $this->getElementByKey( $property );
		}
	}

	return $data;
}



/**
 * Internal helper function for extracting valid (public) attributes from ReflectionProperty() array.
 *
 * @param $reflectionProperties
 * @param $data
 */
private function buildPropertyArray( $reflectionProperties, &$data ) {
	foreach ( $reflectionProperties as $property ) {
		$propertyName = $property->getName();

		if ( substr( $propertyName, 0, 1 ) == '_' ) {
			continue;
		}

		$data[] = $property->getName();
	}
}
```

La méthode auxiliaire ```buildPropertyArray()``` sert en premier lieu à éviter le code dupliqué, et en même temps à ignorer les attributs qui commencent par un underscore ("_"). Dans ce cas, les attributs commençant par un tiret bas ne sont pas exportés vers l'extérieur via getDocument() et restent donc secrets.

### Dériver ses propres entités

Pour dériver nos propres classes d'entités à l'aide de la classe de base, il suffit de créer une nouvelle classe avec le nom souhaité, qui hérite de la classe de base que nous avons créée précédemment.

Dans celle-ci, on peut définir des attributs individuels selon le même principe - c'est tout ce qui est nécessaire ici.

```php
/**
 * Class Dummy
 */
class Dummy extends BaseElement {


	/**
	 * @var string $title
	 */
	private $title;



	/**
	 * Returns the title.
	 *
	 * @return string
	 */
	public function getTitle() {
		return $this->title;
	}


	/**
	 * Set the title.
	 *
	 * @param string $title
	 */
	public function setTitle( string $title ) {
		$this->title = $title;
	}

	
}
```

Pour tester notre classe d'entités, nous définissons un petit tableau de données, avec quelques valeurs de test. Dans notre cas, ce tableau doit simuler une source de données externe.

```php
$data = [
	"id"	=> 14,
	"title"	=> "Lorem ipsum",
];
```

Dans l'étape suivante, nous initialisons notre classe d'entités nouvellement créée avec ce tableau de données et pouvons ensuite exporter le résultat complet à l'aide de getDocument() :

```php
$entity = new Dummy( $data );
print_r( $entity->getDocument() );
```

## Conclusion

Grâce à Reflection, le programme peut agir de manière "intelligente" dans le développement moderne de logiciels, car il est en mesure d'analyser et même de modifier les propriétés de ses propres fonctions pendant l'exécution.

L'implémentation de Reflection en PHP est toutefois si vaste que nous n'avons démontré ici qu'une petite partie des possibilités. Il existe encore d'innombrables autres fonctions permettant de décomposer encore plus le code du programme.

En résumé, nous constatons que Reflection est une technologie très puissante qui permet de faire énormément de choses.

# Contenu de ./0670 - Les opérateurs binaires/content.md

Les opérateurs Bitwise sont utilisés pour effectuer des opérations au niveau du bit sur les opérandes. Les opérateurs sont d'abord convertis au niveau du bit, puis le calcul est effectué sur les opérandes. Les opérations mathématiques telles que l'addition, la soustraction, la multiplication, etc. peuvent être effectuées au niveau du bit pour un traitement plus rapide. En PHP, les opérateurs qui fonctionnent au niveau du bit sont :

## & (ET Binaire)

C'est un opérateur binaire, c'est-à-dire qu'il fonctionne sur deux opérandes. L'opérateur ET binaire en PHP prend deux nombres comme opérandes et effectue un ET sur chaque bit des deux nombres. Le résultat du ET est 1 seulement si les deux bits sont 1.

### Syntaxe

```php
$Premier & $Second
```

Cela retournera un autre nombre dont les bits sont activés si les bits du premier et du second sont activés.

### Exemple

```php
Entrée : $Premier = 5,  $Second = 3
Réponse : Le & binaire de ces deux valeurs sera 1.
```

La représentation binaire de 5 est 0101 et 3 est 0011. Par conséquent, leur bit & sera 0001 (c'est-à-dire qu'il sera activé si le premier et le second ont tous deux leur bit activé).

## | (OU Binaire)

Il s'agit également d'un opérateur binaire, c'est-à-dire qu'il fonctionne sur deux opérandes. L'opérateur OU par bit prend deux nombres comme opérandes et effectue un OU sur chaque bit des deux nombres. Le résultat de l'opération OU est 1 si l'un des deux bits est 1.

### Syntaxe

```php
$Premier | $Second
```

Cela retournera un autre nombre dont les bits sont activés si le bit du premier ou du second est activé.

### Exemple

```php
Entrée : Premier = 5, Second = 3
Réponse : Le OU binaire de ces deux valeurs sera 7.
```

La représentation binaire de 5 est 0101 et 3 est 0011. Par conséquent, leur combinaison binaire sera 0111 (c'est-à-dire qu'elle sera activée si le premier ou le second ont leur bit activé).

## ^ (OU exclusif Binaire)

Il s'agit également d'un opérateur binaire, c'est-à-dire qu'il fonctionne sur deux opérandes. Il est également connu sous le nom d'opérateur OU exclusif. L'opérateur XOR par bit prend deux nombres comme opérandes et effectue le XOR sur chaque bit des deux nombres. Le résultat de l'opération XOR est 1 si les deux bits sont différents.

### Syntaxe

```php
$Premier ^ $Second
```

Cela renvoie un autre nombre dont les bits sont activés si l'un des bits du premier ou du deuxième est activé, mais pas les deux.

### Exemple

```php
Entrée : Premier = 5, Second = 3
Réponse : La OU exclusif Binaire de ces deux valeurs sera 6.
```

La représentation binaire de 5 est 0101 et 3 est 0011. Par conséquent, leur ^ binaire sera 0110 (c'est-à-dire qu'il sera activé si le premier ou le second ont leur bit activé mais pas les deux).

## ~ (NON Binaire)

Il s'agit d'un opérateur unitaire, c'est-à-dire qu'il ne fonctionne que sur un seul opérande. L'opérateur NON Binaire prend un nombre et inverse tous les bits de celui-ci.

### Syntaxe

```php
~$number
```

Cela va inverser tous les bits de $number.

### Exemple

```php
Entrée : nombre = 5
Réponse : Le ~ binaire de ce nombre sera -6.
```

La représentation binaire de 5 est 0101. Par conséquent, la représentation binaire de 5 sera 1010 (inverse tous les bits du nombre d'entrée).

## << (Décalage binaire à gauche)

Il s'agit d'un opérateur binaire, c'est-à-dire qu'il travaille sur deux opérandes. L'opérateur Décalage binaire à gauche (*Bitwise Left Shift* en anglais) prend deux nombres, décale à gauche les bits du premier opérande, le second opérande décide du nombre de positions à décaler.

### Syntaxe

```php
$Premier << $Second
```

Cela va décaler les bits de ```$Premier``` vers la gauche. ```$Second``` décide du nombre de fois que les bits seront décalés.

### Exemple

```php
Entrée : Premier = 5, Second = 1
Réponse : Le << binaire de ces deux valeurs sera 10.
```

La représentation binaire de 5 est 0101 . Par conséquent, le << binaire décalera les bits de 5 une fois vers la gauche (c'est-à-dire 01010).

*Remarque : le décalage à gauche d'un bit est équivalent à une multiplication par 2.*

## >> (Décalage binaire à droite)

Il s'agit également d'un opérateur binaire, c'est-à-dire qu'il fonctionne sur deux opérandes. L'opérateur Décalage binaire à droite (*Bitwise Right Shift* en anglais) prend deux nombres, décale à droite les bits du premier opérande, le second opérande décide du nombre de positions à décaler.

### Syntaxe

```php
$Premier >> $Second
```

Cela va décaler les bits de ```$Premier``` vers la droite. ```$Second``` décide du nombre de fois que les bits seront décalés.

### Exemple

```php
Entrée : Premier = 5, Second = 1
Réponse : La combinaison >> binaire de ces deux valeurs sera 2.
```

La représentation binaire de 5 est 0101 . Par conséquent, le >> binaire déplacera les bits de 5 une fois vers la droite (c'est-à-dire 010).

*Remarque : Le décalage vers la droite d'un bit est équivalent à une division par 2.*

# Contenu de ./0680 - PSR 14 - Event Dispatcher/content.md

## Objectif du PSR 14

Event Dispatching est un mécanisme courant et bien testé qui permet aux développeurs d'injecter de la logique dans une application facilement et de manière cohérente.

L'objectif de ce PSR est d'établir un mécanisme commun pour l'extension et la collaboration basées sur les événements afin que les bibliothèques et les composants puissent être réutilisés plus librement entre diverses applications et frameworks.

L'objectif est de disposer d'interfaces communes pour la distribution et la gestion des événements permettant aux développeurs de créer des bibliothèques pouvant interagir avec de nombreux frameworks et autres bibliothèques de façon commune.

Quelques exemples :

- Un cadre de sécurité qui empêchera l'enregistrement/l'accès aux données lorsqu'un utilisateur n'a pas l'autorisation.
- Un système commun de mise en cache pleine page.
- Bibliothèques qui étendent d'autres bibliothèques, quel que soit le framework dans lequel elles sont toutes deux intégrées.
- Un package de journalisation pour suivre toutes les actions entreprises dans l'application

## Définitions

- ```Event``` - Un événement est un message produit par un émetteur. Il peut s'agir de n'importe quel objet PHP arbitraire.
- ```Listener``` - Un écouteur est tout appelable PHP qui s'attend à recevoir un événement. Le même événement peut être passé à zéro ou plusieurs écouteurs. Un écouteur peut mettre en file d'attente un autre comportement asynchrone s'il le souhaite.
- ```Emitter``` - Un émetteur est tout code arbitraire qui souhaite envoyer un événement. Ceci est également connu sous le nom de "code d'appel". Il n'est représenté par aucune structure de données particulière, mais fait référence au cas d'utilisation.
- ```Dispatcher``` - Un Dispatcher est un objet de service auquel un émetteur donne un objet Event. Le répartiteur est chargé de s'assurer que l'événement est transmis à tous les auditeurs pertinents, mais doit reporter la détermination des auditeurs responsables à un fournisseur d'écouteurs.
- ```Listener Provider``` - Un fournisseur d'écoute est chargé de déterminer quels auditeurs sont pertinents pour un événement donné, mais ne doit pas appeler les auditeurs lui-même. Un fournisseur d'écoute peut spécifier zéro ou plusieurs écouteurs pertinents.

## Les Events

Les événements sont des objets qui servent d'unité de communication entre un émetteur et les auditeurs appropriés.

Les objets d'événement peuvent être modifiables si le cas d'utilisation appelle des écouteurs fournissant des informations à l'émetteur. Cependant, si une telle communication bidirectionnelle n'est pas nécessaire, il est recommandé que l'événement soit défini comme immuable ; c'est-à-dire défini de telle sorte qu'il manque de méthodes de mutation.

Les implémenteurs doivent supposer que le même objet sera passé à tous les auditeurs.

Il est recommandé, mais non obligatoire, que les objets Événement prennent en charge la sérialisation et la désérialisation sans perte ; ```$event == unserialize(serialize($event))``` devrait être vrai. Les objets peuvent exploiter l'interface ```Serializable``` de PHP , ```__sleep()``` ou ```__wakeup()``` des méthodes magiques, ou des fonctionnalités de langage similaires, le cas échéant.

## Les stoppable events

Un événement stoppable est un cas particulier d'événement qui contient des moyens supplémentaires d'empêcher l'appel d'autres écouteurs. Il est indiqué par la mise en œuvre du ```StoppableEventInterface```. Un événement qui implémente ```StoppableEventInterface``` soit revenir à “true” partir du ```isPropagationStopped()``` moment où l'événement qu'il représente est terminé. C'est à l'implémentation de la classe de déterminer quand c'est. Par exemple, un événement qui demande qu'un ```RequestInterface``` objet PSR-7 soit mis en correspondance avec un ```ResponseInterface``` objet correspondant peut avoir une ```setResponse(ResponseInterface $res)``` méthode à appeler par un écouteur, ce qui provoque ```isPropagationStopped()``` le retour de “true”.

## Les listeners

Un écouteur peut être n'importe quel appel PHP. Un écouteur doit avoir un et un seul paramètre, qui est l'événement auquel il répond. Les auditeurs devraient saisir ce paramètre de manière aussi précise que cela est pertinent pour leur cas d'utilisation ; c'est-à-dire qu'un indice de type Listener peut sur une interface pour indiquer qu'elle est compatible avec tout type d'événement qui implémente cette interface, ou avec une implémentation spécifique de cette interface. Un écouteur devrait avoir un “void” retour et devrait taper un indice qui retourne explicitement. Un Dispatcher doit ignorer les valeurs de retour des Listeners. Un écouteur peut déléguer des actions à un autre code. Cela inclut un Listener étant un wrapper mince autour d'un objet qui exécute la logique métier réelle. Un auditeur peut mettre en file d'attente les informations de l'événement pour un traitement ultérieur par un processus secondaire, en utilisant cron, un serveur de file d'attente ou des techniques similaires. Il peut sérialiser l'objet Event lui-même pour le faire ; cependant, il faut veiller à ce que tous les objets Event ne soient pas sérialisables en toute sécurité. Un processus secondaire doit supposer que toute modification qu'il apporte à un objet Événement ne se propagera pas aux autres auditeurs.

## Les dispatchers

Un Dispatcher est un objet de service implémentant “EventDispatcherInterface”. Il est chargé de récupérer les écouteurs d'un fournisseur d'écouteurs pour l'événement distribué et d'appeler chaque écouteur avec cet événement.

Un répartiteur :

- doit appeler les écouteurs de manière synchrone dans l'ordre où ils sont renvoyés par un ```ListenerProvider```.
- doit retourner le même objet Event qu'il a été passé après avoir appelé les écouteurs.
- ne doit pas retourner à l'émetteur tant que tous les écouteurs n'ont pas été exécutés. Si un événement stoppable est passé, un répartiteur
- doit appeler ```isPropagationStopped()``` l'événement avant que chaque écouteur n'ait été appelé. Si cette méthode retourne, “true” elle doit retourner l'événement à l'émetteur immédiatement et ne doit pas appeler d'autres écouteurs. Cela implique que si un événement est passé au ```Dispatcher``` qui revient toujours “true” de ```isPropagationStopped()```, aucun écouteur ne sera appelé.

Un dispatcher devrait supposer que tout écouteur qui lui est renvoyé par un fournisseur d'écouteur est de type sûr. C'est-à-dire que le Dispatcher devrait supposer que l'appel ```$listener($event)``` ne produira pas de “TypeError”.

La gestion des erreurs :

Une exception ou une erreur lancée par un écouteur DOIT bloquer l'exécution de tout autre écouteur. Une exception ou une erreur lancée par un écouteur DOIT être autorisée à se propager jusqu'à l'émetteur.

Un Dispatcher PEUT attraper un objet lancé pour le consigner, permettre que des actions supplémentaires soient prises, etc., mais DOIT ensuite relancer l'objet jetable d'origine.

## Les listeners provider

Un listener provider est un objet de service chargé de déterminer quels écouteurs sont pertinents et doivent être appelés pour un événement donné. Il peut déterminer à la fois quels auditeurs sont pertinents et l'ordre dans lequel les renvoyer par le moyen qu'il choisit. Cela peut inclure :

- Permettre une certaine forme de mécanisme d'enregistrement afin que les implémenteurs puissent affecter un écouteur à un événement dans un ordre fixe.
- Dérivation d'une liste d'auditeurs applicables par réflexion basée sur le type et les interfaces implémentées de l'événement.
- Génération d'une liste compilée d'écouteurs à l'avance qui peuvent être consultés au moment de l'exécution.
- Implémenter une forme de contrôle d'accès afin que certains écouteurs ne soient appelés que si l'utilisateur actuel dispose d'une certaine autorisation.
- Extraire certaines informations d'un objet référencé par l'événement, tel qu'une entité, et appeler des méthodes de cycle de vie prédéfinies sur cet objet.
- Déléguer sa responsabilité à un ou plusieurs autres listener provider en utilisant une logique arbitraire.

Toute combinaison de ce qui précède, ou d'autres mécanismes, peut être utilisée comme vous le souhaitez. Les listener provider devraient utiliser le nom de classe d'un événement pour différencier un événement d'un autre. Ils peuvent également considérer toute autre information sur l'événement, le cas échéant. Les listener provider doivent traiter les types parents de la même manière que le propre type de l'événement lorsqu'ils déterminent l'applicabilité de l'écouteur. Dans le cas suivant :

```php
class A {}

class B extends A {}

$b = new B();

function listener(A $event): void {};
```

Un fournisseur d'écoute ```listener()``` doit traiter comme un écouteur applicable pour ```$b```, car il est de type compatible, à moins que d'autres critères ne l'empêchent de le faire.

# Contenu de ./0690 - PSR 16 - Simple Cache/content.md

La mise en cache est un moyen courant d'améliorer les performances de tout projet, faisant des bibliothèques de mise en cache l'une des fonctionnalités les plus courantes de nombreux frameworks et bibliothèques. L'interopérabilité à ce niveau signifie que les bibliothèques peuvent supprimer leurs propres implémentations de mise en cache et s'appuyer facilement sur celle qui leur est fournie par le framework ou sur une autre bibliothèque de cache dédiée.

PSR-6 résout déjà ce problème, mais de manière assez formelle et verbeuse pour ce dont les cas d'utilisation les plus simples ont besoin. Cette approche plus simple vise à construire une interface rationalisée standardisée pour les cas courants. Il est indépendant du PSR-6, mais a été conçu pour rendre la compatibilité avec le PSR-6 aussi simple que possible.

## Définitions

Les définitions de la bibliothèque d'appel, de la bibliothèque d'implémentation, de la durée de vie, de l'expiration et de la clé sont copiées de PSR-6 car les mêmes hypothèses sont vraies.

- ```Calling Library``` - La bibliothèque ou le code qui a réellement besoin des services de cache. Cette bibliothèque utilisera des services de mise en cache qui implémentent les interfaces de cette norme, mais n'aura autrement aucune connaissance de la mise en œuvre de ces services de mise en cache.

- ```Implementing Library``` - Cette bibliothèque est responsable de la mise en œuvre de cette norme afin de fournir des services de mise en cache à toute bibliothèque appelant. La bibliothèque d'implémentation doit fournir une classe implémentant l'interface ```Psr\SimpleCache\CacheInterface```. La mise en œuvre des bibliothèques doit prendre en charge au minimum la fonctionnalité TTL comme décrite ci-dessous avec une granularité à la seconde entière.
- ```TTL``` - La durée de vie (TTL) d'un élément est le temps qui s'écoule entre le moment où cet élément est stocké et celui où il est considéré comme périmé. Le TTL est normalement défini par un entier représentant le temps en secondes ou un objet DateInterval.
- ```Expiration``` - L'heure réelle à laquelle un élément est configuré pour devenir périmé. Ceci est calculé en ajoutant le TTL au moment où un objet est stocké.
Un élément avec un TTL de 300 secondes stocké à 1:30:00 aura une expiration de 1:35:00.
Les bibliothèques de mise en œuvre peuvent expirer un élément avant son heure d'expiration demandée, mais doivent traiter un élément comme expiré une fois que son heure d'expiration est atteinte. Si une bibliothèque appelant demande qu'un élément soit sauvegardé, mais ne spécifie pas de délai d'expiration, ou spécifie un délai d'expiration nul ou un TTL, une bibliothèque de mise en œuvre peut utiliser une durée par défaut configurée. Si aucune durée par défaut n'a été définie, la bibliothèque de mise en œuvre doit interpréter cela comme une demande de mise en cache de l'élément pour toujours, ou aussi longtemps que la mise en œuvre sous-jacente le prend en charge.
Si un TTL négatif ou nul est fourni, l'élément doit être supprimé du cache s'il existe, car il a déjà expiré.
- ```Key``` - Une chaîne d'au moins un caractère qui identifie de manière unique un élément mis en cache. Les bibliothèques de mise en œuvre doivent prendre en charge les clés composées des caractères “A-Z, a-z, 0-9, _”, et dans n'importe quel ordre de codage UTF-8 et d'une longueur allant jusqu'à 64 caractères. Les bibliothèques de mise en œuvre peuvent prendre en charge des caractères et des codages supplémentaires ou des longueurs plus longues, mais doivent prendre en charge au moins ce minimum. Les bibliothèques sont responsables de leur propre échappement des chaînes de clé, le cas échéant, mais doivent être capables de retourner la chaîne de clé originale non modifiée. Les caractères suivants sont réservés pour de futures extensions et ne doivent pas être pris en charge par l'implémentation des bibliothèques : ```{}()/\@:```
- ```Cache``` - Un objet qui implémente l'“Psr\SimpleCache\CacheInterface” interface.
- ```Cache Misses``` - Un cache miss renverra null et donc détecter si un stocké “null” n'est pas possible. C'est le principal écart par rapport aux hypothèses de PSR-6.

## Cache

Les mises en œuvre peuvent fournir un mécanisme permettant à un utilisateur de spécifier un TTL par défaut s'il n'en est pas spécifié pour un élément de cache spécifique. Si aucune valeur par défaut spécifiée par l'utilisateur n'est fournie, les mises en œuvre doivent par défaut la valeur légale maximale autorisée par la mise en œuvre sous-jacente. Si la mise en œuvre sous-jacente ne prend pas en charge le TTL, le TTL spécifié par l'utilisateur doit être ignoré en silence.

## Les données

Les bibliothèques d'implémentation doivent prendre en charge tous les types de données PHP sérialisables, notamment :

- ```Strings``` - Chaînes de caractères de taille arbitraire dans n'importe quel encodage compatible PHP.
- ```Integers``` - Tous les entiers de toute taille pris en charge par PHP, jusqu'à 64 bits signés.
- ```Floats``` - Toutes les valeurs à virgule flottante signées.
- ```Booleans``` - Vrai et Faux.
- ```Null``` - La valeur nulle (bien qu'elle ne soit pas distinguable d'un échec de cache lors de sa lecture).
- ```Arrays``` - Tableaux indexés, associatifs et multidimensionnels de profondeur arbitraire.
- ```Objects``` - Tout objet qui prend en charge la sérialisation et la désérialisation sans perte tel que ```$o == unserialize(serialize($o))```. Les objets peuvent exploiter l'interface sérialisable de PHP, ```__sleep()``` ou ```__wakeup()``` des méthodes magiques, ou des fonctionnalités de langage similaires, le cas échéant.

Toutes les données transmises à la bibliothèque de mise en œuvre doivent être retournées exactement telles qu'elles ont été transmises. Cela inclut le type de variable. C'est-à-dire que c'est une erreur de renvoyer (string) 5 si (int) 5 était la valeur enregistrée. L'implémentation des bibliothèques peut utiliser les fonctions serialize()/unserialize() de PHP en interne, mais n'est pas obligé de le faire. La compatibilité avec eux est simplement utilisée comme référence pour les valeurs d'objet acceptables.

S'il n'est pas possible de retourner la valeur sauvegardée exacte pour quelque raison que ce soit, les bibliothèques de mise en œuvre doivent répondre avec un cache manquant plutôt que des données corrompues.

## CacheInterface

L'interface de cache définit les opérations les plus élémentaires sur une collection d'entrées de cache, ce qui implique la lecture, l'écriture et la suppression d'éléments de cache individuels. De plus, il dispose de méthodes pour traiter plusieurs ensembles d'entrées de cache telles que l'écriture, la lecture ou la suppression de plusieurs entrées de cache à la fois. Ceci est utile lorsque vous avez beaucoup de lectures/écritures de cache à effectuer et vous permet d'effectuer vos opérations en un seul appel au serveur de cache en réduisant considérablement les temps de latence. Une instance de “CacheInterface” correspond à une seule collection d'éléments de cache avec un seul espace de nom de clé et équivaut à un "Pool" dans PSR-6. Différentes instances de “CacheInterface” peuvent être soutenues par le même magasin de données, mais doivent être logiquement indépendantes.

```php
<?php

namespace Psr\SimpleCache;

interface CacheInterface
{
    /**
     * @param string $key    
     * @param mixed  $default
     * @return mixed
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function get($key, $default = null);

    /**
     * @param string $key   
     * @param mixed                 
     * @param null|int|\DateInterval $ttl  
     * @return bool
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function set($key, $value, $ttl = null);

    /**
     * @param string $key
     * @return bool
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function delete($key);

    /**
     * @return bool
     */
    public function clear();

    /**
     * @param iterable $keys   
     * @param mixed 
     * @return iterable
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function getMultiple($keys, $default = null);

    /**
     * @param iterable              
     * @param null|int|\DateInterval $ttl  
     * @return bool
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function setMultiple($values, $ttl = null);

    /**
     * @param iterable $keys
     * @return bool
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function deleteMultiple($keys);

    /**
     * @param string $key
     * @return bool
     * @throws \Psr\SimpleCache\InvalidArgumentException
     */
    public function has($key);
}
```

## CacheException

```php
<?php

namespace Psr\SimpleCache;

interface CacheException
{
}
```

## InvalidArgumentException

```php
<?php

namespace Psr\SimpleCache;

interface InvalidArgumentException extends CacheException
{}
```

# Contenu de ./0700 - injection de dépendances/content.md

Les objets dépendent souvent d'autres objets. Au lieu de créer la dépendance dans le constructeur, la dépendance doit être passée en paramètre dans le constructeur. Cela garantit qu'il n'y a pas de couplage étroit entre les objets et permet de modifier la dépendance lors de l'instanciation de la classe. Cela présente un certain nombre d'avantages, notamment celui de rendre le code plus facile à lire en rendant les dépendances explicites, ainsi que de simplifier les tests puisque les dépendances peuvent être changées et simulées plus facilement.

Dans l'exemple suivant, Component dépend d'une instance de Logger, mais il n'en crée pas. Il exige qu'une instance soit passée comme argument au constructeur.

```php
interface Logger {
    public function log(string $message);
}

class Component {
    private $logger;

    public function __construct(Logger $logger) {
        $this->logger = $logger;
    }
}
```

Sans injection de dépendances, le code ressemblerait probablement à ceci :

```php
class Component {
    private $logger;

    public function __construct() {
        $this->logger = new FooLogger();
    }
}
```

L'utilisation de new pour créer de nouveaux objets dans le constructeur indique que l'injection de dépendances n'a pas été utilisée (ou l'a été de manière incomplète), et que le code est étroitement couplé. C'est également un signe que le code est incomplètement testé ou qu'il peut avoir des tests fragiles qui font des hypothèses incorrectes sur l'état du programme.

Dans l'exemple ci-dessus, où nous utilisons plutôt l'injection de dépendances, nous pourrions facilement passer à un autre ```Logger``` si cela s'avérait nécessaire. Par exemple, nous pourrions utiliser une implémentation de ```Logger``` qui enregistre à un endroit différent, ou qui utilise un format d'enregistrement différent, ou qui enregistre dans la base de données plutôt que dans un fichier.

## Injection dans un conteneur

L'injection de dépendances (DI) dans le contexte de l'utilisation d'un conteneur d'injection de dépendances (DIC) peut être considérée comme un sur-ensemble de l'injection de constructeurs. Un DIC analysera généralement les indications de type du constructeur d'une classe et répondra à ses besoins, en injectant effectivement les dépendances nécessaires à l'exécution de l'instance.

L'implémentation exacte va bien au-delà de la portée de ce document, mais dans son essence même, un DIC repose sur l'utilisation de la signature d'une classe...

```php
namespace Documentation;

class Example
{
    private $meaning;

    public function __construct(Meaning $meaning)
    {
        $this->meaning = $meaning;
    }
}
```

... pour l'instancier automatiquement, en s'appuyant la plupart du temps sur un système de chargement automatique.

```php
// older PHP versions
$container->make('Documentation\Example');

// since PHP 5.5
$container->make(\Documentation\Example::class);
```

Dans ce cas, ```Documentation\Example``` sait qu'il a besoin d'un ```Meaning```, et un DIC instancierait à son tour un type de ```Meaning```. L'implémentation concrète ne doit pas dépendre de l'instance consommatrice.

Au lieu de cela, nous définissons des règles dans le conteneur, avant la création de l'objet, qui indiquent comment des types spécifiques doivent être instanciés si nécessaire.

Cela présente un certain nombre d'avantages, car un DIC peut

- partager des instances communes
- fournir un factory pour résoudre une signature de type
- Résoudre la signature d'une interface

Si nous définissons des règles sur la façon dont un type spécifique doit être géré, nous pouvons obtenir un contrôle fin sur les types qui sont partagés, instanciés ou créés à partir d'une usine.

## Injection de setter

Les dépendances peuvent également être injectées par des setters.

```php
interface Logger {
    public function log($message);
}

class Component {
    private $logger;
    private $databaseConnection;

    public function __construct(DatabaseConnection $databaseConnection) {
        $this->databaseConnection = $databaseConnection;
    }

    public function setLogger(Logger $logger) {
        $this->logger = $logger;
    }

    public function core() {
        $this->logSave();    
        return $this->databaseConnection->save($this);
    }

    public function logSave() {
         if ($this->logger) {
            $this->logger->log('saving');
        }
    }
}
```

Ceci est particulièrement intéressant lorsque la fonctionnalité principale de la classe ne dépend pas de la dépendance pour fonctionner.

Ici, la seule dépendance nécessaire est la ```DatabaseConnection```, elle se trouve donc dans le constructeur. La dépendance ```Logger``` est facultative et n'a donc pas besoin de faire partie du constructeur, ce qui rend la classe plus facile à utiliser.

Notez que lorsque vous utilisez l'injection de setter, il est préférable d'étendre la fonctionnalité plutôt que de la remplacer. Lorsque vous définissez une dépendance, rien ne confirme que la dépendance ne changera pas à un moment donné, ce qui peut entraîner des résultats inattendus. Par exemple, un ```FileLogger``` pourrait être défini dans un premier temps, puis un ```MailLogger``` pourrait être défini. Cela brise l'encapsulation et rend les journaux difficiles à trouver, car nous remplaçons la dépendance.

Pour éviter cela, nous devons ajouter une dépendance avec injection de setter, comme suit :

```php
interface Logger {
    public function log($message);
}

class Component {
    private $loggers = array();
    private $databaseConnection;

    public function __construct(DatabaseConnection $databaseConnection) {
        $this->databaseConnection = $databaseConnection;
    }

    public function addLogger(Logger $logger) {
        $this->loggers[] = $logger;
    }

    public function core() {
        $this->logSave();
        return $this->databaseConnection->save($this);
    }

    public function logSave() {
        foreach ($this->loggers as $logger) {
            $logger->log('saving');
        }
    }
}
```

Ainsi, chaque fois que nous utiliserons la fonctionnalité de base, elle ne sera pas interrompue même si aucune dépendance n'a été ajoutée au logger, et tout logger ajouté sera utilisé même si un autre logger aurait pu être ajouté. Nous étendons la fonctionnalité au lieu de la remplacer.

# Contenu de ./0710 - Générateurs/content.md

Parcourir une grande collection de données en utilisant une construction en boucle telle que FOREACH nécessiterait une grande mémoire et un temps de traitement considérable. Avec les **générateurs**, il est possible d'itérer sur un ensemble de données sans ces frais généraux. Une fonction de générateur est similaire à une fonction normale. Toutefois, au lieu de l'instruction return dans une fonction, le générateur utilise le mot-clé ```yield``` pour être exécuté de manière répétée afin de fournir des valeurs à itérer.

Le mot-clé ```yield``` est le cœur du mécanisme du générateur. Même si son utilisation semble être semblable à celle de return, il n'arrête pas l'exécution de la fonction. Il fournit la valeur suivante pour l'itération et met en pause l'exécution de la fonction.

## Valeur de yield

Une boucle FOR qui donne chaque valeur de la variable de bouclage est utilisée dans une fonction de générateur.

### Exemple 1 

```php
<?php
function squaregenerator(){
   for ($i=1; $i<=5; $i++){
      yield $i*$i;
   }
}
$gen=squaregenerator();
foreach ($gen as $val){
   echo($val . " ");
}
?>
```

La réponse est semblable à une boucle FOREACH normale.

### Réponse 1

```php
1 4 9 16 25
```

La fonction ```range()``` de PHP retourne une liste d'entiers de début à fin avec un intervalle de ```$step``` entre chaque nombre. Le programme suivant implémente ```range()``` comme générateur.

### Example 2

```php
<?php
function rangegenerator($start, $stop, $step){
   for ($i=$start; $i<=$stop; $i+=$step){
      yield $i;
   }
}
foreach (rangegenerator(2,10,2) as $val){
   echo($val . " ");
}
?>
```

### Réponse 2

La réponse est similaire à range(2,20,2).

```php
2 4 6 8 10
```

Un tableau associatif peut aussi être implémenté comme générateur :

### Example 3

```php
<?php
function arrgenerator($arr){
   foreach ($arr as $key=>$val){
      yield $key=>$val;
   }
}
$arr=array("one"=>1, "two"=>2, "three"=>3, "four"=>4);
$gen=arrgenerator($arr);
foreach ($gen as $key=>$val)
echo($key . "=>" . $val . "\n");
?>
```

### Réponse 3

```php
one=>1
two=>2
three=>3
four=>4
```

# Contenu de ./0720 - Fonctions anonymes/content.md

Une fonction anonyme est une fonction sans nom défini par l'utilisateur. Une telle fonction est également appelée **closure** ou fonction **lambda**. Parfois, vous pouvez vouloir une fonction pour un usage unique. La fermeture est une fonction anonyme qui se ferme sur l'environnement dans lequel elle est définie. L'utilisation la plus courante de la fonction anonyme est la création d'une fonction de rappel en ligne.

## Syntaxe

```php
$var=function ($arg1, $arg2) { return $val; }
```

- Il n'y a pas de nom de fonction entre le mot-clé function et la parenthèse ouvrante.
- Il y a un point-virgule après la définition de la fonction, car les définitions de fonctions anonymes sont des expressions.
- La fonction est assignée à une variable, et appelée plus tard en utilisant le nom de la variable.
- Lorsqu'elle est transmise à une autre fonction qui peut l'appeler ultérieurement, elle est appelée "callback".
- La fonction est retournée depuis une fonction externe afin qu'elle puisse accéder aux variables de la fonction externe. C'est ce qu'on appelle une fermeture.

## Exemple de fonction anonyme

### Exemple

```php
<?php
$var = function ($x) {return pow($x,3);};
echo("cube of 3 = " . $var(3));
?>
```

### Réponse

```php
cube of 3 = 27
```

## Fonction anonyme callback

Dans l'exemple suivant, une fonction anonyme est utilisée comme argument pour une fonction intégrée ```usort()```. La fonction ```usort()``` trie un tableau donné en utilisant une fonction de comparaison.

### Exemple

```php
<?php
$arr = [10,3,70,21,54];
usort ($arr, function ($x , $y) {
    return $x > $y;
});
foreach ($arr as $x){
    echo($x . "\n");
}
?>
```

### Réponse

```php
3
10
21
54
70
```

## Fonction anonyme closure

Closure est également une fonction anonyme qui peut accéder à des variables en dehors de sa portée à l'aide du mot-clé use.

### Exemple

```php
<?php
$maxmarks=300;
$percent=function ($marks) use ($maxmarks) {return $marks*100/$maxmarks;};
echo("marks=285 percentage=". $percent(285));
?>
```

### Réponse

```php
marks=285 percentage=95
```

# Contenu de ./0730 - PSR 15 - HTTP Handlers/content.md

Les gestionnaires de requêtes HTTP sont un élément fondamental de toute application Web. Le code côté serveur reçoit un message de demande, le traite et produit un message de réponse. L'intergiciel HTTP est un moyen de déplacer le traitement commun des demandes et des réponses loin de la couche d'application.

Les interfaces décrites dans ce document sont des abstractions pour les gestionnaires de demandes et les middlewares.

## Request Handlers

Un gestionnaire de requêtes est un composant individuel qui traite une requête et produit une réponse, comme défini par PSR-7.

Un gestionnaire de demande peut lever une exception si les conditions de la demande l'empêchent de produire une réponse. Le type d'exception n'est pas défini.

Les gestionnaires de requêtes utilisant cette norme doivent implémenter l'interface suivante : ```Psr\Http\Server\RequestHandlerInterface```

## Middleware

Un composant middleware est un composant individuel participant, souvent avec d'autres composants middleware, au traitement d'une demande entrante et à la création d'une réponse résultante, comme défini par PSR-7.

Un composant middleware peut créer et retourner une réponse sans déléguer à un gestionnaire de demande, si des conditions suffisantes sont remplies.

Le middleware utilisant cette norme doit implémenter l'interface suivante : ```Psr\Http\Server\MiddlewareInterface```

## Générer les réponses

Il est recommandé que tout middleware ou gestionnaire de requêtes qui génère une réponse compose soit un prototype d'un PSR-7, ```ResponseInterface``` soit une fabrique capable de générer une ```ResponseInterface``` instance afin d'éviter de dépendre d'une implémentation de message HTTP spécifique.

## Traitement des exceptions

Il est recommandé que toute application utilisant un middleware inclut un composant qui intercepte les exceptions et les convertit en réponses. Ce middleware devrait être le premier composant exécuté et envelopper tous les traitements ultérieurs pour s'assurer qu'une réponse est toujours générée.

## Les interfaces

“RequestHandlerInterface” :

```php
namespace Psr\Http\Server;

use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

interface RequestHandlerInterface
{
    public function handle(ServerRequestInterface $request): ResponseInterface;
}
```

“MiddlewareInterface” :

```php
namespace Psr\Http\Server;

use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

interface MiddlewareInterface
{
    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface;
}
```

# Contenu de ./0740 - PSR 17 - HTTP Factories/content.md

Une HTTP factory est une méthode par laquelle un nouvel objet HTTP, tel que défini par PSR-7, est créé. Les factory HTTP doivent implémenter ces interfaces pour chaque type d'objet fourni par le package.

## Les interfaces

Les interfaces suivantes peuvent être mises en œuvre ensemble au sein d'une même classe ou dans des classes distinctes.

“RequestFactoryInterface” :

```php
namespace Psr\Http\Message;

use Psr\Http\Message\RequestInterface;
use Psr\Http\Message\UriInterface;

interface RequestFactoryInterface
{
    /**
     * Créer une nouvelle requête
     *
     * @param string $method la méthode Http est associé à la requête 
     * @param UriInterface|string $uri Uri associé à la requête
     */
    public function createRequest(string $method, $uri): RequestInterface;
}
```

“ResponseFactoryInterface” :

```php
namespace Psr\Http\Message;

use Psr\Http\Message\ResponseInterface;

interface ResponseFactoryInterface
{
    /**
     * créer une nouvelle réponse
     *
     * @param int $code le status code Http est par défaut 200
     * @param string $reasonPhrase phrase associé avec le status code              qui génère une réponse 
     */
    public function createResponse(int $code = 200, string $reasonPhrase = ''): ResponseInterface;
}
```

“ServerRequestFactoryInterface” :

```php
namespace Psr\Http\Message;

use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Message\UriInterface;

interface ServerRequestFactoryInterface
{
    /**
     * @param string $method méthode Http associé à la requête
     * @param UriInterface|string $uri Uri associé à la requête
     * @param array $serverParams
     */
    public function createServerRequest(string $method, $uri, array $serverParams = []): ServerRequestInterface;
}
```

“StreamFactoryInterface” :

```php
namespace Psr\Http\Message;

use Psr\Http\Message\StreamInterface;

interface StreamFactoryInterface
{
    /**
     * @param string $content
     */
    public function createStream(string $content = ''): StreamInterface;

    /**
     * @param string $filename
     * @param string $mode
     * @throws \RuntimeException
     * @throws \InvalidArgumentException
     */
    public function createStreamFromFile(string $filename, string $mode = 'r'): StreamInterface;

    /**
     * @param resource $resource
     */
    public function createStreamFromResource($resource): StreamInterface;
}
```

“UploadedFileFactoryInterface” :

```php
namespace Psr\Http\Message;

use Psr\Http\Message\StreamInterface;
use Psr\Http\Message\UploadedFileInterface;

interface UploadedFileFactoryInterface
{
    /**
     * @param StreamInterface $stream
     * @param int $size
     * @param int $error
     * @param string $clientFilename
     * @param string $clientMediaType
     * @throws \InvalidArgumentException
     */
    public function createUploadedFile(
        StreamInterface $stream,
        int $size = null,
        int $error = \UPLOAD_ERR_OK,
        string $clientFilename = null,
        string $clientMediaType = null
    ): UploadedFileInterface;
}
```

“UriFactoryInterface” :

```php
namespace Psr\Http\Message;

use Psr\Http\Message\UriInterface;

interface UriFactoryInterface
{
    /**
     * @param string $uri
     * @throws \InvalidArgumentException
     */
    public function createUri(string $uri = '') : UriInterface;
}
```

# Contenu de ./0750 - PSR 18 - HTTP Client/content.md

## Objectif du PSR 18

Le but de ce PSR est de permettre aux développeurs de créer des bibliothèques découplées des implémentations clientes HTTP. Cela rendra les bibliothèques plus réutilisables, car cela réduira le nombre de dépendances et la probabilité de conflits de versions.

Un deuxième objectif est que les clients HTTP puissent être remplacés selon le principe de substitution de Liskov. Cela signifie que tous les clients doivent se comporter de la même manière lors de l'envoi d'une demande.

## Définitions

- ```Client``` - Un client est une bibliothèque qui implémente cette spécification dans le but d'envoyer des messages de demande HTTP compatibles PSR-7 et de renvoyer un message de réponse HTTP compatible PSR-7 à une bibliothèque appelante.
- ```Calling Library``` - Une bibliothèque d'appels est tout code qui utilise un client. Il n'implémente pas les interfaces de cette spécification mais consomme un objet qui les implémente (un Client).

## Client

Un Client est un objet implémentant ```ClientInterface```.

Un client peut:

- Envoyer une requête HTTP modifiée à partir de celle qui a été fournie. Par exemple, il pourrait compresser un corps de message sortant.
- Modifier une réponse HTTP reçue avant de la renvoyer à la bibliothèque appelante. Par exemple, il peut décompresser le corps d'un message entrant.

Si un client choisit de modifier soit la demande HTTP, soit la réponse HTTP, il doit s'assurer que l'objet reste cohérent en interne. Par exemple, si un client choisit de décompresser le corps du message, il doit également supprimer l'en- “Content-Encoding”tête et ajuster l'en- “Content-Length”tête. Notez qu'en conséquence, puisque les objets PSR-7 sont immuables , la bibliothèque appelant ne doit pas supposer que l'objet transmis “ClientInterface::sendRequest()” sera le même objet PHP qui est réellement envoyé. Par exemple, l'objet Request qui est renvoyé par une exception peut être un objet différent de celui passé à “sendRequest()”, donc la comparaison par référence (===) n'est pas possible.Un client doit rassembler une réponse HTTP 1xx à plusieurs étapes elle-même afin que ce qui est renvoyé à la bibliothèque appelante soit une réponse HTTP valide de code d'état 200 ou supérieur.

## Error handling

Un client ne doit pas traiter une demande HTTP ou une réponse HTTP bien formée comme une condition d'erreur. Par exemple, les codes d'état de réponse dans la plage 400 et 500 ne doivent pas provoquer d'exception et doivent être renvoyés à la bibliothèque appelant normalement. Un client doit lancer une instance de ```Psr\Http\Client\ClientExceptionInterface``` si et seulement s'il est incapable d'envoyer la demande HTTP du tout ou si la réponse HTTP n'a pas pu être analysée dans un objet de réponse PSR-7. Si une demande ne peut pas être envoyée parce que le message de demande n'est pas une demande HTTP bien formée ou qu'il manque une information critique (telle qu'un hôte ou une méthode), le client doit lancer une instance de ```Psr\Http\Client\RequestExceptionInterface```. Si la demande ne peut pas être envoyée en raison d'une défaillance du réseau de quelque nature que ce soit, y compris un délai d'attente, le client doit lancer une instance de ```Psr\Http\Client\NetworkExceptionInterface```. Les clients peuvent lancer des exceptions plus spécifiques que celles définies ici (a ```TimeOutException``` ou ```HostNotFoundException``` par exemple), à ​​condition qu'ils implémentent l'interface appropriée définie ci-dessus.

## Les interfaces

“ClientInterface” :

```php
namespace Psr\Http\Client;

use Psr\Http\Message\RequestInterface;
use Psr\Http\Message\ResponseInterface;

interface ClientInterface
{
    /**
     * @param RequestInterface $request
     * @return ResponseInterface
     * @throws \Psr\Http\Client\ClientExceptionInterface
     */
    public function sendRequest(RequestInterface $request): ResponseInterface;
}
```

“ClientExceptionInterface” :

```php
namespace Psr\Http\Client;

interface ClientExceptionInterface extends \Throwable
{
}
```

“RequestExceptionInterface” :

```php
namespace Psr\Http\Client;

use Psr\Http\Message\RequestInterface;

interface RequestExceptionInterface extends ClientExceptionInterface
{
    /**
     * @return RequestInterface
     */
    public function getRequest(): RequestInterface;
}
```

“NetworkExceptionInterface” :

```php
namespace Psr\Http\Client;

use Psr\Http\Message\RequestInterface;

interface NetworkExceptionInterface extends ClientExceptionInterface
{
    /**
     * @return RequestInterface
     */
    public function getRequest(): RequestInterface;
}
```

