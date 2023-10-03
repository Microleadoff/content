## Mise en index

Bien qu'il soit extrêmement pratique de pouvoir organiser les commits à sa guise, la gestion de la zone d'index peut parfois sembler plus compliquée que nécessaire lors d'une utilisation normale. Si vous souhaitez éviter l'étape d'ajout des fichiers à la zone d'index, Git propose une solution simplifiée. En utilisant l'option **-a** avec la commande **git commit**, Git sera automatiquement chargé d'ajouter tous les fichiers déjà sous suivi de version à la zone d'index avant d'effectuer la validation, vous évitant ainsi d'avoir à saisir les commandes **git add** :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git checkout -- <fichier>..." pour annuler les modifications dans la copie de travail)

        modifié :         CONTRIBUTING.md

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")
$ git commit -a -m 'added new benchmarks'
[master 83e38c7] added new benchmarks
 1 file changed, 5 insertions(+), 0 deletions(-)
```

Notez bien que vous n’avez pas eu à lancer **git add** sur le fichier CONTRIBUTING.md avant de valider.
