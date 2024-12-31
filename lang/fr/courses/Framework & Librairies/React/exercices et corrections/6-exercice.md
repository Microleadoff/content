## Exercice du cours 6 : Intégrer du JSX

1. **Utilisation du JSX dans un composant React**

1. Créez un nouveau composant nommé `UserCard` dans un fichier `UserCard.js`.
2. Ce composant doit retourner une balise `<div>` avec la structure suivante :
   - Un titre contenant le nom d'un utilisateur (par exemple : "John Doe").
   - Un paragraphe affichant son email (par exemple : "john.doe@example.com").
   - Un boutton avec le texte "Afficher les détails".
3. Importez ce composant dans le fichier `App.js` et affichez-le sous le composant `Welcome`.

---

#### Rendu attendu
<img src="../img/rendu_exo_6_1.png" alt="rendu attendu de l'exercice">

---

2. **Utilisation des balises HTML dans JSX**

1. Créez un fichier `Profile.js`.
2. Ce composant doit retourner une balise `<div>` contenant :
   - Une image `<img>` avec l'attribut `src` pointant vers une URL d'image de profil (par exemple : "https://via.placeholder.com/150").
   - Un titre `<h3>` affichant "John Doe".
   - Une description `<p>` affichant "Développeur Web passionné".
3. Importez ce composant dans `App.js` et affichez-le sous le composant `UserCard`.

---

#### Rendu attendu
<img src="../img/rendu_exo_6_2.png" alt="rendu attendu de l'exercice">