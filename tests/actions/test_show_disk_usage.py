from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import Mock
# @pytest.mark.parametrize(
#     "context, expect",
#     [
#         ({"all_files": []}, 'Total size: 0\n'),
#         (
#             {
#                 "all_files": [
#                     "pro_filer/__main__.py", "pro_filer/__init__.py",
#                 ]
#             },
#             f"""'pro_filer/__main__.py':{''.ljust(47)}129 (100%)
# 'pro_filer/__init__.py':{' '.ljust(47)}0 (0%)
# Total size: 129\n""",
#         )
#     ],
# )


def test_show_disk_usage_expected(monkeypatch, tmp_path, capsys):
    mock = Mock(return_value='teste.txt')
    new_path = tmp_path / "teste.txt"
    new_path2 = tmp_path / "teste2.txt"
    new_path.write_text('heloo')
    new_path2.write_text('hello word!')
    new_path = str(new_path)
    new_path2 = str(new_path2)
    context = {"all_files": [new_path, new_path2]}
    funct_path = (
        'pro_filer.actions.main_actions._get_printable_file_path'
        )
    monkeypatch.setattr(funct_path, mock)
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == f''''teste.txt':{''.ljust(59)}11 (68%)
'teste.txt':{''.ljust(59)}5 (31%)
Total size: 16\n'''
