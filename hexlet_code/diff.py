from hexlet_code.parser import parse_file
from hexlet_code.formatters.stylish import format_diff
from hexlet_code.formatters.plain import format_plain
from hexlet_code.formatters.json import format_json


def generate_diff(first_file, second_file, format_name='stylish'):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    if format_name == 'plain':
        return format_plain(data1, data2)

    if format_name == 'json':
        return format_json(data1, data2)

    return format_diff(data1, data2)