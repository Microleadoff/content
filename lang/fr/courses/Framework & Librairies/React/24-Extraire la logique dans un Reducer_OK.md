## Extraire la logique d’état dans un reducer

Gérer l’état devient essentiel dans les applications React, notamment lorsque les composants se complexifient. Si la logique d’état est dispersée dans plusieurs gestionnaires d’événements, le code peut devenir difficile à comprendre et à maintenir. Extraire cette logique dans une fonction dédiée, appelée **reducer**, centralise les mises à jour et apporte une structure claire et robuste.

### Qu’est-ce qu’un reducer ?

Un reducer est une fonction pure qui détermine comment l’état évolue en réponse à une **action**. Cette approche centralise la logique de mise à jour, ce qui rend le code plus prévisible et testable.

### Pourquoi utiliser un reducer ?

- **Centralisation** : La logique d’état est regroupée dans une fonction unique, ce qui facilite la compréhension et la maintenance.
- **Réduction des bugs** : Les mises à jour centralisées limitent les incohérences liées à des modifications dispersées.
- **Testabilité** : Les reducers étant des fonctions pures, ils peuvent être testés indépendamment.
- **Évolutivité** : Un reducer permet de gérer des états complexes et d’ajouter de nouvelles fonctionnalités sans désorganiser le code.

## Mise en place d’un reducer avec `useReducer`

### Création d’un reducer

Un reducer reçoit deux arguments :
- L’état actuel.
- Une action décrivant l’intention utilisateur.

Il retourne le nouvel état. Voici un exemple simple pour un compteur :

```javascript
function counterReducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    default:
      throw new Error(`Action inconnue : ${action.type}`);
  }
}
```

Chaque action (`increment`, `decrement`, `reset`) met à jour l’état en renvoyant un nouvel objet, garantissant ainsi l’immutabilité. Les actions inconnues déclenchent une erreur pour éviter des comportements inattendus.

### Utilisation avec `useReducer`

Le Hook `useReducer` remplace `useState` lorsque l’état est complexe ou implique des mises à jour liées. Voici une implémentation :

```javascript
import React, { useReducer } from 'react';

function CounterApp() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Compteur : {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+1</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-1</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Réinitialiser</button>
    </div>
  );
}
```

Dans cet exemple, `dispatch` envoie des actions au reducer, qui détermine comment l’état doit évoluer. La logique d’état reste centralisée dans la fonction `counterReducer`, simplifiant ainsi le composant.

## Gérer un état complexe : application de tâches

Un reducer est particulièrement utile pour des états complexes impliquant plusieurs types d’interactions. Prenons une application de gestion de tâches.

### Définir le reducer

```javascript
function tasksReducer(state, action) {
  switch (action.type) {
    case 'add':
      return [...state, { id: action.id, text: action.text, done: false }];
    case 'toggle':
      return state.map(task =>
        task.id === action.id ? { ...task, done: !task.done } : task
      );
    case 'remove':
      return state.filter(task => task.id !== action.id);
    default:
      throw new Error(`Action inconnue : ${action.type}`);
  }
}
```

Ce reducer gère les ajouts, modifications et suppressions de tâches. Chaque modification retourne un nouvel état, en respectant l’immutabilité.

### Intégration dans un composant

```javascript
function TaskApp() {
  const [tasks, dispatch] = useReducer(tasksReducer, []);

  function handleAddTask(text) {
    dispatch({ type: 'add', id: Date.now(), text });
  }

  function handleToggleTask(id) {
    dispatch({ type: 'toggle', id });
  }

  function handleRemoveTask(id) {
    dispatch({ type: 'remove', id });
  }

  return (
    <div>
      <TaskInput onAddTask={handleAddTask} />
      <TaskList
        tasks={tasks}
        onToggleTask={handleToggleTask}
        onRemoveTask={handleRemoveTask}
      />
    </div>
  );
}
```

Ce composant utilise le Hook `useReducer` pour gérer une liste de tâches. Les gestionnaires d’événements transmettent des actions au reducer, centralisant ainsi la logique.

## Bonnes pratiques pour écrire des reducers

1. **Actions explicites** : Les noms des actions doivent clairement refléter l’intention utilisateur (ex. `add_task`, `toggle_task`).
2. **Respect de l’immutabilité** : Toujours créer un nouvel état plutôt que de modifier directement l’existant.
3. **Éviter les effets secondaires** : Les reducers doivent rester purs ; les effets comme les appels réseau doivent être gérés dans des gestionnaires ou des hooks séparés.
4. **Diviser si nécessaire** : Un reducer volumineux peut être scindé en plusieurs reducers spécialisés.

### Cas avancés : simplifier avec Immer

Pour simplifier la gestion de l’immutabilité, la bibliothèque **Immer** permet de manipuler un état de manière intuitive grâce à un brouillon (`draft`).

```javascript
import produce from 'immer';

function tasksReducer(state, action) {
  return produce(state, draft => {
    switch (action.type) {
      case 'add':
        draft.push({ id: action.id, text: action.text, done: false });
        break;
      case 'toggle':
        const task = draft.find(t => t.id === action.id);
        if (task) task.done = !task.done;
        break;
      case 'remove':
        return draft.filter(t => t.id !== action.id);
      default:
        throw new Error(`Action inconnue : ${action.type}`);
    }
  });
}
```

Avec Immer, la gestion des états imbriqués devient plus lisible, tout en maintenant les principes d’immutabilité.

### Comparaison entre `useState` et `useReducer`

- **`useState`** convient aux états simples ou indépendants.
- **`useReducer`** est adapté aux états complexes ou dépendant de plusieurs types d’interactions.
- Les reducers étant des fonctions pures, ils sont plus facilement testables que `useState`.

### Conclusion

Extraire la logique d’état dans un reducer apporte une structure claire et une meilleure maintenabilité, particulièrement dans des applications complexes. En utilisant des outils comme `Immer` et en appliquant des bonnes pratiques, les reducers deviennent une solution puissante et évolutive pour la gestion de l’état dans React.