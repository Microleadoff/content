## Créer un bouton avec un gestionnaire d'événement

### ClickButton.js
```javascript
// ClickButton.js
import React from 'react';

function ClickButton() {
    const handleClick = () => {
        console.log('Bouton cliqué !');
    };

    return <button onClick={handleClick}>Cliquez-moi</button>;
}

export default ClickButton;
```

### App.js
```javascript
// App.js
import React from 'react';
import ClickButton from './ClickButton';

function App() {
    return (
        <div>
            <h1>Test des événements</h1>
            <ClickButton />
        </div>
    );
}

export default App;
```