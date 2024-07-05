import pytest


@pytest.fixture
def file_paths():
    file1_path = 'file1.json'
    file2_path = 'file2.json'
    return file1_path, file2_path


def test_generate_diff(file_paths):
    return file_paths


@pytest.fixture
def file_yaml():
    file1_yml = 'filepath1.yml'
    file2_yml = 'filepath2.yml'
    return file1_yml, file2_yml


expected_output = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_yaml(file_yaml):
    return expected_output
