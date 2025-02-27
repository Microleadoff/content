### Effets lifecycle : un aperçu complet

Les effets lifecycle, ou effets réactifs, constituent un aspect essentiel de la gestion des interactions entre vos composants React et des systèmes ou événements extérieurs. Ils permettent de synchroniser un composant avec des données, d'établir des abonnements ou encore de gérer des tâches spécifiques au cycle de vie du composant. Bien que leur utilisation soit souvent simplifiée, comprendre leurs mécanismes est essentiel pour produire un code fiable et performant.

#### Comprendre le cycle de vie des effets

Un composant React suit un cycle de vie composé de trois étapes principales : le montage, la mise à jour et le démontage. Cependant, le cycle de vie des effets diffère. Chaque effet est conçu pour démarrer une synchronisation, comme se connecter à une source de données, et, si nécessaire, arrêter cette synchronisation, par exemple se déconnecter. Ces cycles peuvent se produire plusieurs fois pour un même composant.

```jsx
import { useEffect } from 'react';

function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection('https://localhost:1234', roomId);
    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, [roomId]);

  return <h1>Bienvenue dans le salon {roomId} !</h1>;
}
```

Dans cet exemple, lors du montage, l'effet établit une connexion au salon de discussion spécifié. Si `roomId` change, la fonction de nettoyage est appelée pour déconnecter l'ancien salon avant de connecter le nouveau. Lors du démontage, la déconnexion finale est effectuée.

#### Dépendances des effets

Les dépendances d'un effet déterminent quand il doit être réexécuté. Elles incluent toutes les valeurs réactives, comme les props, états ou variables calculées pendant le rendu, que l'effet utilise.

```jsx
import { useState, useEffect } from 'react';

function DataFetcher({ query }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let isActive = true;

    fetchData(query).then(result => {
      if (isActive) {
        setData(result);
      }
    });

    return () => {
      isActive = false;
    };
  }, [query]);

  return <div>{data ? JSON.stringify(data) : 'Chargement...'}</div>;
}
```

Cet effet se resynchronise chaque fois que `query` change. La fonction de nettoyage garantit que les réponses réseau obsolètes n'affectent pas l'état.

#### Tableau de dépendances vide

Un tableau de dépendances vide indique que l'effet ne dépend d'aucune valeur réactive et ne s'exécute qu'une seule fois : au montage.

```jsx
useEffect(() => {
  console.log('Le composant est monté.');

  return () => {
    console.log('Le composant est démonté.');
  };
}, []);
```

Cet effet se limite aux événements du montage et du démontage, car aucune dépendance n'est fournie.

#### Nettoyage des effets

Les fonctions de nettoyage sont essentielles pour éviter des comportements indésirables, comme les fuites de mémoire. Elles permettent d'annuler ou de désactiver ce que l'effet a initié.

```jsx
import { useEffect } from 'react';

function EventListenerExample() {
  useEffect(() => {
    const handleResize = () => console.log('Fenêtre redimensionnée');
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return <p>Redimensionnez la fenêtre pour voir un effet.</p>;
}
```

Dans cet exemple, l'événement `resize` est écouté au montage. La fonction de nettoyage désactive cet événement au démontage.

#### Pièges et bonnes pratiques

Il est essentiel de suivre des règles strictes pour garantir la fiabilité des effets. Éviter les dépendances manquantes est crucial, car toutes les valeurs réactives utilisées dans un effet doivent être listées comme dépendances. Le linter React vous aidera à identifier les oublis. De plus, modifier une dépendance utilisée dans l'effet peut entraîner une boucle infinie. Il est donc conseillé d’examiner si une logique plus simple pourrait remplacer l'effet. Enfin, chaque effet doit représenter un processus de synchronisation distinct pour assurer une clarté maximale.

```jsx
function ChatRoom({ roomId }) {
  useEffect(() => {
    logVisit(roomId);
  }, [roomId]);

  useEffect(() => {
    const connection = createConnection('https://localhost:1234', roomId);
    connection.connect();

    return () => connection.disconnect();
  }, [roomId]);
}
```

Dans cet exemple, les processus de journalisation et de connexion sont séparés en deux effets distincts.

#### Cas avancés : réagir à des changements complexes

Lorsque des dépendances sont calculées, elles doivent être incluses dans le tableau des dépendances.

```jsx
function ChatRoom({ roomId, selectedServerUrl }) {
  const settings = useContext(SettingsContext);
  const serverUrl = selectedServerUrl || settings.defaultServerUrl;

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();

    return () => connection.disconnect();
  }, [serverUrl, roomId]);
}
```

Dans ce cas, `serverUrl` est calculée mais réactive, car elle dépend de `selectedServerUrl` et des `settings`. Elle doit donc figurer dans les dépendances.

#### Conclusion

Les effets lifecycle sont un outil puissant pour gérer des interactions complexes avec des systèmes externes. En maîtrisant leurs dépendances et leur cycle de vie, il est possible de garantir des composants React robustes et performants. Chaque effet doit être autonome, bien nettoyé et utilisé uniquement lorsque cela est nécessaire.