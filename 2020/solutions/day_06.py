test_input = ["abc", "a\nb\nc", "ab\nac", "a\na\na\na", "b"]
challenge_input_loc = "2020/inputs/day_06.txt"
challenge_input = open(challenge_input_loc).read().split("\n\n")


def unique_char(group: str) -> int:
    chars = set()
    for i in group.split("\n"):
        chars = chars.union(set([j for j in i]))
    return len(chars)


def challenge_01(groups: list) -> int:
    output = 0
    for i in groups:
        output += unique_char(i)
    return output


print(challenge_01(test_input))
print(challenge_01(challenge_input))


def overlap_char(group: str) -> int:
    split_group = group.split("\n")
    chars = set(j for j in split_group[0])
    for i in split_group:
        chars = chars.intersection(set([j for j in i]))
    return len(chars)


def challenge_02(groups: list) -> int:
    output = 0
    for i in groups:
        output += overlap_char(i)
    return output


print(challenge_02(test_input))
print(challenge_02(challenge_input))
