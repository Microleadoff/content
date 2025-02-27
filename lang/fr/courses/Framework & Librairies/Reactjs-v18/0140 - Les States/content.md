## Les États dans React

Dans React, l’état permet aux composants de stocker et de gérer des informations qui évoluent selon les interactions utilisateur, comme le texte d’un champ de saisie ou le nombre d’articles dans un panier. Contrairement aux données statiques, l’état rend les composants interactifs et permet de rafraîchir l’interface en fonction des actions de l’utilisateur sans recharger la page.

### L'État : isolé et privé

L'état est spécifique au composant qui le déclare, ce qui signifie que chaque instance d'un composant garde son propre état. Par exemple, deux compteurs affichés simultanément dans une application auront chacun leur propre état indépendant.

Cette isolation rend l'état privé au composant qui le détient. Contrairement aux props, l'état n'est pas accessible de l'extérieur et ne peut être modifié que par le composant lui-même, favorisant ainsi la modularité et l’autonomie des composants.

### Les Hooks : ajouter des fonctionnalités aux composants

Les **Hooks** sont des fonctions spéciales de React qui permettent aux composants d’utiliser des fonctionnalités avancées comme l’état. Chaque Hook commence par le mot-clé "use". `useState` est l’un des hooks les plus courants dans React, et permet de gérer l’état dans un composant fonctionnel.

### Utilisation du Hook `useState`

Le Hook `useState` est la méthode principale pour gérer l’état dans un composant fonctionnel. Il crée une variable d’état et une fonction pour la mettre à jour, permettant de gérer les données qui changent en fonction de l’utilisation.

#### Initialisation et mise à jour de l’état avec `useState`

Pour initialiser l’état, `useState` prend une valeur initiale et retourne un tableau avec deux éléments : la valeur actuelle de l’état et une fonction de mise à jour.

```javascript
import React, { useState } from 'react';

function SimpleCounter() {
  const [count, setCount] = useState(0); // Initialisation avec une valeur de départ de 0

  const increaseCount = () => setCount(count + 1); // Mise à jour de l’état

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={increaseCount}>Incrémenter</button>
    </div>
  );
}
```

Dans cet exemple :
- `count` représente la valeur actuelle de l’état, initialisée à 0.
- `setCount` est la fonction qui met à jour `count`.
- Cliquer sur le bouton déclenche `increaseCount`, qui ajoute 1 à `count` et actualise l’affichage.

### Le Rerendering

Le **rerendering** est le processus par lequel React actualise un composant pour afficher les données mises à jour. Lorsqu'un état change via `useState`, React réexécute la fonction du composant pour synchroniser l’affichage avec les nouvelles valeurs. Cela permet d’obtenir une interface dynamique qui réagit instantanément aux interactions sans nécessiter de rechargement complet de la page.

Contrairement aux variables classiques, qui ne déclenchent pas de mise à jour visuelle, les variables d’état créées avec `useState` sont spécialement conçues pour réagir aux modifications. À chaque changement de valeur, elles provoquent un rerendering automatique, garantissant ainsi que l’interface utilisateur reste cohérente avec les données du composant en temps réel.

### Pourquoi ne pas utiliser de variables classiques ?

Les variables classiques, quant à elles, ne provoquent pas de rerendering automatique de l’interface. Si une variable classique est modifiée, React ne la surveille pas, ce qui signifie que l’interface ne se mettra pas à jour.

#### Exemple :

```javascript
import React from 'react';

function NonReactiveCounter() {
  let count = 0;

  const increaseCount = () => {
    count++;
    console.log(count); // La valeur change, mais l'affichage ne se met pas à jour.
  };

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={increaseCount}>Incrémenter</button>
    </div>
  );
}
```

Ici, bien que `count` augmente dans la console, l’affichage reste inchangé, car React ne considère pas `count` comme une donnée à surveiller. Avec `useState`, chaque mise à jour de `count` est suivie d’un rerendering, assurant ainsi que l’affichage reflète la dernière valeur de l’état.

### Utiliser plusieurs variables d’état dans un composant

Dans un composant React, il est possible d’utiliser plusieurs variables d’état pour gérer des informations indépendantes. Cela permet de structurer l’état de façon claire, notamment si les données sont distinctes les unes des autres. Par exemple, un formulaire pourrait avoir un état pour chaque champ, tandis qu’un composant de galerie pourrait gérer l’indice d’une image actuelle et un booléen pour afficher ou masquer les détails.

```javascript
import React, { useState } from 'react';

function Profile() {
  const [username, setUsername] = useState('Alice');      // État pour le nom d'utilisateur
  const [age, setAge] = useState(25);                     // État pour l’âge
  const [showDetails, setShowDetails] = useState(false);  // État pour afficher ou masquer les détails

  return (
    <div>
      <h2>{username}</h2>
      <p>Âge : {age}</p>
      <button onClick={() => setShowDetails(!showDetails)}>
        {showDetails ? "Masquer les détails" : "Afficher les détails"}
      </button>
      {showDetails && <p>Détails supplémentaires ici...</p>}
    </div>
  );
}
```

Dans cet exemple :
- `username`, `age`, et `showDetails` sont trois variables d’état distinctes qui stockent des informations différentes.
- Chaque variable peut être modifiée indépendamment des autres, ce qui rend le code clair et facilement maintenable.

L'utilisation de plusieurs variables d'état rend le code plus modulaire, car chaque état est géré séparément et peut être mis à jour selon les besoins du composant, sans interférer avec les autres variables.