Il est courant de constater que certains types de fichiers présents dans la copie de travail ne doivent pas être ajoutés automatiquement, voire ne doivent même pas être pris en compte pour le suivi de version. Ces fichiers comprennent notamment ceux générés automatiquement, tels que les fichiers journaux ou de sauvegarde produits par les outils que vous utilisez. Dans de tels cas, vous pouvez spécifier les modèles de noms de fichiers à ignorer en créant un fichier nommé **.gitignore** placé à la racine du projet. Voici un exemple de contenu pour un fichier **.gitignore** :

```bash
*.[oa]
*~
```

La première ligne indique à Git d'ignorer tous les fichiers ayant une extension ".o" ou ".a", qui sont généralement des fichiers objets ou des archives générés lors de la compilation d'un programme. La deuxième ligne demande à Git d'ignorer tous les fichiers se terminant par un tilde (~), comme c'est le cas pour les fichiers temporaires générés par de nombreux éditeurs de texte tels qu'Emacs. Vous pouvez également spécifier d'autres fichiers ou répertoires à ignorer, tels que "log", "tmp", des répertoires de documentation générée automatiquement, ou tout autre fichier. Définir un fichier **.gitignore** avant de commencer à travailler est généralement une bonne pratique pour éviter d'inclure par mégarde des fichiers qui ne devraient pas être suivis dans le dépôt Git.

Les règles pour créer des modèles à placer dans le fichier **.gitignore** sont les suivantes :

- Les lignes vides ou commençant par "#" sont ignorées, il s'agit de commentaires,
- Les modèles standard de fichiers peuvent être utilisés.
- Si un modèle se termine par une barre oblique ("/"), il fait référence à un répertoire.
- Un modèle commençant par un point d'exclamation ("!") indique des fichiers à inclure malgré les autres règles.

Les modèles standards de fichiers sont des expressions régulières simplifiées utilisées par les interpréteurs de commandes (shells). Un astérisque (*) correspond à un ou plusieurs caractères, "[abc]" correspond à l'un des trois caractères énumérés entre les crochets (c'est-à-dire "a", "b" ou "c"), et un point d'interrogation ("?") correspond à un seul caractère. Les crochets entourant des caractères séparés par un tiret ("[0-9]") correspondent à un caractère compris dans l'intervalle défini par les deux caractères spécifiés (par exemple, de 0 à 9). Vous pouvez également utiliser deux astérisques ("") pour indiquer une série de répertoires inclus, ce qui signifie que "a//z" correspondra à "a/z", "a/b/z", "a/b/c/z", et ainsi de suite.

Voici un autre exemple de contenu pour un fichier **.gitignore** :

```bash
# Ne pas ignorer les fichiers .a
*.a

# Cependant, suivre le fichier lib.a malgré la règle précédente
!lib.a

# Ignorer uniquement le fichier TODO à la racine du projet
/TODO

# Ignorer tous les fichiers du répertoire build
build/

# Ignorer doc/notes.txt, mais pas doc/server/arch.txt
doc/*.txt

# Ignorer tous les fichiers .txt sous le répertoire doc/
doc/**/*.txt
```
