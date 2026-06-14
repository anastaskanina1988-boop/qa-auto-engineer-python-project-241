import json


def format_json(data1, data2):
    return json.dumps(
        {
            'file1': data1,
            'file2': data2,
        },
        indent=4,
    )