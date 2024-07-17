import os
import pytest
from gendiff import generate_diff


FIXTURES_DIR = os.path.abspath('tests/fixtures')
FILE1_JSON = os.path.join(FIXTURES_DIR, 'file1.json')
FILE2_JSON = os.path.join(FIXTURES_DIR, 'file2.json')
FILE1_YML = os.path.join(FIXTURES_DIR, 'file1.yml')
FILE2_YML = os.path.join(FIXTURES_DIR, 'file2.yml')
DIFF_TXT = os.path.join(FIXTURES_DIR, 'diff.txt')
JSON_OUTPUT_TXT = os.path.join(FIXTURES_DIR, 'json_output.txt')


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize("file1, file2, expected_file, formatter", [
    (FILE1_JSON, FILE2_JSON, DIFF_TXT, "stylish"),
    (FILE1_YML, FILE2_YML, DIFF_TXT, "stylish"),
    (FILE1_JSON, FILE2_JSON, JSON_OUTPUT_TXT, "json"),
    (FILE1_YML, FILE2_YML, JSON_OUTPUT_TXT, "json"),
])
def test_generate_diff(file1, file2, expected_file, formatter):
    expected_result = read_file(expected_file)
    result = generate_diff(file1, file2, formatter)
    assert result == expected_result, (
        f"Failed on {formatter} with {file1} and {file2}"
    )
