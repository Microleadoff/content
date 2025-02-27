## Ajouter une nouvelle fonctionnalité à l’arborescence

### TaskActions.js
```javascript
// TaskActions.js
import React from 'react';

// Composant pour les actions sur une tâche
function TaskActions() {
    return (
        <div>
            <button>Compléter</button>
            <button>Supprimer</button>
        </div>
    );
}

export default TaskActions;
```

### Task.js
```javascript
// Task.js
import React from 'react';
import TaskActions from './TaskActions';

// Composant pour afficher une tâche avec des actions
function Task({ name }) {
    return (
        <li>
            {name}
            <TaskActions />
        </li>
    );
}

export default Task;
```

### styles.css
```css
/* styles.css */
header {
    background-color: #f4f4f4;
    padding: 10px;
    text-align: center;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin: 10px 0;
    display: flex;
    justify-content: space-between;
}

button {
    margin-left: 5px;
}

footer {
    background-color: #f4f4f4;
    text-align: center;
    padding: 10px;
    margin-top: 20px;
}
```