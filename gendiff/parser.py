import json
import yaml
import os.path


def parse(file, format_name):
    if format_name == ".json":
        return json.load(file)

    elif format_name == ".yaml" or format_name == ".yml":
        return yaml.safe_load(file)

    raise ValueError("Unknown format")


def get_data(file_path):
    extension = os.path.splitext(file_path)[1]
    file = open(file_path)
    if extension == ".json":
        return parse(file, extension)
    elif extension == ".yaml" or extension == ".yml":
        return parse(file, extension)
