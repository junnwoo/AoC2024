from pathlib import Path
import argparse


def main(input_file: Path):
    with input_file.open() as f:
        input_data: List[str] = f.readlines()
        result = part1(input_data)
    print(result)


def part1(input: List[str]) -> int:
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    main(input_file=args.input_file)
