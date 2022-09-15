# import json
import os
from gendiff.parser import parse


def get_file_extension(file_path):
    (name, file_extension) = os.path.splitext(file_path)
    file = open(file_path)
    return parse(file, file_extension)


def generate_diff(file_path1, file_path2):
    dict1 = get_file_extension(file_path1)
    dict2 = get_file_extension(file_path2)
    result = '{\n'
    keys = dict1.keys() | dict2.keys()
    for key in sorted(keys):
        if key not in dict2:
            result += f'  - {key}: {dict1[key]}\n'
        elif key not in dict1:
            result += f'  + {key}: {dict2[key]}\n'
        elif dict1[key] == dict2[key]:
            result += f'    {key}: {dict1[key]}\n'
        elif dict1[key] != dict2[key]:
            result += f'  - {key}: {dict1[key]}\n' \
                      f'  + {key}: {dict2[key]}\n'
    return result.lower() + '}'
