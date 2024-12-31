## Partage du state entre plusieurs composants

Le partage du state est une pratique essentielle pour coordonner les interactions entre différents composants React. Lorsque plusieurs composants dépendent des mêmes données, il est crucial de structurer et de centraliser le state afin de garantir une logique claire et une interface cohérente. Ce cours explore les différentes méthodes pour partager efficacement le state tout en évitant les pièges courants.

### Comprendre le partage du state

Dans une application React, chaque élément d’état doit avoir une **source de vérité unique**. Cela signifie qu’un composant est responsable de la gestion d’un état particulier. Lorsque plusieurs composants nécessitent un accès ou une mise à jour synchronisée de cet état, il devient nécessaire de partager cet état entre eux.

Le partage du state repose sur deux concepts clés :
1. **Lever le state** : Déplacer l’état dans un composant parent commun pour coordonner les composants enfants.
2. **Propagation descendante** : Distribuer le state centralisé via des props aux composants qui en ont besoin.

### Comparatif des méthodes de partage du state

#### Lever le state

Cette méthode est idéale lorsque des composants proches dans l’arborescence doivent partager un état commun. L’état est déplacé dans un parent commun, qui le gère et le transmet aux enfants via des props. Cela offre une solution claire et explicite, bien adaptée aux scénarios simples. Cependant, cette approche peut entraîner un passage excessif de props ("prop drilling") dans des structures plus complexes ou profondes.

#### Utiliser le contexte

Le contexte est particulièrement utile lorsque des données doivent être accessibles dans plusieurs parties éloignées de l’arborescence. Plutôt que de transmettre manuellement des props à chaque niveau intermédiaire, le contexte fournit un mécanisme pour partager le state directement avec les composants enfants. Cela simplifie la structure, mais peut parfois rendre les relations entre composants moins explicites, compliquant le débogage.

#### État global (ex. Redux ou Zustand)

Pour les applications complexes, où de nombreux états doivent être accessibles globalement ou interconnectés, des outils comme Redux ou Zustand permettent une gestion centralisée. Ces solutions sont extensibles et maintenables, même dans de grands projets, mais nécessitent une configuration initiale plus complexe. Elles sont particulièrement adaptées pour des applications à grande échelle, comme les boutiques en ligne ou les tableaux de bord complexes.

### Lever le state : une solution locale

Lever le state signifie déplacer un état local vers un composant parent commun afin de coordonner plusieurs composants enfants. Cette méthode est idéale lorsque les composants à synchroniser sont proches dans la hiérarchie.

#### Exemple : synchronisation entre un champ de saisie et son affichage

Dans cet exemple, un composant parent coordonne un champ de texte et une zone d’affichage.

```javascript
import React, { useState } from 'react';

function ParentComponent() {
  const [text, setText] = useState('');

  function handleChange(e) {
    setText(e.target.value);
  }

  return (
    <div>
      <InputField value={text} onChange={handleChange} />
      <TextDisplay value={text} />
    </div>
  );
}

function InputField({ value, onChange }) {
  return <input type="text" value={value} onChange={onChange} />;
}

function TextDisplay({ value }) {
  return <p>Texte entré : {value}</p>;
}
```

**Explication :**
- Le composant parent `ParentComponent` gère le state `text`.
- Les composants enfants `InputField` et `TextDisplay` accèdent à ce state via des props.
- Le levage de l’état garantit que les deux composants restent synchronisés.

### Partage global avec le contexte

Lorsque plusieurs composants distants nécessitent un état commun, utiliser un **contexte React** est une solution plus efficace. Cela permet de partager l’état sans avoir à transmettre les props à chaque niveau intermédiaire.

#### Exemple : gestion d’un thème dans une application

```javascript
import React, { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Header />
      <Content />
    </ThemeContext.Provider>
  );
}

function Header() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <header>
      <p>Thème actuel : {theme}</p>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Basculer le thème
      </button>
    </header>
  );
}

function Content() {
  const { theme } = useContext(ThemeContext);

  return (
    <main style={{ backgroundColor: theme === 'light' ? '#fff' : '#333', color: theme === 'light' ? '#000' : '#fff' }}>
      <p>Contenu principal</p>
    </main>
  );
}
```

**Explication :**
- `ThemeContext` centralise l’état du thème.
- Tous les composants descendants (comme `Header` et `Content`) peuvent accéder directement aux données partagées via `useContext`.

### État global : une approche centralisée

Pour les applications complexes avec des états nombreux et interconnectés, des solutions comme **Redux** ou **Zustand** offrent une gestion centralisée. Ces outils permettent de stocker et manipuler tous les états de l’application dans un seul endroit, ce qui facilite la scalabilité.

#### Cas d’utilisation typique :
Une boutique en ligne où le panier, les préférences utilisateur et les produits affichés doivent être partagés entre différents composants.

### Conclusion

Le partage du state est essentiel pour concevoir des applications React robustes et cohérentes. Selon le contexte, lever l’état, utiliser un contexte ou opter pour un état global sont des solutions adaptées. En choisissant la méthode la plus appropriée, il est possible de maintenir une logique claire tout en simplifiant la gestion des interactions.
