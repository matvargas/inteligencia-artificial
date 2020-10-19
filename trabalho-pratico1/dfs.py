from common import *


def cell_type(shed_map, curr):
    return shed_map[curr[0]][curr[1]]


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


def define_reachable_cells(cell, x_dim, y_dim, shed_map):
    reachable_cells = []

    if LOG:
        print("From [{},{}]".format(cell[0], cell[1]))

    if cell[1] - 1 >= 0 and shed_map[cell[0]][cell[1] - 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] - 1, [cell[0], cell[1]]])

    if cell[1] + 1 < y_dim and shed_map[cell[0]][cell[1] + 1] != OBSTACLE:
        reachable_cells.append([cell[0], cell[1] + 1, [cell[0], cell[1]]])

    if cell[0] - 1 >= 0 and shed_map[cell[0] - 1][cell[1]] != OBSTACLE:
        reachable_cells.append([cell[0] - 1, cell[1], [cell[0], cell[1]]])

    if cell[0] + 1 < x_dim and shed_map[cell[0] + 1][cell[1]] != OBSTACLE:
        reachable_cells.append([cell[0] + 1, cell[1], [cell[0], cell[1]]])

    if LOG:
        print("Reachable cells are: ", end='')
        print_queue(reachable_cells)

    return reachable_cells


def do_dfs(shed_map, curr, visited, entrance, w, starvation, path):

    if LOG:
        print("Current cell:{}".format(curr))

    if cell_type(shed_map, curr) == GOAL:
        retrieve_shortest_path(curr, entrance, shed_map, path)
        exit()

    if cell_type(shed_map, curr) == CONTROL_POINT:
        starvation = 0
    else:
        starvation += 1

    # print("Starvation: {}".format(starvation))

    visited[curr[0]][curr[1]] = 1

    for cell in define_reachable_cells(curr, len(shed_map), len(shed_map[0]), shed_map):
        if visited[cell[0]][cell[1]] != 1:
            if starvation <= w or cell_type(shed_map, cell) == CONTROL_POINT:
                path.append(cell)
                do_dfs(shed_map, cell, visited, entrance, w, starvation, path)


def dfs(shed_map, entrances, w):

    for entrance in entrances:
        x_dim = len(shed_map)
        y_dim = len(shed_map[0])

        visited = [([0] * y_dim) for i in range(x_dim)]

        if cell_type(shed_map, entrance) == CONTROL_POINT:
            starvation = 0
        else:
            starvation = 1

        path = [entrance]

        do_dfs(shed_map, entrance, visited, entrance, w, starvation, path)
