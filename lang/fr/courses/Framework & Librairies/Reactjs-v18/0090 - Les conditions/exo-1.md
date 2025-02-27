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

<img src="../img/rendu_exo_9_1.png" alt="rendu attendu de l'exercice">