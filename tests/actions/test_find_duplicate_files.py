from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_fail():
    context = {
        "all_files": [
            ".gitignore",
            "src/app.py",
            "src/utils/__init__.py",
        ]
    }
    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)


def test_find_duplicate_expected():
    context = {
        "all_files": [
            "./tests/__init__.py",
            "./tests/actions/__init__.py",
            "./pro_filer/__init__.py",
        ]
    }
    assert find_duplicate_files(context) == [
        ("./tests/__init__.py", "./tests/actions/__init__.py"),
        ("./tests/__init__.py", "./pro_filer/__init__.py"),
        ("./tests/actions/__init__.py", "./pro_filer/__init__.py"),
    ]


def test_show_disk_usage_expected_tmp_path(monkeypatch, tmp_path, capsys):
    new_path = tmp_path / "teste.txt"
    new_path2 = tmp_path / "teste2.txt"
    new_path.write_text("heloo")
    new_path2.write_text("hello word!")
    new_path = str(new_path)
    new_path2 = str(new_path2)
    context = {"all_files": [new_path, new_path2]}
    assert find_duplicate_files(context) == []
