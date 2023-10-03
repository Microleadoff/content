Commençons par nous pencher sur le processus de fusion des branches. Mais avant cela nous apprendrons ce qu'est un état de divergence.

Un état de divergence signifie que bien que les deux branches partagent un commit ancestral commun, elles pointent désormais vers des commits distincts, chacun représentant potentiellement des modifications différentes apportées à un même fichier du projet.

Pour mieux comprendre ce concept, retournons légèrement en arrière et examinons un exemple plus simple où notre projet se trouve dans cet état :

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-6-image-à-remplacer)

Ici, nous avons une branche **test** pointant vers le commit **commitN+1** et une branche **master** pointant vers le commit **commitN**. Le **commitN** est l'ancêtre direct du **commitN+1**, ce qui signifie qu'il n'y a pas de problème de divergence entre les deux branches.

Pour fusionner ces deux branches, nous allons d'abord nous placer sur la branche **master** en utilisant la commande ```git checkout```, puis nous allons lancer la commande ```git merge``` avec le nom de la branche que nous souhaitons fusionner avec **master**.

Dans ce cas, la fusion de nos deux branches revient essentiellement à faire avancer la branche **master** jusqu'au commit pointé par la branche **test**. Git effectue cette opération de manière automatique, ce qui est appelé un **fast forward** (avance rapide).

Ensuite, nous pouvons simplement supprimer la branche **test** en utilisant la commande *$git branch -d**.

Revenons maintenant à la situation précédente, où nous avions deux branches avec des historiques divergents. Cette situation peut être représentée comme suit :

![Représentation d'un lien entre plusieurs acteurs et la boîte noire](branche-7-image-à-remplacer)

Pour fusionner deux branches dans cette situation plus complexe, nous devons d'abord nous placer dans la branche dans laquelle nous souhaitons effectuer la fusion, puis exécuter la commande ```git merge```.

Dans ce cas, il est intéressant d'expliquer comment Git procède pour fusionner les branches. Lors d'une fusion complexe, Git utilise trois sources : le dernier commit commun aux deux branches et le dernier commit de chaque branche.

Au lieu de simplement effectuer un **fast forward**, Git crée automatiquement un nouvel instantané (snapshot) dont le contenu est le résultat de la fusion, puis il crée un commit qui pointe vers cet instantané. Ce commit est appelé un "commit de fusion" et il est spécial car il a plusieurs parents, contrairement aux commits normaux qui n'ont qu'un seul parent.

Il est important de noter que lors d'une fusion à trois sources, des conflits peuvent survenir. Cela se produit notamment si une même partie d'un fichier a été modifiée de différentes manières dans les différentes branches. Lors de la fusion, Git détectera ces conflits et nous demandera de les résoudre avant de finaliser la fusion des branches.

Pour identifier les fichiers à l'origine des conflits, nous pouvons utiliser la commande ```git status```. Par exemple, si nos deux branches ont un fichier **LISEZMOI.txt** avec des contenus différents, Git fusionnera automatiquement ces contenus en un seul fichier. Le fichier résultant contiendra les textes des deux fichiers d'origine, l'un après l'autre, avec des indicateurs de séparation.

Nous devrons alors ouvrir le fichier manuellement et choisir quelles parties conserver (en supprimant les parties non nécessaires, par exemple). Une fois l'édition terminée, nous utiliserons la commande ```git add``` pour marquer le conflit comme résolu. Enfin, nous effectuerons un ```git commit``` pour finaliser le commit de fusion.
