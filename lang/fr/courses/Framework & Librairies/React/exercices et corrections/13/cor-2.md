## Créer une boîte de texte avec un événement `onChange`

### InputField.js
```javascript
// InputField.js
import React from 'react';

function InputField() {
    const handleChange = (event) => {
        console.log('Contenu actuel :', event.target.value);
    };

    return <input type="text" onChange={handleChange} placeholder="Tapez quelque chose" />;
}

export default InputField;
```

### App.js
```javascript
// App.js
import React from 'react';
import InputField from './InputField';

function App() {
    return (
        <div>
            <h1>Test des événements</h1>
            <InputField />
        </div>
    );
}

export default App;
```
