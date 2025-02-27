## Introduction

Ce cours est dédié à l'apprentissage de React, un Framework JavaScript qui permet de créer des interfaces utilisateur rapidement. Pour rappel, un framework est un ensemble structuré d'outils, de bibliothèques et de bonnes pratiques permettant de simplifier et standardiser le développement d'applications, en offrant des fonctionnalités prêtes à l'emploi et en facilitant la gestion du code.

Avec React, le développement d'applications web est facilité par une structure de code basée sur l’utilisation de composants réutilisables. Chaque composant peut inclure du HTML, du CSS et du Javascript grâce à une syntaxe intuitive appelée JSX, qui simplifie l'intégration de la logique dans l'interface. Ce cours vous permettra de créer des applications solides et faciles à maintenir, tout en apprenant les bases de cette bibliothèque.

## Créer un nouveau projet avec React

###  Node Package Execute

Pour la création de nouveau projet avec React il faut avoir installé **npx**, c'est un outil de commande intégré à Node.js. Il permet d'éxécuter des packages npm (gestionnaire de paquets Node) directement sans les installer. C'est particulièrement utile pour lancer des scripts ou des outils temporaires, sans surcharger le système avec des installations locales.

Pour pouvoir utiliser **npx** il faut avoir installé **Node.js** voici un lien vers le <a href="https://nodejs.org/fr/download/package-manager/current" title="node.js" target="_blank">site officiel</a>.  

Pour vérifier que npx est installé il suffit d'exécuter la commande suivante dans le terminal :

```bash
npx --version
```

### React

Pour créer un projet React, il suffit d'exécuter la commande suivante dans le terminal :

```bash
npx create-react-app nom-du-projet
```

## Framework basé sur React

Il existe de nombreuses façons d'utiliser React, notamment grâce à des frameworks qui en sont dérivés. Ces frameworks enrichissent les fonctionnalités de base en ajoutant des outils supplémentaires adaptés aux besoins spécifiques de chaque projet, toujours en facilitant le processus de développement. Par exemple, des frameworks comme **Next.js** permettent de créer des applications web full-stack. D’autres outils comme **Remix** offrent une gestion avancée des routes et des chargements de données, tandis qu’**Expo** facilite le développement mobile pour iOS et Android avec l'intégration de React Native.

### Next.js

Next.js est un framework React adapté au développement d'applications de toute envergure, allant des blogs statiques aux applications dynamiques complexes. Pour créer un nouveau projet avec Next.js, il suffit d'exécuter la commande suivante dans le terminal :

```bash
npx create-next-app@latest
```

### Remix

Remix est un framework React doté d'une gestion des routes imbriquées. Il permet de diviser l'application en plusieurs parties, qui chargent les données en parallèle et se mettent à jour en fonction des actions de l'utilisateur. Pour initier un nouveau projet avec Remix, il suffit d'exécuter la commande suivante :

```bash
npx create-remix
```

### Expo

Expo est un framework React conçu pour le développement d'applications Android, iOS et web avec des interfaces utilisateur natives. Il intègre un SDK (kit de développement logiciel) pour React Native, simplifiant l'ajout de fonctionnalités natives. Pour démarrer un nouveau projet avec Expo, exécutez la commande suivante :

```bash
npx create-expo-app
```

### Next.js (App Router)

L'App Router, refonte des API de Next.js, permet aux composants asynchrones de charger des données côté serveur ou lors du build. Ces composants gèrent des opérations longues, telles que les requêtes API, en attendant les données avant l'affichage.Que ce soit côté serveur ou lors du processus de build.