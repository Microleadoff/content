## Avoir une bonne utilisation des effets

Les effets (`useEffect`) sont un outil puissant de React permettant de synchroniser les composants avec des systèmes externes tels que le DOM, des API ou des widgets tiers. Cependant, ils ne doivent être utilisés que lorsque cela est absolument nécessaire. Une utilisation excessive ou superflue peut rendre le code moins performant, plus complexe et susceptible d’introduire des bugs.

### Quand utiliser un effet ?

Les effets sont utiles dans les cas suivants :  
1. **Interaction avec des systèmes extérieurs** : Par exemple, gérer une API ou synchroniser un composant React avec un widget tiers.  
2. **Mise à jour ou abonnement au DOM** : Manipuler directement un élément DOM ou écouter des événements globaux (par exemple, `window.addEventListener`).  
3. **Effets de bord liés à l’affichage** : Par exemple, démarrer une animation, connecter un websocket ou charger des données lorsque le composant s’affiche.

Exemple : Supposons un composant `ChatRoom` qui se connecte à un serveur lorsque l’utilisateur accède à la discussion :

```jsx
import { useEffect } from 'react';

function ChatRoom() {
  useEffect(() => {
    const connection = createConnection();
    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, []);

  return <h1>Bienvenue dans la discussion !</h1>;
}
```

L’effet démarre une connexion au serveur lors du montage du composant et s'assure de la fermer proprement lors de son démontage. Cela évite d'accumuler des connexions inutilisées et garantit une bonne gestion des ressources.

### Quand ne pas utiliser un effet ?

Dans de nombreux cas, les effets sont inutiles. Les alternatives naturelles de React permettent souvent d’obtenir le même résultat avec moins de complexité.

#### 1. **Calculer des données dérivées**  

Si une valeur peut être calculée à partir des `props` ou de l’état, inutile d’utiliser un effet. Il est préférable de calculer cette valeur pendant le rendu.

Exemple incorrect :
```jsx
function UserProfile({ firstName, lastName }) {
  const [fullName, setFullName] = useState('');

  useEffect(() => {
    setFullName(`${firstName} ${lastName}`);
  }, [firstName, lastName]);

  return <p>{fullName}</p>;
}
```

Exemple corrigé :
```jsx
function UserProfile({ firstName, lastName }) {
  const fullName = `${firstName} ${lastName}`;
  return <p>{fullName}</p>;
}
```

En calculant `fullName` directement pendant le rendu, on évite un effet superflu et une passe de rendu supplémentaire, simplifiant ainsi le code.

#### 2. **Gérer les événements utilisateurs**  
   Les gestionnaires d’événements suffisent pour gérer la plupart des interactions. Ajouter un effet dans ces cas crée des redondances et des bugs potentiels.

Exemple incorrect :
```jsx
function Form() {
  const [formData, setFormData] = useState({});

  useEffect(() => {
    if (formData.submitted) {
      sendDataToServer(formData);
    }
  }, [formData]);

  return (
    <button onClick={() => setFormData({ submitted: true })}>
      Soumettre
    </button>
  );
}
```

Exemple corrigé :
```jsx
function Form() {
  const [formData, setFormData] = useState({});

  function handleSubmit() {
    setFormData({ submitted: true });
    sendDataToServer(formData);
  }

  return <button onClick={handleSubmit}>Soumettre</button>;
}
```

En plaçant la logique dans un gestionnaire d’événement, on évite les effets superflus et on améliore le contrôle de la logique métier.

### Optimiser les calculs complexes

Lorsque des calculs sont coûteux en temps ou mémoire, il est parfois nécessaire de les optimiser avec `useMemo`. Cela évite de recalculer des valeurs inutiles.

Exemple :
```jsx
function TodoList({ todos, filter }) {
  const visibleTodos = useMemo(() => {
    return todos.filter(todo => todo.includes(filter));
  }, [todos, filter]);

  return <ul>{visibleTodos.map(todo => <li key={todo}>{todo}</li>)}</ul>;
}
```

L’utilisation de `useMemo` garantit que le filtrage des tâches n’est recalculé que lorsque `todos` ou `filter` changent, ce qui améliore les performances pour des listes importantes.

### Réinitialiser l’état d’un composant sur changement de `props`

Pour réinitialiser automatiquement l’état d’un composant lors d’un changement de `props`, utilisez une clé (`key`). Cela force React à recréer le composant.

Exemple :
```jsx
function ProfilePage({ userId }) {
  return <Profile userId={userId} key={userId} />;
}

function Profile({ userId }) {
  const [comment, setComment] = useState('');
  return <textarea value={comment} onChange={e => setComment(e.target.value)} />;
}
```

Passer `userId` comme clé (`key`) force React à recréer un nouvel état pour chaque utilisateur, garantissant ainsi une séparation claire des données.

## Bonnes pratiques générales

### 1. **Limiter les dépendances des effets**  
   Déclarez uniquement les dépendances nécessaires pour éviter des ré-exécutions inutiles.

Exemple incorrect :
```jsx
useEffect(() => {
  fetchData();
}, []);
```

Exemple corrigé :
```jsx
useEffect(() => {
  fetchData();
}, [query]);
```

L’ajout de la dépendance `query` garantit que les données sont rechargées dès que la requête change, assurant la cohérence de l’affichage.

### 2. **Ajouter des fonctions de nettoyage**  
   Toujours nettoyer les effets qui laissent des abonnements ou manipulent des ressources, comme dans cet exemple :

```jsx
useEffect(() => {
  const id = setInterval(() => {
    console.log('Tick');
  }, 1000);

  return () => clearInterval(id);
}, []);
```

La fonction de nettoyage empêche que l’intervalle continue de fonctionner après le démontage du composant, évitant ainsi des comportements imprévus.

### 3. **Utiliser des hooks personnalisés**  
   Si un effet est récurrent dans plusieurs composants, encapsulez-le dans un hook pour simplifier le code.

Exemple :
```jsx
function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let ignore = false;
    fetch(url).then(response => response.json()).then(json => {
      if (!ignore) setData(json);
    });
    return () => { ignore = true; };
  }, [url]);

  return data;
}
```

Le hook personnalisé `useFetch` encapsule la logique de chargement et peut être réutilisé dans plusieurs composants pour centraliser la gestion des données.

### Conclusion

Les effets sont une fonctionnalité clé de React, mais leur utilisation doit être justifiée. Privilégiez les alternatives naturelles de React comme les calculs pendant le rendu ou les gestionnaires d’événements. Lorsque vous utilisez un effet, assurez-vous qu’il soit correctement configuré, avec des dépendances précises et une fonction de nettoyage si nécessaire. En simplifiant vos composants et en limitant les effets, vous obtiendrez un code plus performant, lisible et facile à maintenir.