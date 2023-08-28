from pro_filer.actions.main_actions import show_details  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expect",
    [
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
    ],
)
def test_show_details_expect_response(context, expect, capsys):
    show_details(context)
    capt = capsys.readouterr()
    assert capt.out == expect


@pytest.mark.parametrize(
    "context2, expect",
    [
        ({}, KeyError),
        ({"base_path": 1}, AttributeError),
    ],
)
def test_show_details_expect_fail(context2, expect):
    with pytest.raises(expect):
        show_details(context2)


def test_show_details_expect_expected_tmp_path(monkeypatch, tmp_path, capsys):
    new_path = tmp_path / "teste"
    new_path2 = tmp_path / "teste2.txt"
    new_path.write_text("heloo")
    new_path2.write_text("hello word!")
    new_path = str(new_path)
    new_path2 = str(new_path2)

    context = {"base_path": new_path}
    show_details(context)
    capt = capsys.readouterr()
    assert (
        capt.out
        == """File name: teste
File size in bytes: 5
File type: file
File extension: [no extension]
Last modified date: 2023-08-18\n"""
    )

    context = {"base_path": new_path2}
    show_details(context)
    capt = capsys.readouterr()
    assert (
        capt.out
        == """File name: teste2.txt
File size in bytes: 11
File type: file
File extension: .txt
Last modified date: 2023-08-18\n"""
    )
