def process_input(input_data):
    return [eval(i) for i in input_data.split(' ')]

def split_stone(stone):
    length = len(str(stone))
    new_stone_1 = eval(str(stone)[:length // 2])
    try:
        new_stone_2 = eval(str(stone)[-length // 2:])
    except:
        new_stone_2 = eval(str(stone)[-length // 2:].lstrip('0'))
    return [new_stone_1, new_stone_2]

def update_stones(input_stones):
    u_stones = []
    for i in input_stones:
        if i == 0:
            u_stones += [1]
        elif len(str(i)) % 2 == 0:
            u_stones += split_stone(i)
        else:
            u_stones += [i * 2024]
    return u_stones

def task_01(initial_stones, no_blinks) -> int:
    final_stones = initial_stones.copy()
    for _ in range(no_blinks):
        final_stones = update_stones(final_stones)
    return len(final_stones)

def convert_to_dict(input_stones):
    stones_dict = {}
    for value in set(input_stones):
        stones_dict[value] = input_stones.count(value)
    return stones_dict

def update_stones_dict(input_stones_dict):
    u_stones_dict = {}
    for value, count in input_stones_dict.items():
        if value == 0:
            new_values = [1]
        elif len(str(value)) % 2 == 0:
            new_values = split_stone(value)
        else:
            new_values = [value * 2024]
        for n in new_values:
            if n in u_stones_dict:
                u_stones_dict[n] += count
            else:
                u_stones_dict[n] = count
    return u_stones_dict

def task_02(initial_stones, no_blinks) -> int:
    final_stones_dict = convert_to_dict(initial_stones)
    for _ in range(no_blinks):
        final_stones_dict = update_stones_dict(final_stones_dict)
    return sum(final_stones_dict.values())

def main(input_data):
    initial_stones = process_input(input_data)
    output_01 = task_01(initial_stones, no_blinks=25)
    output_02 = task_02(initial_stones, no_blinks=75)
    return output_01, output_02

if __name__ == "__main__":
    test_input = '125 17'
    challenge_input = open("2024/inputs/day_11.txt").read()

    # test_01 = main(test_input)
    test_01, test_02 = main(test_input)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')