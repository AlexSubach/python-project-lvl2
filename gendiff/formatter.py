from gendiff.formatters.stylish import formatting_stylish


def formatting(tree, format_name):
    if format_name == "stylish":
        return formatting_stylish(tree)
