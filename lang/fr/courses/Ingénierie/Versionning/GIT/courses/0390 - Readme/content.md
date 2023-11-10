## Accès rapide

Si vous souhaitez accéder rapidement à notre template de markdown, vous pouvez utiliser directement ce lien : XXX . Si vous n'avez aucune idée de ce qu'est ce template, alors vous devriez commencé par lire la suite du cours !

## Qu'est-ce qu'un readme ?

Un ```readme``` est un fichier contenant des informations ou des instructions concernant un projet. Sa dénomination encourage ainsi à lire le fichier avant de faire une quelconque action. Les readme existent depuis de nombreuses années, mais l'arrivée du versionning et de GIT ont largement favoriser son utilisation.

Au sein d'un projet GIT, les readme sont souvent rédigés en utilisant le format appelé **Markdown**. Ce format est en réalité une simplification restreinte du langage HTML, reprenant ses éléments fondamentaux, mais simplifié par sa syntaxe et sa mise en place pour permettre à n'importe qui de l'utiliser simplement. Les fichiers markdown utilisent l'extension ```.md```.

Lors de l'affichage d'un readme par un navigateur par exemple, le format Markdown est transformé en HTML ce qui permet d'en afficher son contenu. Notez également qu'il est toutefois possible d'écrire directement du HTML dans un fichier Markdown si vous souhaitez apportez des éléments spécifiques non disponible.

## Structure

Ce point du cours est souvent sujet à questionnement de la part des développeurs juniors ou des étudiants encore en apprentissage. Il est bien de savoir ce qu'est un fichier readme, mais que devez-vous mettre dedans ? Dans quel ordre ? Avec quelle organisation ?

Cette partie du cours à donc pour objectif de vous présenter les différentes parties que l'on retrouve généralement dans un readme. Notez toutefois que **toutes les parties ne sont pas obligatoire** et certaines peuvent être supprimées si elles ne correspondent pas à vos besoins ! Gardez bien en tête que l'objectif premier n'est pas de donner des informations inutiles à propos de votre projet !

### 1 - Le nom

Le premier élément que vous devez positionner tout en haut de votre readme, en tant que titre principal, est le nom de votre projet. Donnez un nom explicite et parfaitement représentatif du projet pour faciliter son identification.

### 2 - La description

Souvent juste en dessous du titre, sous forme de paragraphe, une description succincte du projet est attendue. L'idée est ici de contextualiser l'ensemble du projet pour qu'une personne externe puisse bien comprendre ce qu'est votre projet. Cette partie contient également souvent une liste des fonctionnalités que vous proposez, et essaye généralement de se démarquer des projets alternatifs présentants des similarités avec le vôtre en listant les facteurs différanciant.

### 3 - Les badges

Certains readme mettent en avant des "badges" qui fournissent différentes informations additionnelle à propos de votre projet. Voici deux exemples de badges que vous pouvez retrouver sur un readme : 

![premier badge](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0390%20-%20Readme/images/img_1.svg "premier badge")
![deuxième badge](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0390%20-%20Readme/images/img_2.svg "deuxième badge")



Structure
- dépend du type de projet
----> DEV
- Une description générale du système ou du projet.
- Le statut du projet, qui est surtout utile lorsqu’il est encore en stade du développement. Évoquez les modifications prévues et l’objectif du développement ou signalez clairement que le développement du projet est terminé.
- Les exigences concernant l’environnement de développement en vue de son intégration.
- Une instruction pour l’installation et l’utilisation.
- Une liste des technologies utilisées et, le cas échéant, des liens vers d’autres informations sur ces technologies.
- Les projets open source que les développeurs modifient ou complètent par eux-mêmes doivent être complétés par un paragraphe « collaboration souhaitée » dans leur fichier readme.md. Comment contourner un problème ? Comment les développeurs doivent-ils appliquer les modifications ?
- Bugs connus et corrections éventuelles apportées.
- Section FAQ reprenant toutes les questions posées jusqu’à présent.
- Droits d’auteurs et informations sur la licence.
----> Data
- Les noms de l'investigateur/trice principal-e et des co-investigateurs/trices de l’étude
- Une description de la méthodologie et des outils utilisés pour la collecte des données
- Les dates de collecte des données
- Une description de la hiérarchie du répertoire, du type de données qu'il contient et de la convention de dénomination des fichiers
- Une liste complète de tous les titres/codes/abréviations et conventions utilisées dans les fichiers.
- Les conditions de partage et d'accès (licence) pendant et après la fin du projet.

----> autres
- un titre, le nom du projet ;
- une description de ce que fait le plugin, sans trop entrer dans la technique ;
- Les pré-requis à l’utilisation du plugin (version de node si besoin, dépendances, etc.)
- le guide d’installation (les commandes à exécuter pour l’installation, les éventuels problèmes qui peuvent intervenir, etc.) ;
- le guide d’utilisation : les méthodes, leurs options, ce qu’elles retournent, etc.
- une roadmap, pour présenter ce que vous avez prévu pour le futur du plugin, avec d’éventuelles dates comme jalons ;
- la licence d’utilisation, si vous voulez notamment limiter l’utilisation de votre plugin ;
- les divers contributeurs, s’il y en a, ainsi qu’un moyen de les ou de vous contacter directement.

LIENS

- https://www.makeareadme.com/
- https://shields.io/


TEMPLATE

