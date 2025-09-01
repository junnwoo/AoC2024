from pathlib import Path

input_data = Path("input.txt").read_text(encoding="utf8")


def mix(secret_num: int, num: int) -> int:
    return secret_num ^ num


def prune(secret_num: int) -> int:
    return secret_num % 16777216


def next_number(secret_num: int) -> int:
    num = prune(mix(secret_num, secret_num * 64))
    num = prune(mix(num, int(num / 32)))
    num = prune(mix(num, int(num * 2048)))
    return num


def get_num_after(steps, secret_num):
    num = secret_num
    for _ in range(steps):
        num = next_number(num)
        # print(num)
    return num


# print(get_num_after(10, 123))
total_sum = 0
for s in input_data.split("\n"):
    secret_num = int(s.strip())
    final_num = get_num_after(2000, secret_num)
    print(f"{secret_num}: {final_num}")
    total_sum += final_num
#
print(f"Final sum is {total_sum}")
#
