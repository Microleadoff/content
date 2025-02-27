## Corriger un effet mal utilisé

### Timer.js
```javascript
import React, { useState, useEffect } from 'react';

function Timer() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setCount((prevCount) => prevCount + 1);
        }, 1000);

        return () => clearInterval(interval); // Nettoyage de l'effet pour éviter les fuites
    }, []); // L'effet s'exécute uniquement une fois au montage

    return <h1>Compteur : {count}</h1>;
}

export default Timer;
```

### App.js
```javascript
import React from 'react';
import Timer from './Timer';

function App() {
    return (
        <div>
            <Timer />
        </div>
    );
}

export default App;
```