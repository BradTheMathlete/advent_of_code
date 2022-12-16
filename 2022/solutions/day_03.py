from string import ascii_letters


test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
challenge_input_loc = "2022/inputs/day_03.txt"
challenge_input = open(challenge_input_loc).read()


def process_input_1(input_data):
    output = []
    for i in input_data.split('\n'):
        c1 = i[:len(i) // 2]
        c2 = i[-len(i) // 2:]
        output.append([c1, c2])
    return output


def process_input_2(input_data):
    output = []
    for n, i in enumerate(input_data.split('\n')):
        if n % 3 == 0:
            output.append([])
        output[-1].append(i)
    return output


prioritisation_scorecard = {}
for value, char in enumerate(ascii_letters):
    prioritisation_scorecard[char] = value + 1
del value, char


def find_overlaps_1(processed_data):
    overlaps = []
    for r in processed_data:
        o = list(set(r[0]).intersection(set(r[1])))[0]
        overlaps.append(o)
    return overlaps


def find_overlaps_2(processed_data):
    overlaps = []
    for g in processed_data:
        o = list(set(g[0]).intersection(set(g[1])).intersection(g[2]))[0]
        overlaps.append(o)
    return overlaps


def sum_priorities(overlaps):
    return sum(map(prioritisation_scorecard.get, overlaps))


def main(input_data):
    p1 = sum_priorities(find_overlaps_1(process_input_1(input_data)))
    p2 = sum_priorities(find_overlaps_2(process_input_2(input_data)))
    return p1, p2
