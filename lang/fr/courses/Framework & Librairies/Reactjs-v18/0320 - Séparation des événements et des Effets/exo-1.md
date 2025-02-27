## Séparer les effets et les événements

1. Voici un composant `ClickCounter.js` qui mélange logique d'événement et effets dans un même bloc. Cela cause des comportements imprévisibles :
    - L’effet est exécuté chaque fois que le compteur change, alors qu’il devrait être déclenché uniquement lorsque le composant est monté.
    - La gestion des clics est incluse dans l’effet, ce qui complique le débogage.
2. Séparez les événements et les effets dans le fichier `ClickCounter.js` pour corriger ces problèmes.

### Code de départ
```javascript
import React, { useState, useEffect } from 'react';

function ClickCounter() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        document.addEventListener('click', () => {
            setCount(count + 1);
        });

        return () => {
            document.removeEventListener('click', () => {
                setCount(count + 1);
            });
        };
    }, [count]);

    return <h1>Nombre de clics : {count}</h1>;
}

export default ClickCounter;
```

## Rendu attendu

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0320%20-%20S%C3%A9paration%20des%20%C3%A9v%C3%A9nements%20et%20des%20Effets/rendu_exo_32_1.png?raw=true" alt="Rendu attendu de l'exercice">