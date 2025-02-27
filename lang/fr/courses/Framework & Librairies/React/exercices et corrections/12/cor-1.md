## Créer une arborescence de projet React

### Header.js
```javascript
// Header.js
import React from 'react';

// Composant d'en-tête
function Header() {
    return (
        <header>
            <h1>Gestionnaire de tâches</h1>
        </header>
    );
}

export default Header;
```

### Task.js
```javascript
// Task.js
import React from 'react';

// Composant pour afficher une tâche
function Task({ name }) {
    return <li>{name}</li>;
}

export default Task;
```

### TaskList.js
```javascript
// TaskList.js
import React from 'react';
import Task from './Task';

// Composant pour afficher la liste des tâches
function TaskList() {
    const tasks = ['Tâche 1', 'Tâche 2', 'Tâche 3'];

    return (
        <ul>
            {tasks.map((task, index) => (
                <Task key={index} name={task} />
            ))}
        </ul>
    );
}

export default TaskList;
```

### Footer.js
```javascript
// Footer.js
import React from 'react';

// Composant de pied de page
function Footer() {
    return (
        <footer>
            <p>© 2023 Mon Application</p>
        </footer>
    );
}

export default Footer;
```

### App.js
```javascript
// App.js
import React from 'react';
import Header from './components/Header';
import TaskList from './components/TaskList';
import Footer from './components/Footer';

// Composant principal
function App() {
    return (
        <div>
            <Header />
            <TaskList />
            <Footer />
        </div>
    );
}

export default App;
```