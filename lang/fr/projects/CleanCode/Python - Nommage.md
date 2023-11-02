## Énoncé

### Description courte

En réutilisant un code fourni, vous allez devoir mettre en place l'ensemble des règles du Clean Code relatif au nommage.

### Éléments donnés

Voici le code sur lequel vous devez travailler : 

```python
from donnees import *
import pickle 
from random import randrange
import os

def recup_pseudo(): 
	try : 
		pseudo = input("Rentrez votre pseudo...")
		return pseudo
	except NameError :
		print("Votre pseudo doit être une chaine de caractere")

def scores_recuperation():
	if os.path.exists("score"):
		files_scores = open("score", "rb")
		mon_depickler = pickle.Unpickler(files_scores)
		scores = mon_depickler.load()
		files_scores.close()
	else :
		scores = {}
	return scores

def getWord():
	num = randrange(20)
	return liste_mots[num]

def get_string_reponse(word):
	size = len(word)
	i = 0
	string = "*"
	while i < size - 1 :
		string = string + "*"
		i += 1
	return (string)

def prend_letter(letter_liste):
	lettre = input("Tapez une lettre: ")
	if len(lettre)>1 or not lettre.isalpha():
		print("Vous n'avez pas saisi une lettre valide.")
		return prend_letter(letter_liste)
	else:
		if lettre in letter_liste :
			print("{} déjà rentre...".format(lettre))
			return prend_letter(letter_liste)
	return lettre

def get_letter_degage(word, letter, position):
		word = list(word)
		word[position] = '$'
		word_modif = ''.join(word)
		return word_modif

def check_si_letter_ok(word, letter, nb_coup, answer_chaine_caractere):
	if word.find(letter) == -1 :
		print("Nope {} n'est pas dans ce mot".format(letter))
		answer_modif = answer_chaine_caractere
		nb_coup -= 1
	else :
		while word.find(letter) != -1 :
			print("GREAT {} est dans le mot".format(letter))
			position = word.find(letter)
			word = get_letter_degage(word, letter, position)
			answer_chaine_caractere = list(answer_chaine_caractere)
			answer_chaine_caractere[position] = letter
			answer_modif = ''.join(answer_chaine_caractere)
	return answer_modif, nb_coup

def sovegard_score(scores, pseudo):
	files_scores = open("score", "wb") # On écrase les anciens scores
	mon_pickler = pickle.Pickler(files_scores)
	mon_pickler.dump(scores)
	files_scores.close()
```

### Contraintes

- Respectez les spécificités du langage python pour la réalisation de vos commentaires

### Critères de réussite

L'ensemble des règles de nommage sont en place et décrivent parfaitement ce à quoi ils sont rattachés. Ils permettent de simplifier la lecture du code et sa compréhension.

### Astuces

#### Astuce 1

- Vous pouvez vous aidez d'outils tels que ```flake8``` pour vérifier le respect des normes de python