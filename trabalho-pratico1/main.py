import sys


class MCell:
    def __init__(self, xpos, ypos, value):
        self.xpos = xpos
        self.ypos = ypos
        self.value = value


def print_matrix(m):
    for l in m:
        for char in l:
            print(char, end='')
        print()


def define_possible_entries(shed_map, w):
    start_x = 0
    start_y = 0
    star_point = True
    for i in shed_map:
        for j in i:
            if star_point:
                start_x = i
                start_y = j


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
        shed_map = []  # Maps the shed into a matrix of chars

        while True:
            c = f.read(1)
            if not c:
                break
            if c != '' and ord(c) != 10:
                arr.append(c)
                y_count += 1
            if y_count % y_dim == 0:
                shed_map.append(list)
                arr = []

        # TODO fix this function
        # define_possible_entries(shed_map, w)
