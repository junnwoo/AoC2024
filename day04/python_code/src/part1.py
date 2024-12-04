import argparse
from pathlib import Path


def main(input_file: Path):
    with input_file.open("r") as f:
        input_data: list[str] = f.readlines()
    input_data = [s.strip("\n") for s in input_data]

    found = 0
    possible_strings = [row for row in input_data]
    cols = [[row[c] for row in input_data] for c in range(len(input_data[0]))]
    for col in cols:
        possible_strings.append(''.join(col))

    window_size = 4
    for r in range(len(input_data) - window_size + 1):
        for c in range(len(input_data[r]) - window_size + 1):
            fdiag = [input_data[r + i][c + i] for i in range(window_size)]
            bdiag = [input_data[r + i-1][c + window_size - i] for i in range(1, window_size+1)]
            possible_strings.append("".join(fdiag))
            possible_strings.append("".join(bdiag))

    for string in possible_strings:
        found += find_xmas_in_str(string)
    print(found)

def find_xmas_in_str(string: str) -> int:
    return string.count("XMAS") + string.count("SAMX")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    main(args.input_file)
