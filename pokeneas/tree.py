import os

# Carpetas o archivos que quieres ignorar completamente
EXCLUDE = {'.git', '.env', '__pycache__', 'env', '.idea', '.vscode'}

def print_tree(start_path='.', prefix=''):
    try:
        entries = [
            e for e in os.listdir(start_path)
            if not e.startswith('.') and e not in EXCLUDE
        ]
        entries.sort()

        for i, entry in enumerate(entries):
            path = os.path.join(start_path, entry)
            connector = '└── ' if i == len(entries) - 1 else '├── '
            print(prefix + connector + entry)
            if os.path.isdir(path):
                extension = '    ' if i == len(entries) - 1 else '│   '
                print_tree(path, prefix + extension)
    except PermissionError:
        pass  # Ignora carpetas sin permiso de lectura

if __name__ == '__main__':
    print("Estructura completa del proyecto:\n")
    print_tree('.')
