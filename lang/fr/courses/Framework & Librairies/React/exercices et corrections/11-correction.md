## **Correction des exercices du cours 11**

### **1. Créer une fonction pure pour le calcul d'une réduction**

#### DiscountCalculator.js
```javascript
// DiscountCalculator.js
import React from 'react';

// Fonction pure pour calculer le prix après réduction
function calculateDiscount(price, discount) {
    return price - price * (discount / 100);
}

// Composant affichant le prix réduit
function DiscountDisplay({ price, discount }) {
    const discountedPrice = calculateDiscount(price, discount);
    return (
        <div>
            <ul>
                <li>prix : {price}</li>
                <li>pourcentage de reduction : {discount}</li>
            </ul>
            <p>Prix après réduction : {discountedPrice.toFixed(2)} €</p>
        </div>
    );
}

export default DiscountDisplay;
```

#### App.js
```javascript
// App.js
import React from 'react';
import DiscountDisplay from './DiscountCalculator';

// Affichage du composant DiscountDisplay avec des exemples
function App() {
  return (
    <div>
      <DiscountDisplay price={100} discount={20} />
      <DiscountDisplay price={50} discount={10} />
    </div>
  );
}

export default App;
```

---

### **2. Créer une fonction pure pour convertir des températures**

Cet exercice vise à pratiquer la création d'une fonction pure et son utilisation dans un composant React.

#### TemperatureConverter.js
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

#### App.js
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

---


