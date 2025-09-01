import argparse
from pathlib import Path


def main(input_file: Path):
    with input_file.open("r") as f:
        input_data: list[str] = f.readlines()
    input_data = [s.strip("\n") for s in input_data]

    found = 0
    window_size = 3
    for r in range(len(input_data) - window_size + 1):
        for c in range(len(input_data[r]) - window_size + 1):
            fdiag = ''.join([input_data[r + i][c + i] for i in range(window_size)])
            bdiag = ''.join([input_data[r + i-1][c + window_size - i] for i in range(1, window_size+1)])
            if contains_xmas(( fdiag, bdiag )):
                found += 1
    print(found)


def contains_xmas(diags: tuple[str,str]) -> bool:
    mas_strings = ["MAS", "SAM"]
    return diags[0] in mas_strings and diags[1] in mas_strings


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    main(args.input_file)
