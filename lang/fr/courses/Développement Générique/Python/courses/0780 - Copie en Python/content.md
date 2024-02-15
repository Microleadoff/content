## Réalisation de Copies d'Objets en Python

En Python, la copie d'objets peut être réalisée de manière superficielle ou profonde, en utilisant respectivement les fonctions ```copy``` et ```deepcopy``` du module ```copy```.

## Importation du Module ```copy```

```python
import copy
```
## Copie Superficielle (copy)

### Fonctionnement 

Crée une nouvelle instance de l'objet avec des références identiques aux objets contenus.

### Utilisation

```python
copie_superficielle = copy.copy(objet_original)
```

### Caractéristiques de la Copie Superficielle

Copie l'objet lui-même mais pas les objets imbriqués.
Utile pour les objets sans objets imbriqués complexes.

## Copie Profonde (deepcopy)

### Fonctionnement 

Crée une copie indépendante de l'objet original et de tous les objets imbriqués.

### Utilisation

```python
copie_profonde = copy.deepcopy(objet_original)
```

### Caractéristiques de la Copie Profonde

Copie l'objet ainsi que tous les objets qu'il référence.
Nécessaire pour les objets qui contiennent d'autres objets, comme des listes ou des dictionnaires.

## Exemples

### Exemple de Copie Superficielle

```python
liste_originale = [1, 2, [3, 4]]
liste_copie = copy.copy(liste_originale)
```
Modifier liste_originale[2][0] affectera aussi liste_copie.

### Exemple de Copie Profonde

```python
liste_originale = [1, 2, [3, 4]]
liste_copie = copy.deepcopy(liste_originale)
```
Modifier liste_originale[2][0] n'affectera pas liste_copie.

## Bonnes Pratiques

**Choix du Type de Copie** : Utilisez deepcopy pour les objets complexes avec des objets imbriqués et copy pour les objets simples.
**Attention aux Références Circulaires** : Faites attention lors de l'utilisation de deepcopy sur des objets avec des références circulaires, car cela peut entraîner des appels récursifs infinis.
**Performances** : Soyez conscient des implications sur les performances lors de l'utilisation de deepcopy sur de grands objets.