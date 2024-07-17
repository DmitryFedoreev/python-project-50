from gendiff.format.json import json_format
from gendiff.format.stylish import format_stylish


def format_diff(diff, formatter):
    match formatter:
        case 'stylish':
            return format_stylish(diff)
        case 'json':
            return json_format(diff)
        case _:
            raise ValueError(f"Unsupported formatter: {formatter}")
