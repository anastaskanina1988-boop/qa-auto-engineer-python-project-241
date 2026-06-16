import json


def format_json(data1, data2):
    result = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in keys:
        if key not in data2:
            result.append({
                'key': key,
                'status': 'removed',
                'value': data1[key],
            })
        elif key not in data1:
            result.append({
                'key': key,
                'status': 'added',
                'value': data2[key],
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'status': 'unchanged',
                'value': data1[key],
            })
        else:
            result.append({
                'key': key,
                'status': 'changed',
                'oldValue': data1[key],
                'newValue': data2[key],
            })

    return json.dumps(result, indent=4)
