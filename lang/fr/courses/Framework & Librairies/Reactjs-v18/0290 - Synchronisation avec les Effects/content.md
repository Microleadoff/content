### La synchronisation avec les effets en React

En React, le hook `useEffect` propose un moyen structuré de gérer les **effets secondaires**, des tâches qui ne relèvent pas directement du rendu de l’interface utilisateur. Il synchronise un composant avec des systèmes externes comme une API, une bibliothèque tierce ou un élément du DOM. Les effets sont déclenchés après chaque mise à jour ou rendu initial, garantissant que l’état du DOM est à jour avant leur exécution.

#### Comprendre les effets secondaires et leur rôle en React

Un **effet secondaire** est une opération dépassant le cadre strict du calcul pur nécessaire pour produire du JSX. Par exemple, la mise à jour d’une base de données, une connexion réseau ou l’écoute d’événements utilisateurs sont des effets secondaires. En React, ces tâches doivent être explicitement gérées via `useEffect` pour ne pas interférer avec le cycle de vie du composant.

Le hook `useEffect` est conçu pour exécuter ces tâches au bon moment, après le rendu ou la mise à jour d’un composant.

#### Différence entre rendu, gestionnaires d’événements et effets

Le **rendu** d’un composant React décrit uniquement ce qui doit être affiché à l’écran. Il est purement fonctionnel et déterministe : une même combinaison d'état et de props produit toujours le même résultat.

Les **gestionnaires d’événements** sont déclenchés par des actions spécifiques de l'utilisateur, comme un clic ou une saisie, et permettent de modifier l’état ou d’interagir avec une API.

Les **effets**, quant à eux, réagissent aux changements d’état ou de props, en synchronisant le composant avec des systèmes extérieurs, indépendamment d’une action utilisateur.

#### Utiliser `useEffect` pour synchroniser les composants

Pour intégrer un effet à un composant React, il suffit d’utiliser `useEffect` :

```javascript
import { useEffect } from 'react';

function Logger() {
  useEffect(() => {
    console.log('Effet exécuté après chaque rendu ou mise à jour');
  });

  return <div>Regardez la console pour les logs.</div>;
}
```

La fonction passée à `useEffect` est exécutée après chaque rendu ou mise à jour du composant. Ce comportement peut être restreint grâce aux dépendances pour éviter des exécutions inutiles.

#### Contrôler l'exécution des effets avec les dépendances

Par défaut, `useEffect` s’exécute après **chaque rendu**. Il est souvent utile de limiter cette exécution aux changements d’états ou de props spécifiques en utilisant un tableau de dépendances :

```javascript
useEffect(() => {
  console.log('Cet effet s’exécute uniquement lorsque count change.');
}, [count]);
```

Ici, l’effet est déclenché uniquement si `count` change. Si le tableau est vide (`[]`), l’effet s’exécute uniquement lors du montage initial du composant.

#### Exemple : synchronisation d’un compteur

Voici un compteur dont l’effet s’exécute uniquement lorsque sa valeur est mise à jour :

```javascript
import { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log(`Compteur mis à jour : ${count}`);
  }, [count]);

  return (
    <button onClick={() => setCount(count + 1)}>
      Incrémenter ({count})
    </button>
  );
}
```

Chaque clic sur le bouton met à jour `count`, déclenchant l’exécution de l’effet et affichant un message dans la console.

#### Nettoyage des effets pour une meilleure gestion des ressources

Certains effets, comme les abonnements à des événements ou l’utilisation de timers, nécessitent un nettoyage pour éviter les fuites de mémoire. Cela se fait en retournant une fonction dans `useEffect` :

```javascript
useEffect(() => {
  const interval = setInterval(() => {
    console.log('Interval actif');
  }, 1000);

  return () => clearInterval(interval);
}, []);
```

Dans cet exemple, la fonction de nettoyage `clearInterval` est appelée avant que l’effet ne soit réexécuté ou lorsque le composant est démonté. Cela garantit que chaque intervalle actif est correctement supprimé.

#### Cas pratiques : manipulation du DOM et appels API

Si un effet nécessite une interaction directe avec le DOM, `useEffect` permet de s’assurer que ces manipulations se produisent au bon moment :

```javascript
import { useRef, useEffect } from 'react';

function FocusInput() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} placeholder="Focus automatique" />;
}
```

Pour récupérer des données lors du montage d’un composant, `useEffect` est également utile :

```javascript
useEffect(() => {
  async function fetchData() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  }

  fetchData();
}, []);
```

Dans ce cas, l’effet ne s’exécute qu’une fois, au montage initial, grâce au tableau de dépendances vide.

#### Gestion des effets en mode strict

En mode strict, React exécute chaque effet deux fois en développement pour détecter d’éventuelles erreurs. Cela peut entraîner des comportements inattendus si le nettoyage de l’effet n’est pas correctement géré. Par exemple :

```javascript
useEffect(() => {
  console.log('Connexion au serveur');
  return () => console.log('Déconnexion du serveur');
}, []);
```

En développement, ce code affiche « Connexion au serveur » puis « Déconnexion du serveur » deux fois. Cela simule un démontage/remontage pour vérifier que la logique de nettoyage fonctionne. En production, l’effet ne s’exécutera qu’une seule fois.

#### Bonnes pratiques avec `useEffect`

Spécifier les dépendances nécessaires garantit que l’effet s’exécute uniquement lorsque cela est pertinent. Les abonnements, timers ou connexions doivent être correctement fermés ou annulés pour éviter les fuites de mémoire. Enfin, il convient de s’assurer que l’effet ne modifie pas une variable utilisée comme dépendance, afin d’éviter des boucles infinies.

### Conclusion

`useEffect` est un outil essentiel pour gérer les effets secondaires en React. Une gestion rigoureuse des dépendances et des nettoyages permet de concevoir des composants robustes et performants. Que ce soit pour interagir avec une API, manipuler le DOM ou gérer des abonnements, `useEffect` offre un cadre structuré pour toutes ces tâches.