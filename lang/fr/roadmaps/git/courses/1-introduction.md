## Introduction

Qu'est-ce que la gestion de version et pourquoi est-il important de la comprendre ? La gestion de version est un
processus qui permet de suivre l'évolution d'un fichier ou d'un ensemble de fichiers au fil du temps, offrant ainsi la
possibilité de restaurer des versions antérieures à tout moment. Dans les exemples présentés, nous
utiliserons des fichiers sources de logiciels comme exemples de fichiers soumis à la gestion de version (exemple: .env,
.md, .js), mais il est important de noter que cette approche peut être appliquée à pratiquement tous les types de
fichiers présents sur un ordinateur.

Que vous soyez un graphiste, un développeur web ou tout autre professionnel souhaitant conserver toutes les versions
d'une image ou d'une mise en page (ce qui est souvent une exigence cruciale), un système de gestion de version (ou VCS
pour Version Control System en anglais) est un outil judicieux à utiliser. Il vous permet de restaurer un fichier à un
état précédent, de ramener l'ensemble du projet à un état antérieur, de suivre les modifications au fil du temps,
d'identifier qui a apporté des modifications pouvant potentiellement poser problème, de déterminer qui a introduit un
bug et quand, et bien d'autres fonctionnalités utiles. L'utilisation d'un VCS signifie également généralement que vous
pouvez facilement revenir à une version stable en cas d'erreur ou de perte de fichiers, avec un minimum d'effort
supplémentaire.

## L'histoire de Git

Git est issu d'une combinaison de créativité visionnaire et de controverses passionnées. Le projet du noyau Linux, qui
est un projet open source de grande envergure, a connu différentes méthodes de gestion des modifications au fil du
temps. Pendant la majeure partie de son existence (1991-2002), les modifications étaient soumises sous forme de
correctifs et d'archives de fichiers. Cependant, en 2002, le projet du noyau Linux a adopté l'utilisation d'un système
de gestion de version distribué (DVCS) propriétaire appelé BitKeeper.

En 2005, des différents sont survenus entre la communauté du développement du noyau Linux et la société derrière
BitKeeper, ce qui a entraîné la fin de la gratuité de l'outil. Cet événement a incité la communauté du développement de
Linux, en particulier Linus Torvalds, le créateur de Linux, à développer son propre système en tirant des enseignements
de l'expérience avec BitKeeper. Les objectifs clés du nouveau système étaient les suivants :

- Rapidité,
- Conception simple,
- Prise en charge des développements non linéaires (avec la capacité de gérer des milliers de branches parallèles),
- Entièrement distribué,
- Capacité à gérer efficacement des projets de grande envergure comme le noyau Linux, en offrant rapidité et efficacité,
  dans la gestion des données.

Depuis sa création en 2005, Git a évolué et s'est perfectionné pour devenir convivial tout en conservant ses
caractéristiques fondamentales. Il est réputé pour sa vitesse impressionnante, son efficacité dans la gestion de grands
projets et son système de gestion de branches exceptionnellement puissant, idéal pour les développements non linéaires.
