## Afficher un message basé sur une condition

Cet exercice introduit l'utilisation de conditions simples dans les composants React.

### LoginMessage.js
```javascript
// LoginMessage.js
import React from 'react';

// Composant LoginMessage affichant un message conditionnel
function LoginMessage({ isLoggedIn }) {
    return (
        <div>
            {isLoggedIn ? 'Bienvenue, John Doe !' : 'Veuillez vous connecter.'}
        </div>
    );
}

export default LoginMessage;
```

### App.js
```javascript
// App.js
import React from 'react';
import LoginMessage from './LoginMessage';

// Utilisation du composant LoginMessage avec différentes conditions
function App() {
    return (
        <div>
            <LoginMessage isLoggedIn={true} />
            <LoginMessage isLoggedIn={false} />
        </div>
    );
}

export default App;
```