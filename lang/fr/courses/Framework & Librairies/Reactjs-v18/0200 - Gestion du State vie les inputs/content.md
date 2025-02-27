## Gérer l'état des inputs dans React

Dans React, la gestion de l’état des inputs suit une approche **déclarative** : au lieu de manipuler directement les éléments de l'interface, il s’agit de définir les différents états possibles du composant, et React se charge d’actualiser l’affichage en fonction des interactions utilisateur. Cette méthode simplifie la création d’interfaces dynamiques et réactives.

### Comprendre l’approche déclarative de React

Dans une approche de programmation classique (dite impérative), chaque action de l'utilisateur déclenche une série d’instructions spécifiques pour ajuster l’affichage. En React, l’approche est déclarative : les états du composant sont prédéfinis en fonction des actions utilisateur, et React gère ensuite les transitions. Cela permet de structurer les interfaces en fonction de situations précises, facilitant la maintenance et l’évolution du code.

### Identifier les états essentiels

Prenons l’exemple d’un formulaire simple où un utilisateur entre son nom :

1. **Vide** : l’input est vide et le bouton est désactivé.
2. **Rempli** : l’utilisateur a saisi du texte, le bouton devient actif.
3. **En cours d’envoi** : lors de la soumission, le formulaire est temporairement désactivé.

Ces états permettent de gérer efficacement les changements d’interface en fonction des actions de l’utilisateur.

### Suivre les valeurs des inputs avec `useState`

Le hook `useState` permet de capturer et de gérer en temps réel les changements d’un input. Voici un exemple où la saisie de l’utilisateur est suivie et affichée :

```javascript
import React, { useState } from 'react';

function NameForm() {
  const [name, setName] = useState('');

  function handleChange(e) {
    setName(e.target.value);
  }

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={handleChange}
        placeholder="Entrez votre nom"
      />
      <p>Nom entré : {name}</p>
    </div>
  );
}
```

Dans cet exemple :
- La fonction `handleChange` est déclenchée à chaque saisie de l’utilisateur dans l’input.
- La mise à jour de `name` avec `setName(e.target.value)` permet d’obtenir en temps réel le texte saisi, accessible via `e.target.value`.

### Gérer l'état des boutons et la soumission

L'état de l'input peut également influencer l'activation ou la désactivation d'un bouton. Par exemple, le bouton "Envoyer" peut n’être activé que si du texte est entré :

```javascript
function NameForm() {
  const [name, setName] = useState('');
  const [status, setStatus] = useState('empty');

  function handleChange(e) {
    setName(e.target.value);
    setStatus(e.target.value ? 'filled' : 'empty');
  }

  function handleSubmit(e) {
    e.preventDefault();
    alert(`Nom soumis : ${name}`);
    setStatus('empty');
    setName('');
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={handleChange}
        placeholder="Entrez votre nom"
      />
      <button type="submit" disabled={status === 'empty'}>
        Envoyer
      </button>
    </form>
  );
}
```

Cet exemple montre comment ajuster l’état d’un bouton en fonction de la saisie utilisateur et réinitialiser le champ après soumission :

1. **Activation conditionnelle du bouton** :
   - L'état `status` permet de déterminer si le bouton "Envoyer" est activé.
   - `handleChange` vérifie si l'input contient du texte et définit `status` en conséquence : `'filled'` si du texte est présent, `'empty'` s'il est vide.
   - Le bouton "Envoyer" utilise `disabled={status === 'empty'}` pour rester désactivé tant qu'aucun texte n'est saisi.

2. **Soumission et réinitialisation du formulaire** :
   - Lors de la soumission, `handleSubmit` affiche le nom entré dans une alerte, puis réinitialise le champ de saisie et le bouton.
   - `handleSubmit` remet `name` et `status` à leur état initial (`''` et `'empty'`), rendant le bouton inactif après l’envoi.