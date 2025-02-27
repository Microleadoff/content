## Ajouter un champ à un objet

### App.js
```javascript
// App.js
import React from 'react';
import ProfileEditor from './ProfileEditor';

function App() {
    return (
        <div>
            <h1>Ajout de champ au profil</h1>
            <ProfileEditor />
        </div>
    );
}

export default App;
```

### ProfileEditor.js
```javascript
import React, { useState } from 'react';

function ProfileEditor() {
    const [profile, setProfile] = useState({
        name: 'John Doe',
        email: 'john.doe@example.com',
    });

    const handleChange = (key, value) => {
        setProfile((prevProfile) => ({ ...prevProfile, [key]: value }));
    };

    const addField = () => {
        const newFieldKey = prompt("Entrez le nom du nouveau champ (ex: 'phone'):");
        if (newFieldKey && !profile[newFieldKey]) {
            setProfile((prevProfile) => ({
                ...prevProfile,
                [newFieldKey]: '', 
            }));
        }
    };

    return (
        <div>
            <h1>Éditeur de profil</h1>
            {Object.entries(profile).map(([key, value]) => (
                <div key={key}>
                <label>
                    {key.charAt(0).toUpperCase() + key.slice(1)} :
                    <input
                    type="text"
                    value={value}
                    onChange={(e) => handleChange(key, e.target.value)}
                    />
                </label>
                </div>
            ))}
            <button onClick={addField}>Ajouter un champ</button>
            <ul>
                {Object.entries(profile).map(([key, value]) => (
                <li key={key}>
                    {key.charAt(0).toUpperCase() + key.slice(1)} : {value}
                </li>
                ))}
            </ul>
        </div>
    );
}

export default ProfileEditor;
```