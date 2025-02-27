## Afficher des informations utilisateur avec des props

Cet exercice pratique l'utilisation de plusieurs props dans un composant.

### UserProfile.js
```javascript
// UserProfile.js
import React from 'react';

// Composant UserProfile affichant les informations utilisateur
function UserProfile({ name, email }) {
    return (
        <div>
            <h3>{name}</h3>
            <p>{email}</p>
        </div>
    );
}

export default UserProfile;
```

### App.js
```javascript
// App.js
import React from 'react';
import UserProfile from './UserProfile';

// Utilisation des props pour afficher les profils des utilisateurs
function App() {
    return (
        <div>
            <UserProfile name="John Doe" email="john.doe@example.com" />
            <UserProfile name="Jane Doe" email="jane.doe@example.com" />
        </div>
    );
}

export default App;