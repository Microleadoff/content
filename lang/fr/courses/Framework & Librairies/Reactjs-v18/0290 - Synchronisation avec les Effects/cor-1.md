## Compteur et horloge

### Clock.js
```javascript
import React, { useState, useEffect } from 'react';

function Clock() {
    const [time, setTime] = useState(new Date().toLocaleTimeString());

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(new Date().toLocaleTimeString());
        }, 1000);

        return () => clearInterval(interval); // Nettoyage de l’effet
    }, []);

    return <h1>Heure actuelle : {time}</h1>;
}

export default Clock;
```

### TitleCounter.js
```javascript
import React, { useState, useEffect } from 'react';

function TitleCounter() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        document.title = `Compteur : ${count}`;
    }, [count]);

    return (
        <div>
            <p>Compteur : {count}</p>
            <button onClick={() => setCount(count + 1)}>Incrémenter</button>
            <button onClick={() => setCount(count - 1)}>Décrémenter</button>
        </div>
    );
}

export default TitleCounter;
```

### App.js
```javascript
import React from 'react';
import Clock from './Clock';
import TitleCounter from './TitleCounter';

function App() {
    return (
        <div>
            <h1>Synchronisation avec les Effects</h1>
            <Clock />
            <TitleCounter />
        </div>
    );
}

export default App;
```
