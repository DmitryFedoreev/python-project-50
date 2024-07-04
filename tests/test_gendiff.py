import pytest


@pytest.fixture
def file_paths():
    file1_path = 'file1.json'
    file2_path = 'file2.json'
    return file1_path, file2_path


def test_generate_diff(file_paths):
    file1_path, file2_path = file_paths


