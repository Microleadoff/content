## Créer une fonction pure pour convertir des températures

Cet exercice vise à pratiquer la création d'une fonction pure et son utilisation dans un composant React.

### TemperatureConverter.js
```javascript
// TemperatureConverter.js
import React from 'react';

// Fonction pure pour convertir des Celsius en Fahrenheit
function convertToFahrenheit(celsius) {
    return (celsius * 9) / 5 + 32;
}

// Composant affichant les températures en Celsius et Fahrenheit
function TemperatureDisplay({ celsius }) {
    const fahrenheit = convertToFahrenheit(celsius);

    return (
        <div>
            <ul>
                <li>Température en Celsius : {celsius}°C</li>
                <li>Température en Fahrenheit : {fahrenheit.toFixed(2)}°F</li>
            </ul>
        </div>
    );
}

export default TemperatureDisplay;
```

### App.js
```javascript
// App.js
import React from 'react';
import TemperatureDisplay from './TemperatureConverter';

// Affichage du composant TemperatureDisplay avec des exemples
function App() {
    return (
        <div>
            <TemperatureDisplay celsius={0} />
            <TemperatureDisplay celsius={25} />
            <TemperatureDisplay celsius={100} />
        </div>
    );
}

export default App;
```