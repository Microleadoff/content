## Correction des exercices du cours 5

### **1. Organisation des composants**

Cet exercice introduit l’organisation des composants en fichiers distincts.

#### Header.js
```javascript
// Header.js
import React from 'react';

// Composant Header affichant un titre
function Header() {
  return (
    <header>
      <h1>Mon application React</h1>
    </header>
  );
}

export default Header;
```

#### App.js
```javascript
// App.js
import React from 'react';
import Header from './Header';
import Welcome from './Welcome';

// Intégration des composants Header et Welcome
function App() {
  return (
    <div>
      <Header />
      <Welcome />
    </div>
  );
}

export default App;
```

---

### **2. Ajout d'un composant de navigation**

Cet exercice développe la pratique d'importation/exportation avec plusieurs composants.

#### Navbar.js
```javascript
// Navbar.js
import React from 'react';

// Composant Navbar affichant une navigation
function Navbar() {
  return (
    <nav>
      <ul>
        <li>Accueil</li>
        <li>À propos</li>
        <li>Contact</li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

#### App.js
```javascript
// App.js
import React from 'react';
import Navbar from './Navbar';
import Header from './Header';
import Welcome from './Welcome';

// Intégration des composants Navbar, Header et Welcome
function App() {
  return (
    <div>
      <Navbar />
      <Header />
      <Welcome />
    </div>
  );
}

export default App;
```

---