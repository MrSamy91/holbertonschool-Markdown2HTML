#!/usr/bin/python3
"""
Script to convert Markdown to HTML.
"""
import sys
import os


def main():
    """Main function to handle markdown to html conversion"""
    # Vérifier le nombre d'arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Récupérer les noms de fichiers des arguments
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérifier si le fichier markdown existe
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    try:
        # Lire le contenu du fichier markdown
        with open(markdown_file, 'r') as md:
            content = md.read()

        # Créer le fichier HTML (pour l'instant, juste copier le contenu)
        with open(html_file, 'w') as html:
            html.write(content)

    except Exception as e:
        sys.exit(1)

    # Si tout est OK, sortir avec succès
    sys.exit(0)


if __name__ == "__main__":
    main()