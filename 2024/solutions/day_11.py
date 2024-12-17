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

def main(input_data):
    initial_stones = process_input(input_data)
    output_01 = task_01(initial_stones, no_blinks=25)
    # output_02 = task_02(initial_stones)
    return output_01

if __name__ == "__main__":
    test_input = '125 17'
    challenge_input = open("2024/inputs/day_11.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')