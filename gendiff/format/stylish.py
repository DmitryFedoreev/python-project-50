def format_value(value, spaces_count=2):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = ' ' * (spaces_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = format_value(inner_value, spaces_count + 4)
            lines.append(f'{indent}  {key}: {formatted_value}')
        formatted_string = '\n'.join(lines)
        end_indent = ' ' * (spaces_count + 2)
        return f'{{\n{formatted_string}\n{end_indent}}}'
    else:
        return str(value)


def format_stylish(diff):
    def _iter(diff, spaces_count=2):
        lines = []

        for key, item in diff.items():
            indent = ' ' * spaces_count

            match item['type']:
                case 'unchanged':
                    current_value = format_value(item['value'], spaces_count)
                    lines.append(f"{indent}  {key}: {current_value}")

                case 'changed':
                    old_value = format_value(item.get('old_value'), spaces_count)
                    new_value = format_value(item.get('new_value'), spaces_count)
                    lines.extend([
                        f'{indent}- {key}: {old_value}',
                        f'{indent}+ {key}: {new_value}'
                    ])

                case 'added':
                    current_value = format_value(item['value'], spaces_count)
                    lines.append(f'{indent}+ {key}: {current_value}')

                case 'removed':
                    current_value = format_value(item['value'], spaces_count)
                    lines.append(f'{indent}- {key}: {current_value}')

                case 'nested':
                    nested_diff = _iter(item['children'], spaces_count + 4)
                    lines.append(f"{indent}  {key}: {nested_diff}")

                case _:
                    raise ValueError(
                        f"Unsupported node type at key: {key}, item: {item}"
                    )

        formatted_string = '\n'.join(lines)
        end_indent = ' ' * (spaces_count - 2)
        return f'{{\n{formatted_string}\n{end_indent}}}'

    return _iter(diff)
