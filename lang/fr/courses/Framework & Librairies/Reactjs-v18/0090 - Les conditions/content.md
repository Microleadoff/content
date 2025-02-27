## Les conditions en JSX

Dans React, il est fréquent de devoir afficher du contenu différent en fonction de certaines conditions. Pour cela, l'affichage de JSX peut être conditionné en utilisant des syntaxes JavaScript telles que les instructions `if`, ainsi que l'opérateurs `&&` ou encore l'opérateur ternaire `?:`.

Un opérateur ternaire permet de vérifier une condition et d'exécuter une action ou une autre en fonction de cette condition, le tout en une seule ligne. C'est une manière plus rapide et compacte de faire un `if-else`. Si la condition est vraie, il exécute la première instruction, sinon il exécute la seconde. Cela simplifie le code et le rend plus facile à lire notamment dans le JSX.

Voici quelques exemples simples pour illustrer l'utilisation de conditions dans React :

### Utilisation de `?:`

Voici un exemple d'utilisation de l'opérateur ternaire :

```js
function Greeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn ? <h1>Bienvenue</h1> : <h1>Veuillez vous connecter</h1>}
    </div>
  );
}
```
Dans cet exemple, si `isLoggedIn` est vrai, le message "Bienvenue" s'affiche. Si `isLoggedIn` est faux, "Veuillez vous connecter" est renvoyé.

#### Retourner `Null`
Il est également possible de retourner `null` si l'on souhaite n'afficher aucun contenu lorsque la condition est fausse. Par exemple :

```js
function Greeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn ? <h1>Bienvenue</h1> : null}
    </div>
  );
}
```

### Utilisation de l'opérateur `&&`

L'opérateur `&&` permet l'affichage d'un élément uniquement si la condition est vraie.

```js
function Notification({ hasMessages }) {
  return (
    <div>
      {hasMessages && <p>Vous avez de nouveaux messages</p>}
    </div>
  );
}
```

Dans cet exemple, "Vous avez de nouveaux messages" ne s'affiche que si `hasMessages` est vrai.

### Utilisation de `if-else` dans le corps de la fonction
Une condition `if-else` peut également être utilisée de manière plus classique en JSX.

```js
function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <h1>Bienvenue</h1>;
  } else {
    return <h1>Veuillez vous connecter</h1>;
  }
}
```

### Gérer l'affichage conditionnel avec une variable

Il est souvent plus simple et plus compréhensible de recourir à une instruction `if` combinée à une variable. Cela permet d’attribuer du JSX à une variable de manière conditionnelle, tout en améliorant la lisibilité et la maintenabilité du code.

Il est souvent préférable de déclarer une variable avec `let` pour permettre sa modification. Une valeur par défaut correspondant au rendu initial peut lui être attribuée, puis ajustée à l'aide d'une instruction `if` en fonction des conditions à traiter. Cette approche offre une solution claire et flexible pour gérer et organiser des affichages plus complexes.

#### Exemple :

```js
function Greeting({ isLoggedIn }) {
  let message = <h1>Bienvenue, visiteur</h1>;

  if (isLoggedIn) {
    message = <h1>Bienvenue, utilisateur</h1>;
  }

  return <div>{message}</div>;
}
```

Dans cet exemple, la variable `message` est initialisée avec un contenu par défaut (`<h1>Bienvenue, visiteur</h1>`). Si la condition `isLoggedIn` est vraie, la variable est réaffectée avec une autre valeur (`<h1>Bienvenue, utilisateur</h1>`). Cela permet de gérer plus facilement des affichages complexes ou conditionnels sans rendre le code illisible.

Ces différentes techniques permettent de contrôler l'affichage des composants React en fonction de conditions spécifiques.