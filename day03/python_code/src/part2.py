import re
from pathlib import Path
from pprint import pprint

input_file = Path("aoc_input.txt")
input = input_file.read_text()
dos = input.split("do()")
ans = 0
for do_string in dos:
    mul_string = do_string.split("don't()")[0]
    mul_pat = r"mul\((\d+,\d+)\)"
    matches = re.findall(mul_pat, mul_string)
    if matches:
        for mul in matches:
            first, second = mul.split(",")
            ans += int(first) * int(second)

print(ans)

