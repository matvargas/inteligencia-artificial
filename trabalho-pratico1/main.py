import sys
from typing import List, Any


class MCell:
    def __init__(self, xpos, ypos, value):
        self.xpos = xpos
        self.ypos = ypos
        self.value = value


try:
    filepath = sys.argv[1]
    f = open(filepath, "r")
except:
    print("Could not open the file" + filepath)
finally:
    with open(filepath) as f:
        row = f.readline()
        xdim = int(row[0])  # Defines x dimension of map
        ydim = int(row[2])  # Defines y dimension of map
        w = int(row[4])  # Defines how far can the robot goes without reach a control point

        xcount = 0
        ycount = 0
        matrix = []
        list = []

        while True:
            c = f.read(1)
            if not c:
                break
            if c != '' and ord(c) != 10:
                # TODO: Alter c to MCell type
                list.append(c)
                ycount += 1
            if ycount % ydim == 0:
                matrix.append(list)
                list = []

    for list in matrix:
        for char in list:
            print(char, end='')
        print()