## Gestion des Listes

Pour afficher des composants similaires à partir d'une liste, il est fréquent d'utiliser les méthodes des tableaux provenant de JavaScript pour manipuler ces données. Dans React, des méthodes comme `map()` et `filter()` permettent de transformer et de filtrer les tableaux de données afin de générer dynamiquement des listes de composants. Cela permet une gestion efficace et structurée des listes dans l'interface utilisateur.

### Utilisation de `map()` pour générer des listes de composants

La méthode `map()` est couramment utilisée dans React pour transformer un tableau de données en une liste de composants JSX. Elle permet de parcourir chaque élément du tableau et de retourner un nouveau tableau contenant les éléments JSX correspondants.

### Exemple :

```js
const languages = ["Python", "JavaScript", "C++", "C#"];

function LanguageList() {
  return (
    <ul>
      {languages.map((language, index) => (
        <li key={index}>{language}</li>
      ))}
    </ul>
  );
}
```

Dans cet exemple, `map()` parcourt le tableau `languages` et retourne un élément `<li>` pour chaque langage, affiché dans une liste non ordonnée `<ul>`.

### Ajout d'une clé unique avec `key`

Les clés en React servent à identifier de façon unique chaque élément d'une liste pour faciliter son suivi et ses mises à jour. Il existe deux manières courantes de gérer ces clés :

- **Données de base de données** : Utiliser les ID uniques fournis par la base de données.
- **Données locales** : Pour des données locales, il est possible d'utiliser un générateur de clés comme `crypto.randomUUID()` ou une bibliothèque comme `uuid`.

Pour bien comprendre l'utilité des clés, il faut s'imaginer devoir gérer à la main une liste de 10 éléments. Comment faites-vous pour les identifier indépendament les uns des autres ? Le problème est le même pour React : le framework à besoin d'identifiant unique pour différencier les composants entre eux, d'autant plus lorsque le même composant est réutilisé plusieurs fois.

C'est pourquoi les clés doivent être uniques dans une liste et ne pas changer au fil du temps. Elles permettent à React de reconnaître et de suivre chaque élément, garantissant une mise à jour efficace du DOM. Il est donc fortement recommandé d'ajouter une clé `key` unique à chaque élément lors de la génération de listes.

#### Exemple avec une clé unique pour la liste des langages :

```js
const languages = [
  { id: 1, name: "Python", popularity: 90 },
  { id: 2, name: "JavaScript", popularity: 95 },
  { id: 3, name: "C++", popularity: 75 },
  { id: 4, name: "C#", popularity: 80 },
];

export default function LanguageList() {
  const listItems = languages.map(language => (
    <li key={language.id}>
      {language.name}: Popularité {language.popularity}
    </li>
  ));
  return <ul>{listItems}</ul>;
}
```

Dans cet exemple, `language.id` est utilisé comme clé unique, garantissant que chaque élément de la liste est bien différencié.

### Utilisation de `filter()` pour filtrer les données avant affichage

La méthode `filter()` permet de sélectionner des éléments d’un tableau en fonction d’une condition spécifique avant de les transformer en composants. Cette approche est utile pour afficher uniquement certains éléments d’une collection, comme dans cet exemple avec les langages les plus populaires.

### Exemple :

```js
const languages = [
  { id: 1, name: "Python", popularity: 90 },
  { id: 2, name: "JavaScript", popularity: 95 },
  { id: 3, name: "C++", popularity: 75 },
  { id: 4, name: "C#", popularity: 80 },
];

function PopularLanguages() {
  return (
    <ul>
      {languages
        .filter(language => language.popularity >= 85)
        .map(language => (
          <li key={language.id}>{language.name}</li>
        ))}
    </ul>
  );
}
```

Dans cet exemple, `filter()` est utilisé pour sélectionner uniquement les langages dont la popularité est supérieure ou égale à 85, puis `map()` est utilisé pour les afficher. Comme pour les autres exemples, une clé `key` unique est attribuée à chaque élément en utilisant l'identifiant `language.id` pour garantir un rendu optimisé par React.