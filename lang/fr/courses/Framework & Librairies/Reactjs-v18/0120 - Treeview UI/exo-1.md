## Créer une arborescence de projet React

1. Organisez votre projet React pour qu’il respecte la structure suivante :
    ```
    src/
    ├── components/
    │   ├── Header.js          # Composant d'en-tête
    │   ├── TaskList.js        # Composant pour afficher une liste de tâches
    │   ├── Task.js            # Composant pour une tâche individuelle
    │   └── Footer.js          # Composant de pied de page
    ├── App.js                 # Composant principal
    └── styles.css             # Styles globaux
    ```
2. Implémentez chaque composant avec un contenu simple pour visualiser l’arborescence.
    - **Header.js** : Un `<header>` contenant un titre `<h1>` (par exemple : "Gestionnaire de tâches").
    - **TaskList.js** : Un `<ul>` affichant des tâches via le composant `Task`.
    - **Task.js** : Un `<li>` affichant une tâche (par exemple : "Tâche 1").
    - **Footer.js** : Un `<footer>` avec un texte `<p>` (par exemple : "© 2023 Mon Application").
3. Dans `App.js`, assemblez ces composants pour former l’arborescence complète.

## Rendu attendu

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0120%20-%20Treeview%20UI/rendu_exo_12_1.png?raw=true" alt="Rendu attendu de l'exercice">