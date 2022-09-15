import os
import pytest


@pytest.fixture
def file1_json_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')


@pytest.fixture
def file2_json_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')


@pytest.fixture
def result_stylish_json():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'result_stylish_json.txt')
    with open(result_path) as file:
        return file.read()


@pytest.fixture
def file1_yml_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')


@pytest.fixture
def file2_yml_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')


@pytest.fixture
def result_stylish_yml():
    result_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'result_stylish_yml.txt')
    with open(result_path) as file:
        return file.read()
