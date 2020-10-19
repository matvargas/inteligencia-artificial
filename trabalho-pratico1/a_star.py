from common import *


class Node:
    def __init__(self, position: (), parent: ()):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return '({0},{1})'.format(self.position, self.f)


# A* search
def astar_search(map, start, end, w):
    w_init = w
    control_point_counter = 0
    open = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    open.append(start_node)

    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            path.append(start)

            return path[::-1], control_point_counter

        (x, y) = current_node.position

        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        w -= 1
        for next in neighbors:

            map_value = map.get(next)

            if map_value == OBSTACLE or (map_value != CONTROL_POINT and w == 0):
                continue

            neighbor = Node(next, current_node)

            if neighbor in closed:
                continue

            # Manhattan distance
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(
                neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open, neighbor):
                open.append(neighbor)
                if map.get(neighbor.position) == CONTROL_POINT:
                    control_point_counter += 1
                    w = w_init
    return None, None


def add_to_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


def a_star(filepath, entrances, w):
    grid = {}
    chars = ['c']
    goal = None
    width = 0
    height = 0

    fp = open(filepath, 'r')
    skip = fp.readline()

    while len(chars) > 0:
        chars = [str(i) for i in fp.readline().strip()]
        width = len(chars) if width == 0 else width
        for x in range(len(chars)):
            grid[(x, height)] = chars[x]
            if chars[x] == '$':
                goal = (x, height)

        if len(chars) > 0:
            height += 1
    fp.close()

    min_path = 0
    ans = None
    for entrance in entrances:
        path, control_point_counter = astar_search(grid, tuple(entrance), goal[::-1], w)
        if path and control_point_counter:
            if len(path) > min_path:
                ans = f"{len(path)} {control_point_counter} {entrance}"

    print(ans)
