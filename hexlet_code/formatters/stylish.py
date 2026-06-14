def format_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = ['{']

    for key in keys:
        if key not in data2:
            result.append(f'  - {key}: {str(data1[key]).lower()}')
        elif key not in data1:
            result.append(f'  + {key}: {str(data2[key]).lower()}')
        elif data1[key] == data2[key]:
            result.append(f'    {key}: {str(data1[key]).lower()}')
        else:
            result.append(f'  - {key}: {str(data1[key]).lower()}')
            result.append(f'  + {key}: {str(data2[key]).lower()}')

    result.append('}')

    return '\n'.join(result)