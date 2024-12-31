### JavaScript avec JSX

JSX permet de regrouper le contenu et la logique d’affichage en un seul endroit. Pour ajouter de la logique JavaScript ou référencer une propriété dynamique dans ce balisage, il suffit d’utiliser des accolades `{ }` pour intégrer du JavaScript directement dans le code JSX.

#### Exemple

```js
const siteIntro = {
  title: "Bienvenue sur Microlead",
  description: "LA FORMATION CONTINUE EN DÉVELOPPEMENT INFORMATIQUE",
  paragraph:
    "Trouvez le parcours personnalisé qui vous correspond le mieux. Exploitez nos ressources pédagogiques qui regroupent des cours, exercices, travaux dirigés, travaux pratiques et QCM pour développer de nouvelles compétences !",
  theme: {
    backgroundColor: "#1a1a1a",
    color: "#FFD1DC",
    padding: "20px",
    textAlign: "center",
  },
};

export default function SiteIntro() {
  return (
    <div style={siteIntro.theme}>
      <h1>{siteIntro.title}</h1>
      <img
        className="intro-image"
        src="img/LOGO-FINAL-V2.png"
        alt="logo Microlead"
        style={{ width: "250px", margin: "25px" }}
      />
      <h3>{siteIntro.description}</h3>
      <p>{siteIntro.paragraph}</p>
    </div>
  );
}
```
### Les accolades , les guillemets et les apostrophes

Comme vu dans le cours précédent JSX répond à des règles bien spécifique en terme de syntaxe , typiquement lorsque vous souhaitez attribuer une valeur textuelle fixe à un attribut en JSX, il suffit de l'entourer de guillemets doubles (`" "`) ou simples (`' '`). Cela permet de définir une chaîne de caractères que le navigateur interprète littéralement. Par exemple, pour définir une image avec un chemin fixe, on écrira : `<img src="path/to/image.jpg" alt='description' />`.

Les accolades `{ }`, sont employées pour insérer des expressions JavaScript. Elles permettent d'intégrer des variables, des fonctions, ou même des objets directement dans le JSX, ajoutant ainsi des données dynamiques. Par exemple, dans `<img src={websiteIntro.imageSrc} />`, les accolades autour de `profileIntro.imageSrc` permettent d'insérer la valeur de cette variable directement dans l’attribut `src`.

#### Exemple

```js
const websiteIntro = {
  imageSrc: "img/LOGO-FINAL-V2.png",
  altText: 'Logo Microlead',
};

export default function ProfilePicture() {
  return (
    <div>
      <img
        className="website-profile"
        src={websiteIntro.imageSrc}
        alt={websiteIntro.altText}
        style={{ width: "150px", margin: "15px" }}
      />
    </div>
  );
}
```

En résumé, `" "` et `' '` sont pour les chaînes fixes, tandis que `{ }` servent à injecter des valeurs ou des expressions dynamiques.

### Les doubles accolades

En JSX, les doubles accolades (`{{ }}`) sont utilisées pour définir des objets au sein des attributs, notamment pour appliquer du style directement sur les éléments. La première paire d’accolades `{ }` indique qu'une expression JavaScript est utilisée, tandis que la seconde paire `{ }` définit l'objet proprement dit.

Par exemple, dans l’attribut `style`, on peut écrire :

```js
<div style={{ color: 'blue', fontSize: '18px' }}>
  Texte en bleu avec une taille de 18px
</div>
```

Ici, la première paire d'accolades permet d'exécuter JavaScript dans JSX, et la deuxième paire définit l'objet de style avec ses propriétés CSS en camelCase. Les doubles accolades sont donc un moyen pratique d’ajouter des styles ou des paramètres dynamiques directement à l’intérieur du balisage JSX.

Voici un exemple de l'intégration d'un objet avec les doubles accolades:

```js
export default function websiteStyle() {
  const webStyle = {
    backgroundColor: 'lightblue',
    border: '2px solid darkblue',
    padding: '20px',
    textAlign: 'center',
  };

  return (
    <div style={webStyle}>
      Ce bloc utilise des styles définis par un objet JavaScript.
    </div>
  );
}
```

Cette approche permet de centraliser les styles et de les réutiliser facilement, tout en appliquant du CSS dynamique en ligne dans le JSX.