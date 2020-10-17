from common import *


def add_distinct(a, b, v):
    for i in b:
        if i not in a and v[i[0]][i[1]] != 1:
            a.append(i)


def define_reachable_cells(cell, x_dim, y_dim, shed_map):
    reachable_cells = []

    print("From ", end='')
    print(cell)

    if cell[1] - 1 >= 0 and shed_map[cell[0]][cell[1] - 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] - 1])

    if cell[1] + 1 < y_dim and shed_map[cell[0]][cell[1] + 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] + 1])

    if cell[0] + 1 < x_dim and shed_map[cell[0] + 1][cell[1]] != OBSTACLE:
        reachable_cells.append([cell[0] + 1, cell[1]])

    print("Reachable cells are: ", end='')
    print(reachable_cells)
    return reachable_cells


def bfs(shed_map, entrances, w):
    print("BFS")

    x_dim = len(shed_map)
    y_dim = len(shed_map[0])

    for entrance in entrances:
        movements = 0
        loc_count = 0
        starvation = 0

        print("Starting from ", end='')
        print(entrance)

        visited = [([0] * y_dim) for i in range(x_dim)]
        queue = []

        if shed_map[entrance[0]][entrance[1]] != CONTROL_POINT:
            starvation += 1
        elif shed_map[entrance[0]][entrance[1]] == CONTROL_POINT:
            loc_count += 1

        movements += 1

        queue.append(entrance)

        while len(queue) != 0:
            cell = queue.pop(0)
            print("Current cell: ", end='')
            print(cell)

            if visited[cell[0]][cell[1]] != 1:
                print("Not visited yet, visiting...")
                visited[cell[0]][cell[1]] = 1

                if shed_map[cell[0]][cell[1]] == CONTROL_POINT:
                    starvation = 0
                    loc_count += 1

                movements += 1

                if shed_map[cell[0]][cell[1]] == GOAL:
                    break

                reachable_cells = define_reachable_cells(cell, x_dim, y_dim, shed_map)
                add_distinct(queue, reachable_cells, visited)
                print(queue)
            else:
                print("Already visited")

        print(movements, end=' ')
        print(loc_count, end=' ')
        print(entrance)



