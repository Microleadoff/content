## Partager des données utilisateur avec le Context

### UserContext.js
```javascript
// UserContext.js
import React, { createContext, useState } from 'react';

export const UserContext = createContext();

export function UserProvider({ children }) {
    const [user, setUser] = useState({ name: 'John Doe', email: 'john.doe@example.com' });

    const updateUser = (key, value) => {
        setUser((prevUser) => ({ ...prevUser, [key]: value }));
    };

    return (
        <UserContext.Provider value={{ user, updateUser }}>
            {children}
        </UserContext.Provider>
    );
}
```

### UserDisplay.js
```javascript
// UserDisplay.js
import React, { useContext } from 'react';
import { UserContext } from './UserContext';

function UserDisplay() {
    const { user } = useContext(UserContext);
    return (
        <div>
            <h1>Utilisateur : {user.name}</h1>
            <p>Email : {user.email}</p>
        </div>
    );
}

export default UserDisplay;
```

### UserEditor.js
```javascript
// UserEditor.js
import React, { useContext } from 'react';
import { UserContext } from './UserContext';

function UserEditor() {
    const { user, updateUser } = useContext(UserContext);

    return (
        <div>
            <input
                type="text"
                value={user.name}
                onChange={(e) => updateUser('name', e.target.value)}
                placeholder="Nom"
            />
            <input
                type="email"
                value={user.email}
                onChange={(e) => updateUser('email', e.target.value)}
                placeholder="Email"
            />
        </div>
    );
}

export default UserEditor;
```

### App.js
```javascript
// App.js
import React from 'react';
import { UserProvider } from './UserContext';
import UserDisplay from './UserDisplay';
import UserEditor from './UserEditor';

function App() {
    return (
        <UserProvider>
        <UserDisplay />
        <UserEditor />
        </UserProvider>
    );
}

export default App;
```