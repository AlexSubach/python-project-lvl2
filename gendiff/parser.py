import json
import yaml


def parse(file, extension):
    if extension == ".json":
        return json.load(open(file))
    elif extension == ".yaml" or extension == ".yml":
        return yaml.safe_load(open(file))
