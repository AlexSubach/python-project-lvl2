from gendiff import generate_diff


def test_stylish_json(file1_json_tree, file2_json_tree, result_stylish):
    assert generate_diff(file1_json_tree, file2_json_tree) == result_stylish


def test_stylish_yml(file1_yaml_tree, file2_yaml_tree, result_stylish):
    assert generate_diff(file1_yaml_tree, file2_yaml_tree) == result_stylish


def test_plain(file1_json_tree, file2_json_tree, result_plain):
    assert generate_diff(file1_json_tree, file2_json_tree, format_name='plain') == result_plain


def test_json(file1_json_tree, file2_json_tree, result_json):
    assert generate_diff(file1_json_tree, file2_json_tree, format_name='json') == result_json
