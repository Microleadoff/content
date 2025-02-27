### Combinaison du reducer et du context

Dans une application React complexe, la gestion efficace de l'état global est essentielle pour maintenir un code lisible et organisé. Combiner un **reducer** avec un **context** centralise la logique de mise à jour tout en facilitant le partage des données à travers les composants. Cette approche permet d'éliminer les transmissions excessives de props et d'assurer une gestion plus claire et maintenable des états.

### Objectifs de cette combinaison

Un **reducer** regroupe la logique de mise à jour d’un état dans une fonction unique, tandis que le **context** permet à différents composants de partager facilement cet état. En centralisant à la fois l’état et ses modifications, il devient plus simple de maintenir une cohérence dans l’application. De plus, cette approche simplifie le suivi des changements d’état, même lorsque les interactions utilisateur deviennent complexes.

### Étapes pour mettre en place un reducer et un context

#### Création d’un reducer

Un reducer est une fonction qui gère les mises à jour de l’état en fonction d'actions spécifiques. Prenons un exemple avec une gestion de tâches où il est possible d'ajouter, de basculer et de supprimer des tâches :

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

Ce reducer définit comment les actions modifient l’état des tâches. Par exemple, une action `add` ajoute une nouvelle tâche, `toggle` inverse l’état d’une tâche existante, et `remove` supprime une tâche selon son identifiant.

#### Configuration des contextes

Les contextes sont utilisés pour partager l’état et la fonction `dispatch` entre les composants. Deux contextes sont nécessaires : un pour l’état et un autre pour `dispatch`.

```javascript
import { createContext } from 'react';

export const TasksContext = createContext();
export const TasksDispatchContext = createContext();
```

Cela permet de dissocier l’accès aux données (`TasksContext`) de l’envoi d’actions (`TasksDispatchContext`), ce qui améliore la modularité.

#### Fourniture des données avec un provider

Le provider enveloppe les composants nécessitant un accès à l’état ou à `dispatch`. Il utilise `useReducer` pour gérer l’état global et distribuer les données et actions aux enfants.

```javascript
import React, { useReducer } from 'react';
import { TasksContext, TasksDispatchContext } from './TasksContext';

function TasksProvider({ children }) {
  const [tasks, dispatch] = useReducer(tasksReducer, []);

  return (
    <TasksContext.Provider value={tasks}>
      <TasksDispatchContext.Provider value={dispatch}>
        {children}
      </TasksDispatchContext.Provider>
    </TasksContext.Provider>
  );
}

export default TasksProvider;
```

Ce composant connecte le reducer aux contextes, permettant ainsi aux composants enfants de consommer l’état et de modifier les tâches.

### Utilisation des contextes dans les composants

Les composants enfants utilisent `useContext` pour accéder à l’état ou à `dispatch` sans nécessiter de props intermédiaires.

#### Afficher l’état des tâches

Le composant suivant affiche la liste des tâches. Il consomme `TasksContext` pour accéder directement aux données partagées :

```javascript
import React, { useContext } from 'react';
import { TasksContext } from './TasksContext';

function TaskList() {
  const tasks = useContext(TasksContext);

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>{task.text}</li>
      ))}
    </ul>
  );
}

export default TaskList;
```

Ce composant est simple et lisible. Toute modification de l’état global via `dispatch` sera immédiatement reflétée dans la liste affichée.

#### Modifier l’état avec dispatch

Un autre composant permet à l’utilisateur d’ajouter de nouvelles tâches. Il utilise `TasksDispatchContext` pour envoyer une action au reducer :

```javascript
import React, { useContext, useState } from 'react';
import { TasksDispatchContext } from './TasksContext';

function AddTask() {
  const [text, setText] = useState('');
  const dispatch = useContext(TasksDispatchContext);

  const handleSubmit = e => {
    e.preventDefault();
    dispatch({ type: 'add', id: Date.now(), text });
    setText('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Nouvelle tâche"
      />
      <button type="submit">Ajouter</button>
    </form>
  );
}

export default AddTask;
```

Ce composant se concentre uniquement sur l’ajout de tâches. La logique de mise à jour reste centralisée dans le reducer, ce qui améliore la clarté.

### Structuration globale de l’application

Le provider enveloppe les composants de l’application. Cela garantit que les données des tâches et la logique de mise à jour sont accessibles à tous les niveaux nécessaires.

```javascript
import React from 'react';
import TasksProvider from './TasksProvider';
import TaskList from './TaskList';
import AddTask from './AddTask';

function App() {
  return (
    <TasksProvider>
      <h1>Gestion des tâches</h1>
      <AddTask />
      <TaskList />
    </TasksProvider>
  );
}

export default App;
```

L’état global est géré dans un seul endroit, simplifiant la maintenance et garantissant que les composants ne reçoivent que les données pertinentes.

### Conclusion

Combiner un reducer avec un context est une approche puissante pour structurer l’état global dans une application React. Cette méthode centralise la logique de mise à jour tout en simplifiant l’accès aux données pour les composants enfants. En appliquant cette stratégie de manière réfléchie, il est possible de concevoir des applications plus robustes, lisibles et évolutives, même lorsqu’elles deviennent complexes.