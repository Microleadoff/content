## Correction des exercices du cours 4

**Attention la correction utilise l'import et l'export de composant (voir cours 5)**

### **1. Création de votre premier composant React**

Cet exercice vise à pratiquer la création d’un composant fonctionnel simple.

#### Welcome.js
```javascript
// Welcome.js
import React from 'react';

// Composant simple affichant un message de bienvenue
function Welcome() {
  return <h1>Bienvenue dans mon application !</h1>;
}

export default Welcome;
```

#### App.js
```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';

// Intégration du composant Welcome dans l'application principale
function App() {
  return (
    <div>
      <Welcome />
    </div>
  );
}

export default App;
```

---

### **2. Créer un composant avec un paragraphe**

Cet exercice renforce la pratique de la création de composants et leur intégration.

#### About.js
```javascript
// About.js
import React from 'react';

// Composant About affichant une description de l'application
function About() {
  return <p>Cette application est conçue pour apprendre React.</p>;
}

export default About;
```

#### App.js
```javascript
// App.js
import React from 'react';
import Welcome from './Welcome';
import About from './About';

// Intégration des composants Welcome et About
function App() {
  return (
    <div>
      <Welcome />
      <About />
    </div>
  );
}

export default App;
```

---