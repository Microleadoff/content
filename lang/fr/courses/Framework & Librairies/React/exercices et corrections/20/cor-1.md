## Formulaires

### UserForm.js
```javascript
import React, { useState } from 'react';

function UserForm() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
    });
    const [fields, setFields] = useState([]);

    const handleChange = (key, value) => {
        setFormData((prevData) => ({ ...prevData, [key]: value }));
    };

    const addField = () => {
        const newFieldKey = `field${fields.length + 1}`;
        setFields((prevFields) => [...prevFields, newFieldKey]);
        setFormData((prevData) => ({ ...prevData, [newFieldKey]: '' }));
    };

    return (
        <div>
            <h1>Formulaire d'utilisateur</h1>
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
            <input
                type="password"
                placeholder="Mot de passe"
                value={formData.password}
                onChange={(e) => handleChange('password', e.target.value)}
            />
            {fields.map((field) => (
                <input
                key={field}
                type="text"
                placeholder={field}
                value={formData[field]}
                onChange={(e) => handleChange(field, e.target.value)}
                />
            ))}
            <button onClick={addField}>Ajouter un champ</button>
            <p>
                Données du formulaire : {JSON.stringify(formData, null, 2)}
            </p>
        </div>
    );
}

export default UserForm;
```

### App.js
```javascript
// App.js
import React from 'react';
import UserForm from './UserForm';

function App() {
    return (
        <div>
            <UserForm />
        </div>
    );
}

export default App;
```