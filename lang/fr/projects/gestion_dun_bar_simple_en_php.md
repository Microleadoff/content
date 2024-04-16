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
