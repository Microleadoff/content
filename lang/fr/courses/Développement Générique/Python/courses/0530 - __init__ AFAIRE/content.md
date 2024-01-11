## Utilisation de ```__init__``` en Python

La méthode ```__init__``` est une méthode spéciale en Python, souvent appelée "constructeur" dans d'autres langages de programmation. Elle est automatiquement appelée lors de la création d'une nouvelle instance d'une classe.

## Définition de ```__init__```

**But :** Initialiser les attributs de l'instance de la classe.
**Syntaxe :**
```python
class MaClasse:
  def __init__(self, param1, param2):
      self.param1 = param1
      self.param2 = param2
```

## Exemples

### Exemple Basique

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

ma_voiture = Voiture('Toyota', 'Corolla')
print(ma_voiture.marque)  # Toyota
```

### Avec des Valeurs Par Défaut

```python
class Voiture:
    def __init__(self, marque, modele, annee=2020):
        self.marque = marque
        self.modele = modele
        self.annee = annee

voiture_ancienne = Voiture('Ford', 'Mustang', 1965)
voiture_nouvelle = Voiture('Tesla', 'Model 3')
```

### Points Importants

**self** : Représente l'instance de la classe. Utilisé pour accéder aux attributs et méthodes de la classe.
**Paramètres** : ```__init__``` peut prendre un nombre quelconque de paramètres pour initialiser l'objet.
**Valeurs par Défaut** : Vous pouvez définir des valeurs par défaut pour les paramètres.

## Bonnes Pratiques

**Initialisation Complète** : Assurez-vous que tous les attributs nécessaires à l'objet sont initialisés dans ```__init__```.
**Noms des Attributs Clair** : Utilisez des noms d'attributs explicites pour rendre votre code plus lisible.
**Pas de Logique Complexe dans ```__init__```** : Évitez d'insérer des calculs ou une logique complexe dans ```__init__```. Cette méthode doit être utilisée principalement pour l'initialisation.