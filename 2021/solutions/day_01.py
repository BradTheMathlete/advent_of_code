from typing import List

test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
challenge_input_loc = "2021/inputs/day_01.txt"
challenge_input = open(challenge_input_loc).read().splitlines()
challenge_input = [eval(i) for i in challenge_input]


def challenge_01(measurements: List[int]) -> int:
    increases = 0
    for i in range(len(measurements) - 1):
        if measurements[i + 1] > measurements[i]:
            increases += 1
    return increases


print(challenge_01(test_input))
print(challenge_01(challenge_input))
