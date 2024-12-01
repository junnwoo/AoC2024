from pathlib import Path
import re
from typing import List, Dict
import argparse


def main(input_file: Path):
    with input_file.open() as f:
        input_data: List[str] = f.readlines()
        result = part2(input_data)
    print(result)


def part2(input: List[str]) -> int:
    left_numbers: List[int] = []
    right_numbers_occurances: Dict[int, int] = {}
    input_pattern = r"^(\d+)\s+(\d+)$"
    for l in input:
        numbers = re.findall(input_pattern, l)
        if not numbers:
            raise RuntimeError("Could not obtain numbers from input")
        left_number, right_number = numbers[0]
        left_numbers.append(int(left_number))
        right_number = int(right_number)
        if right_numbers_occurances.get(right_number):
            right_numbers_occurances[right_number] += 1
        else:
            right_numbers_occurances[right_number] = 1

    similarity_score = 0
    for number in left_numbers:
        occurances = right_numbers_occurances.get(number, 0)
        similarity_score += get_similarity_score(number, occurances)
    return similarity_score


def get_similarity_score(number: int, occurances: int):
    return number * occurances


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    main(input_file=args.input_file)
