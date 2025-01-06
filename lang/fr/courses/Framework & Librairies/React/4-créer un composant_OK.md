## Créer un Composant

### Qu'est ce qu'un composant

Un composant React est un bloc indépendant qui représente une partie de l'interface utilisateur, encapsulant la logique et le rendu. Écrit sous forme de fonction ou de classe JavaScript, il renvoie du JSX, une syntaxe similaire à HTML, pour afficher le contenu. Les composants, qu'ils soient de petite taille (comme un bouton) ou plus complexes (comme une page entière), sont réutilisables et peuvent être imbriqués pour créer des interfaces interactives et dynamiques.

React permet ainsi de combiner le balisage avec le CSS et le JavaScript associés pour créer des « composants » personnalisés réutilisables, l'exemple ci-dessous pourrait devenir un composant `<Instructions />` affichable sur chaque page, tout en utilisant les mêmes balises HTML, comme `<div>`, `<h1>`, `<ol>`, `<li>` et `<strong>`.

```html
<!-- Contenu principal classique d'un fichier HTML -->
<div>
    <h1>Instructions</h1>
    <ol> 
        <li>1. Lancer VS Code</li>
        <li>2. Cliquer sur Extensions dans la barre de gauche</li>
        <li>3. Écrire <strong>Prettier</strong> dans le champ</li>
        <li>4. Installer l’extension</li>
    </ol>
</div>
```

Grâce à React, on peut transformer ce code HTML en composant, puis le réutiliser comme bon vous semble dans d'autres. Voici un exemple de composant nommé **Microlead** qui affiche deux autres composants **Instructions** fait à partir du code HTML ci-dessus :


```js
function Instructions() {
  return (
    <div>
        <h2>Instructions</h2>
        <ol> 
            <li>1. Lancer VS Code</li>
            <li>2. Cliquer sur Extensions dans la barre de gauche</li>
            <li>3. Écrire <strong>Prettier</strong> dans le champ</li>
            <li>4. Installer l’extension</li>             
        </ol>
    </div>
  );
}

export default function Microlead() {
  return (
    <section>
      <h1>Microlead cours en ligne</h1>
      <Instructions />
      <Instructions />
    </section>
  );
}
```

Tout comme avec les balises HTML, il est possible de composer, organiser et imbriquer des composants pour construire des pages complètes. On pourrais alors imaginer un composants pour chaque éléments qui composerait la page.

Voici un exemple :

```js
<html>
  <header>
    <Menu />
    <SearchBar />
    <NavBar />
  </header>
  <body>
    <Introduction />
    <Developement />
    <Conclusion />
  </body>
  <footer>
    <Legal />
  </footer>
</html>
```