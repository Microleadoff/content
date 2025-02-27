## Afficher une liste d'éléments

Cet exercice introduit la gestion des listes dans React.

### TodoList.js
```javascript
// TodoList.js
import React from 'react';

// Composant TodoList affichant une liste d'éléments
function TodoList({ todos }) {
    return (
        <ul>
            {todos.map((todo, index) => (
                    <li key={index}>{todo}</li>
            ))}
        </ul>
    );
}

export default TodoList;
```

### App.js
```javascript
// App.js
import React from 'react';
import TodoList from './TodoList';

// Utilisation du composant TodoList pour afficher une liste
function App() {
    const todos = ['Acheter du pain', 'Envoyer un email', 'Préparer une réunion'];

    return (
        <div>
            <TodoList todos={todos} />
        </div>
    );
}

export default App;
```