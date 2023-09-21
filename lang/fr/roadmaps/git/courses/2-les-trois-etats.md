## Les trois états

Il est essentiel de garder à l'esprit les éléments suivants si vous souhaitez que la suite de votre apprentissage se déroule en douceur. Git gère trois états dans lesquels les fichiers peuvent se trouver : validé, modifié et indexé.

- **Validé** signifie que les données sont enregistrées en toute sécurité dans votre base de données locale.
- **Modifié** indique que vous avez apporté des modifications au fichier, mais qu'il n'a pas encore été enregistré dans la base de données de Git.
- **Indexé** signifie que vous avez marqué un fichier modifié dans sa version actuelle pour qu'il fasse partie de la prochaine capture d'écran (instantané) du projet.

Ces concepts nous conduisent aux trois sections principales d'un projet Git : le répertoire Git, le répertoire de travail et la zone d'index.

Le répertoire Git constitue la zone où Git stocke les métadonnées essentielles et la base de données d'objets de votre projet. C'est la partie fondamentale de Git, et c'est ce qui est reproduit lorsque vous effectuez un clonage (clone) d'un dépôt à partir d'un autre ordinateur.

Le répertoire de travail représente une copie unique d'une version spécifique du projet. Ces fichiers sont extraits de la base de données compressée du répertoire Git et sont placés sur votre disque dur pour être utilisés ou modifiés.

La zone d'index est simplement un fichier, généralement situé dans le répertoire Git, qui stocke des informations sur les fichiers qui seront inclus dans le prochain instantané (commit). Parfois, on l'appelle également la zone de préparation.

Le processus standard d'utilisation de Git se déroule comme suit :

1. Vous apportez des modifications aux fichiers de votre répertoire de travail.
2. Vous indexez les fichiers modifiés, ce qui signifie que vous ajoutez des instantanés de ces fichiers à la zone d'index.
3. Vous effectuez une validation (commit), ce qui transfère les instantanés des fichiers de la zone d'index vers la base de données du répertoire Git.

Si une version particulière d'un fichier se trouve dans le répertoire Git, elle est considérée comme validée. Si un fichier a été modifié mais ajouté à la zone d'index, il est indexé. Enfin, s'il a été modifié depuis le dernier instantané mais n'a pas été indexé, il est considéré comme modifié.

## Ligne de commande

Il existe plusieurs approches pour utiliser Git, notamment les outils originaux en ligne de commande et de nombreuses interfaces graphiques dotées de fonctionnalités diverses. Dans ce cours, nous allons privilégier l'utilisation de Git en ligne de commande. Tout d'abord, la ligne de commande est la seule interface qui permet d'exécuter toutes les commandes Git ; la plupart des interfaces graphiques simplifient l'utilisation en ne couvrant qu'une partie des fonctionnalités de Git. Si vous maîtrisez l'utilisation de la ligne de commande, vous serez également capable de comprendre le fonctionnement des interfaces graphiques, mais l'inverse n'est pas nécessairement vrai. De plus, le choix d'une interface graphique dépend souvent des préférences personnelles, mais tous les utilisateurs auront accès aux commandes en ligne, préalablement installées et prêtes à l'emploi.

Nous supposons que vous savez comment ouvrir un Terminal sur un Mac ou une invite de commandes ou PowerShell sur Windows. Si ce n'est pas le cas, vous devrez d'abord vous familiariser avec ces applications pour être en mesure de suivre les exemples qui suivront dans ce cours.
