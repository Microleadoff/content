## Correction des exercices du cours 10

### **1. Afficher une liste d'éléments**

Cet exercice introduit la gestion des listes dans React.

#### TodoList.js
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

#### App.js
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

---

### **2. Afficher une liste de profils avec des clés**

Cet exercice introduit l'utilisation de clés pour les éléments dans une liste.

#### ProfileList.js
```javascript
// ProfileList.js
import React from 'react';

// Composant ProfileList affichant une liste de profils
function ProfileList({ profiles }) {
  return (
    <div>
      {profiles.map((profile) => (
        <div key={profile.id}>
          <h3>{profile.name}</h3>
          <p>{profile.email}</p>
        </div>
      ))}
    </div>
  );
}

export default ProfileList;
```

#### App.js
```javascript
// App.js
import React from 'react';
import ProfileList from './ProfileList';

// Utilisation du composant ProfileList pour afficher une liste de profils
function App() {
  const profiles = [
    { id: 1, name: 'John Doe', email: 'john.doe@example.com' },
    { id: 2, name: 'Jane Doe', email: 'jane.doe@example.com' },
  ];

  return (
    <div>
      <ProfileList profiles={profiles} />
    </div>
  );
}

export default App;
```
---