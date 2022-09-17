from gendiff import generate_diff


def test_generate_diff_json(file1_json_path, file2_json_path, result_json):
    assert generate_diff(file1_json_path, file2_json_path) == result_json


def test_generate_diff_yml(file1_yml_path, file2_yml_path, result_yml):
    assert generate_diff(file1_yml_path, file2_yml_path) == result_yml


def test_generate_diff_tree_json(file1_json_tree_path, file2_json_tree_path, result_json_tree):
    assert generate_diff(file1_json_tree_path, file2_json_tree_path) == result_json_tree


def test_generate_diff_tree_yml(file1_yaml_tree_path, file2_yaml_tree_path, result_yaml_tree):
    assert generate_diff(file1_yaml_tree_path, file2_yaml_tree_path) == result_yaml_tree
