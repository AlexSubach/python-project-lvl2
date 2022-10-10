def make_children(dict1, dict2):
    result = []
    keys = dict1.keys() | dict2.keys()
    for key in sorted(keys):
        if key not in dict1:
            result.append({"key": key, "type": "added", "value": dict2[key]})

        elif key not in dict2:
            result.append({"key": key, "type": "removed", "value": dict1[key]})

        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result.append({"key": key, "type": "parent", "children": make_children(dict1[key], dict2[key])})

        elif dict1[key] == dict2[key]:
            result.append({"key": key, "type": "unchanged", "value": dict1[key]})

        else:
            result.append({"key": key, "type": "updated", "old_value": dict1[key], "new_value": dict2[key]})
    return result


def make_tree(dict1, dict2):
    return {"type": "root", "children": make_children(dict1, dict2)}
