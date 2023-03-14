import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    return head


filename = __file__
breakpoint()
print(f'path = {get_path(filename)}')