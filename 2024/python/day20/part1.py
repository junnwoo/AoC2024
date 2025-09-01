import json
from pathlib import Path

input_data = Path("input.txt").read_text()
split = input_data.split("\n\n")
patterns = split[0].split(", ")
designs = split[1].split("\n")


def create_map(pat: list[str], design: str) -> dict[str, int]:
    res = {}
    for p in pat:
        res[p] = design.count(p)
    return res


possible_designs = 0
valid_str = {}


def valid_design(design: str):
    # print("------------v")
    if design in valid_str:
        # print(f"using cache: {design}")
        return valid_str[design]
    if design == "":
        return True
    for p in patterns:
        # print(f"Matching pattern {p} with design {design}")
        if design.count(p) > 0:
            valid = all(valid_design(s) for s in design.split(p))
            if valid:
                valid_str[design] = True
                return valid

    # print("------------^")
    # valid_str[design] = False
    return False


cache_file = Path("mem.json")
# cache_file.write_text("{}")

with open("mem.json", encoding="utf8") as f:
    valid_str = json.load(f)
with cache_file.open("w") as f:
    valid_str.update({p: True for p in patterns})
    json.dump(valid_str, f)

for d in designs:
    print(d)
    if valid_design(design=d):
        print("Design is valid")
        possible_designs += 1
    else:
        print("Design is invalid")
    with cache_file.open("w", encoding="utf8") as f:
        json.dump(valid_str, f)
print(f"Total possibel desings: { possible_designs }")
# print(valid_design(designs[0]))
