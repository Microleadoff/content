## Tkinter en Python

Tkinter est le module d'interface graphique standard de Python. Il est largement utilisé pour développer des applications GUI (Graphical User Interface) de manière simple et efficace.

## Importation de Tkinter

```python
import tkinter as tk
```

## Création d'une Fenêtre Principale

### Initialisation

```python
root = tk.Tk()
```

## Lancement de la boucle d'événements :

```python
root.mainloop()
```

## Ajout de Widgets

### Bouton

```python
button = tk.Button(root, text='Cliquez-moi', command=ma_fonction)
button.pack()
```

### Étiquette (Label)

```python
label = tk.Label(root, text='Bienvenue sur Tkinter')
label.pack()
```

### Zone de Saisie (Entry)

```python
entry = tk.Entry(root)
entry.pack()
```

## Gestion de la Disposition

### ```Pack``` 

Organise les widgets en blocs avant et après les autres widgets.

### ```Grid``` 

Organise les widgets en grille.

### ```Place``` 

Positionne les widgets à une position absolue.


## Exemple Simple

```python
def dire_bonjour():
    print("Bonjour!")

root = tk.Tk()
root.title("Application Tkinter")

label = tk.Label(root, text='Hello, Tkinter!')
label.pack()

button = tk.Button(root, text='Cliquez-moi', command=dire_bonjour)
button.pack()

root.mainloop()
```

## Bonnes Pratiques

**Organisation du Code** : Structurez votre code en classes ou en fonctions pour gérer les widgets et les événements.
**Utilisation de mainloop** : mainloop est essentiel pour maintenir l'application en cours d'exécution et réagir aux événements.
**Nommez les Widgets** : Donnez des noms explicites aux variables de widgets pour une meilleure lisibilité.