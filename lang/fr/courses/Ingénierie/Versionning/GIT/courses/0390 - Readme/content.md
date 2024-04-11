## Accès rapide

Si vous souhaitez accéder rapidement à notre template de markdown, vous pouvez utiliser directement ce lien : <a href="https://github.com/kevinniel/readme-template-microlead/archive/refs/heads/main.zip" title="Template de readme Microlead" rel="nofollow">Template de readme Microlead</a> . Si vous n'avez aucune idée de ce qu'est ce template, alors vous devriez commencer par lire la suite du cours !

## Qu'est-ce qu'un readme ?

Un ```readme``` est un fichier contenant des informations ou des instructions concernant un projet. Sa dénomination encourage ainsi à lire le fichier avant de faire une quelconque action. Les readme existent depuis de nombreuses années, mais l'arrivée du versionning et de GIT ont largement favorisé son utilisation.

Au sein d'un projet GIT, les readme sont souvent rédigés en utilisant le format appelé **Markdown**. Ce format est en réalité une simplification restreinte du langage HTML, reprenant ses éléments fondamentaux, mais simplifié par sa syntaxe et sa mise en place pour permettre à n'importe qui de l'utiliser simplement. Les fichiers markdown utilisent l'extension ```.md```.

Lors de l'affichage d'un readme par un navigateur par exemple, le format Markdown est transformé en HTML ce qui permet d'en afficher son contenu. Notez également qu'il est toutefois possible d'écrire directement du HTML dans un fichier Markdown si vous souhaitez apporter des éléments spécifiques non disponibles.

## Structure

Ce point du cours est souvent sujet à questionnement de la part des développeurs juniors ou des étudiants encore en apprentissage. Il est bien de savoir ce qu'est un fichier readme, mais que devez-vous mettre dedans ? Dans quel ordre ? Avec quelle organisation ?

Cette partie du cours à donc pour objectif de vous présenter les différentes parties que l'on retrouve généralement dans un readme. Notez toutefois que **toutes les parties ne sont pas obligatoires** et certaines peuvent être supprimées si elles ne correspondent pas à vos besoins ! Gardez bien en tête que l'objectif premier n'est pas de donner des informations inutiles à propos de votre projet !

### 1 - Le nom

Le premier élément que vous devez positionner tout en haut de votre readme, en tant que titre principal, est le nom de votre projet. Donnez un nom explicite et parfaitement représentatif du projet pour faciliter son identification.

### 2 - La description

Souvent juste en dessous du titre, sous forme de paragraphe, une description succincte du projet est attendue. L'idée est ici de contextualiser l'ensemble du projet pour qu'une personne externe puisse bien comprendre ce qu'est votre projet. Cette partie contient également souvent une liste des fonctionnalités que vous proposez, et essaye généralement de se démarquer des projets alternatifs présentant des similarités avec le vôtre en listant les facteurs différenciant.

### 3 - Les badges

Certains readme mettent en avant des "badges" qui fournissent différentes informations additionnelles à propos de votre projet. Voici deux exemples de badges que vous pouvez retrouver sur un readme : 

![premier badge](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0390%20-%20Readme/images/img_1.svg "premier badge")
![deuxième badge](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/Ing%C3%A9nierie/Versionning/GIT/courses/0390%20-%20Readme/images/img_2.svg "deuxième badge")

Il existe différents types de badge, certains sont dits "statics" : vous les créez en y mettant le texte que vous voulez. D'autres sont générés par des labelisateurs auprès desquels vous allez justement chercher une labellisation. Ces badges vous permettent donc de mettre en avant tous les atouts de votre projet.

Pour en savoir plus sur les badges ou en créer vous-même, vous pouvez vous rendre sur le site <a href="https://shields.io" title="shields - le site de gestion des badges pour github" target="_blank" rel="nofollow">https://shields.io</a>

### 4 - Les visuels

En fonction du projet que vous menez, il peut être judicieux d'intégrer des visuels (photos, GIF, vidéos, etc...) de votre projet. Une image valant mille mots, cela peut permettre à d'autres internautes de comprendre plus simplement ce à quoi correspond votre projet et peut les inciter davantage à l'utiliser (l'inverse est vrai aussi d'ailleurs 😇)

### 5 - Les prérequis

Si votre projet nécessite l'installation de dépendances ou de logiciels manuellement pour faire fonctionner votre projet, il est temps de transmettre l'information. Faites attention, n'oubliez pas également de mentionner les numéros de versions minimales requises si existantes !

### 6 - Installation

C'est la partie la plus délicate et la plus importante du readme. Elle doit contenir l'ensemble des informations nécessaires à une installation en partant de zéro de votre projet. Vous devez lister ici toutes les étapes une par une, et de manière réplicable. Afin de vous assurer des informations que vous y mettez, nous vous conseillons de réinstaller votre projet dans un nouvel endroit sur votre ordinateur afin de vous assurer de la **réplicabilité** des actions ainsi listées.

**Note** : Si différentes étapes sont nécessaires en fonction des OS sur lesquels l'installation est effectuée (Windows, Mac, Linux, iOS, Android, etc...), alors il vous appartient de répliquer cette partie pour chacune des différentes plateformes.

### 7 - utilisation

Cette partie contient généralement des exemples d'utilisation de votre projet. Cela permet de démontrer son utilisation et d'exposer le genre d'action et ou de résultats que vous pouvez obtenir. Si toutefois les explications ou exemples d'utilisation sont trop longs pour être présenté dans un readme, alors nous vous recommandons de positionner ici des liens vers d'autres fichiers de type **markdown** que vous pouvez aussi inclure dans votre projet.

### 8 - Support

Renseignez ici les manières disponibles pour les utilisateurs de contacter un support en cas de problème. Il n'y a pas de règle particulière ici, même si nous vous déconseillons évidemment d'exposer publiquement votre mail ou votre téléphone. Préférez un lien vers une page contact d'un site internet, ou bien une procédure à mettre en place directement sur votre plateforme de gestion de projet (Github, Gitlab, etc...)

### 9 - Roadmap

Cette partie n'est à renseigner que si vous êtes toujours en phase de développement. Elle contient comme son nom l'indique les différentes étapes de réalisation du projet, avec si possible des dates ou à minima l'état d'avancement des différentes actions nécessaires pour mener à bien le projet.

### 10 - Contribution

Cette partie indique si vous êtes ouvert ou non à des contributions extérieures. Souhaitez-vous voir d'autres internautes s'impliquer dans votre projet ? Si tel est le cas, alors c'est le parfait endroit pour y documenter les moyens et la manière de prendre part à votre projet.

Si toutefois certaines étapes sont nécessaires à la mise en place d'un projet en tant que contributeur, vous pouvez également les lister ici. Documentez également les commandes de tests si vous en utilisez, ou bien les configurations des linters que vous pourriez utiliser.

### 11 - Auteurs et reconnaissance

Cette partie est souvent dédiée à la mention des personnes ayant pris part au projet. Elle permet de mentionner toute votre équipe et permet d'exposer publiquement votre reconnaissance envers eux. C'est une pratique très courante dans le monde du développement.

Notez évidemment que le but n'est pas d'inclure ici 100% des contributeurs, mais bien des principaux, sans qui le projet n'aurait pas vu le jour où ne pourrait plus fonctionner.

### 12 - Licence

Tout projet doit mentionner la licence qui lui est appliquée afin de renseigner sur les droits d'exploitation, commerciaux ou non, du projet. Parmi les licences les plus utilisées, on retrouve : 

- GPL ou GNU GPL (General Public Licence)
- MIT
- BSD

Pour en savoir plus sur les licences, nous vous recommandons l'excellente description disponible chez <a href="https://fr.wikipedia.org/wiki/Licence_de_logiciel" title="Licences logiciel" target="_blank" rel="nofollow">wikipedia</a>

## Les quelques règle supplémentaires

### Le statut du projet

Si toutefois vous comptez abandonner un projet ou drastiquement réduire le temps que vous allez passer dessus, il est d'usage d'en faire mention **au début du readme** pour permettre à d'autres internautes de forker votre projet et de continuer à le faire vivre.

### Exemples de bons readme ?

Il n'existe pas un readme de référence particulier. Il est encore une fois important de rappeler que chaque projet et la manière dont il est géré est unique. Aussi pour vous rendre compte de ce que sont les readme des gros projets, nous avons fait une petite sélection de liens qui vous permettront de vous en rendre compte : 

- <a href="https://github.com/microsoft/vscode" title="VSCode" target="_blank" rel="nofollow">VSCode</a> : Le dépôt officiel du célèbre éditeur de code. 150 000 étoiles, 27 000 forks, 115 000 commits, 1 900 contributeurs
- <a href="https://github.com/flutter/flutter" title="Flutter" target="_blank" rel="nofollow">Flutter</a> : Le dépôt officiel de Flutter. 158 000 étoiles, 26 000 forks, 38 000 commits, 1 250 contributeurs
- <a href="https://github.com/cypress-io/cypress" title="Cypress" target="_blank" rel="nofollow">Cypress</a> : Le dépôt officiel de Cypress. 45 000 étoiles, 3 000 forks, 20 000 commits, 450 contributeurs, utilisé par plus de 1 100 000 utilisateurs.

### Le template magique !

Pour terminer ce cours, nous vous avons préparé un template complet avec des rappels de formatage markdown pour vous permettre de gagner du temps lors de la rédaction de vos readme. Vous pouvez le télécharger en suivant ce lien : <a href="https://github.com/kevinniel/readme-template-microlead/archive/refs/heads/main.zip" title="Template de readme Microlead" rel="nofollow">Template de readme Microlead</a>