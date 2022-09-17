import os
import pytest


@pytest.fixture
def file1_json_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')


@pytest.fixture
def file2_json_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')


@pytest.fixture
def result_json():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'result_json')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def file1_yml_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')


@pytest.fixture
def file2_yml_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')


@pytest.fixture
def result_yml():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'result_yml')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def file1_json_tree_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1_tree.json')


@pytest.fixture
def file2_json_tree_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2_tree.json')


@pytest.fixture
def result_json_tree():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'result_json_tree')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def file1_yaml_tree_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1_tree.yaml')


@pytest.fixture
def file2_yaml_tree_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2_tree.yaml')


@pytest.fixture
def result_yaml_tree():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'result_yaml_tree')
    with open(result_path) as file:
        return file.read()
