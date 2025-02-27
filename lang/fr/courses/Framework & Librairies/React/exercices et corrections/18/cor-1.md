## Modifier une propriété d'un objet

### App.js
```javascript
// App.js
import React from 'react';
import ProfileEditor from './ProfileEditor';

function App() {
    return (
        <div>
            <h1>Éditeur de profil</h1>
            <ProfileEditor />
        </div>
    );
}

export default App;
```

### ProfileEditor.js
```javascript
// ProfileEditor.js
import React, { useState } from 'react';

function ProfileEditor() {
    const [profile, setProfile] = useState({
        name: 'John Doe',
        email: 'john.doe@example.com',
    });

    const handleChange = (key, value) => {
        setProfile((prevProfile) => ({ ...prevProfile, [key]: value }));
    };

    return (
        <div>
            <input
                type="text"
                value={profile.name}
                onChange={(e) => handleChange('name', e.target.value)}
                placeholder="Nom"
            />
            <input
                type="email"
                value={profile.email}
                onChange={(e) => handleChange('email', e.target.value)}
                placeholder="Email"
            />
            <ul>
                <li>Nom : {profile.name}</li>
                <li>Email : {profile.email}</li>
            </ul>
        </div>
    );
}

export default ProfileEditor;
```