## Pillow en Python

Pillow est une librairie de traitement d'images pour Python, développée comme une extension de PIL (Python Imaging Library). Elle permet d'ouvrir, de manipuler et d'enregistrer des images dans divers formats.

## Installation de Pillow
```shell
pip install pillow
```
## Fonctionnalités Clés de Pillow

**Lecture et Écriture d'Images** : Prise en charge de nombreux formats d'images.
**Manipulation d'Images** : Redimensionnement, rotation, et recadrage d'images.
**Traitement d'Images** : Ajustement de couleurs, application de filtres, et opérations d'images.
**Dessin** : Dessin de formes, de textes, et d'autres graphiques sur des images.

## Utilisation de Base de Pillow

### Ouvrir une Image

```python
from PIL import Image
image = Image.open('chemin/vers/image.jpg')
```

### Afficher une Image

```python
image.show()
```

### Sauvegarder une Image

```python
image.save('chemin/vers/nouvelle_image.jpg')
```

## Manipulation d'Images

### Redimensionnement

```python
image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur))
```

### Rotation

```python
image_rotatee = image.rotate(90)  # Rotation de 90 degrés
```

### Recadrage

```python
zone = (x1, y1, x2, y2)
image_recadree = image.crop(zone)
```

## Exemple de Traitement d'Image

```python
from PIL import Image, ImageFilter

# Ouvrir une image
image = Image.open('chemin/vers/image.jpg')

# Appliquer un filtre de flou
image_floue = image.filter(ImageFilter.BLUR)

# Sauvegarder l'image modifiée
image_floue.save('chemin/vers/image_floue.jpg')
```

## Bonnes Pratiques

**Gestion des Ressources** : Utilisez un gestionnaire de contexte (```with Image.open(...) as image:```) pour s'assurer que les ressources sont correctement libérées.
**Traitement par Lots** : Automatisez le traitement de plusieurs images en utilisant des boucles et des fonctions.
**Optimisation des Performances** : Soyez attentif aux dimensions des images pour éviter une utilisation excessive de la mémoire.