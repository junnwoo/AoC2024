from pathlib import Path

input_data = Path("input.txt").read_text()
stones: list[int] = [int(s.strip()) for s in input_data.split(" ")]
stoness = {s: stones.count(s) for s in stones}


def blink(stones: dict[int:int]):
    new_dict = {}
    for stone, count in stones.items():
        s = str(stone)
        if stone == 0:
            if 1 in new_dict:
                new_dict[1] += count
            else:
                new_dict[1] = count
        elif len(s) % 2 == 0:
            new_stone_left = int(s[: int(len(s) / 2)])
            new_stone_right = int(s[int(len(s) / 2) :])
            if new_stone_left in new_dict:
                new_dict[new_stone_left] += count
            else:
                new_dict[new_stone_left] = count
            if new_stone_right in new_dict:
                new_dict[new_stone_right] += count
            else:
                new_dict[new_stone_right] = count
        else:
            new_stone = stone * 2024
            if new_stone in new_dict:
                new_dict[new_stone] += count
            else:
                new_dict[new_stone] = count
    return new_dict


# stoness = {125: 1, 17: 1}
for i in range(75):
    stoness = blink(stoness)
    print(stoness)
    # print(f"{i+1}/{25}")
length = 0
for _, count in stoness.items():
    length += count
print(f"number of stones: {length}")
