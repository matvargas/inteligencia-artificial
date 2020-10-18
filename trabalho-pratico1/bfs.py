from common import *


def add_distinct(a, b, v):
    for i in b:
        if i not in a and v[i[0]][i[1]] != 1:
            a.append(i)


def print_queue(q):
    for c in q:
        print("[{},{}]".format(c[0], c[1]), end='')
    print()


def retrieve_shortest_path(path, goal_cell, entrance, shed_map):

    steps = 2 # Starting from 2 since the loop will not iterate over entrance and the goal cell
    cntrl_pnts = 0

    if shed_map[entrance[0]][entrance[1]] == CONTROL_POINT:
        cntrl_pnts += 1

    shortest_path = [[goal_cell[0], goal_cell[1]]]

    c = goal_cell[2]
    # print(c)
    while c != entrance:

        for i in path:
            if c[0] == i[0] and c[1] == i[1]:
                steps += 1
                if shed_map[c[0]][c[1]] == CONTROL_POINT:
                    cntrl_pnts += 1
                c = i[2]
                shortest_path.append([c[0], c[1]])
                # print(c)

    print(steps, end=' ')
    print(cntrl_pnts, end=' ')
    print(entrance)

    # print(shortest_path)


def define_reachable_cells(cell, x_dim, y_dim, shed_map):
    reachable_cells = []

    print("From [{},{}]".format(cell[0], cell[1]))

    if cell[1] - 1 >= 0 and shed_map[cell[0]][cell[1] - 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] - 1, [cell[0], cell[1]]])

    if cell[1] + 1 < y_dim and shed_map[cell[0]][cell[1] + 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] + 1, [cell[0], cell[1]]])

    if cell[0] + 1 < x_dim and shed_map[cell[0] + 1][cell[1]] != OBSTACLE:
        reachable_cells.append([cell[0] + 1, cell[1], [cell[0], cell[1]]])

    print("Reachable cells are: ", end='')
    print_queue(reachable_cells)
    return reachable_cells


def bfs(shed_map, entrances, w):
    print("BFS")

    x_dim = len(shed_map)
    y_dim = len(shed_map[0])

    for entrance in entrances:

        starvation = 0
        path = []

        print("====== >>>>> Starting from <<<<< ========= ", end='')
        print(entrance)

        visited = [([0] * y_dim) for i in range(x_dim)]
        queue = []

        queue.append(entrance)

        while len(queue) != 0:
            cell = queue.pop(0)
            print("Current cell: [{},{}]".format(cell[0], cell[1]))

            print("Adding cell to path")
            if cell not in path:
                path.append(cell)

            print("Path: {}".format(path))

            if visited[cell[0]][cell[1]] != 1:
                print("Not visited yet, visiting...")
                visited[cell[0]][cell[1]] = 1

                if shed_map[cell[0]][cell[1]] == CONTROL_POINT:
                    starvation = 0
                else:
                    starvation += 1
                    if starvation > w:
                        print("Starved")
                        starvation = 0
                        break

                print("Starvation: ", end='')
                print(starvation)

                if shed_map[cell[0]][cell[1]] == GOAL:
                    retrieve_shortest_path(path, cell, entrance, shed_map)
                    break

                reachable_cells = define_reachable_cells(cell, x_dim, y_dim, shed_map)
                add_distinct(queue, reachable_cells, visited)

                print("Queue: ", end='')
                print_queue(queue)

            else:
                print("Already visited")




