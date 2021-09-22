test_input = [1721, 979, 366, 299, 675, 1456]
challenge_input_loc = "2020/inputs/day_01.txt"
challenge_input = open(challenge_input_loc).read().splitlines()
challenge_input = [eval(i) for i in challenge_input]


def challenge_01(entries: list) -> int:
    for index, i in enumerate(entries[:len(entries) - 1]):
        for j in entries[index + 1:]:
            if i + j == 2020:
                return i * j


print(challenge_01(test_input))
print(challenge_01(challenge_input))


def challenge_02(entries: list) -> int:
    no_entries = len(entries)
    for index_i, i in enumerate(entries[:no_entries - 2]):
        for index_j, j in enumerate(entries[index_i + 1:no_entries - 1]):
            for k in entries[index_j + 1:]:
                if i + j + k == 2020:
                    return i * j * k


print(challenge_02(test_input))
print(challenge_02(challenge_input))
