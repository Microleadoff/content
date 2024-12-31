## Les états en file d'attente (Queueing States)

Dans React, les mises à jour de l'état ne sont pas appliquées immédiatement lors de l’appel à `setState`. Au lieu de cela, React enregistre ces mises à jour dans une **file d'attente** et les applique au prochain cycle de rendu. Ce fonctionnement permet de regrouper les modifications d'état, réduisant ainsi les rendus inutiles et optimisant les performances de l’application.

Ce regroupement est particulièrement utile dans les composants interactifs, où plusieurs changements peuvent se produire en succession rapide. En utilisant une file d’attente, React traite ces modifications en une seule fois, ce qui améliore la réactivité tout en limitant les rendus intermédiaires.

### Fonctionnement pratique

Lors de plusieurs appels à `setState` dans un même cycle, React ne met pas à jour l’interface utilisateur après chaque appel. Les mises à jour sont empilées dans la file d'attente, puis appliquées en un seul rendu avec l’état final mis à jour.

**Exemple** : Supposons que `setCount(count + 1)` soit appelé trois fois de suite dans une fonction. Plutôt que d’effectuer trois rendus, React regroupe les appels successifs et applique directement la dernière valeur de `count` en un seul cycle de rendu.

### Mises à jour séquentielles

Pour que chaque mise à jour prenne en compte la version la plus récente de l’état, il est recommandé d’utiliser la version callback de `setState`. Cette méthode garantit l’accès à la dernière valeur de l’état, ce qui évite les décalages dans les mises à jour.

```javascript
setState((prevState) => prevState + 1);
```

En utilisant `prevState`, chaque mise à jour repose sur l’état actuel en mémoire, assurant une continuité et une cohérence même lors de mises à jour consécutives.

### Avantages du Queueing States

Le mécanisme de file d'attente des états présente plusieurs avantages :
- **Limite les rendus successifs** : Les modifications d'état sont regroupées pour réduire le nombre de rendus.
- **Évite les recalculs intermédiaires** : Les rendus intermédiaires sont minimisés, même en cas de mises à jour fréquentes.
- **Assure une mise à jour cohérente** : Les modifications de l'interface se basent toujours sur l’état le plus récent.

### Exemple illustratif : gestion d’un compteur

Prenons un exemple de compteur où chaque clic doit augmenter la valeur de 3 unités. En utilisant `prevCount`, chaque mise à jour repose sur la dernière valeur en mémoire, garantissant une mise à jour cohérente en un seul rendu.

```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  const incrementThreeTimes = () => {
    setCount((prevCount) => prevCount + 1);
    setCount((prevCount) => prevCount + 1);
    setCount((prevCount) => prevCount + 1);
  };

  return (
    <div>
      <p>Valeur actuelle : {count}</p>
      <button onClick={incrementThreeTimes}>+3</button>
    </div>
  );
}
```

Dans cet exemple, `count` est bien incrémenté de 3 d'un seul coup, car `prevCount` assure que chaque `setCount` utilise l’état le plus récent. React optimise ainsi le rendu en traitant les trois appels de manière groupée, sans déclencher de rendus intermédiaires.