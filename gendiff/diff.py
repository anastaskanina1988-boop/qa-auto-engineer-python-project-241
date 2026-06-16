from .parser import parse_file
from .formatters.stylish import format_diff
from .formatters.plain import format_plain
from .formatters.json import format_json


def generate_diff(first_file, second_file, format_name='stylish'):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    if format_name == 'plain':
        return format_plain(data1, data2)

    if format_name == 'json':
        return format_json(data1, data2)

    if format_name == 'stylish':
        return format_diff(data1, data2)

    raise ValueError(f'Unknown format: {format_name}')
