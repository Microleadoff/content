## Rédation de votre premier composant React

**Attention la correction utilise l'import et l'export de composant (voir cours 5)**

Cet exercice vise à pratiquer la création d’un composant fonctionnel simple.

### Welcome.js
```javascript
// Welcome.js
import React from 'react';

// Composant simple affichant un message de bienvenue
function Welcome() {
    return <h1>Bienvenue dans mon application !</h1>;
}

export default Welcome;
```

### App.js
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