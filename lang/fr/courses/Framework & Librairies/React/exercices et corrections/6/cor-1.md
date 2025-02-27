## Intégrer du JSX

Cet exercice pratique l’utilisation du JSX pour structurer un composant.

### UserCard.js
```javascript
// UserCard.js
import React from 'react';

// Composant UserCard affichant des informations utilisateur
function UserCard() {
    return (
        <div>
            <h2>John Doe</h2>
            <p>john.doe@example.com</p>
            <button>Afficher les détails</button>
        </div>
    );
}

export default UserCard;
```

### App.js
```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';
import UserCard from './UserCard';

// Intégration des composants Welcome et UserCard
function App() {
    return (
        <div>
            <Welcome />
            <UserCard />
        </div>
    );
}

export default App;
```
