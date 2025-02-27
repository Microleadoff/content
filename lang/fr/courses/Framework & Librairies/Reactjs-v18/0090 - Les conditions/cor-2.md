## Afficher un bouton en fonction de l'état

Cet exercice approfondit l'utilisation des conditions pour afficher des éléments différents.

### ActionButton.js
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

### App.js
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