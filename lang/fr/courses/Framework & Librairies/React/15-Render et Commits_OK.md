## Le rendu, la réconciliation et le commit

Dans React, le **rendu** est le processus de génération et de mise à jour de l'interface utilisateur en fonction des données, des props et de l'état d'un composant. À chaque changement d’état ou de données, React déclenche un nouveau rendu pour s'assurer que l'interface reste synchronisée avec les informations les plus récentes. Ce rendu est d'abord réalisé sur le **Virtual DOM** — une copie légère du DOM réel — afin de déterminer les modifications nécessaires. Pour rappel, le **DOM** (Document Object Model) est la structure en arbre qui représente tous les éléments HTML d’une page web.

Une fois le rendu terminé, React passe à la phase de **réconciliation**. Durant cette étape, React compare la version actuelle du Virtual DOM avec la précédente pour identifier les différences. Cette analyse permet de cibler uniquement les éléments modifiés, optimisant ainsi les performances en évitant les mises à jour inutiles.

Enfin, dans la phase de **commit**, les changements détectés sont appliqués au DOM réel. Cette séparation entre rendu virtuel, réconciliation et commit permet à React de ne mettre à jour que ce qui est nécessaire, offrant ainsi une expérience utilisateur fluide et réactive.

### Exemple de fonctionnement

Prenons un composant simple avec un texte et un bouton qui change la couleur du texte lorsqu'il est cliqué.

1. **Rendu** : Au départ, le texte est affiché en noir. Lors du clic sur le bouton, une mise à jour d'état est déclenchée pour passer la couleur de noir à rouge. React génère alors un nouveau rendu du composant dans le Virtual DOM, où le texte apparaît en rouge.

2. **Réconciliation** : React compare le nouveau Virtual DOM avec l'ancien et note que seule la couleur du texte a changé.

3. **Commit** : Après la réconciliation, React applique cette modification au DOM réel. Le texte passe alors de noir à rouge à l'écran sans nécessiter le rechargement complet de l'interface.

### Importance du cycle de rendu et de commit

Le cycle de rendu, de réconciliation et de commit permet à React de gérer les mises à jour de manière ciblée, en ne modifiant que les éléments nécessaires du DOM. Cela évite les rechargements complets et coûteux de l'interface, ce qui est particulièrement bénéfique dans les applications interactives ou de grande taille, où chaque interaction utilisateur doit être prise en charge de façon rapide et fluide.

## Manipuler le DOM avec `ReactDOM.createRoot` et `ReactDOM.render`

Pour que React commence le cycle de rendu et de commit, il doit être connecté au DOM via un point d’ancrage de rendu. Voici les deux méthodes principales utilisées :

- **`ReactDOM.render`** : Cette méthode monte un composant React dans un élément DOM spécifique de la page, souvent un conteneur `<div>`. Elle établit ainsi le point de départ pour que React gère les changements dans cette partie de l’interface.

    ```javascript
    import React from 'react';
    import ReactDOM from 'react-dom';
    import App from './App';

    ReactDOM.render(<App />, document.getElementById('root'));
    ```

### Mode concurrent

Dans une application React classique, chaque mise à jour d'état déclenche un rendu qui doit être complété avant que l'application puisse traiter d'autres tâches. En mode concurrent, React peut découper le travail en segments et gérer les priorités de rendu pour éviter de bloquer l'interface utilisateur. Ce mode est particulièrement utile pour les applications nécessitant des interactions fréquentes et des mises à jour rapides, car il optimise l’utilisation des ressources et améliore la fluidité pour l'utilisateur.

- **`ReactDOM.createRoot`** : Cette méthode active le **mode concurrent** de React, recommandé pour les interfaces hautement interactives. En utilisant `createRoot`, React peut mieux gérer les priorités des rendus, améliorant ainsi la réactivité dans les applications intensives.

    ```javascript
    import React from 'react';
    import ReactDOM from 'react-dom/client';
    import App from './App';

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);
    ```