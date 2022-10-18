from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def formatting(result_dict, format_name="stylish"):
    if format_name == "stylish":
        return render_stylish(result_dict)

    if format_name == "plain":
        return render_plain(result_dict)

    if format_name == "json":
        return render_json(result_dict)
