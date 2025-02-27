## Créer un hook pour gérer un thème global

1. Créez un fichier `useTheme.js`.
2. Ce hook doit fournir :
    - Un état `theme` pour indiquer le thème actuel (`light` ou `dark`).
    - Une fonction `toggleTheme` pour basculer entre les deux thèmes.
3. Créez un composant `ThemeManager.js` qui utilise ce hook :
    - Affiche le thème actuel.
    - Permet à l’utilisateur de basculer entre `light` et `dark` grâce à un bouton.
    - Change la couleur de fond de la page en fonction du thème.

## Rendu attendu

<img src="../img/rendu_exo_34_2_theme.png" alt="Rendu attendu de l'exercice 2">