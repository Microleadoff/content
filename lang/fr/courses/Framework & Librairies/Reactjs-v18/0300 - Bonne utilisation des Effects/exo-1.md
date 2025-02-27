## Corriger un effet mal utilisé

1. Vous avez reçu un composant `Timer.js` qui utilise `useEffect` pour mettre à jour un compteur toutes les secondes. Cependant, ce composant comporte plusieurs erreurs :
    - Il y a un risque de fuites mémoire lorsque le composant est démonté.
    - L’effet est déclenché à chaque rendu, ce qui n’est pas nécessaire.
2. Corrigez ces problèmes dans le fichier `Timer.js` pour qu’il fonctionne correctement.

### Code de départ
```javascript
import React, { useState, useEffect } from 'react';

function Timer() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        setInterval(() => {
            setCount(count + 1);
        }, 1000);
    });

    return <h1>Compteur : {count}</h1>;
}

export default Timer;
```

#### Rendu attendu

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0300%20-%20Bonne%20utilisation%20des%20Effects/rendu_exo_30_1.png?raw=true" alt="Rendu attendu de l'exercice">