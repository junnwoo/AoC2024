from pathlib import Path

input_data = Path("input.txt").read_text()
stones: list[int] = [int(s.strip()) for s in input_data.split(" ")]
print(stones)


def blink(stones: list[int]):
    new_array = stones.copy()
    current_index = 0
    for stone in stones:
        s = str(stone)
        if stone == 0:
            new_array[current_index] = 1
        elif len(s) % 2 == 0:
            new_array[current_index] = int(s[: int(len(s) / 2)])
            current_index += 1
            new_array.insert(current_index, int(s[int(len(s) / 2) :]))
        else:
            new_array[current_index] *= 2024
        current_index += 1

    return new_array


for i in range(25):
    stones = blink(stones)
    print(f"{i}/{25}")
print(f"number of stones: {len(stones)}")
