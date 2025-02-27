## Créer un compteur partagé entre deux composants

### CounterDisplay.js
```javascript
// CounterDisplay.js
import React from 'react';

function CounterDisplay({ count }) {
    return <h1>Compteur : {count}</h1>;
}

export default CounterDisplay;
```

### CounterControls.js
```javascript
// CounterControls.js
import React from 'react';

function CounterControls({ onIncrement, onDecrement }) {
    return (
        <div>
            <button onClick={onIncrement}>Incrémenter</button>
            <button onClick={onDecrement}>Décrémenter</button>
        </div>
    );
}

export default CounterControls;
```

### App.js
```javascript
// App.js
import React, { useState } from 'react';
import CounterDisplay from './CounterDisplay';
import CounterControls from './CounterControls';

function App() {
    const [count, setCount] = useState(0);

    const increment = () => setCount(count + 1);
    const decrement = () => setCount(count - 1);

    return (
        <div>
            <CounterDisplay count={count} />
            <CounterControls onIncrement={increment} onDecrement={decrement} />
        </div>
    );
}

export default App;
```