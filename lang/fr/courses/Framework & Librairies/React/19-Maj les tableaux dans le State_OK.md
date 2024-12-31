## Mise à jour des tableaux d’état dans React

En React, il est fréquent d’utiliser des tableaux pour gérer des listes d’éléments dynamiques, comme des tâches, des produits dans un panier ou des messages. Cependant, contrairement aux variables JavaScript classiques, les tableaux d’état doivent être manipulés de manière **immuable** pour que React détecte les modifications et déclenche un rerendering. Ce cours présente les bonnes pratiques pour manipuler efficacement les tableaux dans l’état React tout en maintenant leur immutabilité.

### Pourquoi l’immutabilité des tableaux est essentielle

En React, l’immuabilité des données d’état permet à React de détecter les changements et de déclencher automatiquement un rerendering. Si un tableau est modifié directement, React ne le considère pas comme un nouveau tableau et ne mettra pas à jour l’interface utilisateur. En créant une copie du tableau lors de chaque mise à jour, on s’assure que React traite ce tableau comme un nouvel état et réagit en conséquence.

## Techniques de mise à jour d’un tableau d’état

Les opérations les plus courantes avec un tableau d’état sont **l’ajout**, **la suppression**, et **la modification** d’éléments. Chaque opération nécessite la création d’une nouvelle copie du tableau, sans modification directe du tableau original.

### Ajout d’un élément

Pour ajouter un nouvel élément tout en conservant l’immuabilité, utilisez l’opérateur spread (`...`) pour créer un nouveau tableau contenant l’élément ajouté.

```javascript
setItems((prevItems) => [
  ...prevItems, // Copie tous les éléments existants
  newItem // Ajoute le nouvel élément
]);
```

### Suppression d’un élément

Pour supprimer un élément, la méthode `filter` est appropriée car elle retourne un nouveau tableau sans l’élément sélectionné, sans altérer le tableau d’origine.

```javascript
setItems((prevItems) =>
  prevItems.filter(item => item.id !== idToRemove) // Retire l'élément ciblé
);
```

### Modification d’un élément

La méthode `map` permet de cibler un élément spécifique pour le modifier, tout en laissant les autres éléments inchangés. Cela garantit que chaque élément du tableau reste immuable.

```javascript
setItems((prevItems) =>
  prevItems.map(item =>
    item.id === idToUpdate ? { ...item, updatedProp: newValue } : item
  )
);
```

### Pourquoi Préserver l’immutabilité ?

L’utilisation de copies immuables permet à React de **détecter les changements** dans le tableau d’état, ce qui déclenche un rerendering et maintient l’interface synchronisée avec les données les plus récentes. Cela améliore la performance et la fiabilité de l’application.

### Simplifier les mises à jour complexes avec immer

Pour des structures de données imbriquées, **immer** simplifie la gestion de l’état en permettant des modifications directes sur une copie temporaire (appelée `draft`) sans rompre l’immuabilité. Immer crée automatiquement des copies immuables, ce qui évite d’utiliser constamment des opérateurs spread et rend le code plus lisible.

```javascript
import produce from 'immer';

const handleUpdate = () => {
  setItems(produce(draft => {
    draft[indexToUpdate].property = newValue; // Modification directe sur le draft
  }));
};
```

### Bonnes pratiques pour gérer les tableaux d’état

1. **Toujours créer un nouveau tableau** : Utilisez `map`, `filter`, ou l’opérateur spread pour chaque mise à jour afin de garantir l’immuabilité.
2. **Éviter les méthodes qui modifient en place** : Des méthodes comme `push`, `pop`, et `splice` modifient directement le tableau d’origine, ce qui va à l’encontre de l’immuabilité nécessaire dans React.
3. **Utiliser Immer pour des cas complexes** : Lorsqu’il s’agit de structures imbriquées, Immer permet d'écrire du code plus concis tout en préservant l’intégrité de l’état.

En suivant ces pratiques, la gestion des tableaux d’état devient non seulement plus fiable et maintenable, mais elle permet aussi à React de gérer efficacement les changements, pour une interface utilisateur fluide et réactive.