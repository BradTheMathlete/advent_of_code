import itertools

def process_input(input_data):
    equations = []
    for i in input_data.split('\n'):
        temp = i.split(':')
        equations.append([eval(temp[0]), [eval(j) for j in temp[1].lstrip().split(' ')]])
    return equations

def operator_combos(no_values):
    operators = ['a', 'm']
    return set(itertools.combinations(operators * (no_values - 1), no_values - 1))

def output_value(operators, values) -> int:
    output = values[0]
    for i, o in enumerate(operators):
        if o == 'a':
            output += values[i + 1]
        if o == 'm':
            output *= values[i + 1]
    return output

def test_value_achievable(test_value, values) -> bool:
    o_combos = operator_combos(len(values))
    for o in o_combos:
        if test_value == output_value(o, values):
            return True
    return False

def task_01(equations) -> int:
    count = 0
    for i, j in equations:
        if test_value_achievable(i, j):
            count += i
    return count

def operator_combos_02(no_values):
    operators = ['a', 'm', 'c']
    return set(itertools.combinations(operators * (no_values - 1), no_values - 1))

def concat_numbers(a, b) -> int:
    return eval(str(a) + str(b))

def output_value_02(operators, values) -> int:
    output = values[0]
    for i, o in enumerate(operators):
        if o == 'a':
            output += values[i + 1]
        if o == 'm':
            output *= values[i + 1]
        if o =='c':
            output = concat_numbers(output, values[i + 1])
    return output

def test_value_achievable_02(test_value, values) -> bool:
    o_combos = operator_combos_02(len(values))
    for o in o_combos:
        if test_value == output_value_02(o, values):
            return True
    return False

def task_02(equations) -> int:
    count = 0
    for i, j in equations:
        if test_value_achievable_02(i, j):
            print(i, j)
            count += i
    return count

def main(input_data):
    equations = process_input(input_data)
    output_01 = task_01(equations)
    output_02 = task_02(equations)
    return output_01, output_02

if __name__ == "__main__":
    test_input = '190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20'
    challenge_input = open("2024/inputs/day_07.txt").read()

    # test_01 = main(test_input)
    test_01, test_02 = main(test_input)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')