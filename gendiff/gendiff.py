from gendiff.parser import get_file_extension
from gendiff.tree import make_tree
from gendiff.formatter import formatting


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict_1 = get_file_extension(file_path1)
    dict_2 = get_file_extension(file_path2)
    tree = make_tree(dict_1, dict_2)
    diff = formatting(tree, format_name)
    return diff
