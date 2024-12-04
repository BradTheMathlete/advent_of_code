def process_input(input_date):
    data = []
    for i in input_date.split('\n'):
        data.append([eval(j) for j in i.split(' ')])
    return data

def level_is_safe(level_data) -> bool:
    increasing = level_data[0] < level_data[1]
    for i in range(len(level_data) - 1):
        diff = level_data[i + 1] - level_data[i]
        if increasing and (diff < 1 or diff > 3):
            return False
        if not increasing and (diff > -1 or diff < -3):
            return False
    return True

def task_01(report_data) -> int:
    safe_levels = [level_is_safe(l) for l in report_data]
    return sum(safe_levels)

def level_is_safe_with_dampening(level_data) -> bool:
    for i in range(len(level_data)):
        temp = [j for index, j in enumerate(level_data) if index != i]
        if level_is_safe(temp):
            return True
    return False

def task_02(report_data) -> int:
    safe_levels_with_dampening = [level_is_safe_with_dampening(l) for l in report_data]
    return sum(safe_levels_with_dampening)

def main(input_data):
    processed_data = process_input(input_data)
    output_01 = task_01(processed_data)
    output_02 = task_02(processed_data)
    return output_01, output_02

if __name__ == "__main__":
    test_input = '7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9'
    challenge_input = open("2024/inputs/day_02.txt").read()

    # test_01 = main(test_input)
    test_01, test_02 = main(test_input)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')