# Contenu de ./0010 - Introduction/content.md

Cette introduction au cours du langage HTML traite, de manière générale, des différentes fonctions de ce langage et de sa sémantique générale.

Le HTML est le langage de base se trouvant derrière toutes les pages web. Il permet de les structurer, mais ne permet pas la mise en forme du site. 

Ce cours se base sur les dernières versions stables de ce langage, à savoir HTML5 au moment où ces lignes sont écrites.

## Qu'est-ce que le HTML?

- Le HTML est l’acronyme de Hyper Text Markup Language
- Le HTML est le langage de balisage standard pour la création de pages Web
- Le HTML décrit la structure d'une page Web
- Le HTML se compose d'une série d'éléments entourés de balises
- Les éléments HTML indiquent au navigateur comment organiser le contenu
- Les balises autour des éléments HTML permettent d’indiquer le type de contenu (titre, paragraphe, liste, tableau, etc.).

L’exemple ci-dessous présente la structure de base d’une page HTML, avec un titre :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8" />
    <title>Cours HTML</title>
</head>
<body>
    <h1>Titre du document</h1>
</body>
</html>
```

Dans l’exemple ci-dessus, la déclaration ```<!DOCTYPE html>``` indique au navigateur que le document contient du HTML ainsi que la version du langage utilisée pour la construction du site web.

Ensuite, la balise ```<html>``` permet d’indiquer au navigateur que le code HTML commence à cet endroit. Cette balise - comme beaucoup en HTML - est fermée à la fin du document avec ```</html>```, indiquant que le document HTML s’arrête à cet endroit. De plus, l’attribut ```lang="fr"``` permet d’indiquer que la page web est rédigée en français.

Les balises ```<head></head>``` reçoivent des informations qui ne seront pas directement affichées sur la page web. Dans l’exemple ci-dessus, la ligne suivante : ```<meta charset="utf-8" />``` permet d’indiquer que le document utilise l’encodage UTF-8, permettant d’afficher correctement les accents. Elle contient aussi la balise ```<title>``` permettant de définir un titre pour la page web, titre qui sera affiché dans l’onglet du navigateur.

Enfin, les balises ```<body></body>``` définissent le corps de la page HTML. Tout ce qui se trouve entre ces balises est affiché dans la page web. Dans l’exemple ci-dessus, il y a un titre, entouré des balises ```<h1></h1>```. C’est également entre les balises ```<body></body>``` qu’il y aura les paragraphes, les en-tête, etc.

## Qu'est-ce qu'un élément HTML?

En HTML, un élément est entouré de deux balises : **une balise de début**, dite “ouvrante”, contenant le nom de l’élément, puis **le contenu de l’élément**, pour finir avec une **balise de fin**, dite “fermante”, commençant par un slash (/) pour indiquer que c’est une balise fermante. Le nom de l’élément indiqué dans la balise se trouve entre des chevrons : ```<>```.

Exemple :

```html
<h1>Introduction au HTML</h1>
```

L’exemple ci-dessus est constitué d’une balise d’ouverture ```<h1>``` et d’une balise de fermeture ```</h1>``` afin d’indiquer que cet élément est un titre.

__Remarque__ : il existe quelques exceptions à cette règle que nous aborderons dans d'autres cours.

## Navigateurs Web

Le rôle principal des navigateurs web tels que Google Chrome, Mozilla Firefox, Opera, Safari, etc. est d’interpréter le code HTML dans le document et d’afficher la page web en tenant compte des balises. 

__Remarque__ : Les balises HTML ne sont pas affichées sur la page web, mais permettent d’indiquer au navigateur comment afficher tel ou tel élément. Par exemple, les titres ```<h1>``` sont affichés en gros.

En reprenant l’exemple de la structure de base d’un document HTML, donné dans le point “qu’est-ce que le HTML” : 

```html
<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8" />
	<title>Titre de la page web</title>
</head>
<body>
	<h1>Titre du document</h1>
</body>
</html>
```

Voici ce que donne le code HTML de cet exemple :
![Rendu du code ci-dessus](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/D%C3%A9veloppement%20G%C3%A9n%C3%A9rique/HTML/courses/0010%20-%20Introduction/images/image2.png)

Comme indiqué, les balises HTML ne sont pas affichées mais ont permis au navigateur d’afficher “Titre du document” en gros.

## Structure d’une page HTML

Afin de mieux visualiser comment est structurée une page web grâce au HTML, voici un schéma qui reprend le code de l’exemple du point précédent :

![Schématisation du code précédent](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/D%C3%A9veloppement%20G%C3%A9n%C3%A9rique/HTML/courses/0010%20-%20Introduction/images/image1.png)


# Contenu de ./0020 - Bases/content.md

L’objectif de ce cours est de comprendre plus précisément le rôle du HTML dans la création d’une page web.

## Le HTML et les balises

HTML est l’acronyme de “HyperText Markup Language”, signifiant littéralement : “langage de balisage hypertexte”, hypertexte faisant référence à tout ce qui est autour du texte. 

Par conséquent, le HTML est un langage de balises, celles-ci permettent à la fois de structurer la page web, mais également d’indiquer au navigateur comment afficher un élément.

Le langage HTML permet également de créer des liens hypertextes, des images, des vidéos, etc. Tous ces aspects du langage seront traités dans les différents cours. 

## Les titres

Les titres, en HTML, sont structurés avec des balises ```<hn>```, “n” représentant un chiffre de 1 à 6. Ceci pour la simple raison que les titres respectent une hiérarchie, ```<h1>``` représentant un titre principal ou important, et ```<h6>```, en étant le plus bas niveau de titre dans la hiérarchie, représente un titre beaucoup, beaucoup moins important.

Exemple :

```html
<h1>Titre de niveau 1 (important)</h1>
<h6> Titre de niveau 6 (beaucoup, beaucoup moins important)</h6>
```

## Les paragraphes

En HTML, les paragraphes sont définis avec la balise ```<p>```. Lorsque cette balise est fermée avec ```</p>```, un saut de ligne est automatiquement ajouté entre le paragraphe actuel et celui en dessous.

Exemple :

```html
<p>Ceci est un paragraphe</p>
```

## Liens HTML

Il existe deux types de liens, en HTML :

- Les liens “externe”, redirigeant l’utilisateur vers un autre site web, en fournissant l’URL de l’autre site web
- Les liens “internes’, permettant à l’utilisateur de naviguer entre les différentes pages du site, en fournissant le chemin d’accès au fichier HTML concerné.

Pour définir un lien en langage HTML, il faut utiliser la balise ```<a></a>```. Pour spécifier l’URL d’un autre site ou le chemin d’accès à un autre fichier HTML, l’attribut href doit être utilisé. Enfin, le texte du lien cliquable est placé entre les balises ```<a></a>```.

Exemple avec un lien menant vers un autre site web :

```html
<a href="www.google.com">Google</a>
```

Exemple avec lien menant vers une autre page du site :

```html
<a href="index.html">Accueil</a>
```

## Images

En HTML, les images sont définies avec la balise ```<img>```. Le chemin d’accès à l’image est spécifié dans l’attribut ```src```.

__Remarque__ : La balise ```<img>``` fait partie des exceptions, car elle **n’a pas de balise fermante**. Ainsi n’est-il pas possible d’écrire ```<img></img>```. De manière générale, un slash est ajouté à la fin de la balise.

Exemple :

```html
<img src="dossier/image.jpg" />
```

Par soucis d’accessibilité pour les personnes non-voyantes et pour les cas où l’image de s’afficherait pas correctement, il est courant d’utiliser l’attribut ```alt```. Cet attribut fournit un texte alternatif (très court, en général, un mot ou deux suffisent pour décrire l’image) qui s’affiche en cas de défaut d’affichage de l’image, ou qui sera lu par le navigateur des personnes non voyantes. 

Exemple :

```html
<img src="image.jpg" alt="logo" />
```

## Inspecteur d’élément

Il arrive à tout développeur de devoir un jour "déboguer" son code. En effet, lorsque ce dernier ne permet pas d’obtenir le rendu voulu, le développeur doit chercher l’erreur commise afin de la résoudre pour que tout rentre dans l’ordre.

Pour faciliter le travail des développeurs, les concepteurs de navigateurs internets (notamment Mozilla Firefox et Google Chrome) ont développé un outil très utile : l’inspecteur d’élément. Cet outil permet de consulter le code HTML et CSS d’une page web et de le modifier temporairement (au prochain rechargement de la page, le code sera revenu “à la normale”).

Pour accéder à l’inspecteur d’élément, il suffit de faire un clic droit sur une page web et de cliquer sur “inspecter”.

Sur Google Chrome, voici à quoi ressemble l’inspecteur d’éléments :

![Inspecteur d'éléments](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/D%C3%A9veloppement%20G%C3%A9n%C3%A9rique/HTML/courses/0020%20-%20Bases/images/image2.png)

L'inspecteur donne des informations détaillées sur l'élément actuellement sélectionné. Le bouton “Sélectionner un élément” permet de sélectionner un élément à inspecter :

![Inspecteur d'éléments](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/D%C3%A9veloppement%20G%C3%A9n%C3%A9rique/HTML/courses/0020%20-%20Bases/images/image3.png)

Le volet style permet de consulter le code CSS appliqué à un élément. Le CSS est le langage permettant d’appliquer du style à une page web. Ce langage est abordé dans un autre cours. 

![Onglet Style](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/D%C3%A9veloppement%20G%C3%A9n%C3%A9rique/HTML/courses/0020%20-%20Bases/images/image1.png)

# Contenu de ./0030 - Éléments/content.md

Ce cours aborde plus en détails les notions d’éléments et de balises, en HTML.

## Les éléments

Tout le principe du HTML est basé sur la notion d’élément. Lorsque cette notion est comprise, l’essentiel du langage HTML est également compris. 

Les éléments HTML vont permettre de créer la structure de la page HTML, de définir chaque contenu de la page, et de transmettre certaines informations utiles au navigateur pour afficher la page.

En HTML, les éléments permettent à la fois de définir la **structure d’une page web**, en l’organisant avec un en-tête, un corps de page et un pied de page, des titres, des sous-titres, des paragraphes, etc., et également de définir chaque contenu de la page tel que les titres, les paragraphes, les liens (etc…), mais également de **transmettre des informations** au navigateur afin que ce dernier affiche la page correctement. Par exemple lorsque l’attribut **lang** est défini dans la balise ```<html>```, cela informe le navigateur de la langue utilisée sur la page qu’il affiche, ou encore l’encodage qui permet d’indiquer au navigateur la manière dont il va devoir afficher les accents, etc...

Dans un document HTML, les éléments sont utilisés pour **baliser** le contenu, d’où la seconde dénomination : **les balises**.

## Les balises

En HTML, il existe deux types de balises :

- Les balises doubles, composées d’une balise ouvrante et d’une balise fermante
- Les balises orphelines, dont la particularité est qu’elles n’ont pas de balises fermantes

La balise ouvrante est composée de deux chevrons (```<>```) et du nom de l'élément placé entre ces deux chevrons. La balise fermante est quasiment similaire, à ceci près qu’il faut ajouter un slash (```/```) avant le nom de l’élément. Le contenu est placé entre ces deux balises. 

Pour les balises orphelines, qui n’ont pas de balises fermantes, il est d’usage courant d’ajouter un slash juste avant le deuxième chevron, pour indiquer que la balise est orpheline. Cependant, cela n’est pas obligatoire.

Exemple d’une balise double :

```html
<p>Je suis un paragraphe</p>
```

Exemple d’une balise orpheline : 

```html
<img src="photo.jpg" alt="logo" />
```

Ainsi, en ce qui concerne les balises standard (ou non orpheline), ne faut-il jamais oublier de fermer la balise afin d’éviter de perturber l’affichage du contenu par la suite. 

Voici un exemple complet :

```html
<body>
	<h1>Titre principal</h1>
	<p>Je suis un paragraphe</p>
	<img src="illustration.jpg" alt="illustration" />
</body>
```

# Contenu de ./0040 - Attributs/content.md

Ce cours traite des attributs et de leur utilité au sein des balises HTML.

## Les attributs

Les attributs sont des valeurs supplémentaires au sein d’une balise HTML, permettant d’apporter des précisions, de modifier leur comportement, etc. Ils sont placés dans les balises ouvrantes et n’ont pas d’ordre particulier. 

Il arrive que certains attributs ne soient pas obligatoires mais fortement conseillés, pour améliorer le référencement, par exemple ; tandis que pour d’autres éléments HTML, l’utilisation de certains attributs spécifiques est obligatoire.
Le rôle des attributs est de compléter un élément, en lui fournissant, par exemple, une identité, ou encore en y ajoutant des informations sur la manière dont l’élément doit s’afficher. 

Un attribut ne contient qu’une seule valeur. Un mot, en général. Si plusieurs mots doivent être écrits au sein de l’attribut, il est possible d’ajouter un tiret entre chacun de ces mots, pour n’en former plus qu’un. 

La syntaxe d’un attribut est simple :

```html
<element attribut="valeur-de-l-attribut">Contenu</element>
```

Dans le cours précédent, des attributs ont déjà été utilisés avec des balises. Par exemple, pour ajouter une image au sein d’une page web, il faut utiliser le code HTML suivant :

```html
<img src="logo.png" alt="logo" />
```

Dans cette balise, l’élément ```<img />``` est d’abord complété par l’attribut ```src``` (pour source), permettant de préciser quelle image insérer et où elle se trouve, et également par l’attribut ```alt```, permettant d’afficher un texte alternatif en cas de problème d’affichage de l’image, ou qui peut permettre aux personnes malvoyantes visitant le site de savoir que l’image est en réalité un logo (certains équipements spéciaux permettent la lecture “à voix haute” du contenu de l’attribut ```alt```).

**Remarque** : Les guillemets autour des valeurs données aux attributs ne sont pas obligatoires. Cependant, le W3C, l’organisme chargé de standardiser l’utilisation du langage HTML, recommande de les utiliser. Bien que les guillemets doubles soient les plus utilisés, des guillemets simples peuvent également entourer les valeurs des attributs. Par souci de cohérence et d’habitude, nous vous recommandons d’utiliser systématiquement les guillemets doubles.

Exemple :

```html
<p style='color:blue'>Je suis un paragraphe</p>
```

## Les attributs de largeur et de hauteur

Les attributs de largeur et de hauteur, *width* et *height* en anglais, permettent de préciser la taille de l’image, mais pas de modifier ces valeurs. En fait, lorsque ces attributs sont renseignés, le navigateur réserve une place avec la largeur et la hauteur spécifiée sur la page pour pouvoir afficher l’image. Cela permet d’éviter un changement de mise en page lors du chargement de la page.

Exemple :

```html
<img src="logo.jpg" alt="logo" width="300px" height="200px">
```

Dans l’exemple ci-dessus, l’image a une largeur définie à 300 pixels et une hauteur définie à 200 pixels.

## L'attribut de style

Pour changer la couleur de la police d’écriture, par exemple, ou encore pour changer sa taille, ou changer la couleur d’arrière-plan d’un élément, etc., le langage HTML met à disposition l’attribut ```style```. Celui-ci permet d’intégrer du code CSS directement au sein du HTML. Aussi si cette pratique n’est pas conseillée, certains cas de figure entraînent l’obligation de l’utiliser.

Exemple : 

```html
<p style="color:blue">Je suis un paragraphe</p>
```

Dans cet exemple, la couleur de la police de ce paragraphe est définie à bleu.

## L'attribut lang

Dans les cours précédents, cet attribut à déjà été évoqué. Il s’ajoute à l’intérieur de la balise HTML et permet de préciser la langue de la page HTML, ceci pour aider les moteurs de recherche dans le référencement du site web.

Pour une page HTML en français, l’attribut ```lang``` reçoit la valeur ```fr``` (en minuscule).

Exemple :

```html
<!DOCTYPE html>
<html lang="fr">
...
</html>
```

Afin d’encore plus améliorer le référencement d’un site web, il est également possible d’ajouter un “code pays” comme valeur à l’attribut lang. Ainsi, pour un site internet créé en france, l’attribut lang ressemble à ceci :

```html
<!DOCTYPE html>
<html lang="fr-FR">
...
</html>
```

**Remarque** : La langue est écrite en minuscules, tandis que le code pays est écrit en majuscules.

## L’attribut de titre

Le langage HTML permet d’ajouter une info-bulle à afficher lorsque la souris reste un certain temps pointé sur un élément (état de *survol*). Pour ce faire, il faut utiliser l’attribut ```title``` et lui donner en valeur le texte à afficher dans l’info-bulle. Cet attribut est quasiment systématiquement utilisé pour les balises de liens, et même si non obligatoire, tout de même considéré comme tel.

Exemple :

```html
<a href="index.html" title="Revenir à la page d'accueil">Accueil</a>
```

Dans cet exemple, lorsque la souris reste un certain temps pointée sur le lien, une info-bulle s’affiche, contenant le texte “Revenir à la page d’accueil”.

# Contenu de ./0050 - Titres/content.md

Les titres, en HTML, sont définis sur 6 niveaux. Cette notion est abordée dans ce cours.

## Définition de titres en HTML

Les titres (*headings*, en anglais), sont définis avec la double balise ```<hn></hn>```. Il existe 6 niveaux de titres, en HTML - le niveau 1 étant le plus important et le niveau 6 le moins important - et ces niveaux permettent d’organiser et de hiérarchiser les contenus.

```html
<body>
    <!--Un titre très important-->
    <h1>Titre principal</h1>

    <!--Un titre important-->
    <h2>Titre important</h2>

    <!--Un autre titre important-->
    <h2>Titre important</h2>

    <!--Un titre un peu moins important-->
    <h3>Titre d'importance moyenne</h3>

    <!--Etc, etc.-->
    <h4>Un titre pas très important</h4>
    <h5>Un titre peu important</h5>
    <h6>Un titre vraiment peu important</h6>
</body>
```

**Remarque** : bien que conventionnellement seuls 6 niveaux de titres sont utilisés, le HTML ne présente aucune limite quant au nombre de niveaux de titre. Ainsi il est possible d’aller plus loin que **h6**, et d’utiliser par exemple **h7**, **h8**, **h9**, etc…

# Contenu de ./0060 - Paragraphes/content.md

Le langage HTML permet de définir des paragraphes et d’indiquer au navigateur comment les afficher.

## Les paragraphes

En HTML, un paragraphe est délimité par les balises ```<p></p>```. À chaque fois que la balise ```</p>``` ferme un paragraphe, le navigateur effectue un saut de lignes. 

Exemple :

```html
<body>
	<p>Ceci est un paragraphe</p>
	<p>Ceci est un autre paragraphe</p>
</body>
```

## Affichage HTML

Il n’est pas de règles précises quant à l’affichage des paragraphes par les navigateurs. Tout dépend de leurs paramètres, de leurs versions, etc. 

Néanmoins, il est important de noter qu’un paragraphe écrit sur plusieurs lignes en HTML apparaît sur une seule ligne lorsque le navigateur l’affiche. En effet, ce dernier supprime les sauts de lignes et espaces inutiles. 

Pour faire des retours à la ligne au sein d’un paragraphe, le langage HTML met à disposition la balise ```<br />```.

```html
<p>
Un paragraphe
Qui contient plusieurs lignes
Dans le code source 
Mais le navigateur
Les ignores
</p>

<p>
Un paragraphe
Qui contient         plusieurs lignes et espaces
Dans le code         source
Mais le        navigateur
Les ignores
</p>
<p> Ceci est un paragraphe écrit <br />
Sur plusieurs lignes et qui est affiché sur plusieurs <br />
Lignes grâce à la balise <br /></p>
```

## Bordure horizontale

Lorsque plusieurs idées sont évoquées sur une même page web, il est parfois intéressant de pouvoir séparer visuellement les différentes sections à l’aide d’une bordure horizontale. 

Le langage HTML permet cela grâce à la balise unique ```<hr>```.

*Remarque* : ```<hr>``` est une balise unique qui n’est pas auto-fermante et qui ne dispose pas de balise fermante non plus. Ainsi, si le développeur écrit ```<hr />```, la bordure horizontale ne s’affiche pas.

## Texte préformaté

Dans le troisième point de ce cours, il est expliqué qu’au sein des balises ```<p></p>```, les retours à la ligne n’étaient pas pris en compte par le navigateur. Ainsi, si un paragraphe doit revenir à la ligne, la balise ```<br />``` est utilisée. 

Cependant, lorsqu’un long paragraphe est composé de nombreux retours à la ligne, il est assez fastidieux de mettre des balises ```<br />``` à chaque retour à la ligne. 

Le langage HTML règle ce problème grâce aux balises ```<pre></pre>```. Grâce à cela, il est précisé au navigateur qu’il s’agit d’un texte préformaté. Le navigateur affichera donc le paragraphe dans une police de largeur fixe, tout en préservant les espaces et les retours à la ligne.

Exemple :

```html
<pre>
Un paragraphe

Qui contient plusieurs lignes

Dans le code source 

Mais le navigateur

Les ignore
</pre>
```


# Contenu de ./0070 - Styles/content.md

Bien que la méthode présentée soit fortement déconseillée pour styliser des éléments HTML, le langage permet d’inclure du style directement dans les balises. Notez que le présent cours n'est pas dédié au CSS.

## Attribut style

L’attribut **style** permet d’inclure du code CSS directement au sein du HTML, dans n’importe quelle balise, sans passer par un fichier tiers. Quelques exemples vous sont présentés ci-dessous, mais référez-vous aux cours sur le CSS afin de mieux cerner l’étendue des possibilités.

L’utilisation de cet attribut est assez simple : la **propriété CSS** est déclarée entre les guillemets, suivie de **deux points** (:) suivi de la **valeur** à attribuer à cette propriété, suivi d’un **point virgule** (;).

Concrètement, voici la syntaxe de l’attribut style :

```html
<h1 style="propriété-CSS: valeur;">
```

Exemple : 

```html
<body>
    <h1 style="background-color: red;">
        Titre du document
    </h1>
</body>
```

Dans cet exemple, le titre se voit définir un arrière plan de couleur rouge. 

## Couleur du texte

Pour définir la couleur d’un paragraphe, il faut utiliser la propriété ```color```, suivie du nom (en anglais) de la couleur à attribuer au paragraphe.

Exemple :

```html
<p style="color: red";>Je suis un paragraphe</p>
```

## Polices

Grâce à la propriété ```font-family```, il est également possible de définir la police à utiliser pour un paragraphe. Cette propriété reçoit en valeur le nom de la police à utiliser. 

Exemple :

```html
<p style="font-family:courier;">Je suis un paragraphe</p>
```

## Taille du texte

La propriété ```font-size``` définit la taille de la police d’un élément. Cette propriété prend en valeur la taille de la police (principalement en **pt** ou en pixels (**px**)).

```html
<p style="font-size:14pt;">Je suis un paragraphe</p>
```

Dans cet exemple, la police a une taille définie à 14.

## Alignement du texte

Pour définir l’alignement d’un texte, la propriété ```text-align``` doit être utilisée. Cette propriété reçoit une des 4 valeurs suivantes :

- **left** : le texte est aligné à gauche
- **center** : le texte est centré
- **right** : le texte est aligné à droite
- **justify** : le texte est justifié

Exemple :

```html
<p style="text-align:center;">Je suis un paragraphe</p>
```


# Contenu de ./0080 - Formatage/content.md

Le langage HTML met à disposition un certain nombre de balises permettant de pré-formater un texte. Cela va indiquer au navigateur comment afficher un élément, bien que pour certaines balises de pré-formatage, il n’existe pas de règles d’affichages précises. 

## Éléments de formatage HTML

Les balises de pré-formatages sont utilisées afin d’indiquer au navigateur qu’un élément doit s’afficher d’une certaine manière. 

Voici la liste des balises de pré-formatages, mises à disposition par le HTML :

- ```<b></b>``` Permet de mettre du texte en gras (bold, en anglais).
- ```<strong></strong>``` est généralement pour mettre en valeur un texte important. Il n’existe pas de règle d’affichage précise par les navigateurs pour ces éléments; néanmoins ils sont, en général, affichés en gras. 
- ```<i></i>``` permet de mettre du texte en italique.
- ```<em></em>``` définit une partie de texte - généralement un mot - à mettre en valeur. C’est une emphase. L’emphase est généralement utilisée pour insister sur un mot. De manière générale, le navigateur affiche le texte écrit entre ces balises en italique.
- ```<mark></mark>``` Définit un texte à mettre en évidence, un texte à “marquer”.
- ```<small></small>``` Permet de rendre un texte plus petit.
- ```<del></del>``` Défini un texte supprimé. Généralement, le navigateur supprime une ligne du paragraphe se trouvant entre ces balises.
- ```<ins></ins>``` Définit un texte inséré. De manière générale, un texte inséré est souligné par le navigateur, lors de l’affichage.
- ```<sub></sub>``` Définit un indice mathématique. L’indice est placé légèrement sous l’élément qui le précède et dans une police plus petite.
- ```<sup></sup>``` Définit un exposant, comme en mathématiques. Un exposant, par exemple, est le “me” de “Mme” qui est généralement placé un peu au-dessus du “M”, dans une taille de police plus petite.

## Éléments ```<i>``` et ```<em>```

L’élément ```<i></i>``` permet de mettre un texte en italique, tandis que ```<em></em>``` permet d’insister sur un mot. Ce mot est généralement affiché en italique, pour montrer que l’auteur du texte insiste particulièrement sur ce mot.

Exemple avec ```<i></i>``` :

```html
<i>Le texte est en italique</i>
```

Exemple avec ```<em></em>``` :

```html
<em>Insistance</em>
```

## Élément ```<small>```

L'élément HTML ```<small></small>``` définit un texte plus petit :

Exemple :

```html
<small>Texte plus petit</small>
```

## Élément ```<mark>```

L'élément HTML ```<mark></mark>``` définit le texte qui, pour une raison particulière, doit être marqué ou mis en valeur :

Exemple :

```html
<p>Il ne faut pas oublier les <mark>skis</mark></p>
```

## Élément ```<del>```

L'élément HTML ```<del></del>``` définit un texte comme étant “supprimé”. Cet élément est généralement utilisé pour montrer quelque chose d’incorrect, car les navigateurs affichent le texte en le barrant. 

Exemple :

```html
<p>Il ne faut pas oublier les <del>skis</del> snowboards</p>
```

## Élément ```<ins>```

L'élément HTML ```<ins></ins>``` définit un texte qui a été inséré dans un document. Bien qu’il n’y ait pas de règles d’affichage clairement définies pour les éléments insérés, les navigateurs soulignent généralement les textes insérés. 

Exemple :

```html
<p>Il ne faut pas oublier les <ins>skis</ins></p>
```

## Élément ```<sub>```

L'élément HTML ```<sub></sub>``` définit un indice mathématiques. L’indice est généralement placé plus bas que l’élément et dans une taille de police inférieure.

Exemple :

```html
<p>Il faut pas oublier les <sub>skis</sub></p>
```

## Élément ```<sup>```

L'élément HTML ```<sup></sup>``` définit un exposant mathématiques. Un exposant est généralement placé légèrement au-dessus de l’élément, dans une police plus petite. 

Exemple :

```html
<p>Il faut pas oublier les <sup>skis</sup></p>
```

# Contenu de ./0090 - Citations/content.md

Afin que les développeurs puissent respecter les standards et droits d’auteurs concernant une œuvre, ainsi que le droit à la courte citation, le langage HTML met à disposition plusieurs balises. Il est ainsi possible de citer les sources, le nom de l’auteur, le titre d’une œuvre, etc.

## L'élément ```<blockquote>```

L’élément ```<blockquote></blockquote>``` indique que le texte est une citation longue. Dans un ```<blockquote>```, les retours à la ligne sont respectés par le navigateur. 

Le HTML permet également d’utiliser l’attribut cite avec cette balise, afin d’indiquer la source de la citation. Par exemple :

```html
<body>
    <!-- Bloc de citation sans l'attribut cite -->
    <blockquote>
        <p>Bloc de citation</p>
    </blockquote>

    <!-- Bloc de citation avec l'attribut cite -->
    <blockquote cite="https://url.com">
        <p>Bloc de citation</p>
    </blockquote>
</body>
```

## L’élément ```<q>```

L’élément ```<q></q>``` (raccourci de *quote*, “citation” en anglais) indique le texte est une citation. Cet élément est utilisé pour les citations courtes, qui ne nécessitent pas de respecter les retours à la ligne. 

Bien qu’il n’y ait pas de règles d’affichages définies, la plupart des navigateurs modernes affichent les citations placées entre les balises ```<q></q>``` avec des guillemets.

Avec cet élément aussi, l’attribut ```cite``` est utilisable afin de fournir la source de la citation.

Exemple :

```html
<body>
    <!-- Faire une citation en incise dans le paragraphe -->
    <p>Chaque fois que Kenny est tué, Stan dira
        <q cite="http://fr.wikipedia.org/wiki/Kenny_McCormick#Le_dialogue_rituel">
            Oh mon Dieu, ils ont tué Kenny !
        </q>.
    </p>
</body>
```

## L’élément ```<cite>```

```<cite></cite>``` permet d’indiquer le titre d’une œuvre (livre, chanson, sculpture, peinture, etc.) La référence peut être abrégée selon la convention d'utilisation utilisée pour ajouter des métadonnées de référence. Par exemple, pour Arthur Rimbaud, les métadonnées de référence permettent d’écrire A. Rimbaud.

Exemple :

```html
<body>
    <p>Plus d'informations sont disponibles dans <cite>[ISO-0000].</cite></p>
</body>
```

## L’élément ```<abbr>```

L’élément ```<abbr></abbr>``` est utile afin d’indiquer que le texte placé entre les balise est un acronyme ou une abréviation. Cela permet de fournir des informations utiles aux navigateurs, aux systèmes de traduction et aux moteurs de recherche.

Exemple :

```html
<p>La ville de <abbr title="Toulouse">TLS</abbr> est belle.</p>
```

## L’élément ```<address>```

Cet élément est utilisé afin d’indiquer les informations de contact d’un auteur et/ou propriétaire d’un document ou d’un article. Ces informations sont, de manière générale, une adresse email, une adresse URL, une adresse de domicile, un numéro de téléphone, un profil sur les réseaux sociaux, etc. 

Le texte placé entre ```<address>``` et ```</address>``` est généralement affiché en italique, et les navigateurs ajoutent toujours un saut de ligne avant et après l’élément.

Exemple :

```html
<address>
Écrit par John Doe.<br>
Venez sur:<br>
google.com<br>
</address>
```

## L’élément ```<bdo>```

BDO signifie Bi-Directional Override ou l'élément de surcharge bidirectionnelle en français. La balise HTML ```<bdo>``` est utilisée pour remplacer la direction actuelle du texte. Ainsi, la direction d’un texte peut être changée pour aller de la droite vers la gauche, par exemple.

La direction du texte est définie avec l’attribut dir, qui peut recevoir une des valeurs suivantes :

- **ltr** : pour un texte allant de gauche à droite (*left-to-right*, en anglais).
- **rtl** : pour un texte allant de droite à gauche (*right-to-left*, en anglais).
- **auto** : Selon la nature du contenu, le navigateur décide de la direction.

Exemple avec un texte allant de la droite vers la gauche :

```html
<bdo dir="rtl">Le texte est écrit de droite vers la gauche</bdo>
```

# Contenu de ./0100 - Commentaires/content.md

Comme tout langage qui se respecte, le langage HTML donne au développeur la possibilité d’écrire des commentaires pour son code.

## Définition et utilité des commentaires en HTML

Les commentaires sont des lignes de texte qui ne sont **pas interprétées** par le navigateur (cela signifie que le navigateur n’affiche pas les commentaires). Ils sont utilisés afin d’expliquer certaines parties de code qui peuvent s’avérer compliqués à comprendre autrement. C’est également utile lorsque le développeur sait qu’il laissera son code de côté pendant un moment. S’il a commenté certains bouts de code, il lui sera ainsi plus facile de comprendre ce qu’il a voulu faire lorsqu’il se replongera dans son code.

Les commentaires peuvent être très utiles dans trois situations principales :

- Pour les projets de grande envergure, afin de comprendre pourquoi une partie d’un code a été écrit et/ou pour expliquer ce qu’elle fait.
- Si plusieurs développeurs travaillent sur un même projet, les commentaires s’avèrent utiles pour comprendre ce que chacun fait. Cela rend également possible la “distribution” du code. Si un autre développeur reprend le projet, il lui est ainsi plus facile de comprendre le code écrit par son prédécesseur
- Il arrive qu’un développeur ait besoin de faire des tests pour comprendre, par exemple, pourquoi un élément ne s’affiche pas correctement. Les commentaires sont alors utilisés afin “d'isoler un” morceau de code et de le rendre ainsi “invisible” pour le navigateur. 

## Écrire des commentaires en HTML

Les commentaires, en HTML comme dans de nombreux autres langages, peuvent être écrits sur une seule ligne ou s’étendre sur plusieurs lignes. Cependant, contrairement à de nombreux autres langages informatiques, en HTML la syntaxe des commentaires est strictement la même que ces commentaires soient écrits sur une seule ligne ou qu’ils s’étendent sur plusieurs lignes.

En HTML, la syntaxe des commentaires est la suivante :

```html
<!-- Ceci est un commentaire en HTML --> 
```

__Remarque__ : Il est important que la balise fermante du commentaire ne prenne pas de point d’exclamation, contrairement à la balise ouvrante.

Exemple :

```html
<body>
    <!-- Deux titres -->
    <h1>Titre principal</h1>
    <h2>Titre important</h2>

    <!-- Des paragraphes
    Écrit sur plusieurs lignes -->
    <p>Je suis le premier paragraphe</p>
    <p>Et mois le second</p>
</body>
```

__Remarque__ : En langage HTML, les commentaires sont visibles par tout un chacun. Pour ce faire, il suffit simplement de faire un clic droit sur la page web et de cliquer sur “Afficher le code source de la page”. **Ainsi est-il vital de ne pas mettre d’informations sensibles dans les commentaires**. 

# Contenu de ./0110 - Couleurs/content.md

Le langage HTML permet de définir des couleurs pour les différents éléments de la page web, en utilisant les propriétés appropriées dans l’attribut style. 

## Couleurs

Le langage HTML met à disposition plusieurs moyens de définir la couleur d’un élément. En effet, il est possible de préciser directement le nom de la couleur, en anglais (red, green, blue, orange, etc., ou encore en utilisant une valeur hexadécimale, une valeur RGB ou RGBA.

Une couleur hexadécimale est un ensemble de lettres et de chiffres, précédé du signe dièse (**#**), représentant la quantité de vert de rouge et de bleu composant la couleur en question. La couleur blanche, en hexadécimale est la suivante : #FFFFFF (souvent raccourcie #fff).

Le RGB (pour red, green, blue) est également la quantité de rouge, de vert et de bleu présent dans une couleur. La différence avec la notation hexadécimale, est que le RGB reçoit, pour chaque couleur (rouge, vert, bleu), un chiffre entre 0 et 255. Par exemple, en RGB, la couleur rouge serait définie ainsi : RGB(255, 0, 0).

RGBA est presque identique à RGB, à la différence près qu’en plus, il reçoit un chiffre entre 0 et 1 pour définir le degré d’opacité de la couleur ; 0 étant une transparence totale, 1 une opacité totale.

Exemple avec les noms de couleurs en anglais :

``` html
<body>
    <!-- Paragraphe avec fond couleur Tomato -->
    <p style="background-color:Tomato;">Tomato</p>
    <!-- Paragraphe avec fond couleur Orange -->
    <p style="background-color:Orange;">Orange</p>
    <!-- Paragraphe avec fond couleur DodgerBlue -->
    <p style="background-color:DodgerBlue;">DodgerBlue</p>
    <!-- Paragraphe avec fond couleur MediumSeaGreen -->
    <p style="background-color:MediumSeaGreen;">MediumSeaGreen</p>
    <!-- Paragraphe avec fond couleur Gray -->
    <p style="background-color:Gray;">Gray</p>
    <!-- Paragraphe avec fond couleur Slate Blue -->
    <p style="background-color:SlateBlue;">SlateBlue</p>
    <!-- Paragraphe avec fond couleur Light Gray -->
    <p style="background-color:LightGray;">LightGray</p>
</body>
```

Exemple avec l’hexadécimale, le RGB et le RGBA :

```html
<body>
    <p>D'autres valeurs pour la couleur Tomato :</p>
 
    <!-- Paragraphe avec fond Tomata en rgb -->
    <p style="background-color:rgb(255, 99, 71);">rgb(255, 99, 71)</p>
    <!-- Paragraphe avec fond Tomata en hexadécimal -->
    <p style="background-color:#ff6347;">#ff6347</p>
    <!-- Paragraphe avec fond Tomata en RGBA -->
    <p style="background-color:rgba(0, 0, 255, 0,5);">rgba(0, 0, 255, 0,5)</p>
</body>
```

## Couleur du texte

Pour définir la couleur du texte, il suffit passer la propriété color à l’attribut style, suivie de la couleur à attribuer à l’élément.

Exemple :

```html
<!-- Texte de couleur Tomato -->
<p style="color:Tomato;">Tomato</p>
<!-- Texte de couleur DodgerBlue -->
<p style="color:DodgerBlue;">DodgerBlue</p>
<!-- Texte de couleur MediumSeaGreen -->
<p style="color:MediumSeaGreen;">MediumSeaGreen</p>
```

## Couleur de la bordure

L’attribut style permet également d’ajouter une bordure autour d’un élément. Pour ce faire, la propriété border doit être utilisée, suivie de l’épaisseur de la bordure (1 pixel, par exemple), puis du style de la bordure (solid, pour une bordure au trait plein, ou dashed pour une bordure en pointillés), puis, enfin, du nom de la couleur à attribuer à la bordure. 

Exemple :

```html
<!-- Bordure de couleur Tomato large de 2px et de type solid -->
<p style="border:2px solid Tomato;">Tomato</p>
<!-- Bordure de couleur DodgerBlue large de 2px -->
<p style="border:2px solid DodgerBlue;">DodgerBlue</p>
<!-- Bordure de couleur MediumSeaGreen large de 2px -->
<p style="border:2px solid MediumSeaGreen;">MediumSeaGreen</p>
```

# Contenu de ./0120 - Liens/content.md

Les liens représentent un élément important d’un site web. En effet, ils permettent à l’utilisateur de naviguer entre les différentes pages d’un site, ou d’être redirigés vers un autre site en cliquant sur un lien en particulier. Les liens permettent aussi à l’utilisateur de contacter le propriétaire du site, entre autres.

## Créer des liens en HTML

Il existe différents types de liens :

- **Les liens externes** : ce sont des liens qui redirigent l’utilisateur vers un autre site web.
- **Les liens internes** :  ce sont les plus utilisés. En effet, ils permettent à l’utilisateur de naviguer entre les différentes pages d’un site internet.
- **Les liens d’ancres** : ce type de liens sont utilisés comme raccourci sur les pages webs particulièrement longues. Ils donnent la possibilité à l’utilisateur de se rendre à une section plus basse du site, sans que cet utilisateur n’ai besoin de faire défiler la page jusqu’à la partie qui l’intéresse. 

Peu importe le type de lien que le développeur souhaite utiliser pour le site qu’il est en train de construire, un lien en HTML se construit de la manière suivante :

```html
<a href="URL">Texte du lien</a>
```

L’attribut ```href``` est utilisé soit pour indiquer le chemin d’accès vers une autre page du site web, soit pour indiquer l’URL du site web sur lequel l’utilisateur doit être redirigé, soit pour indiquer la section de la page sur laquelle l’utilisateur va être redirigé, dans le cas d’un lien d’ancre. 

## Créer des liens externes

Les liens externes sont destinés à rediriger l’utilisateur vers un autre site web.

En HTML, pour créer un lien externe, il faut passer à l’attribut ```href``` l’URL du site web sur lequel l’utilisateur doit être redirigé.

Exemple :

```html
<body>
    <p>Lien externe</p>

    <!-- Redirige vers Google -->
    <a href="https://www.google.fr/">Lien externe vers Google</a>
</body>
```

## Créer des liens internes 

Le but des liens internes est de permettre à l’utilisateur de naviguer entre les différentes pages du site web.

Pour ce faire, l’attribut ```href``` reçoit en valeur le chemin d’accès qui mène au fichier HTML vers lequel l’utilisateur sera redirigé. 

Si le fichier HTML vers lequel l’utilisateur doit être redirigé se trouve dans le même dossier que le fichier actuel, la valeur passée à href ressemble à ceci :

```html
<a href="nom_du_fichier.html">
```

Cependant, pour des raisons d’organisation, il est possible que le fichier HTML vers lequel l’utilisateur doit être redirigé se trouve dans un autre dossier. Dans un tel cas, la valeur passée à href ressemble à ceci :

```html
<a href="dossier/nom_du_fichier.html">
```

Exemple avec un fichier HTML se trouvant dans le même dossier que le fichier actuel :

```html
<body>
    <p>Lien interne</p>

    <!-- Redirige vers le fichier contact.html -->
    <a href="contact.html">Lien interne vers la page contact</a>
</body>
```

Exemple avec un fichier HTML se trouvant dans un autre dossier :

```html
<body>
    <p>Lien interne</p>

    <!-- Redirige vers le fichier contact.html dans le répertoire dossier -->
    <a href="dossier/contact.html">Lien interne vers la page contact</a>
</body>
```

## Ouvrir un lien dans un nouvel onglet 

De manière générale, pour des raisons de confort et pour éviter à l’utilisateur de quitter le site web qu’il est en train de consulter, un lien externe ouvrira dans un nouvel onglet le site vers lequel l’utilisateur doit être redirigé.

Pour ce faire, l’attribut ```target``` est utilisé, et reçoit une des valeurs suivantes :

- **_self** : Par défaut. Ouvre le document dans la même fenêtre ou le même onglet
- **_blank** : Ouvre le document dans une nouvelle fenêtre ou un nouvel onglet, c’est le plus couramment utilisé
- **_parent** : Ouvre le document dans le cadre parent
- **_top** : Ouvre le document dans le corps entier de la fenêtre

Exemple :

```html
<body>
    <p>Lien externe dans un nouvel onglet</p>

    <!-- Redirigé vers Google dans un nouvel onglet -->
    <a href="https://www.google.fr/" target="_blank">Lien externe vers Google</a>
</body>
```

## Créer des liens d’ancre

Pour rappel, un lien d’ancre est un lien menant vers une partie précise d’une même page web. Ce système est utilisé lorsqu’une page web est très longue et que le développeur souhaite éviter à l’utilisateur d’avoir à faire défiler la page jusqu’à la partie qui l’intéresse.

La création d’un lien d’ancre est assez particulière. Elle se fait en deux parties. 

Dans un premier temps, il faut donner une valeur à l’attribut ```id``` pour chaque élément qui est pointé par un lien. Ensuite, le nom de l’id donné à l’élément est passé comme valeur à l’attribut ```href``` en le précédant du symbole “**#**”.

Exemple :

```html
<body>
    <!-- Créer un lien vers #p1 -->
    <a href="#p1">Vers paragraphe 1</a>
    <!-- Créer un lien vers #p2 -->
    <a href="#p2">Vers paragraphe 2</a>
    <!-- Créer un lien vers #p3 -->
    <a href="#p3">Vers paragraphe 3</a>

    <p id="p1">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam accumsan arcu nisi, quis efficitur diam
        congue vel. Aliquam erat volutpat. Quisque sodales posuere dolor vitae tempus. Curabitur ligula sapien,
        consectetur non tincidunt et, sodales id dolor. Etiam in bibendum velit. Sed tristique bibendum eleifend. Etiam
        tincidunt justo pretium felis ultricies maximus.
    </p>
    <p id="p2">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam accumsan arcu nisi, quis efficitur diam
        congue vel. Aliquam erat volutpat. Quisque sodales posuere dolor vitae tempus. Curabitur ligula sapien,
        consectetur non tincidunt et, sodales id dolor. Etiam in bibendum velit. Sed tristique bibendum eleifend. Etiam
        tincidunt justo pretium felis ultricies maximus.
    </p>
    <p id="p3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam accumsan arcu nisi, quis efficitur diam
        congue vel. Aliquam erat volutpat. Quisque sodales posuere dolor vitae tempus. Curabitur ligula sapien,
        consectetur non tincidunt et, sodales id dolor. Etiam in bibendum velit. Sed tristique bibendum eleifend. Etiam
        tincidunt justo pretium felis ultricies maximus.
    </p>
</body>
```

## Lien vers une adresse e-mail

Le langage HTML donne également la possibilité à l’utilisateur de pouvoir envoyer un mail au propriétaire d’un site web. Pour ce faire, l’attribut href reçoit en valeur un adresse mail, précédé de “**mailto:**”.

Exemple :

```html
<!-- Ouvre le logiciel de messagerie pour envoyer un mail directement à l'adresse mail john@doe.com -->
<a href="mailto:john@doe.com">Envoyer un mail</a>
```

## Ajouter une infobulle

Pour rappel, en HTML, une infobulle est une “bulle” contenant du texte, qui s’affiche lorsque l’utilisateur survole un lien avec la souris. 

Pour afficher une infobulle, l’attribut ```title``` doit être utilisé, avec pour valeur, le texte à afficher lorsque le lien sera survolé par la souris.

Cet attribut est, bien que non obligatoire, très utile à différentes fins : il permet de favoriser le référencement et joue également un rôle concernant l’accessibilité. Il est donc important de le considérer très fortement comme obligatoire.

Exemple :

```html
<!-- Redirigé vers Google et affiche "Go to google" au survol de la souris -->
<a href="https://www.google.com/" title="Go to Google">Faire une recherche</a>
```

# Contenu de ./0130 - Images/content.md

Il n'y a pas de sites web qui n’affichent pas d’images. Que ce soit pour le logo ou à des fins d’illustration, chaque site affiche au moins une image.

## Insérer des images

Pour afficher des images sur une page web, le langage HTML met à disposition l’élément ```<img></img>```. Cet élément est obligatoirement accompagné de l’attribut ```src```, qui sert à préciser le chemin d’accès de l’image à afficher.

Pour des raisons d’accessibilité, il est recommandé d’ajouter l’attribut ```alt```. Celui-ci reçoit en valeur un texte alternatif - court - décrivant l’image. Ce texte a deux utilités. La première est de permettre au navigateur d’afficher le texte alternatif en cas de problème d’affichage de l’image. La seconde, primordiale, permet de rendre le site web accessible à des personnes malvoyantes ou malentendantes. En effet, le texte alternatif sera littéralement lu par une voix artificielle lorsque l’utilisateur malvoyant ou aveugle se rendra sur le site web.

Comme pour les liens internes, évoqués dans le cours précédent, une image peut être soit enregistrée dans le même dossier que le fichier HTML, soit dans un dossier différent. 

Pour le premier cas, l’attribut ```src``` reçoit en valeur le nom de l’image à afficher, suivi de son extension (image.jpg, par exemple). 

Dans le second cas, l’attribut ```src``` reçoit d’abord le nom du dossier contenant l’image, suivi d’un slash (/), suivi du nom de l’image et de son extension (dossier/image.jpg, par exemple).

Exemple :

```html
<body>
    <!-- Affiche de l'image fond.png -->
    <img src="fond.png" alt="L'image est un fond">
</body>
```

## Lier une image depuis un site web externe

Afin de rendre un fichier HTML moins lourd et d’optimiser le temps d’affichage d’une page web, le langage HTML rend possible le fait d’afficher une image provenant directement d’un autre site web.

Pour ce faire, l’attribut ```src``` reçoit en valeur **l’URL complète** de l’image à afficher.

Exemple :

```html
<body>
    <!-- Affiche une image externe à l'aide d'une url -->
    <img src="https://cdn.pixabay.com/photo/2020/11/22/17/28/cat-5767334_960_720.jpg" alt="Un chat">
</body>
``` 

## Largeur et hauteur

Il existe deux moyens de définir la taille d’une image en HTML. La première consiste à utiliser les propriétés ```width``` et ```height``` au sein de l’attribut ```style```, la seconde consiste à utiliser directement les attributs HTML ```width``` et ```height```.

**Remarque** : 

- Lorsque les attributs ```width``` et ```height``` sont spécifiés, cela permet au navigateur de réserver un espace correspondant à la largeur et à la hauteur spécifiées au moment du chargement de la page. Cela permet notamment d’éviter un changement de mise en page lors du chargement de la page. 
- Depuis la version 5 du langage HTML, l’attribut ```width``` accepte seulement les largeurs en **pixels** et non plus en pourcentage.

Exemple avec l’attribut ```style``` :

```html
<!-- Affiche l'image moto.png et spécifiant la hauteur et la largeur -->
<img src="moto.png" alt="Il s'agit d'une photo de moto"  style="width: 500px; height: 600px;">
```

Exemple avec les attributs ```width``` et ```height``` :

```html
<!-- Affiche l'image moto.png et spécifiant la hauteur et la largeur -->
<img src="moto.png" alt="Il s'agit d'une photo de moto"  width="500" height="600">
```


# Contenu de ./0140 - Tableaux/content.md

Pour des raisons de clarté, il est parfois nécessaire d’organiser des données au sein d’un tableau. Le langage HTML permet de faire cela.

## Créer un tableau simple

En HTML, un tableau est créé ligne par ligne.

Pour commencer, le navigateur doit savoir qu’il s’apprête à afficher un tableau. Pour ce faire, les balises ```<table></table>``` sont utilisées afin de déclarer le tableau.

Ensuite, chaque ligne du tableau est créée avec les balises ```<tr></tr>```.

Enfin, les colonnes sont créées avec les balises ```<td></td>```, entourant le nom de chaque colonne.

Exemple :

```html
<body>
    <!-- Tableau -->
    <table>
        <!-- Première ligne -->
        <tr>
            <!-- Première colonne -->
            <td>Nom</td>
            <!-- Deuxième colonne -->
            <td>Prenom</td>
            <!-- Troisième colonne -->
            <td>Age</td>
            <!-- Quatrième colonne -->
            <td>Mail</td>
        </tr>
        <!-- Deuxième ligne -->
        <tr>
            <!-- Première colonne -->
            <td>John</td>
            <!-- Deuxième colonne -->
            <td>Doe</td>
            <!-- Troisième colonne -->
            <td>32</td>
            <!-- Quatrième colonne -->
            <td>johndoe@gmail.com</td>
        </tr>
        <!-- Troisième ligne -->
        <tr>
            <!-- Première colonne -->
            <td>John</td>
            <!-- Deuxième colonne -->
            <td>Doe</td>
            <!-- Troisième colonne -->
            <td>32</td>
            <!-- Quatrième colonne -->
            <td>johndoe@gmail.com</td>
        </tr>
    </table>
</body>
```

## Fusionner des cellules sur plusieurs colonnes

Pour fusionner ensemble plusieurs cellules sur plusieurs colonnes, l’attribut ```colspan``` est utilisé et reçoit en valeur le nombre de colonnes sur laquelle la cellule doit s’étendre.

Exemple :

```html
<table>
    <tr>
        <th>Nom</th>
        <!-- Utilise deux colonnes -->
        <th colspan="2">Téléphone</th>
    </tr>
    <tr>
        <td>John Doe</td>
        <td>0102030405</td>
        <td>0203040506</td>
    </tr>
</table>
```

## Fusionner des cellules sur plusieurs lignes

Pour fusionner des cellules sur plusieurs lignes, l’attribut ```rowspan``` est utilisé. Il reçoit en valeur le nombre de lignes sur lesquelles les cellules sont fusionnées. 

Exemple :

```html
<table>
    <tr>
        <th>Nom:</th>
        <td>John Doe</td>
    </tr>
    <tr>
        <!-- Utilise plus d'une ligne -->
        <th rowspan="2">Telephone:</th>
        <td>0102030405</td>
    </tr>
    <tr>
        <td>0203040506</td>
    </tr>
</table>
```

## Ajouter une légende

Le langage HTML permet d’ajouter une légende à un tableau grâce à l’élément ```<caption></caption>```.

Exemple :

```html
<table>
    <!-- Rajoute une légende -->
    <caption>Utilisateur</caption>
    <tr>
        <th>Nom</th>
        <th colspan="2">Téléphone</th>
    </tr>
    <tr>
        <td>John Doe</td>
        <td>0102030405</td>
        <td>0203040506</td>
    </tr>
</table>
```

# Contenu de ./0150 - Listes/content.md

Le langage HTML permet de créer des listes à puce (appelées listes non ordonnées) et des listes numérotées (appelées listes ordonnées).

## Les listes non ordonnées

Les listes non ordonnées sont utilisées pour répertorier des éléments qui n’ont pas besoin d’être ordonnés, qui n’ont pas de rapport particulier entre eux ou qui ne souffrent pas de hiérarchie. 

Une liste non ordonnée est définie grâce aux balises ```<ul></ul>``` (pour *unordered list*, liste non ordonnée, en anglais). Ensuite, chaque item de la liste est entouré des balises ```<li></li>``` (pour *list item*, item de liste, en anglais).

Exemple :

```html
<body>
    <!-- Liste non ordonnée -->
    <ul>
        <!-- Element -->
        <li>Ski</li>
        <!-- Element -->
        <li>Pomme</li>
        <!-- Element -->
        <li>Stylo</li>
    </ul>
</body>
```

## Les listes ordonnées

Les listes ordonnées sont utilisées pour des items liés entre eux ou qui souffrent d’une hiérarchie. Les items d’une liste ordonnée sont affichés avec des numéros devant, représentant leur importance dans la hiérarchie.

Une liste ordonnée est entourée des éléments ```<ol></ol>``` (pour *ordered list*, liste ordonnée, en anglais). Ici aussi, chaque item de la liste est entouré des balises ```<li></li>```.

Exemple :

```html
<body>
    <!-- Liste ordonnée -->
    <ol>
        <!-- Element -->
        <li>Introduction</li>
        <!-- Element -->
        <li>Partie I</li>
        <!-- Element -->
        <li>Partie II</li>
        <!-- Element -->
        <li>Partie III</li>
    </ol>
</body>
```

## Listes de description

Le HTML permet également de dresser une liste de descriptions. Ce genre de liste est généralement utilisé pour des définitions ou pour décrire des articles.

Une liste de descriptions est entourée des balises ```<dl></dl>```. Ensuite, chaque item de la liste est entouré des éléments ```<dt></dt>```. La description ou la définition, quant à elle, est entourée des balises ```<dd></dd>```.

Exemple :

```html
<!-- Liste de description -->
<dl>
    <!-- Premier terme -->
    <dt>Ski</dt>
    <!-- Description du terme ski -->
    <dd>- freerando pas de fond</dd>
    <!-- Deuxième terme -->
    <dt>Lunettes</dt>
    <!-- Description du terme lunettes -->
    <dd>- Des lunettes pas un masque</dd>
</dl>
```

# Contenu de ./0160 - Block & Inline/content.md

Chaque élément HTML a un niveau d’affichage qui lui est attribué par défaut. Ces niveaux influencent l’affichage des éléments par le navigateur et sont très importants lorsque le développeur commence à faire le design d’un site web.

## Block-level

Les éléments dits **block level**, comme leur nom l’indique, sont affichés comme des blocs par le navigateur. Cela signifie que chaque élément de type **block** s’affiche l’un en dessous de l’autre, prenant toute la largeur disponible - à moins qu’une largeur spécifique soit définie, grâce à l’attribut ```style```.

Voici une liste non exhaustive des éléments nativement traités comme des **blocks** par les navigateurs :

- ```<div>```
- ```<h1>``` à ```<h6>```
- ```<form>```
- ```<header>```
- ```<footer>```
- ```<section>```

Exemple :

```html
<body>
    <!-- Definit un block -->
    <div>Hello World</div>
</body>
```

## Inline

Les éléments de type **inline** continuent sur la ligne en cours et ne prennent que la largeur nécessaire à leur affichage. 

Ci-dessous, une liste non exhaustive des éléments **inline** en HTML :

- ```<span>```
- ```<a>```
- ```<img>```

Exemple :

```html
<body>
 <!-- Hello World ne commence pas sur une nouvelle ligne, car <span> étant un élément inline, il continue sur la ligne en cours -->
    <p>Je suis un paragraphe alors je vous dis <span> Hello World</span></p>
</body>
```

## L'élément ```<div>```

```<div></div>``` est utilisé comme conteneur pour d'autres éléments HTML. Cela signifie que ces balises entourent d’autres éléments HTML. Ainsi, toute la ```<div>``` sera affichée en **bloc**. 

L’élément ```<div>``` n’a pas d’attribut particulier. Néanmoins, il est commun que l’attribut ```id``` soit utilisé afin d’attribuer un **identifiant unique** à l’élément, permettant, par exemple de créer des liens d’ancres ou encore, plus tard, de pouvoir styliser l’ensemble de la ```<div>```.

Exemple :

```html
<!-- Div de fond noir et texte en blanc -->
<div id="contenant">
    <!-- Titre de niveau 2 -->
    <h2>Toulouse</h2>
    <!-- Paragraphe -->
    <p>Toulouse est une belle ville proche des Pyrénées dans le sud de la France.</p>
</div>
```

## L'élément ```<span>```

L'élément ```<span></span>``` est un élément utilisé, en général, pour marquer un mot ou un bout de phrase au milieu d’un paragraphe. C’est un élément de type **inline**, permettant donc de faire continuer la partie marquée sur la ligne en cours. 

Cet élément est principalement utilisé pour pouvoir, plus tard, styliser une partie d’un texte à mettre en valeur, par exemple, sans que cette partie ne soit affichée comme un élément de type **block**.

Exemple :

```html
<p>J'ai des skis <span class="couleur">jaune</span></p>
```

# Contenu de ./0170 - Classes/content.md

Le langage HTML donne la possibilité au développeur de donner des noms à des éléments. Cela permet notamment, plus tard, lors de la phase de design, de pouvoir styliser les éléments portant un nom particulier.

## Attribut class

L’attribut ```class``` est un des deux attributs permettant de donner un nom à un élément. Il permet, en fait, de pouvoir donner **le même nom à plusieurs éléments**.

__Remarque__ : L’attribut ```class``` peut être utilisé avec n’importe quel élément HTML. De plus, des éléments de type différents peuvent avoir un même nom de classe. Par exemple, un élément ```<p>``` peut avoir une classe main, aussi bien qu’un élément ```<div>```.

Exemple :

```html
<body>
    <!-- Applique la classe background sur la div -->
    <div class="background">
        <p>Je suis le paragraphe 1</p>
    </div>
 
    <!-- Applique la classe background sur la div -->
    <div class="background">
        <p>Je suis le paragraphe 2</p>
    </div>
</body>
```

Dans cet exemple, les deux ```<div>``` se sont vues attribuer la même classe, **background**, grâce à l’attribut ```class```.

## Classes multiples

Le langage HTML permet de donner plusieurs noms de classe à un même élément. Pour ce faire, il suffit simplement de mettre un espace entre les deux noms, dans l’attribut ```class``` :

```html
<body>
    <!-- La div ci-dessous appartient à la fois à la classe background et à la class main -->
    <div class="background main">
        <p>Je suis le paragraphe 1</p>
    </div>
</body>
```

# Contenu de ./0180 - Id/content.md

L’attribut ```id``` est le deuxième attribut permettant de donner un nom à un élément HTML. ```Id``` est le raccourci anglais pour “identifiant”. Sa différence avec l’attribut ```class```, est qu’il n’y a qu’**un seul élément par page** qui peut porter un nom particulier d’```id```, contrairement à ```class``` qui permet à plusieurs éléments de porter le même nom.

## Attribut id

L’attribut ```id``` permet de définir un nom (identifiant) unique pour un élément HTML. Il n’autorise pas d’autres éléments à porter le même nom au sein d’une même page web.

L’```id``` est principalement utilisé pour les liens d’ancres, et, plus tard, lors de la phase de design, pour pouvoir styliser l’élément portant l’identifiant défini. Il est également couramment utilisé pour fonctionner avec JavaScript.

__Remarque__ : Contrairement à ```class```, un élément HTML ne peut pas porter plusieurs noms d’id. L’attribut ```id``` doit recevoir au minimum 1 caractère et n’autorise pas les espaces, tabulations, etc.

Exemple :

```html
<body>
    <!-- Le paragraphe ci-dessous sera le seul à avoir l'identifiant "important"  -->
    <p id="important">Je suis un paragraphe avec un l'id important</p>
</body>
```

Il est bon de savoir que la valeur de l’attribut est sensible à la casse. Aussi, il ne peut contenir au minimum un seul caractère et ne peut contenir des espaces, tabulations, etc.


# Contenu de ./0190 - Iframes/content.md

Le langage HTML permet à un développeur d’incorporer du contenu provenant d’un autre site web sur son propre site web. C’est par exemple le cas avec les vidéos YouTube.

## L’élément ```<iframe>``` et ses attributs

L'élément ```<iframe></iframe>``` permet d'incorporer un contenu provenant d’autre site web externe dans le site web actuel. Cet élément est principalement utilisé pour intégrer des vidéos YouTube ou des cartes Google Maps dans un site web.

Voici la liste des attributs utilisables avec ```<iframe>```. Certains sont obligatoires, d’autres non :

- ```src``` : permet d'indiquer l'adresse du document à intégrer. Cet attribut est obligatoire.
- ```width``` et ```height``` sont utilisés pour définir la taille de l'élément iframe. Si on ne peut pas modifier la taille de l'iframe en CSS, on peut les utiliser
- ```allow``` est utilisé pour définir la politique de confidentialité de l’iframe. Cela signifie que le développeur peut autoriser ou non certaines fonctionnalités propres à l’élément important. Le but de cet attribut est de renforcer la sécurité du code.
- ```sandbox``` est relativement récent. Il permet de limiter les possibilités de l’iframe. Le but, ici encore, est de renforcer la sécurité du code.

## Intégrer une vidéo YouTube

L’intégration de vidéos Youtube au sein d’un site internet est relativement courant. Celle-ci s’effectue généralement grâce aux iframes.

Pour intégrer une vidéo sur un site internet grâce aux iframes, il faut se rendre sur une vidéo YouTube, cliquer sur le bouton “Partager”, puis sur “intégrer”. Youtube génère alors un code HTML comprenant une balise “iframe” qu’il suffit de copier-coller pour l’intégrer dans une page.

```html
<body>
    <!-- Vidéo youtube intégrée avec un iframe -->
    <iframe width="560" 
        height="315" src="https://www.youtube.com/embed/22GksMxZPBU" 
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
</body>
```

## Définir la hauteur et la largeur d’un iframe

Pour définir la largeur et la hauteur d’un iframe, les attributs ```width``` et ```height``` doivent être utilisés. Par défaut, la largeur et la hauteur sont en ```pixels```. Il est également possible d’utiliser les propriétés du même nom avec l’attribut ```style```.


Exemple avec ```width``` et ```height``` :

```html
<!-- Iframe avec une hauteur et largeur de 500px -->
<iframe src="#" height="500" width="500" title="Intégrer un iframe"></iframe>
```

Exemple avec l’attribut ```style``` :

```html
<!-- Iframe avec une hauteur et largeur de 500px -->
<iframe src="#" style="width: 500px; height: 500px;" title="Intégrer un iframe"></iframe>
```

## Supprimer la bordure

Par défaut, une iframe est affichée avec une bordure. Pour supprimer cette bordure, il faut utiliser l’attribut ```style``` et définir la propriété ```border``` à ```none```. Il est également possible de réaliser ceci en utilisant du CSS de manière plus conventionnelle. Référez-vous aux cours de CSS afin d’y parvenir.

Exemple :

```html
<!-- Supprime la bordure autour de l'iframe -->
<iframe src="#" style="border: none" title="Intégrer un iframe"></iframe>
```

# Contenu de ./0200 - Chemins relatifs & absolus/content.md

Lorsqu’un développeur a besoin de lier un fichier, une page web ou une image au sein d’un fichier HTML, il a le choix entre préciser le chemin d’accès absolu, qui part du fichier racine et est plus précis, ou préciser le chemin d’accès relatif, moins précis mais beaucoup plus rapide à écrire.

Certains langages n’acceptent que des chemins absolus, car plus précis. D’autres, acceptent des chemins d’accès relatifs. Le langage HTML fait partie des langages informatiques qui acceptent les deux types de chemins d’accès.

## Chemin absolu

Un chemin d’accès à un fichier est dit **absolu** lorsqu’on utilise l’**adresse précise** - depuis le dossier racine - du fichier, du document ou de l’image. C’est le cas, par exemple, lorsqu’une image provenant d’un autre site est intégrée sur un autre site web. L’URL indiquée dans l’attribut ```src``` est absolue.

Exemple:

```html
<body>
    <!-- L'URL de l'image indiquée dans l'attribut src est absolue -->
    <img src="https://cdn.pixabay.com/photo/2020/11/22/17/28/cat-5767334_960_720.jpg" alt="Un chat">
</body>
```

## Chemin relatif

Un **chemin relatif** est un chemin dont l’adresse **n’est pas précise**. Il s’agit simplement d’indiquer le nom du dossier dans lequel se trouve le fichier à inclure, suivi d’un slash et du nom du fichier à inclure, sans oublier de préciser l’extension du fichier.

**Un chemin relatif part toujours du fichier actuellement utilisé**. Le chemin relatif est donc écrit à partir du fichier actuel.

Exemple :

```html
<body>
    <!-- Image avec chemin relatif -->
    <img src="images/picture.jpg" alt="Un chat">
</body>
```

Dans le cas où le fichier actuellement utilisé est situé dans un sous-dossier et que le fichier à inclure se trouve un dossier au-dessus, il suffit de rajouter ```../``` avant le nom du dossier et le nom du fichier.

Exemple :

```html
<body>
    <!-- Image depuis un dossier au-dessus du dossier courant -->
    <img src="../images/picture.jpg" alt="Un chat">
</body>
```

# Contenu de ./0210 - Head/content.md

L’élément ```<head></head>```, bien qu’il ne soit pas interprété ni affiché par le navigateur, contient des informations importantes pour que le navigateur puisse, par exemple, savoir quel encodage utiliser afin de pouvoir afficher correctement les accents.

## Element ```<head>```

Les éléments contenus dans le ```<head>``` (*en-tête*, en anglais), ne sont pas affichés par le navigateur. Ils permettent par exemple d’afficher le texte et les accents correctement, de lier le fichier contenant le design du site web, ou encore de donner un titre à la page web.

## Element ```<title>```

Cet élément permet de définir un titre pour la page en cours. Il est affiché dans la fenêtre ou dans l’onglet du navigateur - c’est d’ailleurs le seul élément contenu dans le ```<head></head>``` qui est affiché par le navigateur. 

Le texte contenu entre les balises ```<title></title>``` est également affiché dans les favoris et dans les résultats des moteurs de recherches.

**Remarque** : Le titre doit être uniquement composé de texte. 

L’élément ```<title></title>``` est nécessaire dans un document HTML, car cela favorise, par la suite, le référencement du site par les moteurs de recherche.

Exemple :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <!-- Titre de du document -->
    <title>Titre de page important</title>
</head>
<body>
    
</body>
</html>
```

## Element ```<style>```

Cet élément est utilisé pour écrire du code CSS (permettant de créer le design du site) directement au sein du document HTML.

Exemple :

```html
<style>
    /* Les paragraphes seront écrits en rouge et le texte sera centré */
    p {
        color: red;
        text-align: center;
    }
</style>
```

## Element ```<link>```

Cet élément est utilisé pour lier une ressource externe au document actuel. De nos jours, il est généralement utilisé pour lier une feuille de style contenant le design, au document HTML actuel.

**Remarque** : ```<link>``` est une balise auto-fermante, il n’est donc pas rare de voir un slash avant le chevron de fin.

Cet élément est **toujours** accompagné des deux attributs suivants :

- **rel** : indique le type de document que représente le source externe. Dans le cas d’une feuille de style, cet attribut recevra la valeur “stylesheet”.
- **href** : reçoit en valeur le chemin absolu ou relatif menant vers la ressource à lier au document.

Exemple :

```html
<!-- Lie un fichier css interne au document -->
<link rel="stylesheet" href="style.css" />
```

## Element ```<meta>```

Meta, par son étymologie, signifie “après” ou “au-delà de”. Cet élément HTML permet donc d’apporter aux navigateurs et aux moteurs de recherches des informations sur le document HTML et sur le site. Ces données ne sont pas affichées par le navigateur.

**Remarque** : ```<meta>``` est également une balise autofermante. 

Exemples d’utilisations de ```<meta>``` :

```html
<!-- Définir l’encodage utilisé afin que les navigateurs affichent correctement les accents -->
<meta charset="UTF-8">
<!-- Définir des mots-clés pour les moteurs de recherche -->
<meta name="keywords" content="Cours, Programmation, Informatique, HTML">
<!-- Définir la description de votre page web -->
<meta name="description" content="Cours de programmation informatique -  HTML">
<!-- Définir l'auteur de la page -->
<meta name="author" content="NK Informatique">
```

## Définition de la taille de la fenêtre du navigateur

La fenêtre d’affichage est l’endroit où le site web s’affiche. Elle ne prend pas en compte la barre d’outil du navigateur. 

De nos jours, avec les smartphones, les tailles de fenêtres d’affichage varient en fonction de l’appareil utilisé pour consulter un site web. Ainsi la fenêtre d’affichage sera-t-elle plus petite sur un smartphone et une tablette, que sur un ordinateur, par exemple. Le principal problème avec les différentes tailles de fenêtres, c’est que le design d’un site web doit rester cohérent et le contenu lisible, quelle que soit la taille de la fenêtre sur lequel le site est consulté.

Pour palier à ce problème, le langage HTML met à disposition 2 attributs utilisables avec l’élément ```<meta>``` :

- **name** : qui contient généralement le mot “viewport” (*fenêtre d’affichage*, en anglais), permet d’indiquer à la balise ```<meta>``` qu’elle va recevoir des informations concernant la fenêtre d’affichage
- **content** : reçoit des informations concernant la largeur de l’appareil utilisé pour consulter le site, et le niveau de zoom à utiliser lors du premier chargement de la page.

Exemple d’utilisation de meta pour les fenêtres d’affichage :

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```width=device-width``` définit la largeur de la fenêtre d’affichage de l’appareil utilisé, afin que le navigateur puisse afficher le site web de manière lisible, quelle que soit la taille de la fenêtre d’affichage.

La partie ```initial-scale=1.0``` définit le niveau de zoom à utiliser lors du premier chargement de la page

Ci-dessous, un exemple de ce que donne une page HTML chargée sans que l’élément **meta viewport** soit renseigné (à gauche), et un autre exemple avec la balise **meta viewport** renseignée (à droite).

Dans l’exemple ci-dessous, la page HTML chargée sans que **meta viewport** soit renseigné (image de gauche) “déborde” de la fenêtre d’affichage du téléphone, ce qui rend le contenu moins lisible, et le design moins agréable.

En revanche, dans l’image de droite, la balise **meta viewport** est renseignée, permettant au navigateur d’adapter l’affichage du contenu afin que celui-ci ne déborde pas de la fenêtre d’affichage. Cela permet également à l’utilisateur de zoomer à sa convenance afin de pouvoir lire le texte.

![Illustration ci-dessus](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/D%C3%A9veloppement%20G%C3%A9n%C3%A9rique/HTML/courses/0210%20-%20Head/images/image1.jpg)

# Contenu de ./0220 - Layout/content.md

La mise en page d’une page web - communément appelée “layout” - est importante pour un site internet.

Tel qu’il a été expliqué dans les cours précédents, le HTML est un langage de balises, chaque balise permettant d’indiquer au navigateur à quoi correspond un élément. Ainsi, pour améliorer la sémantique du langage HTML - sémantique signifiant “qui concerne le sens, la signification” - et savoir à quoi correspond chaque section d’une page HTML lors du travail de mise en page, le langage met à disposition un certain nombre de balises.

## Eléments de mise en page

Le langage HTML dispose de plusieurs balises permettant de “structurer” un site afin d’améliorer sa sémantique. 

**Remarque** : Tous ces éléments de structure se trouvent entre les balises ```<body></body>``` du fichier HTML.

Ci-dessous, la liste des éléments sémantiques mis à disposition pour l’amélioration de la structure d’un document HTML :

- ```<header>``` : Définit un en-tête pour un document ou une section. À ne pas confondre avec l’élément ```<head></head>```. Dans une page HTML, le header contient généralement le logo.
- ```<nav>``` : Cet élément entoure une barre de navigation (menu).
- ```<section>``` : Définit une section dans un fichier HTML
- ```<article>``` : Définit un contenu indépendant et autonome, généralement le contenu de la page web ou de la section en cours.
- ```<aside>``` : Définit un contenu qui sera mis “sur le côté”. En d’autre termes, cet élément est utilisé afin de définir un contenu qui ne peut être mis dans un ```<article>``` (des informations supplémentaires, par exemple).
- ```<footer>``` : Définit un pied de page pour un document ou une section
- ```<details>``` : Définit des détails supplémentaires que l'utilisateur peut ouvrir et fermer à la demande

Exemple d’une structure HTML reprenant les éléments ci-dessus :

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8" />
        <title>Titre de la page web</title>
    </head>
    <body>
        <header>
            Logo
        </header>

        <nav>
            <ul>
                <li><a href="#">Lien 1</a></li>
                <li><a href="#">Lien 2</a></li>
                <li><a href="#">Lien 3</a></li>
            </ul>
        </nav>

        <section>
            <article>
                <p>Je suis un paragraphe contenu dans la balise article</p>
            </article>
            <aside>
                <p>Je contiens des informations supplémentaires</p>
            </aside>
        </section>

        <footer>
            Ici se trouvent généralement un lien pour contacter le propriétaire du site et les droits d'auteur
        </footer>
    </body>
</html>
```

## Éléments de mise en page

### Element ```<section>```

L’élément ```<section></section>``` permet de regrouper des contenus ayant le même thème. Une section commence généralement avec un titre. 

En fonction du type de site développé, il est courant qu’une page web soit divisée en plusieurs sections, toutes avec une thématique différente.

Exemple :

```html
<!-- Définit une section -->
<section>
    <h1>Première section</h1>
    <p>Pellentesque feugiat, mauris nec ornare commodo, nisi leo pellentesque neque, et mollis dui ante mattis felis. Nullam quis lacinia libero, non malesuada tellus. Integer nec augue finibus, tempus magna eget, placerat leo. Nulla hendrerit arcu ipsum, ac pharetra massa sodales id.</p>
</section>

<!-- Définit une autre section -->
<section>
    <h1>Deuxième section</h1>
    <p>Pellentesque feugiat, mauris nec ornare commodo, nisi leo pellentesque neque, et mollis dui ante mattis felis. Nullam quis lacinia libero, non malesuada tellus. Integer nec augue finibus, tempus magna eget, placerat leo. Nulla hendrerit arcu ipsum, ac pharetra massa sodales id.</p>
</section>
```

### Élement ```<article>```

L’élément ```<article></article>``` entoure le contenu d’une page web ; cependant, le contenu d’un ```<article>``` doit être autonome et indépendant. En d’autre termes, il ne doit être raccroché à aucune autre thématique sur la page. 

Concrètement, un contenu de type ```<article></article>``` peut très bien être un message sur un forum, un billet de blog ou un article sur le site d’un journal, par exemple.

Cependant, bien que par définition un article doit représenter un contenu autonome et indépendant, il est courant de voir des sites web incluant des éléments ```<article>``` au sein de  ```<section>```.

Exemple :

```html
<!-- Définit un article -->
<article>
    <h2>Microlead</h2>
    <p>Microlead vous accompagne dans l’apprentissage du développement et dans l’amélioration permanente de vos compétences.</p>
</article>
```

### Élément ```<header>```

Dans sa fonction première, l’élément ```<header></header>``` est utilisé pour définir un en-tête. Généralement il est utilisé pour définir l’en-tête d’une page web, mais rien n’interdit de l’utiliser également pour définir l’en-tête d’une section ou d’un article.

Exemple :

```html
<!-- Définit un article -->
<article>
    <!-- Définit l'en-tête de l'article -->
    <header>
        <h1>Microlead</h1>
        <p>Notre mission :</p>
    </header>
    <!-- Paragraphe -->
    <p>Microlead vous accompagne dans l’apprentissage du développement et dans l’amélioration permanente de vos compétences.</p>
</article>
```

### Element ```<footer>```

L’élément ```<footer></footer>``` définit un “pied” (une fin) pour une section ou une page HTML. Cet élément contient généralement des informations sur l’auteur, sur les droits d’auteur, un lien menant vers un formulaire de contact, etc.

Exemple :

```html
<!-- Définit un pied de page -->
<footer class="sub-footer">
    <div class="footer-content">
        <p><a class="link" href="legals.php">Mentions légales</a> | Microlead </p>
    </div>
</footer>
```

### Élément ```<nav>```

L'élément ```<nav></nav>``` définit un ensemble de liens de navigation. De manière générale, cet élément est utilisé lors de la création d’un menu de navigation pour un site web. C’est d’ailleurs son rôle. En effet, ```<nav>``` n’est utilisé que pour les “blocs” de liens.

Exemple :

```html
<!-- Dans cet exemple, <nav> entoure le menu de navigation -->
<nav class="main-nav">
    <a title="Accueil" class="link" href="#">Accueil</a>
    <a title="Titre 1" class="link" href="#">Titre 1</a>
    <a title="Titre 2" class="link" href="#">Titre 2</a>
    <a title="Titre 3" class="link" href="#">Titre 3</a>
    <a title="Titre 4" class="link" href="#">Titre 4</a>
    <a title="Titre 5" class="link" href="#">Titre 5</a>
    <a title="Titre 6" class="link" href="#">Titre 6</a>
</nav>
```

### Element ```<aside>```

L’élément ```<aside></aside>``` définit un contenu indirectement lié au contenu actuel. C’est généralement un élément qui sera placé sur le côté lors de la phase de design. Cet élément peut, par exemple, contenir des informations supplémentaires sur le contenu, une liste de liens menant à des ressources externes, etc.

Exemple :

```html
<aside>
    <h1>Microlead</h1>
    <p>Microlead vous accompagne dans l’apprentissage du développement et dans l’amélioration permanente de vos compétences.</p>
</aside>
```

# Contenu de ./0230 - Code/content.md

Le langage HTML permet également d’afficher du code qui ne sera pas interprété par le navigateur (pour un site web qui donne des cours de code, par exemple), ou encore, d’afficher des combinaisons de touches (pour des raccourcis claviers, par exemple). Tous ces éléments mis à dispositions par le HTML permettent à un développeur web de créer un site donnant des cours sur des langages informatiques. 

## L’élément ```<kbd>```

Cet élément est utilisé pour afficher une combinaison de touches. Lorsque le navigateur rencontrera cet élément, il l’affichera dans une police monospace, afin de distinguer son contenu du reste du paragraphe.

Exemple :

```html
<!-- Affiche une combinaison de touches -->
<p>Pour quitter le site veuillez faire <kbd> Alt + F4</kbd></p>
```

## L’élément ```<samp>```

Si un développeur se retrouve à créer un site web de cours sur différents langages informatiques, il est possible qu’il faille à un moment afficher un message de sortie de fin de programme. C’est le rôle de l’élément ```<samp></samp>```, dont le rôle est de distinguer ce message du reste du paragraphe.

Exemple :

```html
<p>Message:</p>
<!-- Message de sortie de programme -->
<p><samp>Fichier introuvable.</samp></p>
```

## L’élément ```<code>```

```<code></code>``` permet d’afficher un code source sur la page web, qui ne sera pas interprété par le navigateur. 

__Remarque__ : Lorsque le navigateur rencontre cet élément, il n’affiche pas les espaces ou tabulations, et ne retient pas les retours à la ligne, pourtant essentiels pour un code clair et lisible. Pour résoudre ce problème, il est possible d’entourer le code de l’élément de pré-formatage ```<pre></pre>```.

Exemple :

```html
<!-- Définit un morceau de code -->
<pre>
<code>
    <body>
		<p>Je suis un paragraphe affiché dans du code qui n'est pas interprété par le navigateur</p>
	</body>
</code>
</pre>
```

## L’élément ```<var>```

En informatique, une variable est une place en mémoire qui est allouée à un élément. Le rôle d’une variable est de conserver en mémoire une valeur pendant toute la durée d’exécution d’un programme, et d’effacer ce contenu lorsque le programme n’est plus exécuté.

L’élément ```<var></var>``` permet d’afficher le contenu de variable, afin de les distinguer du reste du paragraphe en cours. 

Exemple :

```html
<!-- Définit des variables -->
<p>Si c désigne la longueur d'un côté d'un triangle et h la hauteur relative à ce côté, l'aire de ce triangle est égale à (<var>c</var> × <var>h</var>) / 2.</p>
```

# Contenu de ./0240 - Sémantique/content.md

Le rôle d’un langage de programmation est d’être compréhensible à la fois pour le développeur et pour la machine qui va devoir interpréter le code pour afficher les résultats attendus. 

Pour cela, les créateurs de langages informatiques se doivent d’adopter une sémantique claire et précise afin que le langage remplisse les deux objectifs ci-dessus.

## Les éléments sémantiques

Un élément sémantique décrit clairement sa fonction, le rôle qu’il remplit, tant pour le développeur qui utilise cet élément, que pour le navigateur qui affiche le résultat ou le contenu de l’élément.

Par exemple, les éléments ```<div>``` et ```<span>``` ne sont pas des éléments sémantiques car ils ne décrivent pas clairement le “rôle” du contenu qu’ils entourent. Le navigateur ne sait pas quel type de contenu il va afficher lorsqu’il rencontre ces éléments.

En revanche, les éléments ```<h1>```, ```<article>```, ```<form>```, ```<nav>```, etc. sont des éléments sémantiques car ils indiquent clairement ce qu’ils entourent, et donnent des informations au navigateur et au développeur sur ce qui va être affiché.

## Éléments sémantiques en HTML

De nombreux développeurs utilisent encore des ```<div id=”id”>``` pour structurer leurs pages webs. Cette technique n’est pas incorrecte, en soit. Mais si le code doit, plus tard, être repris par un autre développeur, ce dernier mettra plus de temps à comprendre le contenu de la ```<div>``` que si des éléments HTML sémantiques avaient été utilisés.

Comme évoqué dans le cours sur la mise en page en HTML, il existe des éléments sémantiques permettant de structurer clairement une page web :

- ```<article>```
- ```<aside>```
- ```<details>```
- ```<figcaption>```
- ```<figure>```
- ```<footer>```
- ```<header>```
- ```<main>```
- ```<mark>```
- ```<nav>```
- ```<section>```
- ```<summary>```
- ```<time>```

## Éléments figure et figcaption

Il existe deux autres éléments sémantiques, en HTML : les éléments ```<figure></figure>``` et ```<figcaption></figcaption>```.

L’élément ```<figure>``` entoure généralement du contenu d’illustration, tel que des photos, des dessins, des graphiques, etc.

L’élément ```<figcaption>```, quant à lui, définit une légende pour le contenu de ```<figure>```. ```<figcaption>``` peut-être placé avant ou après l’élément ```<figure>```.

Exemple :

```html
<figure>
    <img src="chat.jpg" alt="chat">
    <!-- Définit une légende -->
    <figcaption>Image1. - Un chat.</figcaption>
</figure>
```

# Contenu de ./0250 - Conventions de codage/content.md

Afin que chaque développeur puisse s’y retrouver dans le code source des autres, les langages informatiques ont tous une convention de codage. Cela signifie qu’il y a des règles de base d’écriture du code qui sont définies afin que tout le monde code de la même manière.

Bien entendu, rien n’oblige les développeurs à suivre ces règles, mais la plupart s’y plient tout de même afin d’assurer une certaine standardisation du code.

## Toujours déclarer le type de document

Lors de la création du document HTML, le type de document doit toujours être déclaré avec la balise ```<!DOCTYPE html>```. Cela indique au navigateur qu’il s’agit d’un document HTML et pas simplement d’un document texte.

## Utiliser des noms d'éléments et d'attributs en minuscules

Le langage HTML n’est pas sensible à la casse. Cela signifie qu’il ne fait pas la distinction entre un élément écrit en minuscule ou en majuscule.

Néanmoins, par convention, les éléments et attributs sont écrits en minuscule, pour les raisons suivantes :

- Les développeurs utilisent les minuscules
- Les minuscules semblent plus propre dans le code
- Les minuscules sont plus rapides à écrire

Exemple respectant la convention concernant les éléments et attributs :

```html
<body>
    <h1>Cours HTML</h1>
    <p>Voici un cours sur le HTML</p>
</body>

<a href="https://www.google.com/">Google</a>
```

Exemple ne respectant pas la convention concernant les éléments et attributs:

```html
<BODY>
    <H1>Cours HTML</H1>
    <P>Voici un cours sur le HTML</P>
    <A href="https://www.google.com/">Google</A>
</BODY>
```

__Remarque__ : Il est également formellement déconseillé d'utiliser des accents ou des caractères spéciaux à l'exception du tiret ```-``` et de l'underscore ```_```.

## Fermer tous les éléments HTML

HTML permet de ne pas fermer les éléments présents dans le code. Cependant, pour éviter la confusion et rendre le code plus clair, la convention veut qu’il faille fermer tous les éléments. Aussi il est largement recommandé pour toutes les balises non “auto fermantes” de bien spécifier les balises fermantes systématiquement.

Exemple respectant la convention : 

```html
<body>
    <h1>Cours HTML</h1>
    <p>Voici un cours sur le HTML</p>
</body>
```

Exemple ne respectant pas cette convention :

```html
<body>
    <h1>Cours HTML
    <p>Voici un cours sur le HTML
</body>
```

## Mettre les valeurs d’attributs entre guillemets

Le langage HTML permet également de ne pas mettre les valeurs d’attributs entre guillemets.

Cependant, pour les raisons citées ci-dessous, il est recommandé de mettre des guillemets autour des valeurs d’attributs :

- Les valeurs entre guillemets sont plus faciles à distinguer dans le code
- Le langage HTML exige de toute manière que les guillemets soient utilisés en si la valeur contient des espaces.

Exemple respectant la convention :

```html
<p class="container red">Voici un cours sur le HTML</p>
```

Exemple ne respectant pas la convention :

```html
<p class=container red>Voici un cours sur le HTML</p>
```

## Toujours spécifier l'attribut alt, la largeur et la hauteur des images

Comme évoqué dans le cours sur les images, l’attribut ```alt```, bien que non obligatoire, est recommandé. Il permet d’afficher un texte alternatif en cas de problème d’affichage de l’image et rend également le site accessible aux personnes malvoyantes ou non-voyantes.

De plus, la convention exige de spécifier la hauteur et la largeur des images afin de réduire le scintillement. En effet, en spécifiant la hauteur et la largeur de l’image, le navigateur peut allouer l’espace nécessaire à l’affichage de l’image avant le chargement de la page ou du moins avant l’affichage de l’image. 

Exemple respectant la convention :

```html
<img src="chat.png" alt="chat" style="width:500px; height:500px" />
```

Exemple ne respectant pas la convention :

```html
<img src="chat.png" />
```

## Espaces et signe égal

Le langage HTML permet d’ajouter un espace entre l’attribut, le signe égale et la valeur de l’attribut. 

Cependant, pour des raison de lisibilité du code, la convention veut que le développeur ne rajoute pas d’espace entre ces éléments.

Exemple sans espace :

```html
<p class="container">Voici un cours sur le HTML</p>
```

Exemple avec espaces :

```html
<p class     =     "container">Voici un cours sur le HTML</p>
```

## Évitez les longues lignes de code

Pour des raisons de gain de temps et de lecture du code, les longues lignes de code ne sont pas recommandées. En effet, faire défiler l’éditeur de code de gauche à droite pour lire une longue ligne de code fait perdre un temps précieux. 

Il est ainsi recommandé de revenir à la ligne lorsque le code commence à “dépasser” de la fenêtre de l’éditeur. Ainsi, sera-t-il plus facile à lire.

## Lignes vides et indentation

L’indentation est le fait de créer un décalage du contenu sur la droite, et ainsi laisser une marge plus grande sur la gauche. La plupart des éditeurs de code ajoutent automatiquement une indentation lorsque cela est nécessaire. Cela rend le code plus lisible et plus clair lorsqu’il y a des éléments à corriger.

Néanmoins, il ne faut pas rajouter des indentations là où ce n’est pas nécessaire. Cela rend, au contraire, le code moins lisible et moins clair.

Il est de coutume d’ajouter un niveau d’indentation en fonction de l’imbrication des éléments HTML. Ainsi si une balise en contient une autre, il est de convention d’indenter la seconde, de telle sorte à distinguer visuellement l’appartenance de cette dernière.

Exemple respectant la convention :

```html
<table>
    <tr>
        <td>Nom</td>
        <td>Prénom</td>
    </tr>
    <tr>
        <td>Doe</td>
        <td>John</td>
    </tr>
</table>
```

Exemple ne respectant pas la convention :

```html
<table>
    <tr>

<td>Nom</td>
<td>Prénom</td>
    </tr>

    <tr>

        <td>Doe</td>
        <td>John</td>
    </tr>
</table>
```

## Ne jamais sauter l'élément ```<title>```

Dans le document HTML, l’élément ```<title></title>``` doit toujours être renseigné. En effet, en plus de définir un titre dans l’onglet ou la fenêtre du navigateur, en plus de fournir un titre à la page lorsqu’elle est ajoutée en favoris, cela permet aussi un meilleur référencement par les moteurs de recherche.

Il est donc recommandé d’écrire un titre qui soit le plus précis possible - sans être trop long, cependant.

Exemple :

```html
<title>Guide de style HTML et conventions de codage</title>
```

## Omettre les éléments ```<html>``` et ```<body>```

Un document HTML est valide, même sans les éléments ```<html></html>``` et ```<body></body>```. Cependant, par soucis de compatibilité du site web avec les anciens navigateurs, il est tout de même recommandé de mettre ces balises. En effet, l’omission de ces balises peut créer des bugs sur les anciens navigateurs.

Exemple respectant cette convention :

```html
<!DOCTYPE html>
<html lang="fr-FR">
<head>
    <title>Conventions de codage</title>
</head> 

<body>
    <h1>Cours HTML</h1>
    <p>Voici un cours sur le HTML</p>    
</body>
</html>
```

Exemple ne respectant pas cette convention :

```html
<!DOCTYPE html>
<head>
    <title>Conventions de codage</title>
</head>

<h1>Cours HTML</h1>
<p>Voici un cours sur le HTML</p>
```

## Omettre l’élément ```<head>```

Un fichier HTML est également viable sans les balises ```<head></head>```. Si tel est le cas, les navigateurs ajouteront des éléments par défaut contenus dans le ```<head>```.

Malgré tout, il est recommandé d’ajouter l’élément ```<head>```. Cela permet au développeur d’ajouter les informations précises contenues dans cet élément.

Exemple avec le ```<head>``` :

```html
<!DOCTYPE html>
<html lang="fr-FR">
<head>
    <title>Conventions de codage</title>
</head> 

<body>
    <h1>Cours HTML</h1>
    <p>Voici un cours sur le HTML</p>    
</body>
</html>
```

Exemple sans le ```<head>``` :

```html
<!DOCTYPE html>
<html lang="fr-FR">
<title>Conventions de codage</title>

<body>
    <h1>Cours HTML</h1>
    <p>Voici un cours sur le HTML</p>    
</body>
</html>
```

## Fermer les éléments HTML vides

Le langage HTML permet au développeur de ne pas ajouter un slash (/) à la fin d’une balise auto-fermante, et aucune règle précise n’existe sur le fait d’ajouter ce slash. Ceci est à la discrétion du développeur.

Ainsi, l’exemple ci-dessous est-il accepté :

```html
<meta charset="utf-8">
```

Et cet exemple est aussi accepté :

```html
<meta charset="utf-8" />
```

## Ajouter l'attribut lang

En HTML, la convention exige de toujours ajouter et renseigner l’attribut ```lang``` dans la balise ```<html>```, car cela aide les moteurs de recherche pour le référencement du site web.

Exemple :

```html
<!DOCTYPE html>
<html lang="fr-FR">
<head>
    <title>Conventions de codage</title>
</head> 

<body>
	...
</body>
</html>
```

## Extensions des fichiers HTML

Il existe deux extensions pour un fichier HTML :

- L’extension .html
- L’extension .htm

Aucune différence n’existe entre ces deux extensions. Les deux seront traitées, par le navigateur, comme des fichiers HTML.

# Contenu de ./0260 - Entités/content.md

Bien que les entités soient moins utilisées en HTML, surtout lorsque que l’encodage utf-8 est défini dans l’attribut ```charset```, il est des situations où le développeur devra nécessairement les utiliser.

## Les entités HTML

En HTML, une entité est une chaîne de caractères, qui commence avec le signe ```&``` et se termine avec un point-virgule (;).

Les entités se révèlent utiles lorsque le développeur a besoin d’afficher à l’écran un caractère réservé au langage HTML.

Par exemple, si les chevrons (```<>```) doivent être affichés à l’écran, il se peut que le navigateur ne le fasse pas, car ces caractères sont réservés au HTML. C’est typiquement le genre de situation dans laquelle les entités sont utilisées.

## Syntaxe

Deux syntaxes existent pour les entités.

La première ressemble à ceci : ```&nomdelentité;```
La seconde ressemble à ça : ```&#nomdelentité;```

La première syntaxe est la plus utilisée.

__Remarque__ : Ne pas oublier le point virgule à la fin du nom de l’entité, sinon le navigateur ne l'interprète pas.

Ainsi, pour afficher un chevron ouvrant (```<```), l’entité suivante est utilisée : ```&lt;``` ou ```&#60;```

## Espace insécable

Un espace insécable est un espace qui, quoi qu’il arrive au niveau de l’affichage, ne sera pas coupé sur une nouvelle ligne. En d’autres termes, lorsqu’un retour à la ligne se produit à cause des contraintes d’affichage du navigateur, deux mots séparés par un espace insécable iront à la ligne ensemble, il ne seront pas séparés.

C’est l’une des entités les plus utilisées en HTML. Le code pour insérer un espace insécable est le suivant : ```&nbsp;```.

## Tableau d’entités utiles

Ci-dessous, un tableau listant les entités les plus utiles et les plus utilisées en HTML :

| **Résultat** | **Description**      | **Numéro entité** | **Nom entité** |
|----------|----------------------|-------------------|----------------|
| ```  ``` | non-breaking space   | ```  ```          | ```&#160;```   |
| ```<```  | plus petit que       | ```&lt;```        | ```&#60;```    |
| ```>```  | plus grand que       | ```&gt;```        | ```&#62;```    |
| ```&```  | esperluette          | ```&amp;```       | ```&#38;```    |
| ```"```  | guillemet double     | ```&quot;```      | ```&#34;```    |
| ```'```  | guillemet            | ```&apos;```      | ```&#39;```    |
| ```¢```  | cent                 | ```&cent;```      | ```&#162;```   |
| ```£```  | livres               | ```&pound;```     | ```&#163;```   |
| ```¥```  | yen                  | ```&yen;```       | ```&#165;```   |
| ```€```  | euro                 | ```&euro;```      | ```&#8364;```  |
| ```©```  | copyright            | ```&copy;```      | ```&#169;```   |
| ```®```  | registered trademark | ```&reg;```       | ```&#174;```   |

## Combinaison de marques diacritiques

Une marque diacritique est un accent ajouté à une lettre.

Lorsque l’encodage ne comprend pas d’accent et que le développeur doit pourtant en ajouter un sur une des lettres d’un mot, les accents sont rajoutés “à la main” en utilisant les entités correspondantes.

Ci dessous, un tableau listant les principaux accents utilisés :

| **Accent**    | **Caractère** | **Construction** | **Résultat** |
|---------------|---------------|------------------|--------------|
| ```  ̀ . ```  | a             | ```a&#768;```    | ```à```      |
| ```  ́ . ```  | a             | ```a&#769;```    | ```á```      |
| ``` ^ . ```   | a             | ```a&#770;```    | ```â```      |
| ```  ̃ .  ``` | a             | ```a&#771;```    | ```ã```      |
| ```  ̀ . ```  | O             | ```O&#768;```    | ```Ò```      |
| ```  ́ . ```  | O             | ```O&#769;```    | ```Ó```      |
| ``` ^ . ```   | O             | ```O&#770;```    | ```Ô```      |
| ```  ̃ . ```  | O             | ```O&#771;```    | ```Õ```      |

# Contenu de ./0270 - Symboles/content.md

Comme pour les entités, il existe des codes spéciaux (très proches des entités) en HTML pour afficher des symboles qui ne sont pas présents sur un clavier d’ordinateur. L’avantage d’utiliser ces codes plutôt que de taper directement les symboles avec le clavier, est qu’ainsi, le développeur est assuré que ces symboles seront affichés par l’ensemble des navigateurs, peu importe leurs versions ou la langue paramétrée par l’utilisateur.

## Les symboles en HTML

Il y a trois moyens d’afficher un symbole, en HTML :

- Taper le **nom d’entité** du symbole : ```&euro;``` affiche le symbole €
- Taper le **numéro d’entité** du symbole : ```&#8364;``` pour le symbole €
- Taper la **valeur hexadécimale** du symbole : ```&#x20AC;``` pour le symbole €

__Remarque__ : Chaque méthode commence avec une **esperluette** (**&**) et finit avec un **point-virgule**. Oublier un de ces éléments ne permettra pas d’afficher le symbole correctement.

## Les symboles mathématiques en HTML

Ci-dessous un tableau dressant une liste non-exhaustive des symboles disponibles en HTML :
  
| **Caractère** | **Nombre** | **Entité** | **Description** |
| --- | --- | --- | --- |
| ```∀``` | ```&#8704;``` | ```&forall;``` | Pour tous |
| ```∂``` | ```&#8706;``` | ```&part;``` | Différentiel partiel |
| ```∃``` | ```&#8707;``` | ```&exist;``` | Il exist |
| ```∅``` | ```&#8709;``` | ```&empty;``` | Ensemble vide |
| ```∇``` | ```&#8711;``` | ```&nable;``` | Nable |
| ```∈``` | ```&#8712;``` | ```&isin;``` | Élément de |
| ```∉``` | ```&#8713;``` | ```&notin;``` | Pas un élément de |
| ```∋``` | ```&#8715;``` | ```&ni;``` | Contient en tant que membre |
| ```∏``` | ```&#8719;``` | ```&prod;``` | Produit n-ary |
| ```∑``` | ```&#8721;``` | ```&sum;``` | Résumé n-ary |

## Les lettres grecques en HTML

Le langage HTML met également à disposition des entités pour les lettres grecques, dont voici une liste non-exhaustive :

| **Caractère** | **Nombre** | **Entité** | **Description** |
| --- | --- | --- | --- |
| ```A``` | ```&#913;``` | ```&Alpha;``` | Lettre majuscule grecque alpha |
| ```B``` | ```&#914;``` | ```&Beta;``` | Lettre majuscule grecque bêta |
| ```Γ``` | ```&#915;``` | ```&Gamma;``` | Lettre majuscule grecque gamma |
| ```Δ``` | ```&#916;``` | ```&Delta;``` | Lettre majuscule grecque delta |
| ```Ε``` | ```&#917;``` | ```&Epsilon;``` | Lettre majuscule grecque epsilon |
| ```Ζ``` | ```&#918;``` | ```&Zeta;``` | Lettre majuscule grecque zeta |

## Autres symboles courants en HTML

Il existe un myriade d’autres symboles disponibles en HTML. Ci-dessous la liste des symboles les plus utilisés lors de la construction d’un site web :

| **Caractère** | **Nombre** | **Entité** | **Description** |
| --- | --- | --- | --- |
| ```©``` | ```&#169;``` | ```&copy;``` | Signe de copyright |
| ```®``` | ```&#174;``` | ```&reg;``` | Signe de registered |
| ```€``` | ```&#8364;``` | ```&euro;``` | Signe euro |
| ```™``` | ```&#8482;``` | ```&trade;``` | Trademark |
| ```←``` | ```&#8592;``` | ```&larr;``` | Flèche vers la gauche |
| ```↑``` | ```&#8593;``` | ```&uarr;``` | Flèche vers le haut |
| ```→``` | ```&#8594;``` | ```&rarr;``` | Flèche vers la droite |
| ```↓``` | ```&#8595;``` | ```&darr;``` | Flèche vers le bas |

# Contenu de ./0280 - Unicode/content.md

L’unicode (couramment appelé charset) est important car il permet au navigateur de savoir quel “alphabet” utiliser et de pouvoir afficher certains caractères correctement.

## De ASCII à UTF-8

ASCII, pour American Standard Code for Interchange Information (Code Américain standard pour interchanger des informations) a été le premier standard de codage de caractères. L'ASCII a défini 256 caractères différents utilisés pour échanger des informations numériques : des **nombres** (0-9), des **lettres** (A-Z) et des **caractères spéciaux** tels que : ```! $ + - () @ <>```.

Le spécification HTML 5 (dernière version du langage à l’heure où ces lignes sont écrites) encourage à utiliser le charset UTF-8. L’UTF-8 (pour *Universal character set Transformation Format* - 8 bits) a l’avantage de prendre en charge la quasi-totalité des nombres, lettres, caractères spéciaux et symboles du monde entier.

# Contenu de ./0290 - URL Encode/content.md

Une URL est composée d’un nom de domaine (microlead, par exemple), suivi de l’extension (.fr, .com, .tv, etc.). Cependant, derrière le nom de domaine se cache simplement une adresse IP telle que : 192.168.1.1.

D’ailleurs, si un utilisateur tape simplement l’adresse IP du serveur sur lequel un site est hébergé, il pourrait également accéder au site en question. Cependant, les mots étant plus simples à retenir que les chiffres, car plus descriptifs, les développeurs ont créé le principe de l’URL.

## URL - Uniform Resource Locator

Lorsqu’un utilisateur tape le nom d’un site internet dans la barre d’adresse d’un navigateur, celui-ci va simplement aller chercher l’adresse IP correspondant au nom de l’URL renseignée par l’utilisateur, accéder au serveur et afficher la page web demandée. 

Une URL suit les règles suivantes :

```schema://prefix.domaine:port/chemin/nomdefichier```

- **Schéma** définit le type de requête adressée au serveur (les plus courantes sont http et https).
- **Prefix** définit un préfixe de domaine. Le préfixe le plus connu, et qui est rattaché directement au protocole HTTP(S) est : **www**.
- **Domaine** correspond au nom du site web recherché (microLead, par exemple)
- **Port** définit le numéro de port sur l'hôte (la valeur par défaut pour http est 80). Cette valeur est facultative lorsque l’utilisateur tape le nom du site dans la barre de recherche d’un navigateur internet.
- **Chemin** définit un chemin d’accès aux fichiers sur le serveur. Si aucun chemin n’est précisé, le répertoire racine sera sélectionné par défaut.
- **Nomdefichier** concerne le nom du fichier à afficher à l’écran. Dans le cas d’un fichier HTML, si aucun nom de fichier n’est précisé, le navigateur affichera par défaut le fichier index.html.

## Schémas d'URL courants

Ci-dessous, un tableau listant les schémas d’URL les plus couramment utilisés :

| **Schéma** | **Description** | **Utilisé pour** |
| --- | --- | --- |
| http | HyperText Transfer Protocol | Pages Web communes. Non chiffré |
| https | Secure HyperText Transfer Protocol | Pages Web communes. Chiffré |
| ftp | File Transfer Protocol | Téléchargement de fichiers |
| file |  | Un fichier se trouvant sur l’ordinateur de l’utilisateur |

## Encodage d'URL

Les URL ne peuvent comporter que des caractères définis dans la norme ASCII. Si tel n’est pas le cas, l’URL est convertie afin de correspondre à ce standard. 

Lors de ce processus de conversion (appelé codage d’URL), les caractères non-ASCII sont remplacés par le signe pourcentage (**%**) suivi de la valeur hexadécimale du caractère en question.

Les URL ne peuvent pas contenir d'espaces. L’encodage d'URL remplace les espaces soit par un signe plus (**+**), soit par **%20**.

# Contenu de ./0300 - Formulaires/content.md

Les formulaires sont devenus omniprésents sur les sites web, que ce soit pour l’inscription à une newsletter, un formulaire de contact, un formulaire d’inscription, un livre d’or, etc. Ils permettent de renforcer les interactions avec les utilisateurs. 

## L'élément form

L’élément ```<form></form>``` est utilisé pour indiquer au navigateur que tout ce qui se trouve entre ces balises est en rapport avec le formulaire. La balise ouvrante délimite donc le début d’un formulaire, et l’ensemble du contenu jusqu’à la balise fermante sera réputé concerner le formulaire.

L'élément ```<form>``` est un conteneur pour différents types d'éléments, tels que: les champs de texte, cases à cocher, boutons radio, boutons d'envoi, etc.

Exemple :

```html
<form>
    Éléments du formulaire
</form>
```

## L'élément ```<input>```

L’élément ```<input></input>``` (littéralement *saisie*, en anglais), est utilisé afin de permettre à l’utilisateur de saisir des données. Cet élément est obligatoirement accompagné de l’attribut type. En fonction de la valeur passée à celui-ci, l’élément ```<input>``` s’affichera de plusieurs manières différentes. 

Voici un tableau dressant la liste des valeurs qui peuvent être reçues par l’attribut ```type``` :

| **Type** | **Description** |
| --- | --- |
| ```<input type="text">``` | Affiche un champ de saisie de texte sur une seule ligne |
| ```<input type="radio">``` | Affiche un bouton radio (pour sélectionner l'un des nombreux choix) |
| ```<input type="checkbox">``` | Affiche une case à cocher (pour sélectionner zéro ou plus de nombreux choix) |
| ```<input type="submit">``` | Affiche un bouton d'envoi (pour soumettre le formulaire) |
| ```<input type="button">``` | Affiche un bouton cliquable |

## Champs de texte

L’élément ```<input type="text">``` affiche un champ de texte monoligne, permettant à l’utilisateur de saisir des données de type “texte”.

Exemple :

```html
<form>
    <input type="text" id="metier" name="metier">
</form>
```

L’exemple ci-dessus affiche un champ de texte portant le nom “métier”.

## L'élément ```<label>```

```<label></label>``` (*étiquette*, en anglais), permet de définir une “légende” pour chaque élément d’un formulaire. 

Cet élément est généralement accompagné de l’attribut ```for```, bien que ce ne soit pas obligatoire. Cet attribut reçoit en valeur un mot permettant de faire le lien avec l’identifiant (**id**) du champ du formulaire auquel il est rattaché.

Cet élément est particulièrement utile lorsqu’un formulaire contient de case à cocher ou des boutons “radio”, car cela permet à l’utilisateur de cliquer sur le texte contenu entre les balises ```<label></label>``` et de cocher automatiquement la case correspondante. Pour ce faire, la valeur définie dans le **for** doit être la même que la valeur donnée au **id** du champ en question.

Exemple :

```html
<form>
    <label for=nom>Nom :</label><br />
    <input type="text" name="nom" id="nom" />
</form>
```

## Boutons radio

Les boutons radio permettent à l’utilisateur de ne choisir qu’une seule option parmi une liste proposée.

Pour créer un bouton radio, il suffit de passer la valeur **radio** à l’attribut ```type```, dans le ```<input>```.

Exemple :

```html
<form>
    <input type="radio" id="dev" name="metier" value="dev">
    <label for="male">Développeur</label><br>
    <input type="radio" id="res" name="metier" value="res">
    <label for="female">Réseaux</label><br>
</form>
```

## Cases à cocher

Les cases à cocher (*checkbox*, en anglais) permettent à l’utilisateur de sélectionner plusieurs options dans une liste.

Pour créer une case à cocher, l’attribut ```type``` doit recevoir la valeur **checkbox**.

Exemple :

```html
<form>
    <input type="checkbox" id="dev" name="metier" value="dev">
    <label for="male">Développeur</label><br>
    <input type="checkbox" id="res" name="metier" value="res">
    <label for="female">Réseaux</label><br>
</form>
```

## Le bouton Envoyer

Lorsque l’utilisateur clique sur ce bouton, il est redirigé vers une page contenant un script qui va contrôler et traiter les données saisies par le formulaire. 

Pour créer un bouton “envoyer”, il doit disposer d’un attribut ```type``` et doit recevoir la valeur **submit**.

Exemple :

```html
<form>
    <input type="checkbox" id="dev" name="metier" value="dev">
    <label for="male">Développeur</label><br>
    <input type="checkbox" id="res" name="metier" value="res">
    <label for="female">Réseaux</label><br>
    <input type="submit" value="Envoyer">
</form>
```

## Attribut name

Pour que la donnée saisie dans un champ du formulaire puisse être traitée lorsque l’utilisateur clique sur le bouton envoyer, chaque ```<input>``` doit être accompagné de l’attribut ```name```. Cet attribut reçoit en valeur un mot représentant le nom du champ.

Lors du traitement du formulaire, chaque valeur saisie sera identifiée et récupérable grâce à cet attribut. Il est donc primordial de le définir pour chaque champ. Attention à ne pas définir plusieurs fois la même valeur (sauf pour les choix multiples), sans quoi c’est la dernière valeur qui sera transmise, et les autres ne seront pas récupérables.

Exemple :

```html
<form>
    <input type="checkbox" id="dev" name="metier" value="dev">
    <label for="male">Développeur</label><br>
    <input type="checkbox" id="res" name="metier" value="res">
    <label for="female">Réseaux</label><br>
    <input type="submit" value="Envoyer">
</form>
```

# Contenu de ./0310 - Éléments d'un formulaire/content.md

Dans le cours concernant les bases de la création d’un formulaire, l’élément input a été évoqué en détail. Cependant, il existe bien d’autres éléments pouvant composer un formulaire.

## L'élément ```<select>```

L’élément ```<select></select>``` permet de créer une liste déroulante. En général, cet élément est utilisé lorsqu’un grand choix d’options est possible. 

Chaque item de la liste doit être entouré de l’élément ```<option></option>```. Cet élément est accompagné de l’attribut ```value```, qui reçoit en valeur le nom de l’item.

__Remarque__ : Par défaut, c’est toujours le premier item qui est pré-sélectionné.

Exemple :

```html
<form>
    <label for="metier">Métier :</label>
    <!-- Liste déroulante -->
    <select id="metier" name="metier">
        <!-- items de la liste -->
        <option value="dev">Développeur</option>
        <option value="res">Réseaux</option>
    </select>
</form>
```

Pour changer l’item présélectionné, il est possible d’utiliser l’attribut ```selected``` à la fin de l’élément ```<option>``` choisi.

Exemple :

```html
<option value="dev" selected>Développeur</option>
```

Lorsque l’attribut ```multiple``` est ajouté à la fin de l’élément ```<select>```, cela permet à l’utilisateur de sélectionner plusieurs options.

Exemple :

```html
<label for="metier">Métier :</label>
<!-- Liste déroulante avec la possibilité de choisir plusieurs options -->
<select id="metier" name="metier"  multiple>
    <option value="dev" selected>Développeur</option>
    <option value="res">Réseaux</option>
</select>
```

## L'élément ```<textarea>```

L’élément ```<textarea></textarea>``` défini une zone de texte multilignes. Cet élément est généralement utilisé afin que l’utilisateur puisse laisser un message ou un commentaire sous un article, par exemple.

Cet élément est généralement accompagné de l’attribut ```rows```, qui définit le nombre de lignes visibles dans la zone de texte, et de l’attribut ```cols```, qui définit la largeur de la ligne.

Exemple :

```html
<!-- Zone de texte -->
<textarea name="message" rows="10" cols="30">
    Zone de texte
</textarea>
```

## L'élément ```<button>```

L'élément ```<button></button>``` définit un bouton cliquable :

Exemple :

```html
<!-- bouton affichant “Cliquer !” -->
<button type="button">Cliquer !</button>
```

## Les éléments ```<fieldset>``` et ```<legend>```

L’élément ```<fieldset></fieldset>``` permet d’organiser un formulaire en regroupant ensemble les champs qui ont un rapport entre eux. Par exemple, les champs concernant l’identité de l’utilisateur (nom, prénom, date de naissance, etc…), les champs concernant son adresse postale (rue, numéro, code postale, ville, pays, etc…) ou encore ses informations de contact (adresse mail, téléphone, etc...).

L’élément ```<legend></legend>```, quant à lui, permet de définir un nom pour le ```<fieldset>```.

De manière générale, les navigateurs entourent les ```<fieldset>``` d’une bordure, et placent la ```<legend>``` en haut du cadre. 

```html
<form>
    <!-- Regroupe les champs ayant un rapport entre eux -->
    <fieldset>
        <!-- Définit un nom pour le fieldset -->
        <legend>Identité</legend>
        <label for="nom">Nom :</label>
        <input type="text" id="nom" name="nom" />
	    <label for="nom">Prénom :</label>
        <input type="text" id="prenom" name="prenom" />
        <input type="submit" value="Envoyer">
    </fieldset>
</form>
```

## L'élément ```<datalist>```

L’élément ```<datalist></datalist>``` est particulier en ceci qu’il représente à la fois un champ de texte et un liste déroulante. Cependant, le principe est simple. Lorsque l’utilisateur va placer le curseur dans le champ texte (créé par ```<datalist>```), une liste d’options prédéfinies va s’afficher juste en dessous. 

Pour créer une ```<datalist>```, il faut d’abord créer un élément ```<input>```. Cet élément est accompagné du seul attribut ```list```, qui reçoit en valeur l’identifiant qui est donné à l’élément ```<datalist>```.

Ensuite, il faut accompagner l’élément ```<datalist>``` de l’attribut ```id```, qui reçoit en valeur le nom spécifié dans l’attribut list de l’```<input>```.

Enfin, il faut créer l’élément ```<option>```, accompagné de l’attribut ```value```. Cet attribut reçoit en valeur l’option à afficher.

Exemple :

```html
<form>
    <!-- Permet de faire une liste déroulante avec une liste prédéfinie d'options -->
    <input list="metier">
    <datalist id="metier">
        <option value="Développeur">
        <option value="Administrateur">
    </datalist>
</form>
```

# Contenu de ./0320 - Types d'input/content.md

Dans le cours d’introduction aux formulaires, certains types d’input - les plus utilisés - ont déjà été évoqués. 

Le but de ce chapitre est de montrer les autres types d’input mis à disposition des développeurs par le langage HTML.

## Input Type Color

Ce type d’input est utilisé afin que l’utilisateur puisse choisir une couleur.

En fonction du navigateur utilisé et de la version de celui-ci, un sélecteur de couleur peut apparaître.

Exemple :

```html
<input type="color" id="color" name="color">
```

## Input Type Date

Tout bon formulaire d’inscription qui se respecte demande la date de naissance de l’utilisateur. Avant le HTML5, chaque site avait sa manière de faire sélectionner sa date de naissance à l’utilisateur, avant des champs de texte ou des listes déroulantes, par exemple. 

Depuis le HTML5, il est possible de créer un champ de type date. Ce champ permet la saisie d’une date au format jj/mm/aaaa, et en fonction du navigateur utilisé et de sa version, un sélecteur de date peut être disponible.

Exemple :

```html
<input type="date" id="naissance" name="naissance">
```

Les champs de type date permettent également de définir une date minimum et une date maximum sélectionnable par l’utilisateur. 

Pour ce faire, les attributs ```min``` et ```max``` doivent être utilisés. Ils prennent en valeur la date minimum sélectionnable et la date maximum. 

Remarque : Dans les attributs ```min``` et ```max```, les formats de dates sont anglais, à savoir **aaaa-mm-jj**.

Exemple :

```html
<!-- Date minimum possible le 01/01/1980 et maximum le 01/01/2020 -->
<input type="date" id="naissance" name="naissance" min="1980-01-01" max="2020-01-01">
```

## Input Type Datetime-local

Ce type d’input permet d’insérer un champ qui recevra à la fois une date et une heure. 

En fonction du type de navigateur utilisé, un sélecteur de date et heure peut apparaître.

Exemple :

```html
<input type="datetime-local" id="flight" name="flight" title="Date et heure de votre vol" />
```

## Input Type Week

Cet input permet à l’utilisateur de saisir une semaine et une année. 

Selon le navigateur utilisé et sa version, un sélecteur peut apparaître dans le champ. 

Exemple :

```html
<input type="week" id="semaine" name="semaine">
```

## Input Type Month

L’input de type **month** permet de saisir un mois et une année. 

En fonction du navigateur utilisé, un sélecteur de mois et d’année peut-être mis à la disposition de l’utilisateur.

Exemple :

```html
<input type="month" id="naissanceMois" name="naissanceMois">
```

## Input Type Time

Cet input permet à l’utilisateur de saisir une heure. 

En fonction du type de navigateur utilisé et de sa version, un sélecteur d’heure peut apparaître dans le champ de saisie.

Exemple :

```html
<input type="time" id="heure" name="heure">
```

## Input Type Email

Un champ de type email n’aura pas d’affichage particulier. Il apparaît comme un simple champ de texte. Cependant, en fonction du navigateur utilisé, il est possible que si l’email n’est pas au format correct, cela envoie un message d’erreur à l’utilisateur lors de l’envoie du formulaire. 

Exemple :

```html
<input type="email" id="email" name="email" />
```

## Input Type File

Ce type de champ permet d’ajouter un bouton parcourir afin de donner à l’utilisateur la possibilité de sélectionner un fichier. 

C’est ce type d’input qui est utilisé lorsque l’utilisateur doit sélectionner une photo de profil.

Exemple :

```html
<input type="file" id="monfichier" name="monfichier">
```

## Input Type Number

Ce type d’input affiche un champ d’entrée numérique. Sur tous les navigateurs modernes, ce champ est accompagné de deux flèches (haut et bas), permettant la sélection d’un nombre.

De plus, il est possible de définir un nombre minimum et un nombre maximum en utilisant les attributs **min** et **max**. 


L'exemple suivant affiche un champ de saisie numérique, dans lequel l’utilisateur ne peut saisir qu’un nombre en 1 et 50 :

```html
<input type="number" id="age" name="age" min="1" max="50" />
```

## Input Type Range

Un input de type range affiche à l’écran un slider (une barre de défilement) permettant à l’utilisateur de sélectionner un nombre. 

L'intervalle de sélection est définie en utilisant les attributs **min** et **max**. 

Exemple :

```html
<input type="range" id="age" name="age" min="1" max="50">
```

## Input Type Search

Ce type d’input est utilisé pour les barres de recherche. Il s’affiche comme un simple champ de texte. 

Exemple :

```html
<input type="search" id="recherche" name="recherche">
```

## Input Type Tel

Le ```<input type = "tel">``` permet la saisie d’un numéro de téléphone. 

Ce type d’input doit être complété avec l’attribut ```pattern```, définissant le format du numéro de téléphone à saisir sous forme d’expression régulière.

Exemple :

```html
<input type="tel" id="telephone" name="telephone" pattern="[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}">
```

Dans cet exemple, le pattern précise que le numéro de téléphone doit être au format suivant : 5 paires de chiffres allant de 0 à 9.

## Input Type Url

Cet input permet à l’utilisateur de saisir une URL (un lien vers son profil Facebook, par exemple).

Exemple :

```html
<input type="url" id="lien" name="lien">
```

# Contenu de ./0330 - Attributs d'input/content.md

Comme pour beaucoup d’éléments en HTML, ```<input>``` peut-être complété par certains attributs spécifiques, permettant de modifier son affichage ou son comportement.

## L'attribut value

Cet attribut permet d’ajouter une valeur par défaut dans un champ de texte.

Exemple :

```html
<input type="text" id="metier" name="metier" value="Développeur">
```

## L'attribut readonly

Readonly transforme un champ de saisie en champ de texte en lecture seule. Cela signifie que l’utilisateur ne pourra pas modifier le contenu du champ - il pourra seulement le lire. Malgré tout, le contenu d’un champ en lecture seule est tout de même envoyé lors de la soumission du formulaire. 

Ce type d’attribut est généralement utilisé pour les Conditions Générales d’Utilisation d’un site internet. L’utilisateur peut les lire, mais, bien entendu, ne peut pas les modifier. 

Exemple :

```html
<input type="text" id="metier" name="metier" value="Développeur" readonly>
```

## L'attribut disabled

Cet attribut permet de désactiver un champ. Cela a pour conséquence que l’utilisateur ne pourra rien saisir dans ce champ. Le champ de saisie, accompagné de cet attribut, est également rendu non cliquable.

Bien entendu, la valeur d’un champ désactivé n’est pas envoyée lors de la soumission du formulaire.

Exemple :

```html
<input type="text" id="metier" name="metier" value="Développeur" disabled>
```

## L'attribut size

*Size* permet de définir la largeur d’un élément input, en termes de nombres de caractères. Par défaut, la valeur *size* est de 20 caractères. 

**Remarque** : L'attribut size fonctionne seulement avec les types d’input suivants: text, search, tel, url, email et password.

Exemple :

```html
<input type="text" id="pin" name="pin" size="4">
```

## L'attribut maxlength

Cet attribut permet de définir le nombre maximum de caractères qu’un utilisateur peut saisir dans un champ. Ainsi, lorsque ce nombre maximum est atteint, l’utilisateur ne peut automatiquement plus rien saisir dans le champ. 

Cependant, il n’y a aucune action de la part du navigateur pour avertir que l’utilisateur a atteint le nombre maximum de caractères. Pour ce faire, il faudra utiliser d’autres langages tels que le JavaScript.

Exemple :

```html
<input type="text" id="pin" name="pin" size="4" maxlength="4">
```

## Les attributs min et max

Ces deux attributs permettent de spécifier une valeur minimum et une valeur maximum acceptées par l’input. Cela signifie que l’utilisateur ne pourra saisir un nombre inférieur au minimum, ni un nombre supérieur au maximum.

__Remarque__ : Les attributs ```min``` et ```max``` fonctionnent avec les types d’input suivants: number, range, date, datetime-local, month, time et week.

Exemple :

```html
<label for="age">Age (entre 1 et 50):</label>
<input type="number" id="age" name="age" min="1" max="50">
```

## L'attribut multiple

Multiple permet à l’utilisateur de saisir plusieurs entrées dans l’input.

**Remarque** : L'attribut multiple fonctionne avec les types d’input suivants: email et file.

Exemple :

```html
<input type="file" id="fichiers" name="fichiers" multiple>
```

## L'attribut pattern

L’attribut ```pattern``` est assez particulier. En effet, il reçoit en valeur une expression régulière qui permettra que la saisie de l’utilisateur soit correcte, lors de la soumission du formulaire. 

*Pattern* peut être utilisé avec un champ de type *mail* pour vérifier que l’adresse mail saisie respecte la forme attendue. 

**Remarque** : L'attribut pattern fonctionne avec les types d'entrée suivants: text, date, search, url, tel, email et password.

Exemple :

```html
<input type="text" id="codePays" name="codePays" pattern="[A-Za-z]{2}" title="Deux lettres pour le code pays, exemple FR">
```

## L'attribut placeholder

Cet attribut permet de spécifier un texte provisoire à l’intérieur d’un champ. Ce texte est remplacé à partir du moment où l’utilisateur commence à taper du texte à l’intérieur du champ. De manière générale, le texte passé en valeur à l’attribut ```placeholder``` est affiché en gris à l’intérieur du champ.

__Remarque__ : L'attribut ```placeholder``` fonctionne avec les input de type text, search, url, tel, email et password.

Exemple :

```html
<input type="text" id="codePays" name="codePays" pattern="[A-Za-z]{2}" title="Deux lettres pour le code pays, exemple FR" placeholder="FR">
```

## L'attribut required

L’attribut ```required``` ne reçoit pas de valeur, il est généralement placé avant le chevron fermant la balise input. Cet attribut est utilisé afin d’indiquer au navigateur que le champ est obligatoire. Ainsi, sur les navigateurs modernes, lorsque l’utilisateur soumet un formulaire et qu’un champ **required** n’est pas rempli, le navigateur retourne une erreur en disant à l’utilisateur que le champ est obligatoire.

__Remarque__ : ```Required``` fonctionne avec les types d'entrées suivants: text, search, url, tel, email, password, date, number, checkbox, radio et file.

Exemple :

```html
<input type="text" id="metier" name="metier" required>
```

## L'attribut step

Cet attribut définit un intervalle de nombre utilisable. Ainsi, si step = "2", les nombres acceptés sont -2, 0, 2, 4, etc.

Cet attribut peut également être utilisé avec les attributs ```min``` et ```max``` afin de définir une plage de nombres acceptés avec l’intervalle défini dans step.

__Remarque__ : L'attribut ```step``` fonctionne avec les types d'entrées suivants: number, range, date, datetime-local, month, time et week.

Exemple :

```html
<input type="number" id="multiplede2" name="multiplede2" step="2">
```

## L'attribut autofocus

**Autofocus** permet de placer automatiquement le curseur dans un champ lors du premier chargement de la page. Généralement, cet attribut est placé dans le premier input du formulaire.

Cet attribut ne reçoit aucune valeur et est généralement placé avant le chevron fermant la balise.

Exemple:

```html
<input type="text" id="metier" name="metier" autofocus>
```

## L'attribut autocomplete

L’attribut ```autocomplete``` permet au navigateur d’activer l’autocomplétion lors de la saisie utilisateur dans un champ. 

L’autocomplétion est une fonction présente sur tous les navigateurs modernes. Au fur et à mesure que l’utilisateur saisit du texte dans un champ, le navigateur “prédit” sa saisie et lui fournit une liste de propositions. Cette fonction est visible sur certains moteurs de recherche, par exemple.

Cet attribut reçoit la valeur “*on*” si l’autocomplétion doit être activée.

__Remarque__ : L'attribut de saisie semi-automatique fonctionne avec ```<form>``` et les types ```<input>``` suivants: text, search, url, tel, email, password, date, range et color.

Exemple :

```html
<form action="envoyer.php" autocomplete="on">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" autocomplete="off">
    <input type="checkbox" id="dev" name="metier" value="dev">
    <label for="male">Développeur</label><br>
    <input type="checkbox" id="res" name="metier" value="res">
    <label for="female">Réseaux</label><br>
    <input type="submit" value="Envoyer">
    <input type="reset">
</form>
```

# Contenu de ./0340 - Canvas/content.md

Il est des sites web sur lesquels il y a parfois besoin d’afficher des graphiques. L’élément ```<canvas>``` fait partie des balises HTML permettant de répondre à ce besoin.

__Remarque__ : L'élément ```<canvas>``` n'est qu'un conteneur pour les graphiques ; cela veut dire que cet élément n’est présent que pour afficher le graphique. Pour créer ce graphique, le langage JavaScript doit être utilisé.

## Prise en charge du navigateur

Voici la liste des versions de navigateurs prenant en charge l’élément ```<canvas>``` :

| **Navigateur** | **Version** |
| --- | --- |
| **Chrome** | 4.0 |
| **IE/Edge** | 9.0 |
| **Firefox** | 2.0 |
| **Safari** | 3.1 |
| **Opera** | 9.0 |

## Utilisation de l’élément ```<canvas>```

En réalité, cet élément permet simplement de définir un zone rectangulaire sur une page web, permettant, lorsqu’il sera créé, d’afficher le graphique.

__Remarque__ : Cet élément est toujours accompagné des attributs ```id```, ```width``` et ```height```.

Exemple :

```html
<canvas id="monCanevas" width="200" height="100"></canvas>
```

# Contenu de ./0350 - SVG/content.md

SVG signifie en anglais *Scalable Vector Graphics* (graphiques vectoriels évolutifs). Cet élément est généralement utilisé en combinaison avec le langage CSS afin de créer des animations sur des images.

## L'élément HTML ```<svg>```

Cet élément est utilisé en tant que conteneur pour les images SVG.

L’élément ```<svg>``` met à disposition du développeur web plusieurs autres éléments afin de dessiner des cercles, rectangles, images graphiques, etc.

## Prise en charge

Ci-dessous, la liste des versions des navigateurs prenant en charge cet élément :

| **Navigateur** | **Version** |
| --- | --- |
| **Chrome** | 4.0 |
| **IE/Edge** | 9.0 |
| **Firefox** | 3.0 |
| **Safari** | 3.2 |
| **Opera** | 10.1 |

## Dessiner des cercles avec svg

SVG propose plusieurs méthodes pour dessiner des tracés, des boîtes, des cercles, du texte et des images graphiques.

Pour dessiner un cercle avec SVG, il faut d’abord ouvrir et fermer la balise ```<svg>```.

Pour tracer un cercle, l’élément ```<circle>``` doit être utilisé. Il peut être accompagné des attributs ```cx``` et ```cy``` afin de renseigner les coordonnées **x** et **y** du centre du cercle. Si ces attributs ne sont pas renseignés, ils seront par défaut définis à 0.

Il est également possible de renseigner l’attribut ```r```, permettant de définir le rayon du cercle.

Les attributs ```stroke``` et ```stroke-width``` peuvent également compléter l’élément ```<circle>```. Ces deux attributs permettent de définir un contour (une bordure) pour un élément. ```Stroke``` prend en paramètre le nom d’une couleur, tandis que ```stroke-width``` prend en valeur un chiffre définissant l’épaisseur de la bordure. 

Enfin, s’il est renseigné, l’attribut ```fill``` permet de définir une couleur de remplissage pour la forme dessinée.

Exemple :

```xml
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40" stroke="red" stroke-width="4" fill="blue" />
</svg>
```

## Dessiner un rectangle en SVG

Pour dessiner un rectangle en SVG, il faut utiliser l’élément ```<rect>```. Cet élément peut être complété avec les mêmes attributs que pour les cercles.

Exemple :

```xml
<svg width="400" height="100">
    <rect width="400" height="100" style="fill:rgb(126, 126, 187);stroke-width:10;stroke:rgb(211, 15, 15)" />
</svg>
```

## Comparaison entre Canvas et SVG

### Canvas

- Dépendant de la résolution
- Pas de support pour les gestionnaires d'événements
- Mauvaises capacités de rendu du texte
- On peut enregistrer l'image résultante au format .png ou .jpg
- Bien adapté aux jeux à forte intensité graphique

### SVG

- Indépendant de la résolution
- Prise en charge des gestionnaires d'événements
- Idéal pour les applications avec de grandes zones de rendu (Google Maps)
- Rendu lent s'il est complexe 
- Ne convient pas aux applications de jeu

# Contenu de ./0360 - Média/content.md

Le langage HTML permet aux développeurs web d’ajouter des éléments multimédias au sein des pages web. 

Sont considérés comme multimédias, tous les contenus pouvant être regardés ou écoutés. On les utilise majoritairement pour des formats de musique ou de vidéo.

## Formats multimédias

Définis en fonction de plusieurs paramètres, les fichiers de musique ou vidéos ont différents formats, visibles, généralement, en regardant l’extension du fichier. 

### Formats vidéo courants

Le tableau suivant dresse la liste des différents formats vidéos utilisés sur le web :

| **Format** | **Extension** | **Description** |
| --- | --- | --- |
| Ogg | .ogg | Theora Ogg. Développé par la Fondation Xiph.Org. Pris en charge par HTML. |
| WebM | .webm | WebM. Développé par Mozilla, Opera, Adobe et Google. Pris en charge par HTML. |
| MP4 | .mp4 | MP4. Développé par le groupe d'experts Moving Pictures. Couramment utilisé dans les caméras vidéo et le matériel TV. Pris en charge par tous les navigateurs et recommandé par YouTube. |

## Formats audio courants

Le tableau ci-dessous liste les différents formats de fichiers audios pris en charge par le HTML et/ou pris en charge par les navigateurs :

| **Format** | **Extension** | **Description** |
| --- | --- | --- |
| WAV | .wav | WAV. Développé par IBM et Microsoft. Fonctionne bien sur les systèmes d'exploitation Windows, Macintosh et Linux. Pris en charge par HTML. |
| Ogg | .ogg | Ogg. Développé par la Fondation Xiph.Org. Pris en charge par HTML. |
| MP3 | .mp3 | Les fichiers MP3 sont en fait la partie sonore des fichiers MPEG. Le format MP3 est le format le plus populaire pour les lecteurs de musique. Combine une bonne compression (petits fichiers) avec une haute qualité. Pris en charge par tous les navigateurs. |
| MP4 | .mp4 | MP4 est un format vidéo, mais peut également être utilisé pour l'audio. Pris en charge par tous les navigateurs. |

# Contenu de ./0370 - Vidéo/content.md

S’il est un format d’élément multimédia devenu très populaire ces 10 dernières années, c’est bien le format vidéo. Il en existe de plus en plus, et il existe de plus en plus de sites web qui en contiennent. 

Le langage HTML permet donc aux développeurs web d’ajouter des vidéos sur les pages web.

## L'élément video

Pour insérer une vidéo dans une page web - si cette vidéo ne provient pas directement d’une source externe telle que YouTube - l’élément ```<video></video>``` doit être utilisé.

Cet élément est accompagné de l’attribut ```controls```, qui ne reçoit aucune valeur, mais qui permet d’ajouter des contrôles de vidéo, tels que lecture, pause et la gestion du volume.

__Remarque__ : L’élément ```<video></video>``` est un conteneur. C’est à l’intérieur de cet élément que les vidéos sont affichées.

Ensuite, pour indiquer au navigateur quelle vidéo afficher, l’élément ```<source>``` doit être utilisé. Cet élément s’accompagne des attribut ```src```, qui reçoit en valeur le chemin d’accès à la vidéo, et ```type```, qui reçoit en valeur vidéo/format.

__Remarque__ : Il est recommandé d’inclure plusieurs formats pour une même vidéo. Ainsi le navigateur de l’utilisateur peut-il choisir le format qu’il prend en charge. 

Exemple :

```html
<video width="320" height="240" controls>
    <source src="moto.mp4" type="video/mp4">
    <source src="moto.ogg" type="video/ogg">
    Votre navigateur ne peut pas lire cette vidéo.
</video>
```

## Lecture automatique

Le langage HTML permet de lire une vidéo automatiquement lors du premier chargement de la page. Pour ce faire, il faut inclure l’attribut ```autoplay``` dans l’élément ```<video>```. Cet attribut ne reçoit aucune valeur.

__Remarque__ : La lecture automatique de vidéo ne fonctionne pas sur les appareils mobiles. 

Exemple :

```html
<video width="320" height="240" controls>
    <source src="moto.mp4" type="video/mp4">
    <source src="moto.ogg" type="video/ogg">
    Votre navigateur ne peut pas écouter ce son.
</video>
```

## Formats vidéo HTML

Le tableau ci-dessous dresse la liste des formats vidéos pris en charge en fonction du navigateur :

| Navigateur | **MP3** | **WAV** | **OGG** |
| --- | --- | --- | --- |
| Edge/IE | Oui | Oui | Oui |
| Chrome | Oui | Oui | Oui |
| Firefox | Oui | Oui | Oui |
| Safari | Oui | Oui | Non |
| Opera | Oui | Oui | Oui |


# Contenu de ./0380 - Audio/content.md

Le langage HTML permet d’insérer des fichiers audio au sein d’une page web.

## Formats audios en HTML

Comme pour les vidéos, le langage HTML prend en charge 3 formats audios :

| **Navigateur** | **Type de media** |
| --- | --- |
| MP3 | audio/mpeg |
| OGG | audio/ogg |
| WAV | audio/wav |

## Formats et prise en charge des navigateurs

Le tableau ci-dessous résume la prise en charge des trois formats selon le navigateur :

| Navigateur | **MP3** | **WAV** | **OGG** |
| --- | --- | --- | --- |
| Edge/IE | Oui | Non | Non |
| Chrome | Oui | Oui | Oui |
| Firefox | Oui | Oui | Oui |
| Safari | Oui | Oui | Non |
| Opera | Oui | Oui | Oui |

## Prise en charge par les navigateurs

La prise en charge des fichiers audios par le HTML étant relativement récente - elle n’existait pas avant la version 5 du langage - l’élément ```<audio>``` n’est pas supporté par les anciennes versions des navigateurs Internet.

Le tableau ci-dessous résume, pour les navigateurs les plus couramment utilisés, la version à partir de laquelle l’audio est pris en charge :

| **Navigateur** | **Version** |
| --- | --- |
| Chrome | 4.0 |
| Edge/IE | 9.0 |
| Firefox | 3.5 |
| Safari | 4.0 |
| Opera | 10.5 |

## L'élément ```<audio>```

Pour insérer un fichier au sein d’une page web, l’élément ```<audio></audio>``` doit être utilisé. Cet élément est accompagné de l’attribut ```controls``` permettant d’afficher un bouton play/pause ainsi que le contrôle du volume. 

Ensuite, pour inclure le fichier audio, cela fonctionne exactement comme pour l’insertion d’une vidéo. L’élément ```<source>``` est utilisé, accompagné de l’attribut ```src```, qui prend en valeur le chemin d’accès au fichier audio. L’attribut ```type``` est également utilisé, recevant en valeur *audio/format_de_l’audio*.

Exemple :

```html
<audio controls>
    <source src="chat.ogg" type="audio/ogg">
    <source src="chat.mp3" type="audio/mpeg">
</audio>
```


# Contenu de ./0390 - Plugins/content.md

Les plugins, en informatique, sont des “ajouts” qui permettent d’étendre les fonctionnalités d’un langage, tout en facilitant la tâche d’un développeur qui n’a pas besoin de réécrire sans cesse le même code, encore et encore.

## Plug-ins

Avec le langage HTML, les plugins ont été créés afin de résoudre plusieurs problématiques (liste non-exhaustive) :

- Afficher des cartes
- Rechercher des virus
- Vérifier un identifiant bancaire

## L'élément ```<object>```

L'élément ```<object></object>``` est pris en charge par tous les navigateurs. Il représente une source externe. Cette source externe peut être interprétée comme une image ou une ressource à traiter comme un plugin.

Sa principale utilisation est d’intégrer des plugins tels que des lecteurs PDF ou des images, par exemple, directement au sein d’une page web.

Cet élément est au moins accompagné de l’attribut ```data``` qui prend en valeur l’adresse de la ressource à intégrer, ainsi que de l’attribut ```type``` qui reçoit en valeur le type de ressource (*application/pdf*, par exemple pour un fichier PDF).

Exemple :

```html
<object type="application/pdf" data="fichier/lecteur.pdf"></object>
```

## L'élément ```<embed>```

Cet élément a exactement la même fonction et la même utilité que l’élément précédent : inclure un objet ou un plugin. 

La seule différence avec ```<object>``` est que l’élément ```<embed>``` n’est plus beaucoup pris en charge. Pour inclure un plugin, mieux vaut donc utiliser l’élément ```<object></object>```.

L’utilisation de ```<embed>``` est exactement la même que pour ```<object>```.

Exemple :

```html
<embed type="image/jpg" data="images/chat.jpg" />
```

# Contenu de ./0400 - Youtube/content.md

YouTube permet l’intégration de vidéos au sein d’un site web par l’intermédiaire d’un code prêt à l’emploi qu’il n’y a plus qu’à coller dans le document HTML.

Ce cours présente d’abord comment intégrer une vidéo Youtube sur une page web, puis traite des différentes “options” pouvant être ajoutées.

## Intégrer une vidéo YouTube

Pour intégrer une vidéo sur un site web directement depuis YouTube, il suffit de se rendre sur la vidéo souhaitée, puis de cliquer sur “partager”, puis “intégrer”. À partir de là, YouTube fournit directement le code nécessaire pour l’inclusion. Il ne reste plus qu’à le copier/coller au sein du fichier HTML.

Exemple :

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/tbg4EmIJ5pM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Lecture automatique YouTube

La lecture automatique est activée par défaut dans le code fourni par YouTube. Cela signifie qu’au premier chargement de la page web, la vidéo va se lancer automatiquement. 

Pour désactiver cette option, il suffit d’effacer la valeur **autoplay** dans l’attribut ```allow```.

Exemple :

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/tbg4EmIJ5pM" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Désactiver les contrôles de la vidéo

Par défaut, dans le code fourni par YouTube, les contrôles sont activés. Pour les désactiver, il suffit de rajouter ```?controls=0```, à la fin de l’adresse définie dans l’attribut ```src```.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/tbg4EmIJ5pM?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

# Contenu de ./0410 - Caractères spéciaux, codes ISO 5589-1 et abréviations ENTITY/content.md

Voici l’ensemble des caractères et de leurs correspondances selon la norme ISO 5589-1 (couramment nommée ISO-Latin 1), ainsi que les différentes abréviations ENTITY.

| **Caractère** | **Code ISO** | **Entity** |
| --- | --- | --- |
| Espace | ```&#160;``` | ```&nbsp;``` |
| ¡ | ```&#161;``` | ```&iexcl;``` |
| ¢ | ```&#162;``` | ```&cent;``` |
| £ | ```&#163;``` | ```&pound;``` |
| ¤ | ```&#164;``` | ```&curren;``` |
| ¥ | ```&#165;``` | ```&yen;``` |
| ¦ | ```&#166;``` | ```&brvbar;``` |
| § | ```&#167;``` | ```&sect;``` |
| ¨ | ```&#168;``` | ```&uml;``` |
| © | ```&#169;``` | ```&copy;``` |
| ª | ```&#170;``` | ```&ordf;``` |
| « | ```&#171;``` | ```&laquo;``` |
| ¬ | ```&#172;``` | ```&not;``` |
|  | ```&#173;``` | ```&shy;``` |
| ® | ```&#174;``` | ```&reg;``` |
| ¯ | ```&#175;``` | ```&masr;``` |
| ° | ```&#176;``` | ```&deg;``` |
| ± | ```&#177;``` | ```&plusmn;``` |
| ² | ```&#178;``` | ```&sup2;``` |
| ³ | ```&#179;``` | ```&sup3;``` |
| ´ | ```&#180;``` | ```&acute;``` |
| µ | ```&#181;``` | ```&micro;``` |
| ¶ | ```&#182;``` | ```&para;``` |
| · | ```&#183;``` | ```&middot;``` |
| ¸ | ```&#184;``` | ```&cedil;``` |
| ¹ | ```&#185;``` | ```&supl;``` |
| º | ```&#186;``` | ```&ordm;``` |
| » | ```&#187;``` | ```&raquo;``` |
| ¼ | ```&#188;``` | ```&frac14;``` |
| ½ | ```&#189;``` | ```&frac12;``` |
| ¾ | ```&#190;``` | ```&frac34;``` |
| ¿ | ```&#191;``` | ```&iquest;``` |
| À | ```&#192;``` | ```&Agrave;``` |
| Á | ```&#193;``` | ```&Aacute;``` |
|   | ```&#194;``` | ```&Acirc;``` |
| Ã | ```&#195;``` | ```&Atilde;``` |
| Ä | ```&#196;``` | ```&Auml;``` |
| Å | ```&#197;``` | ```&Aring;``` |
| Æ | ```&#198;``` | ```&Aelig;``` |
| Ç | ```&#199;``` | ```&Ccedil;``` |
| È | ```&#200;``` | ```&Egrave;``` |
| É | ```&#201;``` | ```&Eacute;``` |
| Ê | ```&#202;``` | ```&Ecirc;``` |
| Ë | ```&#203;``` | ```&Euml;``` |
| Ì | ```&#204;``` | ```&Igrave;``` |
| Í | ```&#205;``` | ```&Iacute;``` |
| Î | ```&#206;``` | ```&Icirc;``` |
| Ï | ```&#207;``` | ```&Iuml;``` |
| Ð | ```&#208;``` | ```&ETH;``` |
| Ñ | ```&#209;``` | ```&Ntilde;``` |
| Ò | ```&#210;``` | ```&Ograve;``` |
| Ó | ```&#211;``` | ```&Oacute;``` |
| Ô | ```&#212;``` | ```&Ocirc;``` |
| Õ | ```&#213;``` | ```&Otilde;``` |
| Ö | ```&#214;``` | ```&Ouml;``` |
| × | ```&#215;``` | ```&times;``` |
| Ø | ```&#216;``` | ```&Oslash;``` |
| Ù | ```&#217;``` | ```&Ugrave;``` |
| Ú | ```&#218;``` | ```&Uacute;``` |
| Û | ```&#219;``` | ```&Ucirc;``` |
| Ü | ```&#220;``` | ```&Uuml;``` |
| Ý | ```&#221;``` | ```&Yacute;``` |
| Þ | ```&#222;``` | ```&THORN;``` |
| ß | ```&#223;``` | ```&szlig;``` |
| à | ```&#224;``` | ```&agrave;``` |
| á | ```&#225;``` | ```&aacute;``` |
| â | ```&#226;``` | ```&acirc;``` |
| ã | ```&#227;``` | ```&atilde;``` |
| ä | ```&#228``` | ```&auml;``` |
| å | ```&#229``` | ```&aring;``` |
| æ | ```&#230``` | ```&aelig;``` |
| ç | ```&#231``` | ```&ccedil;``` |
| è | ```&#232``` | ```&egrave;``` |
| é | ```&#233``` | ```&eacute;``` |
| ê | ```&#234``` | ```&ecirc;``` |
| ë | ```&#235``` | ```&euml;``` |
| ì | ```&#236``` | ```&igrave;``` |
| í | ```&#237``` | ```&iacute;``` |
| î | ```&#238``` | ```&icirc;``` |
| ï | ```&#239``` | ```&iuml;``` |
| ð | ```&#240``` | ```&eth;``` |
| ñ | ```&#241``` | ```&ntilde;``` |
| ò | ```&#242``` | ```&ograve;``` |
| ó | ```&#243``` | ```&oacute;``` |
| ô | ```&#244``` | ```&ocirc;``` |
| õ | ```&#245``` | ```&otilde;``` |
| ö | ```&#246``` | ```&ouml;``` |
| ÷ | ```&#247``` | ```&divide;``` |
| ø | ```&#248``` | ```&oslash;``` |
| ù | ```&#249``` | ```&ugrave;``` |
| ú | ```&#250``` | ```&uacute;``` |
| û | ```&#251``` | ```&ucirc;``` |
| ü | ```&#252``` | ```&uuml;``` |
| ý | ```&#253``` | ```&yacute;``` |
| þ | ```&#254``` | ```&thorn;``` |
| ÿ | ```&#255``` | ```&yuml;``` |
| Œ | ```&#338;``` | ```&OElig;``` |
| œ | ```&#339;``` | ```&oelig;``` |
| Š | ```&#352;``` |  |
| š | ```&#353;``` |  |
| Ÿ | ```&#376;``` |  |
| Ž | ```&#381;``` |  |
| ž | ```&#382;``` |  |
| ƒ | ```&#402;``` |  |
| ˆ | ```&#710;``` |  |
| ˜ | ```&#732;``` |  |
| – | ```&#8211;``` |  |
| — | ```&#8212;``` |  |
| ‘ | ```&#8216;``` |  |
| ’ | ```&#8217;``` |  |
| ‚ | ```&#8218;``` |  |
| “ | ```&#8220;``` |  |
| ” | ```&#8221;``` |  |
| „ | ```&#8222;``` |  |
| † | ```&#8224;``` | ```&dagger;``` |
| ‡ | ```&#8225;``` |  |
| • | ```&#8226;``` |  |
| … | ```&#8230;``` |  |
| ‰ | ```&#8240;``` | ```&permil;``` |
| ‹ | ```&#8249;``` |  |
| › | ```&#8250;``` |  |
| ™ | ```&#8482;``` | ```&trade;``` |
| & |  | ```&amp;``` |
| › |  | ```&rsaquo;``` |
| > |  | ```&gt;``` |
| ” |  | ```&rdquo;``` |
| ↑ |  | ```&uarr;``` |
| ↓ |  | ```&darr;``` |
| ♠ |  | ```&spades;``` |
| ♥ |  | ```&hearts;``` |
| ‹ |  | ```&lsaquo;``` |
| < |  | ```&lt;``` |
| “ |  | ```&ldquo;``` |
| ← |  | ```&larr;``` |
| → |  | ```&rarr;``` |
| ♦ |  | ```&diams;``` |
| ♣ |  | ```&clubs;``` |
| " |  | ```&quot;``` |

# Contenu de ./0420 - Memento des balises HTML et de leurs attributs/content.md

## Les balises de premier niveau


| **Balise**     | **Description**                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| ```!DOCTYPE``` | Balise de déclaration du type du document permettant au navigateur d’interpréter correctement la version déclarée |
| ```html```     | Balise de definition d’un document HTML                                                                           |
| ```head```     | Balise de définition du bloc d’en-tête de la page                                                                 |
| ```body```     | Balise de définition du bloc du corps de la page                                                                  |

## Les balises d’en-tête

| **Balise**     | **Description**                                               |
|----------------|---------------------------------------------------------------|
| ```link```     | Balise de liaison d’une ressource externe au document HTML    |
| ```meta```     | Balise de métadonnées                                         |
| ```script```   | Balise d’inclusion de script                                  |
| ```noscript``` | Balise ne s’affichant que lorsque les scripts sont désactivés |
| ```style```    | Balise d’insertion de style au sein du document HTML          |
| ```title```    | Balise contenant le titre du document HTML                    |

## Les balises structurelles de texte

| **Balise**       | **Description**                                                        |
|------------------|------------------------------------------------------------------------|
| ```abbr```       | Abréviation                                                            |
| ```blockquote``` | Citation longue                                                        |
| ```cite```       | Citation d’un titre d’oeuvre ou d’évènement                            |
| ```q```          | Citation courte                                                        |
| ```sup```        | Exposant                                                               |
| ```sub```        | Indice                                                                 |
| ```strong```     | Mise en valeur forte                                                   |
| ```em```         | Mise en valeur normale                                                 |
| ```b```          | Mise en valeur graphique (gras)                                        |
| ```i```          | Mise en valeur graphique (italique)                                    |
| ```h1```         | Titre de niveau 1                                                      |
| ```h2```         | Titre de niveau 2                                                      |
| ```h3```         | Titre de niveau 3                                                      |
| ```h4```         | Titre de niveau 4                                                      |
| ```h5```         | Titre de niveau 5                                                      |
| ```h6>```        | Titre de niveau 6                                                      |
| ```img```        | Balise d’insertion d’image                                             |
| ```figure```     | Balise de regroupement d’un ou plusieurs médias                        |
| ```figcaption``` | Description ou légende d’un élément **figure**                         |
| ```audio```      | Balise d’intégration de son                                            |
| ```video```      | Balise d’intégration de vidéo                                          |
| ```source```     | Balise de source de l’audio ou de la vidéo d’une balise correspondante |
| ```a```          | Balise de lien                                                         |
| ```br```         | Balise de retour à la ligne                                            |
| ```p```          | Balise de paragraphe                                                   |
| ```hr```         | Ligne de séparation horizontale                                        |
| ```address```    | Balise d’informations à propos de l’auteur de l’article ou du document |
| ```del```        | Balise encadrant un texte qui a été supprimé d’un document             |
| ```ins```        | Balise encadrant un texte qui a été ajouté dans un document            |
| ```dfn```        | Balise encadrant le sujet de la définition d’un terme                  |
| ```kbd```        | Balise représentant une saisie clavier                                 |
| ```pre```        | Balise d’affichage d’un texte préformaté                               |
| ```progress```   | Balise représentant l’état d’avancement d’une tâche                    |
| ```time```       | Balise représentant une date et / ou une heure                         |

## Les balises de liste

| **Balise** | **Description**                      |
|----------|--------------------------------------|
| ```ul``` | Balise de liste à puces              |
| ```ol``` | Balise de liste numérotée            |
| ```li``` | Élément d’une liste **ul** ou **ol** |
| ```dl``` | Balise de liste de définitions       |
| ```dt``` | Balise encadrant le terme à définir  |
| ```dd``` | Balise de définition du terme        |

## Les balises de tableau

| **Balise**    | **Description**                                                 |
|---------------|-----------------------------------------------------------------|
| ```table```   | Balise de déclaration d’un tableau                              |
| ```thead```   | Balise de déclaration de l’en-tête d’un tableau                 |
| ```tbody```   | Balise de déclaration du corps d’un tableau                     |
| ```tfoot```   | Balise de déclaration du pied d’un tableau                      |
| ```tr```      | Balise de déclaration d’une ligne dans un tableau               |
| ```td```      | Balise de déclaration d’une cellule dans un tableau             |
| ```th```      | Balise de déclaration d’une cellule dans l’en-tête d’un tableau |
| ```caption``` | Titre d’un tableau                                              |

## Les balises de formulaire

| **Balise**     | **Description**                                           |
|----------------|-----------------------------------------------------------|
| ```form```     | Balise de formulaire                                      |
| ```fieldset``` | Balise de regroupement de champs                          |
| ```legend```   | Balise de titre d’un groupe de champs                     |
| ```label```    | Balise de libellé d’un champ                              |
| ```input```    | Balise de champ                                           |
| ```textarea``` | Balise de zone de saisie à plusieurs lignes               |
| ```select```   | Balise de liste déroulante                                |
| ```option```   | Balise d’élément d’une liste déroulante                   |
| ```optgroup``` | Balise de groupement d’éléments dans une liste déroulante |

## Les balises de section

| **Balise**    | **Description**                                                          |
|---------------|--------------------------------------------------------------------------|
| ```header```  | Balise d’en-tête du document ou d’une partie du document                 |
| ```nav```     | Balise contenant les principaux liens représentant le menu de navigation |
| ```footer```  | Balise de pied de page du document ou d’une partie du document           |
| ```section``` | Balise de section du document                                            |
| ```article``` | Balise de définition d’un article                                        |
| ```aside```   | Balise de groupement d’informations complémentaires                      |

## Les balises génériques

| **Balise** | **Description**       |
|------------|-----------------------|
| ```span``` | Balise de type inline |
| ```div```  | Balise de type block  |

## Les attributs génériques

| **Balise**            | **Description**                                                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```accesskey```       | Attribut permettant de définir un raccourci clavier pour activer ou donner le focus à un élément                                                         |
| ```class```           | Attribut permettant d’attacher une ou plusieurs classes à l’élément HTML                                                                                 |
| ```contenteditable``` | Attribut permettant d’indiquer si le contenu est éditable                                                                                                |
| ```contextmenu```     | Référence à l’identifiant d’un élément **menu** pour définir un menu contextuel à l’élément courant                                                      |
| ```dir```             | Attribut définissant la direction du texte                                                                                                               |
| ```hidden```          | Attribut permettant de cacher le rendu visuel d’un élément sans altérer l’affichage des éléments enfants actifs                                          |
| ```id```              | Attribut permettant d’identifier de façon unique un élément                                                                                              |
| ```lang```            | Attribut indiquant la langue utilisée dans l’élément                                                                                                     |
| ```style```           | Attribut permettant de définir des styles CSS directement au sein du code HTML                                                                           |
| ```tabindex```        | Attribut permettant de modifier l’ordre de navigation de la touche tabulation                                                                            |
| ```title```           | Attribut permettant de définir un texte explicatif de l’élément concerné. Ce texte est généralement affiché grâce à une infobulle au survol de l’élément |

## Les attributs pour tableaux

| **Balise**        | **Description**                                               |
|-------------------|---------------------------------------------------------------|
| ```border```      | Définit l’épaisseur de la bordure du tableau                  |
| ```cellspacing``` | Définit l’espace entre les cellules du tableau                |
| ```cellpadding``` | Définit les marges intérieures des cellules d’un tableau      |
| ```width```       | Définit la largeur d’un tableau ou d’une cellule              |
| ```height```      | Définit la hauteur d’un tableau ou d’une cellule              |
| ```bordercolor``` | Définit la couleur des bordures d’un tableau                  |
| ```bgcolor```     | Définit la couleur de fond d’un tableau et / ou d’une cellule |
| ```colspan```     | Définit la fusion de plusieurs cellules en largeur            |
| ```rowspan```     | Définit la fusion de plusieurs cellules en hauteur            |
| ```align```       | Definite l’alignement horizontal du contenu d’une cellule     |
| ```valign```      | Définit l’alignement vertical du contenu d’une cellule        |

## Les attributs des balises d’image

| **Balise**   | **Description**                                                                    |
|--------------|------------------------------------------------------------------------------------|
| ```src```    | Définit le chemin vers le fichier de l’image                                       |
| ```width```  | Définit la largeur de l’image                                                      |
| ```height``` | Définit la hauteur de l’image                                                      |
| ```alt```    | Définit un contenu alternatif à afficher lorsque l’image ne peut pas être affichée |
| ```align```  | Définit l’alignement du texte par rapport à l’image                                |
| ```usemap``` | Définit le nom de l’image interactive à utiliser                                   |

## Les attributs des balises de lien

| **Balise**            | **Description**                                                                         |
|-----------------------|-----------------------------------------------------------------------------------------|
| ```alt```             | Définit un contenu alternatif à afficher lorsque le lien ne peut pas être affiché       |
| ```href```            | Définit l’URL du lien                                                                   |
| ```target=”_blank”``` | Force le navigateur à ouvrir le lien dans un nouvel onglet ou bien une nouvelle fenêtre |

