## Gérer les données grâce au context

Dans React, le **context** offre un moyen efficace de partager des données entre plusieurs composants sans avoir à transmettre des props à chaque niveau de l’arborescence. Cette méthode simplifie la gestion des données globales, telles que les thèmes ou les informations utilisateur, tout en améliorant la lisibilité et la maintenabilité du code.

### Qu’est-ce que le context ?

Le **context** permet à un composant parent de rendre certaines données accessibles à tous ses descendants, indépendamment de leur position dans l’arborescence. Contrairement aux props, les données partagées via le context peuvent être récupérées directement par les composants concernés, évitant ainsi le « prop drilling » (passage répétitif de données à travers des composants intermédiaires inutiles).

#### Exemples d’utilisation fréquents :
- Gestion de thèmes (clair/sombre).
- Informations sur l’utilisateur (authentification, rôle).
- Paramètres globaux (langue, préférences).

### Pourquoi utiliser le context ?

- **Simplification des flux de données** : Réduit la transmission de props inutiles.
- **Centralisation des états globaux** : Garantit un point unique de gestion des données partagées.
- **Réutilisabilité** : Permet aux composants distants d’accéder directement aux mêmes informations.

Bien que puissant, le context doit être utilisé avec modération. Son utilisation excessive ou mal planifiée peut compliquer la maintenance, notamment lorsque plusieurs contextes sont imbriqués.

### Mise en place du context

#### Créer un contexte

Un contexte est défini à l’aide de `React.createContext`. Cela initialise un espace pour partager des données.

```javascript
import { createContext } from 'react';

export const ThemeContext = createContext('light');
```

Dans cet exemple, la valeur par défaut est `'light'`, utilisée si aucun provider explicite n’est défini.

#### Fournir des données avec un provider

Le **provider** est un composant qui enveloppe les parties de l’application devant accéder au contexte. Il fournit les données via sa prop `value`.

```javascript
import React, { useState } from 'react';
import { ThemeContext } from './ThemeContext';

export default function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  function toggleTheme() {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'));
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

#### Consommer le contexte avec `useContext`

Les composants enfants accèdent aux données partagées via le Hook `useContext`.

```javascript
import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

export default function ThemeSwitcher() {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <div>
      <p>Thème actuel : {theme}</p>
      <button onClick={toggleTheme}>Changer de thème</button>
    </div>
  );
}
```

### Exemple complet : gestion d’un thème

Voici une application complète utilisant le contexte pour gérer un thème clair/sombre :

```javascript
import React from 'react';
import ThemeProvider from './ThemeProvider';
import ThemeSwitcher from './ThemeSwitcher';

export default function App() {
  return (
    <ThemeProvider>
      <div>
        <h1>Gestion du thème</h1>
        <ThemeSwitcher />
      </div>
    </ThemeProvider>
  );
}
```

Le provider entoure l’ensemble de l’application, rendant les données `theme` et `toggleTheme` accessibles à tous les composants enfants.

### Avantages et inconvénients du context

#### Avantages
1. **Réduction du prop drilling** : Les composants intermédiaires n’ont plus à transmettre inutilement des données.
2. **Centralisation des données globales** : Améliore la gestion et la cohérence des états globaux.
3. **Aucune dépendance externe** : Solution native à React.

#### Inconvénients
1. **Impact sur les performances** : Une mise à jour du contexte peut provoquer le rerendering de tous les composants qui y accèdent, même si certains n’ont pas besoin des nouvelles données.
2. **Complexité accrue** : Des contextes imbriqués peuvent devenir difficiles à gérer.
3. **Relations implicites** : Les flux de données deviennent moins évidents, compliquant parfois le débogage.

### Bonnes pratiques

1. **Limiter la portée du provider** : Ne pas envelopper l’ensemble de l’application si seuls quelques composants utilisent le contexte.
2. **Utiliser plusieurs contextes si nécessaire** : Préférez diviser les responsabilités (par exemple, un contexte pour le thème et un autre pour les préférences utilisateur) afin d’éviter des rerenderings inutiles.
3. **Préférer les props pour des cas simples** : Réservez le contexte aux données réellement globales.

### Alternatives au context

- **Props** : Idéal pour transmettre des données localisées et simples.
- **State global (Redux ou Zustand)** : Recommandé pour des applications complexes nécessitant une gestion centralisée et extensible des données.

### Conclusion

Le context est une solution native et puissante pour simplifier la gestion des données partagées dans React. Bien qu’il élimine le prop drilling et centralise les données globales, il doit être utilisé avec précaution pour éviter les problèmes de performances et de maintenance. En suivant les bonnes pratiques, le context améliore la lisibilité et la robustesse des applications tout en garantissant une meilleure expérience de développement.