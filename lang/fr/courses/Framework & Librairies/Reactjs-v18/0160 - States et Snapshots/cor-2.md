## Créer une boîte de texte avec un historique

### App.js
```javascript
// App.js
import React from 'react';
import InputWithHistory from './InputWithHistory';

function App() {
    return (
        <div>
            <h1>Boîte de texte avec historique</h1>
            <InputWithHistory />
        </div>
    );
}

export default App;
```

### InputWithHistory.js
```javascript
// InputWithHistory.js
import React, { useState } from 'react';

function InputWithHistory() {
    const [value, setValue] = useState('');
    const [history, setHistory] = useState([]);

    const handleChange = (event) => {
        const newValue = event.target.value;
        setValue(newValue);
        setHistory((prevHistory) => [...prevHistory, newValue]);
    };

  return (
        <div>
            <input type="text" value={value} onChange={handleChange} placeholder="Tapez quelque chose" />
            <ul>
                {history.map((item, index) => (
                <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}

export default InputWithHistory;
```