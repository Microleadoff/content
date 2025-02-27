## 1. Créer un formulaire pour enregistrer un utilisateur

1. Créez un fichier `UserForm.js`.
2. Ce composant doit inclure :
    - Trois champs `<input>` : `name`, `email`, et `password`.
    - Un état `formData` pour stocker les valeurs du formulaire.
3. Affichez les données du formulaire dans une section `<p>` en temps réel lorsque l'utilisateur saisit les données.

## 2. Ajouter un champ dynamique au formulaire

1. Ajoutez un bouton "Ajouter un champ" dans le composant `UserForm`.
2. Lorsque ce bouton est cliqué, un nouveau champ `<input>` est ajouté avec une clé unique (par exemple : `field1`, `field2`).
3. Le champ doit être synchronisé avec l'état `formData`, et toutes les données du formulaire doivent être affichées dans une section `<p>`.

## Rendu attendu

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0200%20-%20Gestion%20du%20State%20vie%20les%20inputs/rendu_exo_20_1.png?raw=true" alt="Rendu attendu de des exercices">