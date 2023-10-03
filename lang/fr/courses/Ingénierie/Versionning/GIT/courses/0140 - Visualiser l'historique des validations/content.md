## Visualiser l’historique des validations

Après avoir créé plusieurs commits ou si vous avez cloné un dépôt ayant un historique de commits, vous souhaitez probablement revoir le fil des évènements. Pour ce faire, la commande **git log** est l’outil le plus basique et le plus puissant.

Les exemples qui suivent utilisent un projet très simple nommé simplegit utilisé pour les démonstrations. Pour récupérer le projet, lancez :

```bash
git clone https://github.com/schacon/simplegit-progit
```

Lorsque vous lancez **git log** dans le répertoire de ce projet, vous devriez obtenir un résultat qui ressemble à ceci :

```bash
$ git log
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number

commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Sat Mar 15 16:40:33 2008 -0700

    removed unnecessary test

commit a11bef06a3f659402fe7563abf99ad00de2209e6
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Sat Mar 15 10:31:28 2008 -0700

    first commit
```

Par défaut, **git log** invoqué sans argument énumère en ordre chronologique inversé les commits réalisés. Cela signifie que les commits les plus récents apparaissent en premier. Comme vous le remarquez, cette commande indique chaque commit avec sa somme de contrôle SHA-1, le nom et l’e-mail de l’auteur, la date et le message du commit.

**git log** dispose d’un très grand nombre d’options permettant de paramétrer exactement ce que l’on cherche à voir. Nous allons détailler quelques-unes des plus utilisées.

Une des options les plus utiles est **-p**, qui montre les différences introduites entre chaque validation. Vous pouvez aussi utiliser **-2** qui limite la sortie de la commande aux deux entrées les plus récentes :

```bash
$ git log -p -2
```

Cette option affiche la même information mais avec un diff suivant directement chaque entrée. C’est très utile pour des revues de code ou pour naviguer rapidement à travers l’historique des modifications qu’un collaborateur a apportées.

Vous pouvez aussi utiliser une liste d’options de résumé avec git log. Par exemple, si vous souhaitez visualiser des statistiques résumées pour chaque commit, vous pouvez utiliser l’option **--stat** :

```bash
$ git log --stat
```

Comme vous pouvez le voir, l’option **--stat** affiche sous chaque entrée de validation une liste des fichiers modifiés, combien de fichiers ont été changés et combien de lignes ont été ajoutées ou retirées dans ces fichiers. Elle ajoute un résumé des informations en fin de sortie. Une autre option utile est **--pretty**. Cette option modifie le journal vers un format différent. Quelques options incluses sont disponibles. L’option **oneline** affiche chaque commit sur une seule ligne, ce qui peut s’avérer utile lors de la revue d’un long journal. En complément, les options short (court), full (complet) et fuller (plus complet) montrent le résultat à peu de choses près dans le même format mais avec plus ou moins d’informations :

```bash
$ git log --pretty=oneline
```

L’option la plus intéressante est **format** qui permet de décrire précisément le format de sortie. C’est spécialement utile pour générer des sorties dans un format facile à analyser par une machine — lorsqu’on spécifie intégralement et explicitement le format, on s’assure qu’il ne changera pas au gré des mises à jour de Git :

```bash
$ git log --pretty=format:"%h - %an, %ar : %s"
```

Options utiles pour **git log --pretty=format** :

| Option | Description du formatage |
| --- | --- |
| **%H** | Somme de contrôle du commit |
| **%h** | Somme de contrôle abrégée du commit |
| **%T** | Somme de contrôle de l’arborescence |
| **%t** | Somme de contrôle abrégée de l’arborescence |
| **%P** | Sommes de contrôle des parents |
| **%p** | Sommes de contrôle abrégées des parents |
| **%an** | Nom de l’auteur |
| **%ae** | E-mail de l’auteur |
| **%ad** | Date de l’auteur (au format de l’option -date=) |
| **%ar** | Date relative de l’auteur |
| **%cn** | Nom du validateur |
| **%ce** | E-mail du validateur |
| **%cd** | Date du validateur |
| **%cr** | Date relative du validateur |
| **%s** | Sujet |

Vous pourriez vous demander quelle est la différence entre auteur et validateur. L'auteur est la personne qui a réalisé initialement le travail, alors que le validateur est la personne qui a effectivement validé ce travail en gestion de version. Donc, si quelqu’un envoie un patch à un projet et un des membres du projet l’applique, les deux personnes reçoivent le crédit — l’écrivain en tant qu’auteur, et le membre du projet en tant que validateur.

Les options **oneline** et **format** sont encore plus utiles avec une autre option **log** appelée **--graph**. Cette option ajoute un joli graphe en caractères ASCII pour décrire l’historique des branches et fusions :

```bash
$ git log --pretty=format:"%h %s" --graph
```

Les options ci-dessus ne sont que des options simples de format de sortie de **git log**. Il y en a de nombreuses autres.

Options usuelles de **git log** :

| Option | Description |
| --- | --- |
| **-p** | Affiche le patch appliqué par chaque commit |
| **--stat** | Affiche les statistiques de chaque fichier pour chaque commit |
| **--shortstat** | N’affiche que les ligne modifiées/insérées/effacées de l’option --stat |
| **--name-only** | Affiche la liste des fichiers modifiés après les informations du commit |
| **--name-status** | Affiche la liste des fichiers affectés accompagnés des informations d’ajout modification/suppression |
| **--abbrev-commit** | N’affiche que les premiers caractères de la somme de contrôle SHA-1 |
| **--relative-date** | Affiche la date en format relatif (par exemple "2 weeks ago" : il y a deux semaines) au lieu du format de date complet |
| **--graph** | Affiche en caractères ASCII le graphe de branches et fusions en vis-à-vis de l’historique |
| **--pretty** | Affiche les commits dans un format alternatif. Les formats incluent oneline, short, full, fuller, et format (où on peut spécifier son propre format) |
| **--oneline** | Option de convenance correspondant à --pretty=oneline --abbrev-commit |