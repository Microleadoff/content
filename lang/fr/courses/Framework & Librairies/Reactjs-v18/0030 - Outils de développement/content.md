## Outils de développement
Les outils de développement React (React Developer Tools) facilitent l'examen des composants, permettant de les inspecter et de les modifier en temps réel. Ils aident également à identifier et à résoudre les problèmes de performance, en offrant une meilleure vue de la structure des composants et de leurs relations, ce qui optimise le débogage et le code.

## Extension de navigateur
Pour déboguer efficacement des sites construits avec React, l'installation de l'extension de navigateur **react Developer Tools**  offre des outils tels que *Components*, qui permet d’inspecter et de modifier les composants en temps réel, et *Profiler*, qui aide à analyser les performances et à repérer les ralentissements, améliorant ainsi l’optimisation des applications React.

### Les autres navigateurs 
Pour les navigateurs sur lesquels l'extension n'est pas disponible, comme Safari, le module npm **react-devtools** peut être installé via un terminal:

```bash
npm install -g react-devtools
```

Les outils de développement peuvent alors être ouverts depuis le terminal :
```bash
React-devtools
```

Pour connecter le site aux outils de développement React, ajoutez la balise `<script>` au début de la balise `<head>` de votre fichier HTML. Cette balise charge le module **react-devtools** et établit la connexion pour le débogage. Une fois le script ajouté, rafraîchissez la page.
```html
<html>
    <head>
        <script src="http://localhost:port"></script>
    </head>
</html>
```
Assurez-vous que l’adresse spécifiée dans la balise `<script>` correspond au serveur local où **react-devtools** est en cours d'exécution.

### React Native
La méthode la plus simple pour utiliser les outils de développement React consiste à les installer globalement :

```bash
npm install -g react-devtools
```

Ensuite, les outils peuvent être lancés depuis le terminal :

```bash
react-devtools
```

Cela permet de se connecter automatiquement à toute application React Native locale en cours d'exécution, facilitant ainsi le débogage en temps réel.