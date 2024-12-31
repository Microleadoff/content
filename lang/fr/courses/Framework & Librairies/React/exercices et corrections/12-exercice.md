## **Exercice du cours 12 : Treeview**

### Exercice 1

**Créer une arborescence de projet React**

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

---

#### Rendu attendu
<img src="../img/rendu_exo_12_1.png" alt="Rendu attendu de l'exercice">

---

### Exercice 2

**Ajouter une nouvelle fonctionnalité à l’arborescence**

1. Ajoutez un nouveau composant `TaskActions.js` dans le dossier `components`.
2. Ce composant doit inclure deux boutons `<button>` :
   - Un bouton "Compléter".
   - Un bouton "Supprimer".
3. Modifiez `Task.js` pour inclure le composant `TaskActions` sous chaque tâche.
4. Ajoutez les styles nécessaires dans `styles.css` pour espacer les tâches et les actions.

---

#### Rendu attendu
<img src="../img/rendu_exo_12_2.png" alt="Rendu attendu de l'exercice">

---

