def get_indent(depth):
    return " " * (depth * 4 - 2)


def make_to_string(value, depth):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent = get_indent(depth)
        current_indent = indent + (" " * 6)
        lines = []
        for k, v in value.items():
            lines.append(f"{current_indent}{k}: {make_to_string(v, depth + 1)}")
        result = "\n".join(lines)
        return f'{{\n{result}\n  {indent}}}'
    return value


def inner(tree, depth=0):
    children = tree.get('children')
    indent = get_indent(depth)
    formatted_value = make_to_string(tree.get('value'), depth)
    formatted_value1 = make_to_string(tree.get('old_value'), depth)
    formatted_value2 = make_to_string(tree.get('new_value'), depth)
    if tree['type'] == 'root':
        lines = map(lambda child: inner(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    if tree['type'] == 'nested':
        lines = map(lambda child: inner(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {tree['key']}: {{\n{result}\n  {indent}}}"
    if tree['type'] == 'changed':
        line1 = f"{indent}- {tree['key']}: {formatted_value1}\n"
        line2 = f"{indent}+ {tree['key']}: {formatted_value2}"
        result = line1 + line2
        return result
    if tree['type'] == 'unchanged':
        return f"{indent}  {tree['key']}: {formatted_value}"
    if tree['type'] == 'removed':
        return f"{indent}- {tree['key']}: {formatted_value}"
    if tree['type'] == 'added':
        return f"{indent}+ {tree['key']}: {formatted_value}"


def formatting_stylish(tree):
    return inner(tree)
