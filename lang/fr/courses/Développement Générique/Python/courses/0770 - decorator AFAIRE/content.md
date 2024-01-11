## Décorateurs en Python

Les décorateurs en Python sont des fonctions qui modifient le comportement d'autres fonctions ou méthodes. Ils sont utiles pour étendre ou modifier le comportement de fonctions de manière réutilisable.

## Qu'est-ce qu'un Décorateur ?

**Définition** : Un décorateur est une fonction qui prend une autre fonction en argument et retourne une nouvelle fonction.
**Usage** : Ils sont souvent utilisés pour ajouter des fonctionnalités communes (logging, vérification d'accès, mesure du temps d'exécution, etc.) de manière non intrusive.

## Création de Décorateurs

### Syntaxe de Base
```python
def mon_decorateur(fonction):
    def fonction_interne(*args, **kwargs):
        # Ajouter des actions avant
        resultat = fonction(*args, **kwargs)
        # Ajouter des actions après
        return resultat
    return fonction_interne

```
### Utilisation d'un Décorateur


```python
@mon_decorateur
def ma_fonction():
    pass

```
## Exemples de Décorateurs

### Décorateur Simple

```python
def decorateur_simple(fonction):
    def fonction_interne():
        print("Avant l'appel de la fonction.")
        fonction()
        print("Après l'appel de la fonction.")
    return fonction_interne

@decorateur_simple
def dit_bonjour():
    print("Bonjour !")

```

### Décorateur avec Arguments

```python
def decorateur_avec_arguments(argument):
    def decorateur_reel(fonction):
        def fonction_interne(*args, **kwargs):
            print(f"Argument du décorateur : {argument}")
            return fonction(*args, **kwargs)
        return fonction_interne
    return decorateur_reel

@decorateur_avec_arguments("exemple")
def ma_fonction():
    pass

```
## Bonnes Pratiques

**Noms Explicites** : Donnez des noms explicites à vos décorateurs et fonctions internes pour une meilleure lisibilité.
**Utilisation Judicieuse** : Utilisez les décorateurs pour des cas où ils simplifient le code sans l'obscurcir.
**Préservation de la Signature** : Utilisez functools.wraps pour préserver la signature de la fonction décorée.