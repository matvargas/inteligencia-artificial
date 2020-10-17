import sys

# MAP ENTITIES
OBSTACLE = '*'
CONTROL_POINT = '#'
GOAL = '$'
FREE_PATH = '.'

shed_map = []  # Maps the shed into a matrix of chars


def print_matrix(m):
    for l in m:
        for char in l:
            print(char, end='')
        print()


def define_entrances(x_dim, y_dim):
    entries = []

    # Adds all possible entrances from north side of shed
    for i in range(0, y_dim):
        if shed_map[0][i] != OBSTACLE:
            entries.append([0, i])

    # Adds all possible entrances from south side of shed
    for i in range(0, y_dim):
        if shed_map[x_dim-1][i] != OBSTACLE:
            entries.append([x_dim-1, i])

    # Adds all possible entrances from west side of shed
    for i in range(0, x_dim):
        if shed_map[i][0] != OBSTACLE:
            entries.append([i, 0])

    # Adds all possible entrances from east side of shed
    for i in range(0, x_dim):
        if shed_map[i][y_dim-1] != OBSTACLE:
            entries.append([i, y_dim-1])

    return entries


try:
    filepath = sys.argv[1]
    f = open(filepath, "r")
except FileNotFoundError:
    print("Could not open the file" + filepath)
finally:
    with open(filepath) as f:
        row = f.readline()
        x_dim = int(row[0])  # Defines x dimension of map
        y_dim = int(row[2])  # Defines y dimension of map
        w = int(row[4])  # Defines how far can the robot goes without reach a control point

        x_count = 0
        y_count = 0
        arr = []

        while True:
            c = f.read(1)
            if not c:
                break
            if c != '' and ord(c) != 10:
                arr.append(c)
                y_count += 1
            if y_count % y_dim == 0:
                if arr:
                    shed_map.append(arr)
                    arr = []

        define_entrances(x_dim, y_dim)