## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction Python cesar(chaine, decalage) qui prend en entrée une chaîne de caractères et un décalage, et qui renvoie la chaîne cryptée en utilisant le chiffrement de César.

### Exemple

```
>>> chaine = "Bonjour le monde"
>>> cesar(chaine, 3)
"Erqmrxu oh phqgh"
```

Dans cet exemple, la fonction cesar(chaine, 3) prend en entrée la chaîne "Bonjour le monde" et le décalage 3 et retourne la chaîne cryptée "Erqmrxu oh phqgh" en utilisant le chiffrement de César.

### Principe du chiffrement de César

Le chiffrement de César est une méthode de cryptage de texte qui consiste à décaler chaque lettre de la chaîne d'un nombre fixe de positions dans l'alphabet. Par exemple, si le décalage est de 3, la lettre "A" est remplacée par la lettre "D", la lettre "B" par la lettre "E", etc. Si le décalage est supérieur à 26 (le nombre de lettres dans l'alphabet), on revient au début de l'alphabet.

### Contraintes

- La fonction doit prendre en entrée une chaîne de caractères et un décalage entier.
- La fonction doit retourner une chaîne de caractères cryptée en utilisant le chiffrement de César.
- Les espaces et les caractères spéciaux ne doivent pas être modifiés.
- Les majuscules et les minuscules doivent être conservées et cryptées de manière appropriée.

### Conseils

- Utilisez la fonction ```ord()``` pour convertir une lettre en son code ASCII.
- Utilisez la fonction ```chr()``` pour convertir un code ASCII en lettre.
- Utilisez l'opérateur modulo (%) pour vous assurer que le décalage reste dans les limites de l'alphabet.

**Note** : Les opérations sur les caractères ne sont pas toujours simples, l'informatique étant à la base faite pour faire des mathématiques plus que du texte. C'est pourquoi il est fortement recommandé de se basé sur les code ASCII des lettres. A tiitre informatif, chaque lettre dispose d'un code ASCII, représenté notamment par un nombre (nombre à partir duquel il est simple de réaliser des calculs !)