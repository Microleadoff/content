## Correction des exercices du cours 7

### **1. Intégrer des expressions dynamiques dans JSX**

Cet exercice utilise des expressions dynamiques dans JSX.

#### Greeting.js
```javascript
// Greeting.js
import React from 'react';

// Composant Greeting affichant un message dynamique basé sur l'heure
function Greeting() {
  const currentHour = new Date().getHours();
  const message = currentHour < 12 ? 'Bonjour !' : 'Bonsoir !';

  return <h2>{message}</h2>;
}

export default Greeting;
```

#### App.js
```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';
import Greeting from './Greeting';

// Intégration des composants Welcome et Greeting
function App() {
  return (
    <div>
      <Welcome />
      <Greeting />
    </div>
  );
}

export default App;
```

---

### **2. Afficher la date actuelle dans un composant**

Cet exercice combine JSX et expressions dynamiques.

#### CurrentDate.js
```javascript
// CurrentDate.js
import React from 'react';

// Composant CurrentDate affichant la date actuelle
function CurrentDate() {
  const today = new Date().toLocaleDateString();

  return <p>Nous sommes le {today}</p>;
}

export default CurrentDate;
```

#### App.js
```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';
import Greeting from './Greeting';
import CurrentDate from './CurrentDate';

// Intégration des composants Welcome, Greeting et CurrentDate
function App() {
  return (
    <div>
      <Welcome />
      <Greeting />
      <CurrentDate />
    </div>
  );
}

export default App;
```

---