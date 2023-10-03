La création de branches dans Git est une opération légère et efficace grâce à la manière dont Git gère les branches. Contrairement à la plupart des systèmes de contrôle de version, Git n'effectue pas une copie physique complète du répertoire de travail à chaque création de branche. Au lieu de cela, Git utilise un modèle de pointeurs et d'objets pour gérer les branches.

Dans Git, une branche est simplement un pointeur vers un commit spécifique. Chaque commit dans Git est identifié par une empreinte SHA-1, une chaîne de 40 caractères. Lorsque vous effectuez un commit, Git stocke un objet commit qui contient des informations sur l'auteur du commit, le message de commit et un pointeur vers un instantané du contenu indexé à ce moment-là. De plus, Git enregistre également des pointeurs vers les commits précédents qui constituent l'historique de votre projet.

La branche par défaut dans Git est généralement appelée **master**. Cette branche master est simplement un pointeur qui se déplace automatiquement vers le dernier commit effectué chaque fois qu'un nouveau commit est créé dans cette branche.

Il est important de noter que dans Git, la branche **master** n'est pas spéciale ni traitée différemment des autres branches. Elle porte ce nom par convention, mais vous pouvez la renommer si vous le souhaitez, bien que cela soit rarement nécessaire.

En résumé, créer une nouvelle branche dans Git consiste simplement à créer un nouveau pointeur qui pointe vers un commit existant. Cela rend les opérations de création de branches rapides et légères, car elles ne nécessitent pas de copier l'intégralité du répertoire de travail. Git tire parti de son modèle de pointeurs et d'objets pour gérer efficacement les branches et les historiques de projet.
