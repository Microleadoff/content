## Gérer l'état d'un champ de texte

### ControlledInput.js
```javascript
// ControlledInput.js
import React, { useState } from 'react';

function ControlledInput() {
    const [value, setValue] = useState('');

    const handleChange = (event) => {
        setValue(event.target.value);
    };

    return (
        <div>
            <input type="text" value={value} onChange={handleChange} placeholder="Tapez quelque chose" />
            <p>Contenu actuel : {value}</p>
        </div>
    );
}

export default ControlledInput;
```

### App.js
```javascript
// App.js
import React from 'react';
import ControlledInput from './ControlledInput';

function App() {
    return (
        <div>
            <h1>Test des états</h1>
            <ControlledInput />
        </div>
    );
}

export default App;
```