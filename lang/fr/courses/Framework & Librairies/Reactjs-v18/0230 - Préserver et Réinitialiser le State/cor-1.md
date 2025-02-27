## Formulaire et historique

### ResettableForm.js
```javascript
import React, { useState } from 'react';

function ResettableForm() {
    const initialFormState = { name: '', email: '' };
    const [formData, setFormData] = useState(initialFormState);
    const [resetHistory, setResetHistory] = useState([]);

    const handleChange = (key, value) => {
        setFormData((prevData) => ({ ...prevData, [key]: value }));
    };

    const handleReset = () => {
        setFormData(initialFormState);
        setResetHistory((prevHistory) => [
            ...prevHistory,
            new Date().toLocaleString(),
        ]);
    };

    return (
        <div>
            <h1>Formulaire réinitialisable</h1>
            <input
                type="text"
                placeholder="Nom"
                value={formData.name}
                onChange={(e) => handleChange('name', e.target.value)}
            />
            <input
                type="email"
                placeholder="Email"
                value={formData.email}
                onChange={(e) => handleChange('email', e.target.value)}
            />
            <button onClick={handleReset}>Réinitialiser</button>
            <h2>Historique des réinitialisations</h2>
            <ul>
                {resetHistory.map((timestamp, index) => (
                <li key={index}>{timestamp}</li>
                ))}
            </ul>
        </div>
    );
}

export default ResettableForm;
```

### App.js
```javascript
// App.js
import React from 'react';
import ResettableForm from './ResettableForm';

function App() {
    return (
        <div>
            <ResettableForm />
        </div>
    );
}

export default App;
```