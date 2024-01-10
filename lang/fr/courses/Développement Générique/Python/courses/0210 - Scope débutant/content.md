## La Portée (Scope) en Python

La portée en Python détermine la visibilité et la disponibilité des variables et des fonctions dans différentes parties du code. Comprendre le scope est essentiel pour gérer correctement les données dans un programme.

## Types de Portée

### Portée Locale (Local Scope)

**Définition :** Variables définies à l'intérieur d'une fonction.

**Accès :** Accessibles uniquement dans la fonction où elles sont déclarées.

  ```python
  def ma_fonction():
      variable_locale = "Je suis locale"
      print(variable_locale)  # Accessible ici
```
### Portée Globale (Global Scope)

**Définition** : Variables définies au niveau principal d'un script ou d'un module.
**Accès** : Accessibles partout dans le module.

```python
    variable_globale = "Je suis globale"

    def ma_fonction():
        print(variable_globale)  # Accessible ici
```

### Portée Englobante (Enclosing Scope)

**Définition** : Pertinent dans le contexte des fonctions imbriquées. C'est la portée du scope englobant.
**Accès** : Variables du scope englobant sont accessibles dans les fonctions imbriquées.

```python

    def exterieur():
        variable_englobante = "Je suis englobante"

        def interieur():
            print(variable_englobante)  # Accessible ici

        interieur()
```

### Portée Intégrée (Built-in Scope)

**Définition** : Noms pré-définis dans Python, comme ```print```, ```len```, etc.
**Accès** : Disponibles globalement, sans importation ni déclaration spécifique.


## Règles de Résolution des Noms (LEGB)

**Ordre de Résolution** : Local → Enclosing → Global → Built-in.
Python suit cet ordre pour trouver la signification d'un nom.

Modification des Variables Globales

  Utilisation de global : Pour modifier une variable globale dans une fonction locale.

```python

    def ma_fonction():
        global variable_globale
        variable_globale = "Modifiée"
```

## Bonnes Pratiques

**Minimisez l'usage de global** : L'utilisation excessive de variables globales peut rendre le code difficile à comprendre et à maintenir.

**Clarté des Noms** : Utilisez des noms de variables distincts pour éviter les confusions entre les scopes.

**Utilisation de Scope Englobant** : Préférez l'utilisation de paramètres pour passer des données aux fonctions.
