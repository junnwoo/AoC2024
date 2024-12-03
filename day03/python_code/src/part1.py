import re
input = ""
pattern = r"[(do)\(\)|(don't)\(\)]mul\((\d+\,\d+)\)"
matches = re.findall(pattern, input)
ans = 0
print(matches)
if matches:
    for mul in matches:
        pat = r"\d+\,\d+"
        dig_res = re.match(pat, mul)
        if dig_res:
            first, second = dig_res[0].split(",")
            ans += int(first) * int(second)
print(ans)

