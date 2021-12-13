from typing import List

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
challenge_input_loc = "2021/inputs/day_03.txt"
challenge_input = open(challenge_input_loc).read().splitlines()


def challenge_01(report: List[str]) -> int:
    no_bits = len(report[0])
    gamma = ""
    epsilon = ""
    for bit in range(no_bits):
        total = sum([eval(i[bit]) for i in report])
        if total > len(report) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


print(challenge_01(test_input))
print(challenge_01(challenge_input))


def challenge_02(report: List[str]) -> int:
    ox_value = find_rating(report, "1", "0")
    co_value = find_rating(report, "0", "1")
    return int(ox_value, 2) * int(co_value, 2)


def find_rating(report: List[str], g_value: str, l_value: str) -> str:
    bit = 0
    while len(report) > 1:
        total = sum([eval(i[bit]) for i in report])
        if total >= len(report) / 2:
            target_value = g_value
        else:
            target_value = l_value
        report = [i for i in report if i[bit] == target_value]
        bit += 1
    return report[0]


print(challenge_02(test_input))
print(challenge_02(challenge_input))
