from common import *


def add_distinct(a, b, v):
    # for i in b:
    #     if i not in a and v[i[0]][i[1]] != 1:
    #         a.append(i)

    for i in b:
        should_add = True
        for j in a:
            # print("Comparing {} and {}, visited: {}".format([i[0], i[1]], [j[0], j[1]], v[i[0]][i[1]]))
            if i[0] == j[0] and i[1] == j[1] or v[i[0]][i[1]] == 1:
                should_add = False
                break

        if should_add:
            # print("Adding {} to queue".format(i))
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

    print(shortest_path)


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


def rmv_subpath(cell, path, shed_map, v):

    c = cell
    stv = 0
    while shed_map[c[0]][c[1]] != CONTROL_POINT:
        print("Cell: {} should be removed from path {}".format(c, path))

        old_len = len(path)
        for i in path:
            if c[0] == i[0] and c[1] == i[1]:
                tmp = i[2]
                if shed_map[tmp[0]][tmp[1]] != CONTROL_POINT:
                    v[tmp[0]][tmp[1]] = 0
                c = tmp
                path.remove(i)
                stv += 1
                break
        new_len = len(path)
        if old_len == new_len:
            break

    return path, stv


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

        queue.append([entrance[0], entrance[1]])

        while len(queue) != 0:
            cell = queue.pop(0)

            if len(cell) > 2:
                if shed_map[cell[2][0]][cell[2][1]] != CONTROL_POINT:
                    print("Removing {} from starvation {}".format(stv, starvation))
                    starvation -= stv

                stv = 0

            print("Current cell: {}".format(cell))

            # print("Adding cell to path")
            if cell not in path:
                path.append(cell)

            print("Path: {}".format(path))

            if visited[cell[0]][cell[1]] != 1:
                print("Not visited yet, visiting...")
                visited[cell[0]][cell[1]] = 1
                starvation += 1

                print("Starvation: ", end='')
                print(starvation)

                if shed_map[cell[0]][cell[1]] == GOAL:
                    retrieve_shortest_path(path, cell, entrance, shed_map)
                    break

                if shed_map[cell[0]][cell[1]] == CONTROL_POINT:
                    starvation = 0
                else:
                    if starvation > w:
                        print()
                        print("Starved {} on cell {}".format(starvation, cell))
                        print()
                        # starvation = 0
                        path, stv = rmv_subpath(cell, path, shed_map, visited)
                        continue

                reachable_cells = define_reachable_cells(cell, x_dim, y_dim, shed_map)
                add_distinct(queue, reachable_cells, visited)

                print("Queue: ", end='')
                print_queue(queue)

            else:
                print("Already visited")




