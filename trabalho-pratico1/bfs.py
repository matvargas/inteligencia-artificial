from common import *


def print_visited(v):
    for i in v:
        for j in i:
            print(j, end="")
        print()


def print_queue(q):
    for c in q:
        print("[{},{}]".format(c[0], c[1]), end='')
    print()


def cell_type(shed_map, curr):
    return shed_map[curr[0]][curr[1]]


def define_reachable_cells(cell, x_dim, y_dim, shed_map):
    reachable_cells = []

    if LOG:
        print("From [{},{}]".format(cell[0], cell[1]))

    if cell[1] - 1 >= 0 and shed_map[cell[0]][cell[1] - 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] - 1, [cell[0], cell[1]]])

    if cell[1] + 1 < y_dim and shed_map[cell[0]][cell[1] + 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] + 1, [cell[0], cell[1]]])

    if cell[0] + 1 < x_dim and shed_map[cell[0] + 1][cell[1]] != OBSTACLE:
        reachable_cells.append([cell[0] + 1, cell[1], [cell[0], cell[1]]])

    if LOG:
        print("Reachable cells are: ", end='')
        print_queue(reachable_cells)

    return reachable_cells


def retrieve_shortest_path(goal_cell, entrance, shed_map, path):

    steps = 2  # Starting from 2 since the loop will not iterate over entrance and the goal cell
    cntrl_pnts = 0

    if cell_type(shed_map, entrance) == CONTROL_POINT:
        cntrl_pnts += 1

    shortest_path = [[goal_cell[0], goal_cell[1]]]

    c = goal_cell[2]
    while c != entrance:
        for i in path:
            if c[0] == i[0] and c[1] == i[1]:
                steps += 1
                if cell_type(shed_map, c) == CONTROL_POINT:
                    cntrl_pnts += 1
                shortest_path.append([c[0], c[1]])
                c = i[2]

    print(steps, end=' ')
    print(cntrl_pnts, end=' ')
    print(entrance)

    if LOG:
        print(shortest_path)


def bfs(shed_map, entrances, w):
    if LOG:
        print("BFS")

    x_dim = len(shed_map)
    y_dim = len(shed_map[0])

    visited = [([0] * y_dim) for i in range(x_dim)]

    for entrance in entrances:
        if LOG:
            print("Starting from : {}".format(entrance))

        queue = []
        path = []

        queue.append(entrance)
        visited[entrance[0]][entrance[1]] = 1

        while queue:

            curr = queue.pop(0)

            if cell_type(shed_map, curr) == GOAL:
                if LOG:
                    print("Goal found in: {}".format(curr))
                retrieve_shortest_path(curr, entrance, shed_map, path)
                break

            reachable_cells = define_reachable_cells(curr, x_dim, y_dim, shed_map)

            for i in reachable_cells:
                if not visited[i[0]][i[1]]:
                    path.append(i)
                    queue.append(i)
                    visited[i[0]][i[1]] = 1

            if LOG:
                print("Queue: {}".format(queue))


