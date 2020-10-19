# MAP ENTITIES
OBSTACLE = '*'
CONTROL_POINT = '#'
GOAL = '$'
FREE_PATH = '.'

# PROJECT PROPERTIES
LOG = False

# Commom functions


def print_queue(q):
    for c in q:
        print("[{},{}]".format(c[0], c[1]), end='')
    print()
