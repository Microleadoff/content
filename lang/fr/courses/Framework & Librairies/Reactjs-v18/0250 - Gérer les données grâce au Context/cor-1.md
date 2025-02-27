## Créer un thème global avec le Context

### ThemeContext.js
```javascript
// ThemeContext.js
import React, { createContext, useState } from 'react';

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');

    const toggleTheme = () => {
        setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}
```

### ThemeDisplay.js
```javascript
// ThemeDisplay.js
import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

function ThemeDisplay() {
    const { theme } = useContext(ThemeContext);
    return <h1>Thème actuel : {theme}</h1>;
}

export default ThemeDisplay;
```

### ThemeToggle.js
```javascript
// ThemeToggle.js
import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

function ThemeToggle() {
    const { toggleTheme } = useContext(ThemeContext);
    return <button onClick={toggleTheme}>Changer de thème</button>;
}

export default ThemeToggle;
```

### App.js
```javascript
// App.js
import React from 'react';
import { ThemeProvider } from './ThemeContext';
import ThemeDisplay from './ThemeDisplay';
import ThemeToggle from './ThemeToggle';

function App() {
    return (
        <ThemeProvider>
        <ThemeDisplay />
        <ThemeToggle />
        </ThemeProvider>
    );
}

export default App;
```