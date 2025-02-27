## Afficher un bouton en fonction de l'état

1. Créez un fichier `ActionButton.js`.
2. Ce composant accepte une prop `isEnabled`.
3. Il doit afficher :
    - Un bouton `<button>` avec le texte "Action disponible" si `isEnabled` est `true`.
    - Un texte `<p>` avec "Action désactivée" si `isEnabled` est `false`.
4. Importez ce composant dans `App.js` et affichez-le deux fois :
    - Une fois avec `isEnabled={true}`.
    - Une fois avec `isEnabled={false}`.

## Rendu attendu

<img src="../img/rendu_exo_9_2.png" alt="rendu attendu de l'exercice">