test_input = "A Y\nB X\nC Z"
challenge_input_loc = "2022/inputs/day_02.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    return [i.split(' ') for i in input_data.split('\n')]


def score_strategy_1(processed_data):
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


def score_strategy_2(processed_data):
    win_dict = {'A': 'P', 'B': 'S', 'C': 'R'}
    draw_dict = {'A': 'R', 'B': 'P', 'C': 'S'}
    lose_dict = {'A': 'S', 'B': 'R', 'C': 'P'}
    score = 0
    for r in processed_data:
        if r[1] == 'X':
            shape = lose_dict[r[0]]
        elif r[1] == 'Y':
            score += 3
            shape = draw_dict[r[0]]
        else:
            score += 6
            shape = win_dict[r[0]]
        if shape == 'R':
            score += 1
        elif shape == 'P':
            score += 2
        else:
            score += 3
    return score
