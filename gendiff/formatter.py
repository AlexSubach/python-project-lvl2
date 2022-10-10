from gendiff.formatters.stylish import render_stylish


def formatting(result_dict, format_name="stylish"):
    if format_name == "stylish":
        return render_stylish(result_dict)
