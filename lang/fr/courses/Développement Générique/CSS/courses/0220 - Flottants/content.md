**Attention** : L'utilisation du ```float``` n'est pas recommandé. Il s'agit d'une ancienne pratique et ce cours à pour vocation de vous l'expliquer de telle sorte à ce que vous puissiez comprendre ou modifier un ancien code. Évitez de l'utiliser sur de nouveaux projets 👍 !

La propriété CSS ```float``` définit la manière dont un élément HTML doit “flotter”. En d’autres termes, cette propriété permet de sortir un élément du flux normal de la page et de le placer du côté gauche ou droit de son conteneur. Les éléments de type inline entourent alors l’élément flottant.

La propriété CSS ```clear``` définit quel élément peut flotter à côté des éléments ```clear``` et de quel côté.

## La propriété float

La propriété ```float``` est utilisée pour positionner et formater du contenu, par exemple pour faire flotter une image autour d’un texte dans un contenant.

Cette propriété peut recevoir une des 4 valeurs suivantes :

- ```left``` : L’élément flotte à gauche dans son contenant.
- ```right``` : L’élément flotte à droite dans son contenant. 
- ```none``` : Valeur par défaut. L’élément ne flotte pas et apparaît là où il est inséré.
- ```inherit``` : L’élément hérite de la valeur float de l’élément parent.

__Remarque__ : Float implique que les éléments qui doivent flotter soient dans une disposition block. La propriété ```float``` modifie donc la valeur de ```display``` :

- ```display: inline;``` : est transformé en ```display: block;``` par la propriété float
- ```display: inline-block;``` est transformé en ```display: block;```.

De manière générale, la propriété ```float``` est utilisée pour entourer une image avec du texte.

Exemple :

```css
img.illustration {
	float: left;/* L'élément flotte à gauche dans son contenant */
}

img.legende {
	float: right; /* L'élément flotte à gauche dans son contenant */
}

img {
	float : none; /* L'élément ne flotte pas. Il apparaît là où il est positionné dans le code HTML */
}
```

## La propriété clear

La propriété CSS ```clear``` (*dégager*, en anglais) est utilisée afin de définir quel élément HTML peut flotter à côté de l’élément dégagé, et de quel côté il peut flotter. 

Cette propriété reçoit une des 5 valeurs suivantes :

- ```none``` : Valeur par défaut. Autorise les éléments à flotter des deux côtés
- ```left``` : Aucun élément ne peut flotter à gauche
- ```right``` : Aucun élément ne peut flotter à droite
- ```both``` : Aucun élément ne peut flotter **ni à gauche, ni à droite**
- ```inherit``` : L’élément hérite de la valeur ```clear``` de l’élément parent

De manière générale, la propriété ```clear``` est utilisée après avoir utilisé ```float``` sur un élément. 

Lorsque des ```float``` sont dégagés, il faut utiliser la propriété ```clear``` **du même côté** que le ```float```. Si un élément flotte à gauche, ```clear``` doit être à **gauche** (```clear : left;```).

Exemple :

```css
img {
	clear : left; /* L'élément est dégagé à gauche */
}
```
