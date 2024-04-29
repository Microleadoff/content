## Énoncé

### Description courte

Vous allez devoir réaliser un outil de gestion de bar et de commande simple en utilisant le PHP. Il devra être possible de gérer les éléments suivants : 

- Gestion des boissons
- Gestion des tables
- Gestion des commandes

Il devra être possible de réaliser toutes les opérations CRUD (Create - Read - Update - Delete) pour la gestion des boissons ainsi que des tables.
La gestion des commandes devra également intégrer la gestion automatique du calcul du prix total, de l'enregistrement de la date de commande, ainsi que de la modification d'un statut de paiement. Ce dernier devra être un booléen défini à "False" lorsque la commande n'est pas payée, mais "True" lorsqu'elle l'est.

Vous devrez créer des formulaires en HTML afin de pouvoir récupérer la saisie des informations utilisateurs

Vous pouvez utiliser du CSS pour styliser l'ensemble de votre page, mais ce n'est pas obligatoire.

### Éléments donnés

Voici les informations que vous devez stocker concernant les boissons :

- Nom
- Description (facultatif - recette)
- Prix

Voici les informations que vous devez stocker concernant les tables :

- Nom
- Disponibilité
- Détail de la commande en cours

Voici les informations que vous devez stocker concernant les commandes :

- Numéro (généré automatiquement)
- Contenu (liste de boissons)
- Prix total
- Date
- Statut de paiement

### Contraintes

- N'utiliser que du HTML, CSS et PHP
- Vous devez obligatoirement exploiter l'orienté objet, et tous vos traitements doivent obligatoirement être dans des classes
- L'enregistrement des informations doit se faire grâce aux Cookies, aucune base de données ne doit être utilisée.

## Étapes de réalisation

1. Créer toutes les pages (visuelles) du projet (affichage des listes, tableaux avec données fictives en dur pour le moment, les formulaires, etc...). Attention, pas de PHP nécessaire ici, uniquement le HTML et le CSS sont nécessaires pour faire l'affichage. Nuance tout de même, il est possible d'enregistrer les fichiers en ```.php``` pour permettre les ```include()```, notamment pour éviter les copier/coller des header, menu, footer, etc...
2. Gérer le formulaire de création d'une boisson sur un nouveau fichier PHP, grâce aux superglobales, en procédural. Faire en sorte que le traitement de ce formulaire modifie les cookies et redirige - une fois le traitement terminé - sur le fichier qui affiche la page de listing des boissons.
3. Modifier le fichier qui gère la page d'affichage de la liste des boisons, pour qu'il n'affiche QUE les boissons en provenance des cookies.
4. Mettre en place un fichier, réprésentatif d'une page qui affiche le formulaire de modification d'une boisson.
5. Mettre en place le fichier de gestion de la modification de la boisson, qui redirige une fois le traitement réalisé sur la page de listing des boissons.
6. Mettre en place la suppression d'une boisson sur le même principe
7. Mettre en place une page de visualisation du détail d'une boisson spécifique

Vous avez terminer un CRUD (Create, Read, Update, Delete) complet en PHP. Reproduire les étapes pour les tables et les commandes !

Vous pourrez enfin basculer en orienté objet si vous êtes à l'aise et que vous souhaitez refactorer votre code.

### Astuces

Vous pouvez stocker un tableau d'éléments au format JSON dans vos cookies. Voici un exemple : 

```php
<?php

$info = ["a", "b", "c", "d"];

// Enregistrement du cookie
// setcookie prend 3 paramètres : 
// 1. le nom du cookie, à définir par vos soins
// 2. la donnée à stocker : ici il s'agit du tableau transformé en JSON
// 3. la durée de conservation : ici 1 an
setcookie('le_nom_du_cookie', json_encode($info), strtotime("+1 year"));

// Récupération du cookie
$data = json_decode($_COOKIE['le_nom_du_cookie'], true);
```

