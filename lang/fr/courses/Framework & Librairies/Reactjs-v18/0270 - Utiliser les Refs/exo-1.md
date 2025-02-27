## 1. Créer un formulaire avec un focus automatique

1. Créez un fichier `MultiStepForm.js`.
2. Ce composant doit inclure :
    - Trois champs `<input>` : Nom, Email, et Téléphone.
    - Une ref pour chaque champ.
3. Lorsque l'utilisateur appuie sur la touche "Entrée" dans un champ, le curseur doit automatiquement passer au champ suivant.
4. Utilisez les refs pour gérer la logique de navigation entre les champs.

## 2. Vérification et remise à zéro du formulaire

1. Ajoutez un bouton "Vérifier et réinitialiser" au composant `MultiStepForm`.
2. Lorsque ce bouton est cliqué :
    - Si tous les champs sont remplis, affichez une alerte "Formulaire valide !".
    - Si un champ est vide, mettez-le en surbrillance (par exemple, avec une bordure rouge).
    - Réinitialisez tous les champs après 3 secondes.
3. Utilisez les refs pour gérer le contenu et l'état visuel des champs.

## Rendu attendu (après avoir fait les deux exercices)

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0270%20-%20Utiliser%20les%20Refs/rendu_exo_27_1.png?raw=true" alt="Rendu attendu des exercices">