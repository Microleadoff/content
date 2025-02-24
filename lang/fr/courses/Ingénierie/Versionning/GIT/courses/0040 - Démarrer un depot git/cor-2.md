## Créer un composant avec un paragraphe

Cet exercice renforce la pratique de la création de composants et leur intégration.

### About.js
```javascript
// About.js
import React from 'react';

// Composant About affichant une description de l'application
function About() {
    return <p>Cette application est conçue pour apprendre React.</p>;
}

export default About;
```

### App.js
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
