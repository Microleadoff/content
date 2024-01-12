## Pytest en Python

Pytest est un framework de tests avancé pour Python. Il est apprécié pour sa simplicité, sa facilité d'utilisation, et sa capacité à gérer des tests plus complexes.

## Installation de Pytest
```shell
pip install pytest
```

## Caractéristiques Clés de Pytest

**Simplicité** : Des tests simples peuvent être écrits avec des assertions Python standards.
**Puissants Fixtures** : Offre un système de fixtures avancé pour la configuration et la décomposition des tests.
**Prise en Charge des Exceptions** : Facilité pour tester les exceptions.
**Tests Paramétriques** : Permet de définir plusieurs scénarios pour un même test.

## Structure de Base d'un Test avec Pytest

**Fichier de Test** : Les fichiers de test doivent commencer par test_ ou finir par _test.py.
**Fonctions de Test** : Les fonctions de test à l'intérieur du fichier doivent également commencer par test_.

## Exemple Simple de Test

```python
# test_calcul.py

def addition(a, b):
    return a + b

def test_addition():
    assert addition(2, 3) == 5
```

## Exécution des Tests

```shell
pytest

Fixtures Pytest
```

### Utilisation

Permet de créer une configuration de test réutilisable.

### Exemple

```python
@pytest.fixture
def email():
    return "user@example.com"

def test_email(email):
    assert email == "user@example.com"
```

## Test des Exceptions

### Syntaxe

```python
with pytest.raises(SomeException):
    # Exécutez le code qui doit lever 'SomeException'
```

## Tests Paramétriques

### Syntaxe

```python
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 9)])
def test_addition(a, b, expected):
    assert addition(a, b) == expected
```

## Bonnes Pratiques

**Nommez Clair** : Utilisez des noms descriptifs pour les fonctions de test.
**Tests Indépendants** : Chaque test doit pouvoir s'exécuter indépendamment des autres.
**Utilisation de Fixtures** : Utilisez les fixtures pour une configuration et un nettoyage efficaces.
**Tests Paramétriques** : Utilisez la paramétrisation pour couvrir plusieurs scénarios avec une seule fonction de test.

