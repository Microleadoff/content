
## Importer et exporter des composants

En programmation, il est important de garder les fichiers de code simples et lisibles. Un fichier trop volumineux complique la compréhension du code et sa maintenance. C'est pourquoi on recommande de séparer les éléments en plusieurs fichiers. En JavaScript, vous pouvez créer des fichiers puis les importer dans d'autres fichiers selon les besoins. Cette approche est également utilisée en React, où chaque composant peut être exporté depuis son propre fichier, pour ensuite être réutilisé facilement dans différentes parties de l'application. Cela améliore la lisibilité du code et facilite la réutilisation des composants.

### Partitionner les composants

En React, les différentes parties du code sont séparées en "composants". Aussi en suivant les precepts établis ci-dessus, il convient de séparer autant que possible chaque composant du reste du code. On parlera de **partitionnement**, et on essaiera de faire en sorte que chaque composant dispose de son propre fichier.

Cette approche facilite également la gestion des dépendances, réduit les conflits entre bibliothèques et modules, et optimise la collaboration en équipe en permettant de travailler sur des parties distinctes sans interférences.

Enfin, elle rend le code plus modulaire et testable, chaque fonction étant testée et maintenue de manière indépendante.

Voici un exemple où un composant ```Microlead``` est créé dans un fichier ```./microlead.js``` puis importé dans un autre fichier pour la création d'un autre composant ```Presentation``` :

```js
// Import du composant Microlead
import Microlead from "./microlead.js";

// Création du composant Presentation
export default function Presentation() {
  return (
    <section>
      <h1>Microlead</h1>
      {/* Appel du composant Microlead */}
      <Microlead />
    </section>
  );
}
```

### Organisation

Pour respecter ces principes, il suffit de suivre ces simples étapes pour la création de chaque nouveau composant :

1. Créer un nouveau fichier pour le composant en respectant les conventions de nommage
2. Exporter la fonction composant
3. Puis l'importer dans les fichiers qui utiliseront le composant


Dans JavaScript, il existe deux façons principales d'exporter des éléments depuis un module : les exports **nommés** et les exports **par défaut**.

#### Exports nommés

Les exports nommés permettent d'exporter plusieurs éléments depuis un fichier, chacun étant identifié par un nom spécifique. Lorsque l'on souhaite importer ces éléments dans un autre fichier, il est impératif d'utiliser ces noms exacts. Cela permet de partager plusieurs fonctions ou variables à partir d'un seul fichier. Voici un exemple :

```js
// Hello.js
export function Hello() {
  console.log("Hello!");
}

export function Goodbye() {
  console.log("Goodbye!");
}
```

Dans cet exemple, le fichier ```Hello.js``` exporte deux fonctions distinctes : ```Hello``` et ```Goodbye```.

Lorsqu'on les importe dans un autre fichier, il faut spécifier leurs noms entre accolades :

```js
// main.js
import { Hello, Goodbye } from './Hello';

Hello();    // Affiche "Hello!"
Goodbye();  // Affiche "Goodbye!"
```

#### Exports par défaut

Les **exports par défaut**, quant à eux, permettent d'exporter un seul élément principal par fichier. Contrairement aux exports nommés, l'importation d'un export par défaut ne nécessite pas d'utiliser le nom original de l'élément exporté. Cela offre la flexibilité de renommer cet élément lors de son importation. Par exemple :

```js
// Hello.js
export default function Hello() {
    console.log("Hello!");
}
```

Ici, ```Hello.js``` n'exporte qu'une seule fonction par défaut. Lors de l'importation dans un autre fichier, on peut choisir le nom que l'on veut, ce qui simplifie l'import :

```js
// main.js
import MyFunction from './Hello';

MyFunction(); // Affiche "Hello!"
```

Dans cet exemple, même si la fonction exportée est appelée ```Hello``` dans le fichier d'origine, on peut l'importer sous le nom ```MyFunction```, ou n'importe quel autre nom !

### Composant racine
Le composant racine est le point de départ d'une application dans React. Il s'agit du composant principal, généralement appelé **App.js**, qui englobe tous les autres composants. Le composant racine est rendu directement dans le DOM HTML de la page, souvent à l’intérieur d'un élément comme ```<div id="root">```, et il sert de base pour construire l'ensemble de l'interface en imbriquant et en organisant les composants enfants.

Notez que selon le framework utilisé, il est possible que chaque page ait son propre composant racine !