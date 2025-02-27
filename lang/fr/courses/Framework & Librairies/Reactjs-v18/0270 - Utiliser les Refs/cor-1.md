## Autofocus

### MultiStepForm.js
```javascript
import React, { useRef } from 'react';

function MultiStepForm() {
    const nameRef = useRef();
    const emailRef = useRef();
    const phoneRef = useRef();

    const resetStyles = () => {
        [nameRef, emailRef, phoneRef].forEach((ref) => {
            if (ref.current) {
                ref.current.style.border = '1px solid #ccc';
            }
        });
    };

    const handleKeyPress = (event, nextRef) => {
        if (event.key === 'Enter' && nextRef.current) {
            event.preventDefault(); // Évite le comportement par défaut de soumission
            nextRef.current.focus();
        }
    };

    const handleValidationAndReset = () => {
        let isValid = true;
        resetStyles();

        [nameRef, emailRef, phoneRef].forEach((ref) => {
            if (ref.current && !ref.current.value.trim()) {
                ref.current.style.border = '2px solid red';
                isValid = false;
            }
        });

        if (isValid) {
            alert('Formulaire valide !');
        }

        setTimeout(() => {
            [nameRef, emailRef, phoneRef].forEach((ref) => {
                if (ref.current) {
                    ref.current.value = '';
                    resetStyles();
                }
            });
        }, 3000);
    };

    return (
        <div>
            <h1>Formulaire à étapes</h1>
            <form>
                <input
                type="text"
                placeholder="Nom"
                ref={nameRef}
                onKeyPress={(e) => handleKeyPress(e, emailRef)}
                />
                <input
                type="email"
                placeholder="Email"
                ref={emailRef}
                onKeyPress={(e) => handleKeyPress(e, phoneRef)}
                />
                <input
                type="text"
                placeholder="Téléphone"
                ref={phoneRef}
                />
                <button type="button" onClick={handleValidationAndReset}>
                Vérifier et réinitialiser
                </button>
            </form>
        </div>
    );
}

export default MultiStepForm;
```

### App.js
```javascript
// App.js
import React from 'react';
import MultiStepForm from './MultiStepForm';

function App() {
    return (
        <div>
            <h1>Exercices sur les refs</h1>
            <MultiStepForm />
        </div>
    );
}

export default App;
```