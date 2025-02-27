## Créer un compteur avec un historique

### App.js
```javascript
// App.js
import React from 'react';
import CounterWithHistory from './CounterWithHistory';

function App() {
    return (
        <div>
            <h1>Compteur avec historique</h1>
            <CounterWithHistory />
        </div>
    );
}

export default App;
```

#### CounterWithHistory.js
```javascript
// CounterWithHistory.js
import React, { useState } from 'react';

function CounterWithHistory() {
    const [count, setCount] = useState(0);
    const [history, setHistory] = useState([]);

    const increment = () => {
        setCount((prevCount) => {
            const newCount = prevCount + 1;
            setHistory((prevHistory) => [...prevHistory, newCount]);
            return newCount;
        });
    };

    const reset = () => {
        setCount(0);
        setHistory([]);
    };

    return (
        <div>
            <p>Compteur : {count}</p>
            <button onClick={increment}>Incrémenter</button>
            <button onClick={reset}>Réinitialiser</button>
            <ul>
                {history.map((item, index) => (
                <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}

export default CounterWithHistory;
```