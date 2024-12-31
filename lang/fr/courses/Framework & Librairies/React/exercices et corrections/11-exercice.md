## **Exercice du cours 11 : Les fonctions pures**

### Exercice 1

**Créer une fonction pure pour le calcul d'une réduction de prix**

1. Créez un fichier `DiscountCalculator.js`.
2. Définissez une fonction pure `calculateDiscount` qui prend en entrée :
   - `price` (le prix d'origine).
   - `discount` (le pourcentage de réduction).
3. La fonction doit retourner le prix après réduction.
4. Utilisez cette fonction dans un composant fonctionnel `DiscountDisplay` qui accepte `price` et `discount` comme props et affiche le prix réduit dans un `<p>`.

---

#### Rendu attendu
<img src="../img/rendu_exo_11_1.png" alt="rendu attendu de l'exercice">

---

Voici un nouvel exercice simplifié mais efficace pour le cours 11 ("Les fonctions pures").

---

### Exercice 1

**Créer une fonction pure pour convertir des températures**

1. Créez un fichier `TemperatureConverter.js`.
2. Définissez une fonction pure `convertToFahrenheit` qui prend en entrée une température en Celsius (`celsius`) et retourne la température en Fahrenheit.
   - Formule : `fahrenheit = (celsius * 9/5) + 32`
3. Utilisez cette fonction dans un composant fonctionnel `TemperatureDisplay` qui accepte une prop `celsius` et affiche :
   - La température en Celsius.
   - La température convertie en Fahrenheit.

---

#### Rendu attendu
<img src="../img/rendu_exo_11_2.png" alt="rendu attendu de l'exercice">

---




