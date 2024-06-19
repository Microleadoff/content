## Énoncé

### Description courte

Le principe du projet est de créer un site internet faisant office de calculette pour un prêt immobilier

### Listing de fonctionnalités

A partir d'un formulaire contenant 3 champs distincts (montant emprunté, taux nominal et durée de remboursement), vous devez générer un tableau d'amortissement correspondant à un prêt accordé selon les modalités saisies par l'utilisateur.

Voici quelques informations supplémentaires concernant le formulaire de saisie utilisateur : 

- le champs "Montant Emprunté" doit être stipulé en euro et obligatoirement être un nombre entier
- le champs "Taux nominal" doit être exprimé en pourcentage et être obligatoirement un nombre à virgule
- le champs "durée de remboursement" doit obligatoirement être un nombre entier et être exprimé en année.

Notez que vous devrez vérifier l'ensemble des saisies utilisateur lors de la soumission du formulaire. En cas d'erreur, un message "Veuillez remplir les champs: XXX, XXX, XXX avec des données valides !", où les "XXX" doivent correspondre à la liste des erreurs contenues dans le formulaire (une erreur par champs).

Une fois les champs validés, et lors de la soumission du formulaire, vous devez afficher le tableau d'amortissement correspondant.

Intégrez un bouton "télécharger le PDF" en dessous du tableau d'amortissement. Un fichier PDF doit se télécharger en cliquant dessus et il doit contenir l'ensemble des informations présentes dans le formulaire et dans le tableau.

### Éléments donnés

Vous pouvez retrouver un visuel et un exemple de rendu sur la vidéo youtube suivante : <a href="https://www.youtube.com/watch?v=jdkSxWxZiFk" target="_blank" title="Vidéo de rendu du projet de calculette de prêt immobilier en Javascript sur Microlead">Voir la vidéo</a>

Vous pouvez également retrouver les maquettes Figma du projet sur le lien suivant : <a href="https://www.figma.com/file/SlO9YozC45uw1VBITDZo4q/Modelling_calculatrice_pret?type=design&node-id=0%3A1&mode=design&t=50BGSIIqqgz9f0yv-1" target="_blank" title="Maquette figma du projet de calculette de prêt immobilier en JavaScript sur Microlead">Voir la maquette</a>

**Note** Pour accéder à la maquette, vous devez :

- Vous connecter à Figma
- Vous rendre sur le lien ci-dessus
- cliquez sur le bouton "get a copy"
- Rendez-vous ensuite sur la page "Maquette" pour obtenir le détail de l'intégration à réaliser.

Pour l'export en PDF, vous pouvez utiliser la librairie jsPDF disponible sur le lien suivant : <a href="https://github.com/parallax/jsPDF" target="_blank" rel="nofollow" title="jsPDF">jsPDF</a>

#### Formules mathématiques

##### Calcul du taux d'intérêt mensuel

Le taux d'intérêt est la valeur qui est passée dans le champs "Taux nominal" de la maquette.

```
Taux d'intérêt mensuel = (Taux d'intérêt / 12) / 100
```

##### Calcul de la durée du prêt en mois

```
Durée du prêt en mois = durée total du prêt * 12
```

##### Calcul des intérêts d'un mois

```
Intérêts du mois = montant restant à payer * taux d'intérêt mensuel
```

##### Calcul de l'échéance mensuelle

```
Echeance mensuelle = Montant total du prêt * ( ( taux d'intérêt mensuel * ( (1 + taux d'intérêt mensuel) ** Durée du prêt en mois)) / (((1 + taux d'intérêt mensuel) ** Durée du prêt en mois) - 1));
```

##### Calcul de l'amortissement

```
Amortissement du mois = Echeance mensuelle - intérêts du mois
```

### Contraintes

- N'utilisez que du HTML, du CSS, et du JavaScript
- Respectez scrupuleusement la maquette
- Vérifiez bien les données renseignées par l'utilisateur