La fonction JavaScript ```fetch()``` permet d'exécuter des requêtes HTTP de manière asynchrone. C'est le genre de fonction que l'on utilise pour charger différentes données dans un site internet sans avoir besoin de recharger une page.

La fonction ```fetch()``` à fait suite à l'utilisation de la fonction ```ajax()``` et la remplace très largement aujourd'hui. 

Notez que comme toute requête HTTP, vous pouvez récupérer des informations depuis internet via une url, mais vous pouvez également récupérer des informations en local depuis un fichier sur votre machine !

## Exemples

Vous pouvez utiliser la fonction fetch simplement en enchaînant de manière "synchrone" les actions à réaliser à l'issue de la récupération des informations grâce à l'utilisation du mot-clé ```then```.

```js
fetch(url)
.then(x => x.text())
.then(y => console.log(y))
```

Ou alors vous pouvez utiliser une fonction asynchrone classique en combinant les mots-clés ```async``` et ```await```.

```js
async function getText(url) {
    let x = await fetch(url);
    let y = await x.text();
    document.querySelector("#example").innerHTML = y;
}
```

