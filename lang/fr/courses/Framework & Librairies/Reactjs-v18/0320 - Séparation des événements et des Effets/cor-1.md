## Séparer les effets et les événements

### ClickCounter.js
```javascript
import React, { useState, useEffect } from 'react';

function ClickCounter() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        const handleClick = () => setCount((prevCount) => prevCount + 1);

        document.addEventListener('click', handleClick);

        return () => {
            document.removeEventListener('click', handleClick); // Nettoyage
        };
    }, []); // L'effet ne s'exécute qu'une fois au montage

    return <h1>Nombre de clics : {count}</h1>;
}

export default ClickCounter;
```

### App.js
```javascript
import React from 'react';
import ClickCounter from './ClickCounter';

function App() {
    return (
        <div>
            <ClickCounter />
        </div>
    );
}

export default App;
```