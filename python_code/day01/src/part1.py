from pathlib import Path
import re
from typing import List
import argparse


def main(input_file: Path):
    with input_file.open() as f:
        input_data: List[str] = f.readlines()
        result = part1(input_data)
    print(result)


def part1(input: List[str]) -> int:
    left_numbers: List[int] = []
    right_numbers: List[int] = []
    input_pattern = r"^(\d+)\s+(\d+)$"
    for l in input:
        numbers = re.findall(input_pattern, l)
        if not numbers:
            raise RuntimeError("Could not obtain numbers from input")
        left_number, right_number = numbers[0]
        left_numbers.append(int(left_number))
        right_numbers.append(int(right_number))
    left_numbers.sort()
    right_numbers.sort()
    distance = 0
    for left, right in zip(left_numbers, right_numbers):
        distance += get_distance(left, right)
    return distance


def get_distance(left_number: int, right_number: int):
    return abs(left_number - right_number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    main(input_file=args.input_file)
