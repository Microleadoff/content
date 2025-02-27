## Gestion des Événements dans React

Dans React, interagir avec l'utilisateur en réponse à des événements comme les clics, les survols ou les saisies est essentiel pour créer des interfaces dynamiques. Cette interaction se fait via des **gestionnaires d'événements**, qui définissent les actions à déclencher lors d'une interaction de l'utilisateur.

### Ajouter un Gestionnaire d'Événements

Un gestionnaire d'événements est une fonction associée à un élément JSX, comme un bouton. Voici un exemple où un message s'affiche lorsqu'un bouton est cliqué.

```js
function Button() {
  function handleClick() {
    alert('Vous avez cliqué !');
  }

  return <button onClick={handleClick}>Cliquez ici</button>;
}
```

Ici, `handleClick` est associé au bouton via la prop `onClick` et ne s'exécute que lorsqu'on clique dessus.

### Gestionnaires en Ligne

Il est parfois plus simple d'utiliser une fonction directement dans le JSX, surtout lorsque la logique est courte. Voici un exemple avec une **fonction fléchée** :

```js
<button onClick={() => alert('Vous avez cliqué !')}>Cliquez ici</button>
```

Ce style convient aux fonctions succinctes et faciles à comprendre.

### Passer des Gestionnaires d'Événements comme Props

Dans React, il est fréquent de **transmettre des fonctions** depuis un composant parent pour que l'enfant réagisse à certains événements. Cela permet de centraliser la logique dans le parent tout en gardant les composants enfants simples et réutilisables.

```js
function Button({ onClick, children }) {
  return <button onClick={onClick}>{children}</button>;
}

function Parent() {
  function handleAction() {
    alert('Action déclenchée');
  }

  return <Button onClick={handleAction}>Cliquez ici</Button>;
}
```

Ici, `handleAction` est passé en tant que prop `onClick` du composant `Button`. Lorsque le bouton est cliqué, la fonction du parent est exécutée.

### Gérer la Propagation des Événements

Les événements dans React se **propagent** dans l'arbre des composants. Cela signifie qu'un événement peut déclencher des gestionnaires sur un élément enfant et sur son parent. Pour stopper cette propagation, la méthode `stopPropagation()` est utilisée.

```js
function Button({ onClick }) {
  return (
    <button onClick={(e) => {
      e.stopPropagation(); // Arrête la propagation
      onClick();
    }}>
      Cliquez ici
    </button>
  );
}

function Parent() {
  return (
    <div onClick={() => alert('Parent cliqué')}>
      <Button onClick={() => alert('Bouton cliqué')} />
    </div>
  );
}
```

Dans cet exemple, cliquer sur le bouton n'affiche que le message du bouton, sans déclencher celui du parent, grâce à `stopPropagation()`.

### Empêcher le Comportement Par Défaut

Certains éléments HTML, comme les formulaires, ont un **comportement par défaut** (par exemple, recharger la page lors de la soumission). `preventDefault()` permet de désactiver ce comportement pour garder le contrôle sur l'action qui suit l'événement.

```js
function Form() {
  function handleSubmit(e) {
    e.preventDefault(); // Empêche le rechargement de la page
    alert('Formulaire soumis');
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" />
      <button type="submit">Envoyer</button>
    </form>
  );
}
```

### Conclusion

Les gestionnaires d'événements dans React permettent de rendre vos interfaces interactives. Ils peuvent être définis directement dans le JSX ou transmis via des props, offrant ainsi flexibilité et contrôle. La maîtrise des méthodes comme `stopPropagation()` et `preventDefault()` est essentielle pour gérer les interactions utilisateur de manière efficace.