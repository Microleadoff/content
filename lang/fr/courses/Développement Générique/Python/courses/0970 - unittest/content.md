# Tests Unitaires en Python avec ```unittest```

```unittest``` est un framework de test unitaire intégré à Python. Il aide à écrire et à exécuter des tests, fournissant un moyen standard de tester des morceaux de code de manière isolée et systématique.

## Importation de ```unittest```
```python
import unittest
```

## Structure de Base d'un Test avec unittest

### Création d'une Classe de Test

```python
class MonTest(unittest.TestCase):
    def test_fonctionnalite_x(self):
        # Code de test ici
```

**Méthodes de Test** : Les méthodes qui commencent par ```test_``` sont automatiquement exécutées comme des tests.

## Exécution des Tests

### Lancement des Tests

```python
if __name__ == '__main__':
    unittest.main()
```

## Exemples de Méthodes d'Assert

**Égalité** : ```self.assertEqual(a, b)```
**Vérité** : ```self.assertTrue(x)```
**Exceptions** : ```self.assertRaises(SomeException)```
**Presque Égal** : ```self.assertAlmostEqual(a, b)```

## Organisation des Tests

### setUp et tearDown :

```python
class MonTest(unittest.TestCase):
    def setUp(self):
        # Code de mise en place avant chaque test

    def tearDown(self):
        # Code de nettoyage après chaque test
```

**setUpClass et tearDownClass** : Méthodes appelées une fois avant et après tous les tests de la classe.

### Exemple de Test

```python
class TestAddition(unittest.TestCase):
    def test_addition_simple(self):
        self.assertEqual(1 + 1, 2)

    def test_addition_negative(self):
        self.assertEqual(-1 + -1, -2)

if __name__ == '__main__':
    unittest.main()
```

## Bonnes Pratiques

**Nommez les Tests Clair** : Utilisez des noms descriptifs pour les méthodes de test pour indiquer ce qu'ils vérifient.
**Tests Indépendants** : Chaque test doit être indépendant des autres.
**Utilisez setUp et tearDown** : Pour la configuration et le nettoyage nécessaire avant et après les tests.
**Testez les Cas Limites** : Incluez des tests pour les cas normaux, les limites et les cas d'erreur.