## Mise à jour des objets d’état

Dans React, l’état d’un composant est souvent structuré sous forme d’objets lorsque les données sont complexes ou comprennent plusieurs propriétés interdépendantes. Cependant, contrairement aux types primitifs, les objets nécessitent une manipulation prudente pour que React détecte et applique correctement les mises à jour. Ce cours présente les bonnes pratiques pour gérer et mettre à jour les objets d’état, en assurant l’**immutabilité** et la réactivité de l’application.

### Comprendre les objets d’état

L’état d’un composant peut contenir des objets pour structurer logiquement les informations. Par exemple, dans un formulaire, il est courant d’utiliser un objet pour regrouper les valeurs des différents champs :

```javascript
const [userData, setUserData] = useState({
  name: '',
  email: '',
  age: null,
});
```

Dans cet état `userData`, les informations utilisateur sont regroupées en un seul objet. Lors des mises à jour, il est important de modifier chaque propriété sans affecter les autres pour éviter la perte de données.

### L'importance de l'immutabilité

En JavaScript, les objets sont **mutables**, ce qui signifie qu'ils peuvent être modifiés après leur création. Dans React, il est essentiel de **ne pas modifier directement l'état**, car cela peut entraîner des comportements inattendus. React s'appuie sur l'immutabilité pour détecter les changements d'état. Si un objet est modifié directement, React peut ne pas détecter le changement et le composant risque de ne pas se mettre à jour.

### Mise à jour partielle avec la syntaxe de copie

Pour mettre à jour l'état de manière sûre, il est recommandé de créer une **nouvelle copie de l'objet** en utilisant l'opérateur de décomposition (`...`), puis d’appliquer les modifications souhaitées :

```javascript
setUserData((prevData) => ({
  ...prevData,
  email: 'nouvel_email@example.com',
}));
```

Dans cet exemple :
- `...prevData` crée une copie de l'état précédent.
- Seule la propriété `email` est modifiée, tandis que les autres propriétés (`name` et `age`) restent inchangées.

### Pourquoi créer des copies d’état ?

Créer une nouvelle copie de l'état présente plusieurs avantages :
- **Préserver l'immutabilité** : Éviter les mutations directes de l'état prévient des bugs difficiles à diagnostiquer.
- **Permettre la détection des changements** : En remplaçant l'ancien objet par un nouveau, React détecte le changement et déclenche un **rerendering** du composant.
- **Assurer la cohérence des données** : Cette méthode prévient les effets de bord liés à la modification d'objets partagés ou référencés ailleurs.

### Exemple : gestion d’un formulaire

Dans un formulaire à plusieurs champs, un objet d’état permet de regrouper les valeurs et de mettre à jour chaque champ indépendamment des autres :

```javascript
import React, { useState } from 'react';

function UserProfileForm() {
  const [user, setUser] = useState({
    name: '',
    email: '',
    phone: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser((prevUser) => ({
      ...prevUser,
      [name]: value, // Met à jour uniquement le champ modifié
    }));
  };

  return (
    <form>
      <input
        type="text"
        name="name"
        value={user.name}
        onChange={handleChange}
      />
      <input
        type="email"
        name="email"
        value={user.email}
        onChange={handleChange}
      />
      <input
        type="tel"
        name="phone"
        value={user.phone}
        onChange={handleChange}
      />
    </form>
  );
}
```

Dans cet exemple :
- Chaque champ de formulaire met à jour la propriété correspondante de l'objet `user` sans affecter les autres.
- `handleChange` utilise la propriété `name` pour cibler la bonne clé dans l'objet.
- L’opérateur `...prevUser` permet de créer une copie de l'état précédent.

### Gestion des objets imbriqués

Lorsque l'état contient des objets imbriqués, chaque niveau d'imbrication doit être copié pour préserver l'immutabilité.

**Exemple :**

```javascript
const [user, setUser] = useState({
  name: 'Alice',
  address: {
    city: 'Paris',
    zipCode: '75000',
  },
});

const handleCityChange = (e) => {
  const newCity = e.target.value;
  setUser((prevUser) => ({
    ...prevUser,
    address: {
      ...prevUser.address,
      city: newCity,
    },
  }));
};
```

Ici :
- La propriété `user.address.city` est mise à jour sans modifier directement l'objet imbriqué.
- Une copie de `address` est créée pour maintenir l’immutabilité.

### Attention aux mutations directes

Modifier l'état directement peut causer des erreurs difficiles à diagnostiquer. Voici un exemple à **éviter** :

```javascript
// Mauvaise pratique 
userData.email = 'nouvel_email@example.com';
setUserData(userData);
```

Dans ce cas :
- `userData` est modifié directement.
- React peut ne pas détecter le changement, car la référence de l'objet n'a pas changé.

### Utilisation de bibliothèques pour simplifier la gestion de l'état

Pour des structures d'état complexes avec des objets profondément imbriqués, des bibliothèques comme **immer** facilitent la gestion de l'immutabilité.

#### Exemple avec immer :

```javascript
import produce from 'immer';

const handleCityChange = (e) => {
  const newCity = e.target.value;
  setUser(
    produce((draft) => {
      draft.address.city = newCity;
    })
  );
};
```

Avec **immer** :
- **`produce` d'immer** : La fonction `produce` accepte l’état initial, géré implicitement, et une fonction de mise à jour qui modifie un **draft**, une version temporaire de l’état.
- **Application des changements** : Les modifications se font sur le draft sans toucher l’état d’origine. Immer génère ensuite une version immuable de l’état, déclenchant un rerendering sans copier manuellement les niveaux imbriqués.
