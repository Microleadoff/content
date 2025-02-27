## Gestion d'évènements

### ColorChanger.js
```javascript
import React, { useRef } from 'react';

function ColorChanger() {
    const boxRef = useRef();

    const changeColor = () => {
        const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
        if (boxRef.current) {
            boxRef.current.style.backgroundColor = randomColor;
        }
    };

    return (
        <div>
            <div
                ref={boxRef}
                style={{
                width: '200px',
                height: '200px',
                backgroundColor: 'white',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: '1px solid black',
                }}
            >
                Cliquez-moi !
            </div>
            <button onClick={changeColor}>Changer la couleur</button>
        </div>
    );
}

export default ColorChanger;
```

### Resizer.js
```javascript
import React, { useRef } from 'react';

function Resizer() {
    const boxRef = useRef();
    const initialSize = 200;

    const resize = (increment) => {
        if (boxRef.current) {
            const currentSize = parseInt(boxRef.current.style.width || initialSize, 10);
            boxRef.current.style.width = `${currentSize + increment}px`;
            boxRef.current.style.height = `${currentSize + increment}px`;
        }
    };

    const resetSize = () => {
        if (boxRef.current) {
            boxRef.current.style.width = `${initialSize}px`;
            boxRef.current.style.height = `${initialSize}px`;
        }
    };

    return (
        <div>
            <div
                ref={boxRef}
                style={{
                width: `${initialSize}px`,
                height: `${initialSize}px`,
                backgroundColor: '#f0f0f0',
                border: '1px solid black',
                margin: '10px 0',
                }}
            ></div>
            <button onClick={() => resize(50)}>Agrandir</button>
            <button onClick={resetSize}>Réinitialiser</button>
        </div>
    );
}

export default Resizer;
```

### App.js 
```javascript
import React from 'react';
import ColorChanger from './ColorChanger';
import Resizer from './Resizer';

function App() {
    return (
        <div>
            <h1>Manipulation du DOM avec les refs</h1>
            <ColorChanger />
            <Resizer />
        </div>
    );
}

export default App;
```
