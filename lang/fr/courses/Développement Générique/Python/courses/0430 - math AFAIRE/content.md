## Le Module ```math``` en Python

Le module ```math``` en Python offre un ensemble de fonctions mathématiques et de constantes qui permettent d'effectuer des calculs mathématiques précis.

## Importation du Module
```python
import math
```
## Fonctions Principales

### Constantes

```math.pi```: La constante ```π```.
```math.e```: La base des logarithmes naturels.
```math.inf```: Une représentation flottante de l'infini.
```math.nan```: Une représentation flottante de "```Not a Number```".

### Opérations Arithmétiques

```math.sqrt(x)```: Renvoie la racine carrée de x.
```math.pow(x, y)```: Renvoie x élevé à la puissance y.
```math.exp(x)```: Renvoie e^x.
```math.log(x[, base])```: Renvoie le logarithme de x avec la base spécifiée.

### Trigonométrie

```math.sin(x)```: Renvoie le sinus de x (x en radians).
```math.cos(x)```: Renvoie le cosinus de x.
```math.tan(x)```: Renvoie la tangente de x.

### Conversion D'angle

```math.degrees(x)```: Convertit l'angle x de radians en degrés.
```math.radians(x)```: Convertit l'angle x de degrés en radians.

### Arrondissement

```math.ceil(x)```: Renvoie le plafond de x, le plus petit entier supérieur ou égal à x.
```math.floor(x)```: Renvoie le plancher de x, le plus grand entier inférieur ou égal à x.
```math.round(x[, n)```: Arrondit x à n décimales.

### Fonctions Hyperboliques

```math.sinh(x)```: Renvoie le sinus hyperbolique de x.
```math.cosh(x)```: Renvoie le cosinus hyperbolique de x.
```math.tanh(x)```: Renvoie la tangente hyperbolique de x.

## Bonnes Pratiques

Utilisation des Fonctions Appropriées : Utilisez les fonctions spécifiques du module ```math``` pour garantir la précision et l'efficacité des calculs.
Conversion d'Angles : Faites attention à convertir les angles en radians ou en degrés selon les besoins.
Comprendre les Résultats : Soyez conscient de la nature des résultats (par exemple, ```math.sqrt``` renvoie toujours un flottant).