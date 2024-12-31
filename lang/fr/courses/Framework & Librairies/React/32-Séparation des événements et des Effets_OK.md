## La séparation des événements et des effets

Dans une application React, il est crucial de distinguer les **gestionnaires d'événements** des **effets**. Ces deux concepts remplissent des fonctions complémentaires mais différentes : les événements gèrent les interactions directes avec l'utilisateur, tandis que les effets synchronisent un composant avec des systèmes ou données externes. Une séparation claire entre ces deux approches permet de structurer un code lisible, maintenable et performant.

### Différence fondamentale entre événements et effets

#### Les gestionnaires d’événements
Un **événement** correspond à une action déclenchée explicitement par l'utilisateur, comme un clic, une saisie ou un survol. La logique associée à ces événements doit rester immédiate et découplée des changements réactifs automatiques.

**Exemple : Envoi d’un message**
```jsx
function ChatInput() {
  const [message, setMessage] = useState('');

  function handleSendMessage() {
    sendMessageToServer(message); // Envoi explicite
    setMessage(''); // Réinitialisation locale
  }

  return (
    <>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>Envoyer</button>
    </>
  );
}
```
Dans cet exemple, l'envoi d'un message est déclenché uniquement lorsque l'utilisateur clique sur le bouton "Envoyer". Ce comportement est entièrement contrôlé par l'utilisateur.

#### Les effets
Un **effet** gère des tâches asynchrones ou des interactions avec des systèmes externes, comme les appels API, les abonnements à des événements globaux ou les mises à jour DOM. Les effets sont déclenchés automatiquement en réponse à des changements dans les valeurs réactives surveillées (props, state).

**Exemple : Gestion de la connexion à un serveur**
```jsx
function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = connectToRoom(roomId); // Synchronisation automatique
    return () => connection.disconnect(); // Nettoyage lors du démontage
  }, [roomId]); // Dépendance à roomId
}
```
Cet effet garantit que la connexion au serveur change automatiquement lorsque `roomId` est modifié.

### Pourquoi séparer les événements des effets ?

Une séparation claire entre les deux concepts améliore la qualité et la maintenabilité du code :
- **Clarté et modularité** : La logique utilisateur et la synchronisation extérieure sont distinctes, ce qui facilite leur compréhension et leur test.
- **Évitement des dépendances inutiles** : Les effets ne se déclenchent que lorsque les valeurs surveillées changent.
- **Prévention des erreurs** : Mélanger les deux peut entraîner des boucles infinies ou des comportements imprévisibles.

### Structuration du code : exemples pratiques

#### Cas 1 : Interaction utilisateur et synchronisation API
Imaginez une application où l'utilisateur sélectionne un salon de discussion. Lorsqu’un salon est sélectionné, une connexion doit être établie avec le serveur.

**Mauvaise pratique : mélange des logiques**
```jsx
function ChatApp() {
  const [roomId, setRoomId] = useState(null);

  useEffect(() => {
    if (roomId) {
      sendRoomSelectionToServer(roomId);
      const connection = connectToRoom(roomId);
      return () => connection.disconnect();
    }
  }, [roomId]);

  return <button onClick={() => setRoomId('123')}>Rejoindre le salon 123</button>;
}
```
**Problèmes :**
- `sendRoomSelectionToServer` est exécuté automatiquement à chaque changement, même si l'utilisateur n'a pas explicitement validé son choix.
- La logique utilisateur et la logique de synchronisation sont imbriquées.

**Bonne pratique : séparation des responsabilités**
```jsx
function ChatApp() {
  const [roomId, setRoomId] = useState(null);

  function handleJoinRoom() {
    sendRoomSelectionToServer('123'); // Action utilisateur explicite
    setRoomId('123'); // Mise à jour locale
  }

  useEffect(() => {
    if (!roomId) return;

    const connection = connectToRoom(roomId); // Synchronisation automatique
    return () => connection.disconnect(); // Nettoyage
  }, [roomId]);

  return <button onClick={handleJoinRoom}>Rejoindre le salon 123</button>;
}
```
**Avantages :**
- La logique utilisateur (`handleJoinRoom`) est découplée de la logique réactive (`useEffect`).
- L'effet gère uniquement la synchronisation en fonction de `roomId`.

#### Cas 2 : Extraction des dépendances inutiles
Dans certaines situations, des dépendances inutiles peuvent provoquer des exécutions répétées d’un effet. Cela peut être évité en extrayant la logique non réactive.

**Exemple : notification lors de la connexion**
```jsx
function ChatRoom({ roomId, theme }) {
  const notifyConnection = useCallback(() => {
    showNotification('Connexion réussie', theme); // Notification avec le thème
  }, [theme]);

  useEffect(() => {
    const connection = connectToRoom(roomId);
    connection.on('connected', notifyConnection);
    return () => connection.disconnect();
  }, [roomId]);
}
```
**Avantages :**
- `notifyConnection` est stabilisé avec `useCallback`, évitant des reconnexions inutiles lorsque `theme` change.
- L'effet reste focalisé sur la gestion de `roomId`.

### Erreurs courantes à éviter

1. **Mélanger logique événementielle et réactive**
   Évitez d’inclure des actions utilisateur explicites (comme des clics) dans un effet.

2. **Ignorer le nettoyage des effets**
   Assurez-vous de nettoyer les abonnements ou connexions établis dans un effet pour éviter des comportements indésirables lors du démontage du composant.

3. **Créer des dépendances inutiles**
   Analysez les dépendances de chaque effet pour éviter des exécutions non nécessaires.

### Résumé et bonnes pratiques

- Les **événements** gèrent les interactions explicites de l'utilisateur. Utilisez des fonctions comme `onClick` pour encapsuler cette logique.
- Les **effets** synchronisent les composants avec des systèmes externes ou des changements de valeur réactive. Utilisez `useEffect` pour cette tâche.
- Séparez toujours la logique utilisateur de la logique réactive.
- Stabilisez les fonctions ou extrayez les dépendances inutiles à l'aide de `useCallback` ou de gestionnaires dédiés.

En suivant ces principes, vous pouvez construire des composants React robustes, lisibles et faciles à maintenir.