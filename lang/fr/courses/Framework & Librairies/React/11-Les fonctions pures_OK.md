React exploite un concept de fonctions dites" pures" ou "impures". Celui-ci permet d'améliorer la qualité de code ainsi que d'éviter des bugs ou encore d'améliorer la vitesse et la qualité du rendu.

## Les Fonctions Pures

Une **fonction pure** à pour principale propriété de renvoyer le même résultat pour les mêmes entrées et n'a aucun effet en dehors d'elle-même. Elle ne modifie pas l'état global, ne dépend pas d'éléments extérieurs à ses paramètres et n'altère aucune donnée en dehors de son contexte.

Un **composant pur** en React fonctionne de manière similaire : il affiche toujours le même contenu pour les mêmes props et n'a aucun effet sur l'extérieur. Cette approche permet d'éviter des rendus inutiles et d'améliorer les performances.

Comme les fonctions pures en JavaScript, les composants purs en React se limitent à effectuer des calculs sans effets secondaires. Adopter cette méthode réduit le risque de bugs complexes et de comportements inattendus à mesure que le projet grandit. Cependant, certaines règles doivent être respectées pour en tirer pleinement parti.

### Les Règles

Pour qu'une fonction ou un composant React soit pur, il est essentiel de respecter quelques principes :

- **Toujours renvoyer le même résultat** pour les mêmes entrées (props ou paramètres).
- **Ne pas modifier de données externes** : ne pas changer l'état ou des variables globales.
- **Éviter les effets de bord** : ne pas effectuer d'actions comme des requêtes réseau ou des modifications du DOM pendant le rendu.

#### Exemple de composant pur en React :

```js
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

Si la prop `name` ne change pas, le rendu reste identique, ce qui en fait un composant pur.

### Composants Impurs et Conséquences

Un composant devient impur lorsqu'il modifie des variables externes ou produit des effets de bord lors du rendu. Cela peut entraîner des bugs imprévisibles, rendre les tests difficiles à maintenir et causer un comportement incohérent de l'application.

#### Exemple de composant impur :

```js
let counter = 0;

function Counter() {
  counter++;
  return <p>Compteur : {counter}</p>;
}
```

Dans cet exemple, la variable `counter` est modifiée à chaque rendu, ce qui affecte l'état externe. Cela compromet la fiabilité du composant, car le résultat change à chaque rendu.

**Conséquences :**
- Les tests unitaires deviennent peu fiables, car le comportement du composant dépend d'un état externe.
- Les mises à jour du DOM peuvent être incohérentes, provoquant des bugs difficiles à diagnostiquer.

### Gestion des Effets de Bord

Dans React, un effet de bord désigne toute action qui affecte l'extérieur d'un composant, comme un appel réseau ou une modification du DOM. Ces actions ne doivent pas se produire pendant le rendu, car elles nuisent à la pureté du composant et peuvent entraîner des comportements imprévisibles.

Pour gérer ces effets, React utilise le hook `useEffect`, qui déclenche des actions après le rendu du composant, garantissant ainsi que le rendu reste pur.

#### Exemple :

```js
import { useEffect } from 'react';

function Example() {
  useEffect(() => {
    console.log('Effet déclenché après le rendu');
  }, []);

  return <div>Exemple d'effet de bord</div>;
}
```

Dans cet exemple, `useEffect` est utilisé pour exécuter un effet de bord (un message dans la console) après le rendu du composant.

### StrictMode et Détection des Impuretés

React propose `StrictMode`, un outil pour identifier les composants impurs et les mauvaises pratiques. Lorsqu'il est activé, `StrictMode` double certains appels de cycle de vie pour détecter les comportements inattendus, sans affecter la production.

#### Exemple d'activation de `StrictMode` :

```js
import React from 'react';

function Example() {
  return <div>Composant sous StrictMode</div>;
}

export default function App() {
  return (
    <React.StrictMode>
      <Example />
    </React.StrictMode>
  );
}
```

`StrictMode` permet de repérer les erreurs en simulant des rendus supplémentaires, révélant ainsi les effets de bord ou les mutations d'état indésirables.

### Optimisation des Performances avec les Composants Purs

L’un des principaux avantages des composants purs est leur impact positif sur les performances. En garantissant qu'un composant produit toujours le même résultat pour les mêmes props, React peut optimiser les mises à jour du DOM et éviter les rendus inutiles, réduisant ainsi les calculs redondants et améliorant la fluidité des applications.

React propose également `React.memo`, un outil qui permet de rendre un composant pur et de le mémoriser. Si les props ne changent pas, React ne re-rendra pas le composant.

#### Exemple avec `React.memo` :

```js
const Greeting = React.memo(function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
});
```

Grâce à `React.memo`, `Greeting` ne sera pas re-rendu si la prop `name` reste inchangée, ce qui améliore les performances de l'application.

### Conclusion

Respecter la pureté des composants dans React est essentiel pour garantir la stabilité, les performances et la maintenabilité du code. En gérant correctement les effets de bord avec `useEffect`, en évitant les composants impurs, et en utilisant des outils comme `StrictMode`, il devient possible de créer des applications plus robustes et efficaces.