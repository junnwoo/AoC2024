import z3
from pathlib import Path
from typing import Tuple

input_file: Path = Path("input.txt")
input_data = input_file.read_text(encoding="utf8")
games = [i.strip() for i in input_data.split("\n\n")]


def get_x_y_from_prize(button: str) -> Tuple[int, int]:
    pos = [p.strip() for p in button.split(":")[1].split(",")]
    x = pos[0].split("=")[1]
    y = pos[1].split("=")[1]
    return (int(x) + 10000000000000, int(y) + 10000000000000)


def get_x_y_from_button(button: str) -> Tuple[int, int]:
    pos = [p.strip() for p in button.split(":")[1].split(",")]
    x = pos[0].split("+")[1]
    y = pos[1].split("+")[1]
    return (int(x), int(y))


def solve_equation(ax, ay, bx, by, price_x, price_y) -> Tuple[int, int]:
    a = z3.Int("a")
    b = z3.Int("b")
    s = z3.Solver()
    s.add(a > 0)
    s.add(b > 0)
    s.add(ax * a + bx * b == price_x)
    s.add(ay * a + by * b == price_y)
    if s.check() == z3.sat:
        m = s.model()
        return (int(m[a].as_string()), int(m[b].as_string()))
    return (0, 0)


ans = 0
for game in games:
    info = game.split("\n")
    ax, ay = get_x_y_from_button(info[0])
    bx, by = get_x_y_from_button(info[1])
    price_x, price_y = get_x_y_from_prize(info[2])
    tokens = solve_equation(ax, ay, bx, by, price_x, price_y)
    ans += tokens[0] * 3 + tokens[1]
print(ans)
