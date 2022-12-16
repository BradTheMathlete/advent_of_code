test_input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
challenge_input_loc = "2022/inputs/day_01.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    temp = input_data.split('\n\n')
    output = []
    for i in temp:
        output.append([eval(j) for j in i.split('\n')])
    return output


def sum_calories(processed_data):
    total_calories = []
    for i in processed_data:
        total_calories.append(sum(i))
    return total_calories


def top_x_calories(total_calories, x):
    return sum(sorted(total_calories)[-x:])


def main(input_data):
    processed_data = process_input(input_data)
    total_calories = sum_calories(processed_data)
    max_calories = top_x_calories(total_calories, 1)
    top_3_calories = top_x_calories(total_calories, 3)
    return max_calories, top_3_calories


test_output = main(test_input)
challenge_output = main(challenge_input)
