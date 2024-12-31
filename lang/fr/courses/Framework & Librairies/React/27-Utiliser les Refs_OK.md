## Introduction aux refs en React

Une **ref** est un moyen d'accéder directement à un élément ou de conserver une valeur. Dans React, les **refs** sont utilisées pour gérer des valeurs mutables ou interagir directement avec des éléments du DOM, sans passer par le cycle de rendu habituel. Contrairement au state, modifier une ref ne déclenche pas de re-render, ce qui en fait un outil adapté pour des scénarios spécifiques où les données doivent persister entre les rendus sans affecter l’affichage.

### Pourquoi et quand utiliser les refs en React ?

Une ref est un objet React contenant une propriété `.current`. Cette propriété peut pointer vers n’importe quelle donnée, qu’il s’agisse d’un élément DOM, d’une valeur temporaire ou d’une fonction. Les refs permettent de conserver des données entre les rendus, sans pour autant participer au cycle de rendu, ce qui les distingue du state.

Les refs sont particulièrement utiles pour des cas où les données ne nécessitent pas une synchronisation avec l’interface utilisateur, comme le suivi d’un timer ou l’accès direct à des éléments DOM.

## Création et manipulation des refs

### Exemple simple : stockage d’une valeur mutable

```javascript
import { useRef } from 'react';

function Counter() {
  const countRef = useRef(0);

  function increment() {
    countRef.current += 1;
    console.log('Valeur actuelle :', countRef.current);
  }

  return <button onClick={increment}>Incrémenter</button>;
}
```

Dans cet exemple, `countRef.current` conserve la valeur d’un compteur incrémenté à chaque clic. Contrairement au state, cette modification n’affecte pas le rendu du composant. Cette approche est idéale pour des données temporaires ou non liées à l’interface.

## Interagir avec le DOM

Les refs sont aussi utilisées pour manipuler directement des éléments DOM. Voici un exemple avec un champ de texte :

```javascript
import { useRef } from 'react';

function FocusInput() {
  const inputRef = useRef(null);

  function handleFocus() {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Tapez ici" />
      <button onClick={handleFocus}>Donner le focus</button>
    </div>
  );
}
```

La ref `inputRef` pointe ici vers le champ de texte `<input>`. Cela permet d’interagir directement avec l’élément DOM natif pour lui appliquer des actions comme le focus, sans passer par React pour ce type de manipulation.

### Exemple avancé : chronomètre combinant state et refs

Dans un chronomètre, l’identifiant de l’intervalle est stocké dans une ref (car il ne nécessite pas de rendu), tandis que le temps écoulé est géré avec le state (car il est affiché à l’écran).

```javascript
import { useState, useRef } from 'react';

function Stopwatch() {
  const [time, setTime] = useState(0);
  const timerRef = useRef(null);

  function startTimer() {
    if (!timerRef.current) {
      timerRef.current = setInterval(() => {
        setTime((prevTime) => prevTime + 1);
      }, 1000);
    }
  }

  function stopTimer() {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  }

  return (
    <div>
      <h1>{time} secondes</h1>
      <button onClick={startTimer}>Démarrer</button>
      <button onClick={stopTimer}>Arrêter</button>
    </div>
  );
}
```

Dans ce cas, la ref `timerRef` permet de conserver l’identifiant du timer créé par `setInterval`, sans influencer le rendu. Le state `time`, quant à lui, met à jour l’affichage de l’interface utilisateur.

## Différence entre refs et state

Les refs et le state ont des rôles distincts dans React. Le state est utilisé pour des données qui influencent directement le rendu de l’interface utilisateur. Les refs, en revanche, servent à gérer des données non liées au rendu, comme des informations temporaires ou des interactions directes avec le DOM.

Exemple :
- Le state est idéal pour gérer un compteur dont la valeur doit être affichée.
- Une ref est plus adaptée pour suivre un identifiant de timer ou une valeur temporaire invisible à l’utilisateur.

### Bonnes pratiques pour les refs

- **Utilisation limitée** : Les refs doivent être utilisées uniquement lorsque le state n’est pas adapté, par exemple pour des interactions DOM ou des données éphémères.
- **Ne pas modifier pendant le rendu** : Les modifications de `ref.current` dans le cycle de rendu peuvent entraîner des comportements imprévisibles.
- **Combiner avec le state** : Les refs peuvent être utilisées conjointement avec le state pour tirer parti de leurs atouts respectifs, comme dans le chronomètre vu précédemment.

### Conclusion

Les refs sont un outil puissant dans React, offrant une flexibilité supplémentaire pour gérer des scénarios où le state ne convient pas. Que ce soit pour interagir avec le DOM ou pour conserver des données temporaires, elles apportent une solution efficace et performante. Cependant, leur usage doit rester ciblé et respectueux des bonnes pratiques afin de garantir la maintenabilité et la clarté du code.