import pytest
import json


@pytest.fixture
def file_paths():
    file1_path = '/home/dmitry/PycharmProjects/python-project-50/file1.json'
    file2_path = '/home/dmitry/PycharmProjects/python-project-50/file2.json'
    return file1_path, file2_path


def test_generate_diff(file_paths):
    file1_path, file2_path = file_paths

    with open(file1_path) as f1, open(file2_path) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
