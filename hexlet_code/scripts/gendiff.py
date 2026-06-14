import argparse
import json


def generate_diff(first_file, second_file):
    with open(first_file) as file1:
        data1 = json.load(file1)

    with open(second_file) as file2:
        data2 = json.load(file2)

    return data1, data2


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output',
    )

    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()