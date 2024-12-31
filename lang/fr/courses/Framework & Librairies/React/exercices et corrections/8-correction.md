## Correction des exercices du cours 8

### **1. Utiliser des props pour personnaliser un composant**

Cet exercice vise à pratiquer l'utilisation des props pour transmettre des données à un composant.

#### WelcomeMessage.js
```javascript
// WelcomeMessage.js
import React from 'react';

// Composant fonctionnel affichant un message de bienvenue avec une prop "name"
function WelcomeMessage({ name }) {
  return <h1>Bienvenue, {name} !</h1>;
}

export default WelcomeMessage;
```

#### App.js
```javascript
// App.js
import React from 'react';
import WelcomeMessage from './WelcomeMessage';

// Utilisation de props pour personnaliser le message de bienvenue
function App() {
  return (
    <div>
      <WelcomeMessage name="John Doe" />
      <WelcomeMessage name="Jane Doe" />
    </div>
  );
}

export default App;
```

---

### **2. Afficher des informations utilisateur avec des props**

Cet exercice pratique l'utilisation de plusieurs props dans un composant.

#### UserProfile.js
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

#### App.js
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
```