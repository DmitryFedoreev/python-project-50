import json
import yaml


def parse_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def parse_yaml(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def parse_file(file_path):
    if file_path.endswith(('.yml', '.yaml')):
        return parse_yaml(file_path)
    elif file_path.endswith('.json'):
        return parse_json(file_path)
    else:
        raise ValueError('Unsupported file format')
