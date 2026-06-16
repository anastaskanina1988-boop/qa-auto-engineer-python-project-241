def format_plain(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = []

    for key in keys:
        if key not in data2:
            result.append(f"Property '{key}' was removed")
        elif key not in data1:
            result.append(
                f"Property '{key}' was added with value: {str(data2[key]).lower()}"
            )
        elif data1[key] != data2[key]:
            result.append(
                f"Property '{key}' was updated. "
                f"From {data1[key]} to {data2[key]}"
            )

    return '\n'.join(result)