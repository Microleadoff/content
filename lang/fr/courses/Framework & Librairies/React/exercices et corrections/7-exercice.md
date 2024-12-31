
## Exercice du cours 7 : JSX et les accolades

**Intégrer des expressions dynamiques dans JSX**

1. Créez un composant nommé `Greeting` dans un fichier `Greeting.js`.
2. Ce composant doit inclure :
   - Une constante `currentHour` définie dans le composant et contenant l'heure actuelle (utilisez `new Date().getHours()`).
   - Une logique pour afficher un message dynamique dans une balise `<h2>` :
     - Si l'heure est inférieure à 12, affichez "Bonjour !".
     - Sinon, affichez "Bonsoir !".
3. Importez ce composant dans le fichier `App.js` et affichez-le sous le composant `Welcome`.

---

#### Rendu attendu
<img src="../img/rendu_exo_7_1.png" alt="rendu attendu de l'exercice">

---

2. **Afficher la date actuelle dans un composant**

1. Créez un fichier `CurrentDate.js`.
2. Ce composant doit calculer la date actuelle (utilisez `new Date().toLocaleDateString()`) et l'afficher dans un `<p>` avec le texte : "Nous sommes le [date actuelle]".
3. Importez ce composant dans `App.js` et affichez-le sous le composant `Greeting`.

---

#### Rendu attendu
<img src="../img/rendu_exo_7_2.png" alt="rendu attendu de l'exercice">