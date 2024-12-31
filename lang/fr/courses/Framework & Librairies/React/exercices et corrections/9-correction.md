## Correction des exercices du cours 9

### **1. Afficher un message basé sur une condition**

Cet exercice introduit l'utilisation de conditions simples dans les composants React.

#### LoginMessage.js
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

#### App.js
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

---

### **2. Afficher un bouton en fonction de l'état**

Cet exercice approfondit l'utilisation des conditions pour afficher des éléments différents.

#### ActionButton.js
```javascript
// ActionButton.js
import React from 'react';

// Composant ActionButton affichant un bouton ou un texte en fonction de l'état
function ActionButton({ isEnabled }) {
  return isEnabled ? (
    <button>Action disponible</button>
  ) : 
  (
    <p>Action désactivée</p>
  );
}

export default ActionButton;
```

#### App.js
```javascript
// App.js
import React from 'react';
import ActionButton from './ActionButton';

// Utilisation du composant ActionButton avec différentes conditions
function App() {
  return (
    <div>
      <ActionButton isEnabled={true} />
      <ActionButton isEnabled={false} />
    </div>
  );
}

export default App;
```

---