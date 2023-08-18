"""Arquivo que estudantes não devem editar"""

from datetime import date
import filecmp
import itertools
from pro_filer.cli_helpers import _get_printable_file_path
import os


def find_duplicate_files(context):
    """
    Encontra arquivos duplicados, comparando todos os arquivos entre si.
    Retorna uma lista de tuplas com os pares de arquivos duplicados.
    """

    all_files = context["all_files"]
    duplicate_files = []

    for file1, file2 in itertools.combinations(all_files, 2):
        try:
            if filecmp.cmp(file1, file2, shallow=False):
                duplicate_files.append((file1, file2))
        except FileNotFoundError:
            raise ValueError("All files must exist")

    return duplicate_files

context = {
    "all_files": [
        ".gitignore",
        "src/app.py",
        "src/utils/__init__.py",
    ]
}
find_duplicate_files(context)