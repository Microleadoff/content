## Code

```python
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
```

## Explications

- La fonction ```fib(n)``` prend en entrée un entier ```n``` qui représente le numéro du terme de la suite de Fibonacci à calculer.
- Si ```n``` est inférieur ou égal à 1, c'est-à-dire que ```n``` est 0 ou 1, la fonction retourne directement ```n```. En effet, les deux premiers termes de la suite de Fibonacci sont 0 et 1.
- Sinon, la fonction utilise la relation de récurrence de la suite de Fibonacci pour calculer le n-ème terme en faisant appel récursivement à la fonction ```fib(n-1)``` pour calculer le (n-1)-ème terme et à la fonction ```fib(n-2)``` pour calculer le (n-2)-ème terme. La fonction ```fib(n)``` est donc définie par la somme des deux termes précédents de la suite de Fibonacci.
- La fonction retourne finalement le n-ème terme de la suite de Fibonacci.