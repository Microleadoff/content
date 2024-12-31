import os

def collect_markdown_files(root_dir="."):
    """
    Collecte tous les fichiers .md à partir du répertoire racine donné, dans l'ordre des dossiers.
    
    Args:
        root_dir (str): Répertoire de départ pour la recherche.
    
    Returns:
        list: Liste des chemins relatifs des fichiers .md triés.
    """
    markdown_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in sorted(filenames):  # Tri des fichiers dans chaque dossier
            if file.endswith(".md"):
                markdown_files.append(os.path.join(dirpath, file))
    return sorted(markdown_files, key=lambda x: os.path.dirname(x))  # Tri par dossiers

def merge_markdown_files(output_file="final.md"):
    """
    Lit tous les fichiers .md dans l'ordre des dossiers et les fusionne dans un fichier unique.
    
    Args:
        output_file (str): Nom du fichier de sortie.
    """
    markdown_files = collect_markdown_files()
    with open(output_file, "w", encoding="utf-8") as final_file:
        for file_path in markdown_files:
            with open(file_path, "r", encoding="utf-8") as md_file:
                final_file.write(f"# Contenu de {file_path}\n\n")  # Optionnel : titre pour chaque fichier
                final_file.write(md_file.read() + "\n\n")
    print(f"Fusion terminée. Contenu sauvegardé dans {output_file}")

if __name__ == "__main__":
    merge_markdown_files()
