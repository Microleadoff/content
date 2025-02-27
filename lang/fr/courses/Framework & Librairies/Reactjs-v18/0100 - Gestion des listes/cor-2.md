## Afficher une liste de profils avec des clés

Cet exercice introduit l'utilisation de clés pour les éléments dans une liste.

### ProfileList.js
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