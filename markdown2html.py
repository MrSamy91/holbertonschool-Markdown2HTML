#!/usr/bin/python3
"""
Script to convert Markdown to HTML.
"""
import sys
import os


def convert_markdown_to_html(content):
    """Convert markdown content to HTML"""
    html_lines = []
    
    for line in content.split('\n'):
        # Skip empty lines
        if not line.strip():
            continue
            
        # Handle headers
        if line.startswith('#'):
            # Count the number of # to determine header level
            level = 0
            for char in line:
                if char == '#':
                    level += 1
                else:
                    break
                    
            # Ensure header level is between 1 and 6
            if 1 <= level <= 6:
                # Remove the #s and leading/trailing spaces
                header_text = line[level:].strip()
                html_lines.append(f"<h{level}>{header_text}</h{level}>")
        else:
            html_lines.append(line)
            
    return '\n'.join(html_lines)


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

        # Convertir le markdown en HTML
        html_content = convert_markdown_to_html(content)

        # Écrire le contenu HTML dans le fichier de sortie
        with open(html_file, 'w') as html:
            html.write(html_content)

    except Exception as e:
        sys.exit(1)

    # Si tout est OK, sortir avec succès
    sys.exit(0)


if __name__ == "__main__":
    main()