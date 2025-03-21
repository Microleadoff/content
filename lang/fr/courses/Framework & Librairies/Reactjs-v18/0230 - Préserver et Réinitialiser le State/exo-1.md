## 1. Créer un formulaire avec un bouton de réinitialisation

1. Créez un fichier `ResettableForm.js`.
2. Ce composant doit inclure :
    - Deux champs `<input>` pour `name` et `email`.
    - Un bouton "Réinitialiser" qui remet le formulaire à son état initial.
3. Gérez l'état des champs via un objet `formData`.

## 2. Ajouter un historique de réinitialisations

1. Modifiez le composant `ResettableForm` pour inclure un historique des réinitialisations.
2. Chaque fois que le formulaire est réinitialisé, ajoutez une entrée dans un tableau `resetHistory` contenant un horodatage (date et heure).

## Rendu attendu (après avoir fait les deux exercices)

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0230%20-%20Pr%C3%A9server%20et%20R%C3%A9initialiser%20le%20State/rendu_exo_23_1.png?raw=true" alt="Rendu attendu des exercices">