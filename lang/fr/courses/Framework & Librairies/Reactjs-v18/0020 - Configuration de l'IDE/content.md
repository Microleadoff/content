## Configuration de l’éditeur

Un IDE est un éditeur de texte spécifiquement développé pour écrire du code informatique. Il dispose de nombreux outils pour vous faciliter la vie, accélérer votre vitesse d'écriture de code et en améliorer la qualité. Nous recommandons principalement l'utilisation de VS Code, qui propose une vaste sélection d'extensions et s'intègre facilement avec des services comme Git. Il présente également l'avantage de disposer d'une (très) large communauté qui développe et maintient des extensions très pratique pour le quotidien des développeurs.

Parmi les autres éditeurs les plus courants dans la communauté React, on trouve **Atom**, open-source et personnalisable, qui prend en charge de nombreux langages et intègre des plugins pour React. Il existe aussi **Vim**, un éditeur configurable en ligne de commande, qui est souvent inclus sur les systèmes UNIX et macOS sous le nom "vi" (prononcé "vi aïe"). On dispose aussi de **WebStorm** qui est spécialement conçu pour JavaScript par JetBrains, et enfin **Sublime Text** qui offre un support natif pour JSX et TypeScript avec coloration syntaxique et autocomplétion.

Un seul mot d'ordre ici : faites des tests et trouvez celui qui vous correspond le mieux !

## Fonctionnalités Recommandées pour un Éditeur de Texte

Nous recommandons à minima des fonctionnalités de linting et de formatage dans vos IDE. Le linting vise à analyser le code pour détecter des erreurs potentielles, alors que le formatage se concentre uniquement sur l'apparence du code. Ce sont deux bonnes pratiques que tout développeur devrait apprendre à maîtriser au fur et à mesure de son apprentissage.

### Le Linting

Les linters (analyseurs statiques) de code détectent les problèmes dans votre code au fur et à mesure de son écriture, ils vont aussi détecter les incohérences de style et les mauvaises pratiques de programmation, ce qui facilite leur correction. Pour pouvoir utiliser **Eslint** il faut bien avoir installé **Node.js**. Vous trouverez ici le <a href="https://www.npmjs.com/package/eslint-config-react-app" target="_blank" title="lien d'installation et de configuration pour ESLint">lien d'installation et de configuration pour ESLint</a>.


<!-- NATHAN ICI -->
Pour installer l'extension *ESLint* sur VS Code, voici les étapes à suivre :

1. Lancer VS Code
2. Cliquer sur Extensions dans la barre de gauche 
3. Écrire <strong>ESLint</strong> dans le champ
4. Installer l’extension 

Veillez à activer toutes les règles de `eslint-plugin-react-hooks` dans votre projet. Elles sont cruciales pour identifier et corriger rapidement les bugs majeurs.

#### *Illustration VS Code pour l'extension ESLint*
<img src="https://raw.githubusercontent.com/Microleadoff/content/55d6f07295e69b18d4a1c0ec1a7cca5a4ea76a5b/lang/fr/courses/Framework%20%26%20Librairies/React/img/vscode%20ESLint.png" alt="Illustration de VS Code pour l'extension ESLint">


### Formatage

Le formatage de code consiste à organiser et structurer son code pour améliorer sa lisibilité et sa cohérence. Cela comprend l'indentation, l'espacement, la disposition des accolades et des parenthèses, ainsi que l'alignement. Un code bien formaté est plus facile à comprendre, à déboguer et à maintenir, en particulier dans un contexte de travail d'équipe.

**Prettier** reformate votre code pour le rendre conforme à des règles prédéfinies et configurables. Lors de son exécution, il remplace les tabulations par des espaces et ajuste les indentations, guillemets, etc..., selon la configuration. Idéalement, il s'exécute automatiquement à chaque enregistrement de fichier pour effectuer ces ajustements pour vous.

Pour installer l’extension *Prettier* sur VS Code, voici les étapes à suivre:

1. Lancer VS Code
2. Cliquer sur Extensions dans la barre de gauche (Rouge)
3. Écrire <strong>Prettier</strong> dans le champ (Bleu)
4. Installer l’extension (Vert)

Attention à bien prendre l'extension officiel !

#### *Illustration VS Code pour l'installation de l'extension prettier*
<img src="https://raw.githubusercontent.com/Microleadoff/content/55d6f07295e69b18d4a1c0ec1a7cca5a4ea76a5b/lang/fr/courses/Framework%20%26%20Librairies/React/img/install%20prettier%20vscode.png" alt="Illustration de VS Code pour prettier">

### Formatage à la sauvegarde

Dans l’idéal, vous devriez formater votre code à chaque sauvegarde. Cela garantit un code constamment lisible et cohérent, sans effort supplémentaires.

Suivez ces étapes pour activer l’option sur VS Code.

1. Dans VS Code aller dans **File** dans le menu en haut à gauche
2. Puis dans **Preferences** presque tout en bas de la liste
3. Ensuite cliquer sur **settings** 
4. Dans la barre de recherche, entrer **format on save** puis cochez la première option.

#### *Illustration VS Code pour les instructions 1/2/3*
<img src="https://raw.githubusercontent.com/Microleadoff/content/55d6f07295e69b18d4a1c0ec1a7cca5a4ea76a5b/lang/fr/courses/Framework%20%26%20Librairies/React/img/format%20auto%20vscode%201.png" alt="Illustration de VS Code pour le Formatage à la sauvegarde 1">

#### *Illustration VS Code pour l'instruction 4*
<img src="https://raw.githubusercontent.com/Microleadoff/content/55d6f07295e69b18d4a1c0ec1a7cca5a4ea76a5b/lang/fr/courses/Framework%20%26%20Librairies/React/img/format%20auto%20vscode%202.png" alt="Illustration de VS Code pour le Formatage à la sauvegarde 2">