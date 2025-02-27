## Créer un hook pour gérer un thème global

### useTheme.js
```javascript
import { useState } from 'react';

function useTheme(initialTheme = 'light') {
    const [theme, setTheme] = useState(initialTheme);

    const toggleTheme = () => {
        setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
    };

    return { theme, toggleTheme };
}

export default useTheme;
```

### ThemeManager.js
```javascript
import React, { useEffect } from 'react';
import useTheme from './useTheme';

function ThemeManager() {
    const { theme, toggleTheme } = useTheme();

    useEffect(() => {
        document.body.style.backgroundColor = theme === 'light' ? '#ffffff' : '#333333';
        document.body.style.color = theme === 'light' ? '#000000' : '#ffffff';
    }, [theme]);

    return (
        <div>
            <h1>Thème actuel : {theme}</h1>
            <button onClick={toggleTheme}>Changer de thème</button>
        </div>
    );
}

export default ThemeManager;
```

### App.js
```javascript
import React from 'react';
import ThemeManager from './ThemeManager';

function App() {
    return (
        <div>
            <ThemeManager />
        </div>
    );
}

export default App;
```