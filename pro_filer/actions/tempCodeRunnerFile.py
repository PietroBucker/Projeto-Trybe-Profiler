def show_preview(context):
    """Mostra uma prévia dos detalhes do arquivo ou diretório"""

    print(
        f'Found {len(context["all_files"])} files '
        f'and {len(context["all_dirs"])} directories'
    )
    if context["all_files"] or context["all_dirs"]:
        print(f'First 5 files: {context["all_files"][:5]}')
        print(f'First 5 directories: {context["all_dirs"][:5]}')


context = {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/app.py",
                    "src/app.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            }
show_preview(context)