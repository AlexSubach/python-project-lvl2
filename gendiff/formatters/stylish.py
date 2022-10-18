def build_indent(depth):
    return " " * (depth * 4 - 2)


def to_str(value, depth):
    if isinstance(value, bool):
        return "true" if value else "false"

    elif value is None:
        return "null"

    elif isinstance(value, dict):
        indent = build_indent(depth)
        big_indent = indent + (" " * 6)
        line = []
        for k, v in value.items():
            line.append(f"{big_indent}{k}: {to_str(v, depth + 1)}")
        result = "\n".join(line)
        return f'{{\n{result}\n  {indent}}}'

    return value


def tree_to_stylish(tree, depth=0):
    children = tree.get("children")
    key = tree.get("key")
    value = to_str(tree.get("value"), depth)
    value1 = to_str(tree.get("old_value"), depth)
    value2 = to_str(tree.get("new_value"), depth)
    indent = build_indent(depth)

    if tree["type"] == "root":
        lines = map(lambda child: tree_to_stylish(child, depth + 1), children)
        result = "\n".join(lines)
        return f"{{\n{result}\n}}"

    elif tree["type"] == "parent":
        lines = map(lambda child: tree_to_stylish(child, depth + 1), children)
        result = "\n".join(lines)
        return f"{indent}  {key}: {{\n{result}\n  {indent}}}"

    elif tree["type"] == "added":
        return f"{indent}+ {key}: {value}"

    elif tree["type"] == "removed":
        return f"{indent}- {key}: {value}"

    elif tree["type"] == "unchanged":
        return f"{indent}  {key}: {value}"

    elif tree["type"] == "updated":
        line1 = f"{indent}- {key}: {value1}\n"
        line2 = f"{indent}+ {key}: {value2}"
        return line1 + line2


def render_stylish(diff):
    return tree_to_stylish(diff)
