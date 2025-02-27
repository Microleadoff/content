## Créer un compteur avec des états

### Counter.js
```javascript
// Counter.js
import React, { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    const increment = () => setCount(count + 1);
    const decrement = () => setCount(count - 1);

    return (
        <div>
            <p>Compteur : {count}</p>
            <button onClick={increment}>Incrémenter</button>
            <button onClick={decrement}>Décrémenter</button>
        </div>
    );
}

export default Counter;
```

### App.js
```javascript
// App.js
import React from 'react';
import Counter from './Counter';

function App() {
    return (
        <div>
            <h1>Test des états</h1>
            <Counter />
        </div>
    );
}

export default App;
```