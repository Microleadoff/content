## Créer un hook pour gérer les fenêtres modales

### useModal.js
```javascript
import { useState } from 'react';

function useModal() {
    const [isOpen, setIsOpen] = useState(false);

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);

    return { isOpen, openModal, closeModal };
}

export default useModal;
```

### Modal.js
```javascript
import React from 'react';

function Modal({ isOpen, closeModal }) {
    if (!isOpen) return null;

    return (
        <div style={{ background: 'rgba(0, 0, 0, 0.5)', padding: '20px' }}>
            <div style={{ background: 'white', padding: '20px' }}>
                <p>Voici une fenêtre modale !</p>
                <button onClick={closeModal}>Fermer</button>
            </div>
        </div>
    );
}

export default Modal;
```

### App.js
```javascript
import React from 'react';
import useModal from './useModal';
import Modal from './Modal';

function App() {
    const { isOpen, openModal, closeModal } = useModal();

    return (
        <div>
            <button onClick={openModal}>Ouvrir la modale</button>
            <Modal isOpen={isOpen} closeModal={closeModal} />
        </div>
    );
}

export default App;
```