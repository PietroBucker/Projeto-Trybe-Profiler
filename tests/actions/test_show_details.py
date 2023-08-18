from pro_filer.actions.main_actions import show_details  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expect",
    [
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
        (
            {"base_path": "pro_filer.egg-info/"},
            """File name: 
File size in bytes: 4096
File type: directory
File extension: [no extension]
Last modified date: 2023-08-16\n""",
        ),
        (
            {"base_path": "pro_filer.egg-info/SOURCES.txt"},
            """File name: SOURCES.txt
File size in bytes: 1318
File type: file
File extension: .txt
Last modified date: 2023-08-16\n""",
        ),
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
