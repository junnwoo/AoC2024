from pathlib import Path

input_data = Path("input.txt").read_text()
floor = [[c for c in line] for line in input_data.strip().split("\n")]
print(input_data)


class Pos:
    def __init__(self, i, j):
        self.r: int = i
        self.c: int = j


class Guard:
    pos: Pos
    direction: int
    exited: bool = False
    viewed: list[list[bool]]

    def turn(self):
        self.direction += 1
        self.direction %= 4

    def can_move(self, floor):
        next_pos = self.get_next_pos()
        if (
            next_pos.r < 0
            or next_pos.c < 0
            or next_pos.r > len(self.viewed)
            or next_pos.c > len(self.viewed[0])
        ):
            self.exited = True
            print(f"exit found {next_pos.r},{next_pos.c}")
            return False
        next_char = floor[next_pos.r][next_pos.c]
        if next_char == "#":
            return False
        return True

    def get_next_pos(self):
        ahead_row = self.pos.r
        ahead_col = self.pos.c
        if self.direction == 0:
            ahead_row -= 1
        elif self.direction == 1:
            ahead_col += 1
        elif self.direction == 2:
            ahead_row += 1
        elif self.direction == 3:
            ahead_col -= 1
        else:
            raise Exception("Direction not found")
        return Pos(ahead_row, ahead_col)

    def load_map(self, floor):
        self.viewed = [[False for c in r] for r in floor]

    def move(self, floor):
        if self.exited:
            return 0
        if self.can_move(floor):
            self.pos = self.get_next_pos()
            self.viewed[self.pos.r][self.pos.c] = True
            print(f"moving to {self.pos.r},{self.pos.c}")
        else:
            self.turn()
            self.move(floor)


guard = Guard()
guard.load_map(floor)
for i, r in enumerate(floor):
    for j, c in enumerate(r):
        if c == "^":
            pos = Pos(i, j)
            guard.pos = pos
            guard.direction = 0
            floor[i][j] = "."
        elif c == ">":
            pos = Pos(i, j)
            guard.pos = pos
            guard.direction = 1
            floor[i][j] = "."
        elif c == "v":
            pos = Pos(i, j)
            guard.pos = pos
            guard.direction = 2
            floor[i][j] = "."
        elif c == "<":
            pos = Pos(i, j)
            guard.pos = pos
            guard.direction = 3
            floor[i][j] = "."

guard.viewed[guard.pos.r][guard.pos.c] = True
while not guard.exited:
    guard.move(floor)

places = 0
for r in guard.viewed:
    places += r.count(True)

print(f"Visited {places} places")
