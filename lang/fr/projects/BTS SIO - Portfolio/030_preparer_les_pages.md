## Énoncé

### Description courte

Maintenant que vous avez découpé votre template, il est temps d'attaquer la réalisation ou du moins la mise en place des pages de votre portfolio.

## Étapes

### 1. Lister les pages nécessaires

Il est possible d'avoir de nombreux plans et de nombreuses pages pour les portfolio. Cependant, à des fins d'unification et de facilitation, voici une liste des pages que vous devrez réaliser et donc préparer. Notez que la liste n'est pas exhaustive, et que vous pouvez choisir d'ajouter d'autres pages.

#### Liste des pages

- Accueil
- Entreprise
- Veille
- BTS SIO
- Mentions légales
- Missions (plus 1 page par mission réalisée)
- Projets (plus 1 page par projet réalisé)
- Compétences (plus 1 page par compétence mise en oeuvre)
- Synthèse

#### Création des pages

Pour chacune des pages listées ci-dessus, vous allez devoir créer un fichier du nom de la page, avec l'extension ```.php```. Placez ce fichier à la racine de votre projet (au même niveau que le fichier ```index.php```).

Remettre en place le contenu de base pour chaque page : c'est à dire le header, le footer à minima. Le plus simple à ce stade, est de copier/coller le contenu du fichier index, de telle sorte à avoir le même contenu sur toutes les pages.

Vous pourrez enfin commencer à réfléchir à l'agencement de chaque page.

### 2. Implémenter le menu

Mettre en place votre menu principal, avec les liens fonctionnels vers vos pages PHP. Plusieurs cas de figure sont possibles, en fonction de si votre template intègre des sous-menus ou non.

#### Sans sous-menu

Voici le plan de votre menu si votre template n'implémente pas de design pour les sous-menus :

- Accueil : redirige vers la page d'accueil (index)
- BTS SIO : redirige vers la page qui va présenter le BTS SIO
- Entreprise : redirige vers la page qui va présenter l'entreprise
- Veille : redirige vers la page de veille
- Projets : redirige sur la page qui liste les projets réalisés
- Missions : redirige sur la page qui liste les missions réalisées
- Compétences : redirige sur la page qui liste les compétences et sous-compétences, ainsi que les projets et travaux associés.
- Synthèse : redirige sur la page qui liste l'association des compétences et des projets

_Note_ : Les **projets** sont des travaux qui sont suffisamment conséquents pour être présentés lors de l'épreuve E5

_Note_ : Les **travaux** sont la liste de tous les projets que vous avez réalisés : en cours, en entreprise ou à titre personnel. Les petits exercices de pratique ne sont pas consiédérés comme des travaux !

#### Avec sous-menu

Voici le plan de votre menu si votre template implémente un design pour les sous-menus :

- Accueil : redirige vers la page d'accueil (index)
- BTS SIO : redirige vers la page qui va présenter le BTS SIO
- Entreprise : redirige vers la page qui va présenter l'entreprise
- Veille : redirige vers la page de veille
- Projets : redirige sur la page qui liste les projets réalisés
    - Projet 1
    - Projet 2
    - Projet 3
    - ...
- Missions : redirige sur la page qui liste les missions réalisées
    - Mission 1
    - Mission 2
    - Mission 3
    - ...
- Compétences : redirige sur la page qui liste les compétences
    - Gérer le patrimoine informatique
    - Répondre aux incidents et aux demandes d'assistance et d'évolution
    - Déelopper la présence en ligne de l'organisation
    - Travailler en mode projet
    - Mettre à disposition des utilisateurs un service informatiqe
    - Organiser son développement professionel
- Synthèse : redirige sur la page qui liste l'association des compétences et des projets

Comparativement avec les templates qui n'ont pas de sous-menu, vous allez ici intégrer un lien par travail ou projet réalisé en sous-menu !

_Note_ : Les **projets** sont des missions qui sont suffisamment conséquents pour être présentés lors de l'épreuve E5

_Note_ : Les **missions** sont la liste de tous les projets que vous avez réalisés : en cours, en entreprise ou à titre personnel. Les petits exercices de pratique ne sont pas consiédérés comme des missions !

### 3. Implémenter les éléments du footer

Il est maintenant temps de gérer l'ensemble des informations contenues dans votre footer. Notez ici qu'on doit à minima y retrouver un lien vers vos mentions légales. Voici tout de même une liste non exhaustive des éléments que l'on pourrait y retrouver, et qu'il faut implémenter maintenant : 

- Les mentions légales
- Les informations de contact (nom/prénom, tel, mail, adresse, etc...)
- Un copyright
- Des liens vers les pages internes du site
- Les informations de contact & liens vers vos réseaux sociaux (LinkedIn, Github à minima, + mail & téléphone si vous le souhaitez)
- Etc...

Une fois cette étape réalisée, il va être temps de commencer à agencer les pages !


