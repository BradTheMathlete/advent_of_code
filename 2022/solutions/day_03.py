from string import ascii_letters


test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
challenge_input_loc = "2022/inputs/day_03.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    output = []
    for i in input_data.split('\n'):
        c1 = i[:len(i) // 2]
        c2 = i[-len(i) // 2:]
        output.append([c1, c2])
    return output


prioritisation_scorecard = {}
for value, char in enumerate(ascii_letters):
    prioritisation_scorecard[char] = value + 1
del value, char


def find_overlaps(processed_data):
    overlaps = []
    for r in processed_data:
        o = list(set(r[0]).intersection(set(r[1])))[0]
        overlaps.append(o)
    return overlaps


def sum_priorities(overlaps):
    return sum(map(prioritisation_scorecard.get, overlaps))
