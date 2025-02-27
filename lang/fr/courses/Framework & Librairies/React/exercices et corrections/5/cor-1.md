## Organisation des composants

Cet exercice introduit l’organisation des composants en fichiers distincts.

### Header.js
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

### App.js
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