from hexlet_code.parser import parse_file
from hexlet_code.formatters.stylish import format_diff


def generate_diff(first_file, second_file):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    return format_diff(data1, data2)