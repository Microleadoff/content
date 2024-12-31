## Les props

Les composants React utilisent les **props** ou **properties** pour échanger des informations entre eux. Un composant parent transmet des données à ses composants enfants en leur assignant des props. Les props permettent de passer n’importe quelle valeur JavaScript, y compris des objets, des tableaux ou des fonctions, offrant ainsi une grande flexibilité dans la gestion des données. Elles permettent d’adapter le comportement ou l'affichage du composant enfant en fonction des données reçues. En résumé, une prop sert à personnaliser et à dynamiser un composant en lui fournissant des valeurs ou des fonctions.

#### Exemple
Dans l'exemple ci-dessous, la balise `<StudentCard />` représente un composant qui reçoit plusieurs props : `name`, `age`, `isLoggedIn`, `profilePicture`, et `handleClick`. Ces props permettent de transmettre des informations et des comportements spécifiques au composant `StudentCard`.

```js
function StudentProfile() {
  return (
    <StudentCard
      name="John Doe"
      age={19}
      isLoggedIn={true}
      profilePicture="img/LOGO-FINAL-V2.png"
      handleClick={() => alert('Profile clicked!')}
    />
  );
}
```

### De props à composant

Les props permettent de traiter les composants parent et enfant de manière indépendante. Par exemple, il est possible de modifier les props `name` et `age` dans `StudentProfile` sans se soucier de la manière dont `StudentCard` les utilise. De même, l'utilisation de ces props à l'intérieur de `StudentCard` peut être ajustée sans impacter le composant parent `StudentProfile`.

Voici un exemple d'utilisation de props :

```js
function StudentProfile() {
  return (
    <StudentCard
      name="John Doe"
      age={19}
      isLoggedIn={true}
      profilePicture="img/LOGO-FINAL-V2.png"
      handleClick={() => alert('Profile clicked!')}
    />
  );
}

function StudentCard({ name, age, isLoggedIn, profilePicture, handleClick }) {
  return (
    <div onClick={handleClick}>
      <img src={profilePicture} alt={`${name}'s profile`} />
      <h2>{name}</h2>
      <p>Age: {age}</p>
      {isLoggedIn && <p>Status: Logged In</p>}
    </div>
  );
}
```

Dans cet exemple, le composant `StudentProfile` transmet les props (`name`, `age`, `isLoggedIn`, `profilePicture`, `handleClick`) à `StudentCard`, qui les utilise ensuite pour afficher les informations du profil de l'étudiant. La prop `handleClick` est utilisée pour déclencher un message lorsque le profil est cliqué.

Il est également possible de transmettre une valeur par défaut lorsque le prop du composant parent ne contient pas de valeur, par exemple :

```js
function StudentCard({ name, age='21', isLoggedIn, profilePicture, handleClick }) {
    return();
}
```

Les props représentent l’état des données d’un composant à un moment donné, et non uniquement lors de l’initialisation. Elles sont immuables, c’est-à-dire qu'elles ne peuvent pas être modifiées directement. Si un composant doit ajuster ses props en réponse à une interaction utilisateur ou à l'arrivée de nouvelles informations, il doit demander à son parent de lui fournir des props différentes, ce qui créera un nouvel objet. Les anciennes props seront alors supprimées.

Il est donc essentiel de ne pas modifier directement les props. Pour répondre à une interaction, comme changer une couleur sélectionnée, il est nécessaire de mettre à jour l'état `(state)` du composant plutôt que ses props.

### Spreading

Afin d'éviter de rappeler chaque prop individuellement dans le composant, l'utilisation du spreading est possible. Cette technique permet de décomposer un objet ou un tableau pour en extraire ses éléments ou propriétés. Dans le contexte de React, elle est souvent employée pour passer facilement toutes les props d'un composant parent à un composant enfant, sans avoir à les énumérer individuellement.

#### Exemple
```js
const studentInfo = {
  name: "John Doe",
  age: 19,
  isLoggedIn: true,
  profilePicture: "image",
};

function StudentProfile() {
  return (
    <StudentCard {...studentInfo} />
  );
}
```

Dans cet exemple, la syntaxe `...studentInfo` décompose l’objet `studentInfo` et passe chaque propriété comme prop au composant `StudentCard`. Cela permet d’éviter de devoir écrire chaque prop séparément, comme `name={studentInfo.name}`, `age={studentInfo.age}`, etc.

La syntaxe spread rend le code plus concis et pratique, surtout lorsqu'il y a de nombreuses props à transmettre.

### Utilisation de JSX comme contenu enfant

L'utilisation de JSX en tant qu'enfant consiste à placer du contenu JSX entre les balises d'un composant, de la même manière que pour des éléments HTML. Ce contenu est ensuite récupéré via la prop `children` dans le composant, ce qui permet de rendre les éléments enfants dynamiques à l'intérieur du composant parent.

### Exemple :

```js
function Container({ children }) {
  return <div className="container">{children}</div>;
}

export default function App() {
  return (
    <Container>
      <h1>Bienvenue</h1>
      <p>Ceci est un exemple d'utilisation de JSX comme enfant.</p>
    </Container>
  );
}
```

Dans cet exemple, le composant `Container` reçoit du JSX (`<h1>` et `<p>`) comme enfants via la prop `children`. Cela permet au composant parent (`App`) de contrôler ce qui est affiché à l'intérieur du composant enfant (`Container`), offrant ainsi une grande flexibilité dans la composition d’interfaces.
