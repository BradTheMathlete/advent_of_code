from typing import List

test_input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]
challenge_input_loc = "2021/inputs/day_02.txt"
challenge_input = open(challenge_input_loc).read().splitlines()


def challenge_01(instructions: List[str]) -> int:
    h_pos = 0
    d_pos = 0
    for i in instructions:
        direction, distance = i.split(" ")
        if direction == "forward":
            h_pos += eval(distance)
        if direction == "down":
            d_pos += eval(distance)
        if direction == "up":
            d_pos -= eval(distance)
    return h_pos * d_pos


print(challenge_01(test_input))
print(challenge_01(challenge_input))


def challenge_02(instructions: List[str]) -> int:
    aim = 0
    h_pos = 0
    d_pos = 0
    for i in instructions:
        direction, distance = i.split(" ")
        if direction == "forward":
            distance = eval(distance)
            h_pos += distance
            d_pos += (distance * aim)
        if direction == "down":
            aim += eval(distance)
        if direction == "up":
            aim -= eval(distance)
    return h_pos * d_pos


print(challenge_02(test_input))
print(challenge_02(challenge_input))
