## Les hooks personnalisés

Les hooks personnalisés permettent de partager facilement des morceaux de logique entre plusieurs composants. Ils encapsulent des comportements spécifiques souvent absents des hooks intégrés de React. En isolant cette logique, ils améliorent la lisibilité et la maintenabilité du code tout en rendant chaque composant plus autonome. Cette approche modulaire contribue à structurer les applications de manière claire et évolutive, tout en évitant la duplication de code.


### Qu'est-ce qu'un hook personnalisé ?

Un hook personnalisé est une fonction JavaScript qui commence par `use`. Cette convention indique qu’il suit les règles des hooks de React, notamment leur usage uniquement à l’intérieur des composants fonctionnels ou d’autres hooks. En appelant d'autres hooks intégrés, un hook personnalisé encapsule une logique réutilisable et peut gérer son propre état ou ses propres effets. Par exemple, un hook comme `useCounter` peut encapsuler la logique d’un compteur tout en permettant son utilisation dans plusieurs composants.

```javascript
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);

  const increment = () => setCount((prev) => prev + 1);
  const decrement = () => setCount((prev) => prev - 1);

  return { count, increment, decrement };
}
```

Dans cet exemple, le hook `useCounter` gère un état indépendant pour chaque composant qui l’utilise. Cela permet de réutiliser la logique du compteur sans répéter son implémentation.

### Pourquoi utiliser des hooks personnalisés ?

L’un des principaux avantages des hooks personnalisés est qu’ils simplifient le code tout en le rendant plus modulaire. Lorsqu’une logique complexe est partagée entre plusieurs composants, l’encapsuler dans un hook évite de répéter les mêmes lignes de code. Cela réduit également les erreurs potentielles liées à la duplication et améliore la lisibilité globale de l’application. Les hooks personnalisés sont également utiles pour isoler des comportements spécifiques, comme la gestion des états réseau ou des animations.

Un bon exemple est la détection du statut réseau, où l’état `isOnline` est surveillé et mis à jour en temps réel. En créant un hook personnalisé pour cette fonctionnalité, il est possible de réutiliser la même logique dans différents composants.

### Exemple pratique : Détection du statut réseau

Le hook `useOnlineStatus` encapsule la logique nécessaire pour surveiller si l'utilisateur est en ligne ou hors ligne. Il initialise l'état avec la valeur actuelle de la connectivité via `navigator.onLine`, puis écoute les événements `online` et `offline` pour mettre à jour cet état en conséquence.

```javascript
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  return isOnline;
}
```

Ce hook est utile dans des composants comme une barre de statut ou un bouton d’enregistrement. Par exemple, un composant `StatusBar` peut afficher si l’utilisateur est connecté ou non en temps réel, tandis qu’un composant `SaveButton` peut désactiver le bouton si l’utilisateur est hors ligne. La logique reste centralisée dans le hook `useOnlineStatus`, simplifiant ainsi les composants individuels.

### Simplifier les appels API avec un hook personnalisé

Les appels API nécessitent souvent une gestion complexe des états de chargement, des erreurs et des données. En encapsulant cette logique dans un hook comme `useFetch`, il devient facile de gérer ces aspects tout en évitant la duplication de code.

```javascript
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, [url]);

  return { data, loading, error };
}
```

Ce hook gère trois états (`data`, `loading` et `error`) et réagit automatiquement aux changements d’URL. Par exemple, dans un composant `UserList`, il suffit d’utiliser ce hook pour récupérer et afficher les données des utilisateurs, tout en déléguant la gestion des erreurs et des chargements au hook.

### Encapsulation de l’état des formulaires

Un autre cas d’usage courant est la gestion des formulaires. Le hook personnalisé `useFormInput` simplifie la gestion de l’état et des événements d’un champ de saisie, permettant de réutiliser cette logique dans différents formulaires.

```javascript
function useFormInput(initialValue) {
  const [value, setValue] = useState(initialValue);

  const handleChange = (e) => setValue(e.target.value);

  return {
    value,
    onChange: handleChange,
  };
}
```

Dans un composant de formulaire, chaque champ peut utiliser ce hook pour gérer son propre état de manière indépendante, ce qui réduit la complexité et améliore la modularité du code.

### Optimisation et gestion avancée des hooks

Lorsqu’un hook doit gérer des objets ou des fonctions dépendantes, il est essentiel de stabiliser ces références pour éviter des exécutions inutiles ou des effets secondaires indésirables. Des outils comme `useCallback` et `useMemo` peuvent être utilisés pour optimiser les performances en réduisant les recalculs.

Par exemple, un hook qui effectue des recherches dynamiques peut encapsuler la logique dans une fonction stabilisée avec `useCallback`, évitant ainsi que chaque rendu ne recrée une nouvelle référence pour cette fonction.

```javascript
function useSearch(query) {
  const [results, setResults] = useState([]);

  const fetchResults = useCallback(() => {
    fetch(`/search?q=${query}`)
      .then((response) => response.json())
      .then(setResults);
  }, [query]);

  useEffect(() => {
    fetchResults();
  }, [fetchResults]);

  return results;
}
```

### Cas avancés : Gestion des animations

Les hooks personnalisés peuvent également être utilisés pour encapsuler des animations complexes. Par exemple, un hook `useFadeIn` permet de gérer une transition progressive de l’opacité d’un élément.

```javascript
function useFadeIn(ref, duration) {
  useEffect(() => {
    const node = ref.current;
    let start = performance.now();

    function frame(now) {
      const progress = Math.min((now - start) / duration, 1);
      node.style.opacity = progress;

      if (progress < 1) {
        requestAnimationFrame(frame);
      }
    }

    requestAnimationFrame(frame);
  }, [ref, duration]);
}
```

Ce hook peut être utilisé dans un composant comme `Welcome` pour appliquer une animation d’apparition fluide.

### Conclusion

Les hooks personnalisés offrent une approche puissante et flexible pour structurer et réutiliser la logique dans React. Ils permettent de simplifier le code tout en le rendant plus maintenable, modulaire et performant. Que ce soit pour gérer des appels API, des états réseau ou des animations, leur utilisation améliore considérablement l’architecture de vos applications React.