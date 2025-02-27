## Utilisation des balises HTML dans JSX

Cet exercice exploite les balises HTML au sein du JSX.

### Profile.js
```javascript
// Profile.js
import React from 'react';

// Composant Profile affichant des informations personnelles
function Profile() {
    return (
        <div>
            <img src="https://via.placeholder.com/150" alt="Profil" />
            <h3>John Doe</h3>
            <p>Développeur Web passionné</p>
        </div>
    );
}

export default Profile;
```

### App.js
```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';
import UserCard from './UserCard';
import Profile from './Profile';

// Intégration des composants Welcome, UserCard et Profile
function App() {
    return (
        <div>
            <Welcome />
            <UserCard />
            <Profile />
        </div>
    );
}

export default App;
```