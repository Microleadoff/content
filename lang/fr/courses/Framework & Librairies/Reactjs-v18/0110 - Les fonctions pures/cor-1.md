## Créer une fonction pure pour le calcul d'une réduction

### DiscountCalculator.js
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

### App.js
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