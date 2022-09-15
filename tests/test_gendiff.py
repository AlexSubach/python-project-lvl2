from gendiff import generate_diff


def test_generate_diff_stylish_json(file1_json_path, file2_json_path, result_stylish_json):
    assert generate_diff(file1_json_path, file2_json_path) == result_stylish_json
