## Afficher la date actuelle dans un composant

Cet exercice combine JSX et expressions dynamiques.

### CurrentDate.js
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

### App.js
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