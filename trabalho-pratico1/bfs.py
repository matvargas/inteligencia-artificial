from common import *


def bfs(shed_map, entrances, w):
    print("BFS")

    x_dim = len(shed_map)
    y_dim = len(shed_map[0])

    for entrance in entrances:
        print("Starting from ", end='')
        print(entrance)

        steps = 0

        if shed_map[entrance[0]][entrance[1]] != CONTROL_POINT:
            steps += 1

        visited = []
        queue = []

