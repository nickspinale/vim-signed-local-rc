import os.path


def from_here(*segments):
    here = os.path.dirname(__file__)
    path = (here,) + segments
    return os.path.join(*path)
