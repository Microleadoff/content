### Le balisage avec JSX

Un composant React est une fonction JavaScript qui contient du balisage, que React convertit ensuite en HTML pour l’afficher dans le navigateur. Ce balisage est écrit en JSX, une extension de syntaxe qui ressemble à HTML mais applique des règles plus strictes, offrant également la possibilité d’intégrer des données dynamiques directement dans le composant. JSX facilite ainsi la création d’interfaces utilisateur réactives, bien que certains ajustements soient parfois nécessaires pour assurer la compatibilité avec React. Par exemple, copier directement du code HTML dans un composant peut entraîner des erreurs, car JSX diffère légèrement de la syntaxe HTML classique, notamment dans la manière de gérer les attributs et les expressions JavaScript.

#### Exemple :

Ce composant React *Installationstep* utilise JSX pour structurer un titre, une image, et une liste d’instructions. La syntaxe JSX rend le code clair et centralisé en intégrant le balisage HTML et la logique JavaScript. L'attribut *className* est utilisé à la place de *class*, et chaque ```<li>``` est correctement fermé pour respecter la syntaxe JSX.

```js
export default function Installationstep(){
  return (
    <div>
        <h1>étapes de formatage à la sauvegarde</h1>
        <img src="img/LOGO-FINAL-V2.png" alt="logo microlead" classname="logo">
        <ul>
            <li>Dans VS Code aller dans **File** dans le menu en haut à gauche</li>
            <li>Puis dans **Preferences** presque tout en bas de la liste</li>
            <li>Ensuite cliquer sur **settings**</li>
            <li>Dans la barre de recherche, entrer **format on save** puis cochez la première option.</li>
        </ul>
    </div>
  );
}
```

Cette approche rend le code plus intuitif, car la logique et le rendu visuel sont regroupés, ce qui améliore la maintenabilité et la cohérence de l’application.
Par exemple, avec JSX, il est possible d'afficher une liste d'éléments basée sur un tableau dynamique :

```js
const softskills = ['Communication', 'Travail d\'équipe', 'Adaptabilité', 'Résolution de problèmes', 'Gestion du temps'];

function skills() {
    return (
        <ul>
            {softskills.map((skill, index) => (
                <li key={index}>{skill}</li>
            ))}
        </ul>
    );
}
export default skills;
```

### Du HTML au JSX

Pour intégrer du JSX il va donc falloir respecter de nouvelles règles :

1. **Utilisation des balises HTML ou composants React** : JSX utilise des balises similaires à HTML pour structurer les composants. Les balises peuvent être des éléments HTML (comme `<div>`, `<h1>`) ou des composants React crées par l’utilisateur (comme `<Skills />`).

2. **Syntaxe JavaScript entre accolades** : Pour intégrer des expressions JavaScript dans JSX, il suffit d'utiliser des accolades { }, par exemple `{variable}` ou `{function()}`.

3. **Fermeture des balises** : Toutes les balises doivent être fermées, y compris les balises auto-fermantes, comme `<img />`, `<input />`, ou `<br />`.

4. **Attributs avec camelCase** : Les attributs HTML doivent être en camelCase en JSX. Par exemple, `class` devient `className` et `onclick` devient `onClick`.

5. **élément racine** : Chaque composant JSX doit retourner **un seul élément racine**. Si plusieurs éléments sont nécessaires, ils peuvent être englobés dans une balise `<div>`, `<React.Fragment>`, ou des `<>` `</>` vides.

6. **Les chaînes de caractères** : Les guillemets doubles (`" "`) ou simples (`' '`) sont utilisés pour les chaînes de caractères en JSX, et le contenu entre accolades `{ }` est interprété comme une expression JavaScript.

Le **camelCase** est une convention d'écriture qui combine des mots sans espaces, en mettant la première lettre du premier mot en minuscule, et la première lettre de chaque mot suivant en majuscule, comme dans `myVariableName`.