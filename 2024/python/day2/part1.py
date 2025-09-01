import argparse
from pathlib import Path


def main(input_file: Path):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    main(args.input_file)
