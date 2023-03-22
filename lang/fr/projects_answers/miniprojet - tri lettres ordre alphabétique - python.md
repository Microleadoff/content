## Code

```python
def trier_lettres(chaine):
    # On convertit la chaîne en minuscules pour considérer les lettres majuscules et minuscules comme équivalentes
    chaine = chaine.lower()
    # On enlève tous les caractères qui ne sont pas des lettres
    chaine = ''.join(caractere for caractere in chaine if caractere.isalpha())
    # On trie les lettres de la chaîne par ordre alphabétique
    chaine_triee = ''.join(sorted(chaine))
    return chaine_triee
```

## Explications

- La fonction ```trier_lettres``` prend en entrée une chaîne de caractères chaine.
- On convertit d'abord la chaîne en minuscules avec la méthode ```lower()``` pour considérer les lettres majuscules et minuscules comme équivalentes.
- On enlève ensuite tous les caractères qui ne sont pas des lettres avec une expression de compréhension de liste (```caractere.isalpha()``` renvoie ```True``` si caractere est une lettre, et ```False``` sinon).
- Enfin, on trie les lettres de la chaîne par ordre alphabétique avec la fonction ```sorted()``` qui renvoie une liste triée, et on les concatène à nouveau avec la méthode ```join()```.
- On retourne la chaîne triée ```chaine_triee```.