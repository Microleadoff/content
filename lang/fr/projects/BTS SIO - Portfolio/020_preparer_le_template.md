## Énoncé

### Description courte

Maintenant que vous avez choisi votre template, il est temps de commencer à le préparer pour réaliser votre portfolio. L'idée ici est de basculer des fichiers HTML vers des fichiers PHP afin de commencer à regrouper les informations redondantes.

## Étapes

### 1. Adaptation du template

Je vous recommande dans un premier temps de dissocier votre template de votre projet final. L'idée est que le template doit rester toujours intacte pour vous servir de base de repère. Vous ne devrez donc jamais le modifier, préférez travailler sur une copie.

Si vous souhaitez adapter le template en terme de polices, de couleurs (etc...), voici quelques recommandations :

1. Ne changez que les couleurs de votre template dans le CSS, mais pensez bien à vérifier toutes les utilisations possibles du type de couleurs (dégradés, hexadécimal, RGB, etc...)
2. Attention si toutefois vous souhaitez changer les polices de votre template. Vous devez savoir que les polices ont chacunes leurs propres taille. Ainsi une police "A" en taille "22px" pourra paraître bien plus grande ou bien plus petite qu'une police "B" en taille "22px" ! Faites donc bien attention dans cette adaptation.

### 2. Mise en place de l'architecture

Plusieurs étapes sont à respecter pour rencontrer le moins de difficultés possible : 

- Récupérez tous les dossiers contenant les "assets" (images, fonts, css, etc...) du template et dupliquez-les dans votre propre dossier de portfolio
- Copiez / collez le fichier index.html de votre template vers votre dossier. Vérifiez ensuite qu'il fonctionne et qu'il charge bien toutes les images, polices, etc... Si ce n'est pas le cas, réglez le souci avant d'aller plus loin.
- Mettez votre dossier de portfolio sur un serveur web, afin que le PHP que nous allons y insérer puisse être interprété. Lancez ensuite l'interprétation du fichier via le serveur web dans votre navigateur (ouvrez le via localhost).
- Remplacez l'extension ".html" de votre fichier d'index, par ".php". Vérifiez que le fonctionnement est toujours bon.

Il va maintenant falloir attaquer la partie découpage du reste de la page !

### 3. Découpage de la page d'accueil

#### Identification

Ici il faut identifier l'ensemble des informations qui vont être récurrentes au sein de votre page web. L'objectif ici est de les séparer dans des fichiers spéicifiques, afin de permettre de modifier les informations à un endroit unique, et de les répercuter sur l'ensemble du site internet. Les éléments souvent communs à toutes les pages sont : 

- le contenu des balises ```<head></head>```
- Le menu
- Le footer

La liste n'est pas exhaustive, libre à vous de trouver d'autres éléments récurrents.

#### Découpage

Pour chacun des éléments identifiés, vous allez devoir créer un fichier ```.php``` qui contiendra les éléments HTML. Pour cette réalisation : 

1. Choix d'une section à découper (ex : footer)
2. Création du fichier (ex : ```partials/footer.php```)
3. Copier/coller la section depuis le HTML vers le nouveau fichier PHP
4. Remplacer le contenu du fichier HTML par un ```include_once``` (ex : ```<?php include_once("partials/footer.php"); ?>```)

_Note_ : Ce n'est pas parce que vous créez des fichiers ```.php``` que vous êtes obligé de mettre du PHP dedans. Vous pouvez parfaitement ne laisser que du HTML dedans.

_Note_ : Une bonne pratique est de placer ces fichiers découpés dans un dossier spécifique (en général : "partials").


### Exemple de découpage

Soit le fichier de base nommé ```head.php``` suivant : 

```html
<!-- fichier "head.php" -->
<head>
    <title>Exemple de découpage</title>

    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="Free HTML Templates" name="keywords">
    <meta content="Free HTML Templates" name="description">

    <!-- Favicon -->
    <link href="img/favicon.ico" rel="icon">
    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap" rel="stylesheet"> 
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <!-- Libraries Stylesheet -->
    <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
    <link href="lib/lightbox/css/lightbox.min.css" rel="stylesheet">
    <!-- Customized Bootstrap Stylesheet -->
    <link href="css/style.css" rel="stylesheet">
</head>
```

Voici un découpage final possible à faire : 

```php
// fichier "head.php"
<head>
    <?php include_once("partials/title.php"); ?>
    <?php include_once("partials/metas.php"); ?>
    <?php include_once("partials/links.php"); ?>
</head>
```

```html
<!-- fichier partials/title.php -->
<title>Exemple de découpage</title>
```

```html
<!-- fichier partials/metas.php -->
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<meta content="Free HTML Templates" name="keywords">
<meta content="Free HTML Templates" name="description">
```

```html
<!-- fichier partials/links.php -->
<!-- Favicon -->
<link href="img/favicon.ico" rel="icon">
<!-- Google Web Fonts -->
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap" rel="stylesheet"> 
<!-- Font Awesome -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
<!-- Libraries Stylesheet -->
<link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
<link href="lib/lightbox/css/lightbox.min.css" rel="stylesheet">
<!-- Customized Bootstrap Stylesheet -->
<link href="css/style.css" rel="stylesheet">
```