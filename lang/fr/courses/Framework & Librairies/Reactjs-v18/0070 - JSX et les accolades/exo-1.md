## Intégrer des expressions dynamiques dans JSX

1. Créez un composant nommé `Greeting` dans un fichier `Greeting.js`.
2. Ce composant doit inclure :
    - Une constante `currentHour` définie dans le composant et contenant l'heure actuelle (utilisez `new Date().getHours()`).
    - Une logique pour afficher un message dynamique dans une balise `<h2>` :
        - Si l'heure est inférieure à 12, affichez "Bonjour !".
        - Sinon, affichez "Bonsoir !".
3. Importez ce composant dans le fichier `App.js` et affichez-le sous le composant `Welcome`.

## Rendu attendu

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0070%20-%20JSX%20et%20les%20accolades/rendu_exo_7_1.png?raw=true" alt="rendu attendu de l'exercice">