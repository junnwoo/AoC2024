from pathlib import Path

input_file = Path("input.txt")
grid_size = 71


class Pos:
    def __init__(self, r: int, c: int):
        self.r = r
        self.c = c


class Node:

    def __init__(self, pos: Pos):
        self.pos = pos
        self.parent = None
        self.h = self.dist_to_goal()
        self.g = 0
        self.f = self.g + self.h

    def set_parent(self, parent):
        self.parent = parent
        self.g = parent.g + 1
        self.f = self.g + self.h

    def get_parent(self):
        return self.parent

    def get_neighbours(self):
        neighbours = []
        if self.pos.r > 0:
            new_node = Node(Pos(self.pos.r - 1, self.pos.c))
            new_node.set_parent(self)
            if not plan[new_node.pos.r][new_node.pos.c] == "#":
                neighbours.append(new_node)
        if self.pos.c > 0:
            new_node = Node(Pos(self.pos.r, self.pos.c - 1))
            new_node.set_parent(self)
            if not plan[new_node.pos.r][new_node.pos.c] == "#":
                neighbours.append(new_node)
        if self.pos.r < grid_size - 1:
            new_node = Node(Pos(self.pos.r + 1, self.pos.c))
            new_node.set_parent(self)
            if not plan[new_node.pos.r][new_node.pos.c] == "#":
                neighbours.append(new_node)
        if self.pos.c < grid_size - 1:
            new_node = Node(Pos(self.pos.r, self.pos.c + 1))
            new_node.set_parent(self)
            if not plan[new_node.pos.r][new_node.pos.c] == "#":
                neighbours.append(new_node)
        return neighbours

    def dist_to_goal(self) -> float:
        return ((grid_size - self.pos.r - 1) ** 2 + (grid_size - self.pos.c - 1) ** 2) ** 0.5

    def __str__(self):
        return f"({self.pos.r},{self.pos.c}): {self.f}"

def should_push_to_list(l, node):
    should_push = True
    for n in l:
        if n.pos.r == node.pos.r and n.pos.c == node.pos.c and n.f <= node.f:
            should_push = False
    return should_push


def print_plan(plan: list[list[str]]):
    output = ""
    for r in plan:
        for c in r:
            output += c
        output += "\n"
    print(output)


read_length = 2800
while True:

    read_length += 1
    print(read_length)
    plan = [["." for i in range(grid_size)] for j in range(grid_size)]
    input_data = input_file.read_text(encoding="utf8")

    for i, l in enumerate(input_data.split("\n")):
        if i == read_length:
            break
        pos = l.split(",")
        n1 = int(pos[0].strip())3000
        n2 = int(pos[1].strip())
        plan[n1][n2] = "#"

    current_pos = Node(Pos(0, 0))
    open_list = [current_pos]
    closed_list: list[Node] = []
    goal_reached = False
    while open_list and not goal_reached:
        open_list.sort(key=lambda x: x.f)
        q = open_list.pop(0)
        for successor in q.get_neighbours():
            if successor.h == 0:
                goal_reached = True
                break
            if should_push_to_list(open_list, successor):
                if should_push_to_list(closed_list, successor):
                    open_list.append(successor)
        closed_list.append(q)


    if not goal_reached:
        raise ValueError
    print(f"steps taken: {closed_list[-1].g + 1}")


