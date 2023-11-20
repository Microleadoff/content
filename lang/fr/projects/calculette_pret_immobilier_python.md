## Énoncé

### Description courte

Le principe du projet est de créer un site internet faisant office de calculette pour un prêt immobilier

### Listing de fonctionnalités

A partir de 3 inputs distincts renseignés par l'utilisateur (montant emprunté, taux nominal et durée de remboursement), vous devez générer un tableau d'amortissement correspondant à un prêt accordé selon les modalités saisies par l'utilisateur.

Voici quelques informations supplémentaires concernant le formulaire de saisie utilisateur : 

- le champs "Montant Emprunté" doit obligatoirement être un nombre entier
- le champs "Taux nominal" doit être exprimé en pourcentage et être obligatoirement un nombre à virgule
- le champs "durée de remboursement" doit obligatoirement être un nombre entier et être exprimé en année.

Notez que vous devrez vérifier l'ensemble des saisies utilisateur lors de la soumission du formulaire. En cas d'erreur, un message "Veuillez remplir les champs: XXX, XXX, XXX avec des données valides !", où les "XXX" doivent correspondre à la liste des erreurs contenues dans le formulaire (une erreur par champs).

Une fois les champs validés, et lors de la soumission du formulaire, vous devez afficher le tableau d'amortissement correspondant.

Vous devez ensuite proposer à l'utilisateur d'exporter en PDF son tableau d'amortissement. Un dossier "download" doit automatiquement être créé et l'ensemble des exports PDF ainsi effectués doivent y être placé.

Vous devez ensuite proposer à l'utilisateur de faire une autre simulation. En cas de refus, le programme devra se fermer.


### Éléments donnés

Vous pouvez retrouver un visuel et un exemple de rendu sur la vidéo youtube suivante : <a href="https://www.youtube.com/watch?v=TW_pb41RaZI" target="_blank" title="Vidéo de rendu du projet de calculette de prêt immobilier en Python sur Microlead">Voir la vidéo</a>

Vous pouvez vous servir de <a href="https://pypi.org/project/fpdf/" title="FPDF" target="_blank">fpdf</a> pour la génération des fichiers PDF.

### Contraintes

- N'utilisez que du Python
- Vérifiez bien les données renseignées par l'utilisateur.