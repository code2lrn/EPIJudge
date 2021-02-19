from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    path_stack = []
    if path[0] == '/':
        path_stack.append('/')

    for dir in (d for d in path.split('/') if d not in ['', '.']):
        if dir == '.':
            continue
        elif dir == '..':
            if not path_stack or path_stack[-1] == '..':
                path_stack.append(dir)
            else:
                path_stack.pop()
        else:
            path_stack.append(dir)

    normalized = '/'.join(path_stack)
    return normalized[normalized.startswith('//'):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
