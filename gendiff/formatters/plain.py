def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"

    elif isinstance(value, bool):
        return "true" if value else "false"

    elif value is None:
        return "null"

    elif isinstance(value, int):
        return value

    return f"'{value}'"


def tree_to_plain(tree, path=''):
    children = tree.get('children')
    current_path = f"{path}{tree.get('key')}"

    if tree['type'] == "added":
        value = to_str(tree.get("value"))
        return f"Property '{current_path}' was added with value: {value}"

    elif tree['type'] == "removed":
        return f"Property '{current_path}' was removed"

    elif tree['type'] == "updated":
        value1 = to_str(tree.get("old_value"))
        value2 = to_str(tree.get("new_value"))
        return f"Property '{current_path}' was updated. " \
               f"From {value1} to {value2}"

    elif tree['type'] == "parent":
        lines = map(lambda child: tree_to_plain(child, f"{current_path}."), children)
        return '\n'.join(filter(bool, lines))

    elif tree['type'] == "root":
        lines = map(lambda child: tree_to_plain(child, path), children)
        return "\n".join(filter(bool, lines))


def render_plain(diff):
    return tree_to_plain(diff)
