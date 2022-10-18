import os
import pytest


@pytest.fixture
def file1_json():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')


@pytest.fixture
def file2_json():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')


@pytest.fixture
def file1_yml():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')


@pytest.fixture
def file2_yml():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')


@pytest.fixture
def file1_json_tree():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1_tree.json')


@pytest.fixture
def file2_json_tree():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2_tree.json')


@pytest.fixture
def file1_yaml_tree():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1_tree.yaml')


@pytest.fixture
def file2_yaml_tree():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2_tree.yaml')


@pytest.fixture
def result_json_first():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'json_first')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def result_stylish():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'stylish')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def result_plain():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'plain')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def result_json():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'json')
    with open(result_path) as file:
        return file.read()
