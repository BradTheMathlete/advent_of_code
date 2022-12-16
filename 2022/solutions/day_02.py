test_input = "A Y\nB X\nC Z"
challenge_input_loc = "2022/inputs/day_02.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    return [i.split(' ') for i in input_data.split('\n')]


def score_strategy(processed_data):
    score = 0
    for r in processed_data:
        if r[1] == 'X':
            score += 1
        elif r[1] == 'Y':
            score += 2
        else:
            score += 3
        if r in [['A', 'X'], ['B', 'Y'], ['C', 'Z']]:
            score += 3
        elif r in [['A', 'Y'], ['B', 'Z'], ['C', 'X']]:
            score += 6
    return score
