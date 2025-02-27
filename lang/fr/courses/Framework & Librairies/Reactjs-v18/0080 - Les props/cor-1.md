## Utiliser des props pour personnaliser un composant

Cet exercice vise à pratiquer l'utilisation des props pour transmettre des données à un composant.

### WelcomeMessage.js
```javascript
// WelcomeMessage.js
import React from 'react';

// Composant fonctionnel affichant un message de bienvenue avec une prop "name"
function WelcomeMessage({ name }) {
    return <h1>Bienvenue, {name} !</h1>;
}

export default WelcomeMessage;
```

### App.js
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