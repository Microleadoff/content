## Correction des exercices du cours 6

### **1. Intégrer du JSX**

Cet exercice pratique l’utilisation du JSX pour structurer un composant.

#### UserCard.js
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

#### App.js
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

---

### **2. Utilisation des balises HTML dans JSX**

Cet exercice exploite les balises HTML au sein du JSX.

#### Profile.js
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

#### App.js
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

---