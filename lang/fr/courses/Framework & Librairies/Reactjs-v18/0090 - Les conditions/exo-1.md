## Afficher un message basé sur une condition

1. Créez un fichier `LoginMessage.js`.
2. Dans ce fichier, créez un composant fonctionnel nommé `LoginMessage` qui accepte une prop `isLoggedIn`.
3. Le composant doit afficher :
   - "Bienvenue, John Doe !" si `isLoggedIn` est `true`.
   - "Veuillez vous connecter." si `isLoggedIn` est `false`.
4. Importez ce composant dans `App.js` et affichez-le deux fois :
   - Une fois avec `isLoggedIn={true}`.
   - Une fois avec `isLoggedIn={false}`.

### Rendu attendu

<img src="https://github.com/Microleadoff/content/blob/master/lang/fr/courses/Framework%20&%20Librairies/Reactjs-v18/0090%20-%20Les%20conditions/rendu_exo_9_1.png?raw=true" alt="rendu attendu de l'exercice">