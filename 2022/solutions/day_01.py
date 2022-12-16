test_input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
challenge_input_loc = "2022/inputs/day_01.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    temp = input_data.split('\n\n')
    output = []
    for i in temp:
        output.append([eval(j) for j in i.split('\n')])
    return output


def max_calories(processed_data):
    total_calories = []
    for i in processed_data:
        total_calories.append(sum(i))
    return max(total_calories)


def top_three_calories(processed_data):
    total_calories = []
    for i in processed_data:
        total_calories.append(sum(i))
    return sum(sorted(total_calories)[-3:])
