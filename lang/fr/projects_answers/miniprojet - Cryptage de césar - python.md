## Code

```python
def cesar(chaine, decalage):
    resultat = ""
    for lettre in chaine:
        # Vérifier si la lettre est une lettre de l'alphabet
        if lettre.isalpha():
            # Convertir la lettre en code ASCII
            code_ascii = ord(lettre)
            # Calculer le nouveau code ASCII en ajoutant le décalage
            nouveau_code_ascii = code_ascii + decalage
            # Vérifier si la lettre est une majuscule ou une minuscule
            if lettre.isupper():
                # Si c'est une majuscule, utiliser l'alphabet en majuscules
                base_ascii = ord("A")
            else:
                # Sinon, utiliser l'alphabet en minuscules
                base_ascii = ord("a")
            # S'assurer que le nouveau code ASCII reste dans les limites de l'alphabet
            nouveau_code_ascii = (nouveau_code_ascii - base_ascii) % 26 + base_ascii
            # Convertir le nouveau code ASCII en lettre
            nouvelle_lettre = chr(nouveau_code_ascii)
            # Ajouter la lettre cryptée au résultat
            resultat += nouvelle_lettre
        else:
            # Si ce n'est pas une lettre de l'alphabet, ajouter le caractère original au résultat
            resultat += lettre
    return resultat
```

## Explications

- On parcourt chaque lettre de la chaîne de caractères.
- Si la lettre est une lettre de l'alphabet, on la crypte en suivant les étapes suivantes :
    - On convertit la lettre en code ASCII.
    - On calcule le nouveau code ASCII en ajoutant le décalage.
    - On vérifie si la lettre est une majuscule ou une minuscule.
    - On s'assure que le nouveau code ASCII reste dans les limites de l'alphabet en utilisant l'opérateur modulo (%).
    - On convertit le nouveau code ASCII en lettre.
    - On ajoute la lettre cryptée au résultat.
- Si la lettre n'est pas une lettre de l'alphabet, on ajoute le caractère original au résultat.
- Enfin, on retourne la chaîne cryptée.