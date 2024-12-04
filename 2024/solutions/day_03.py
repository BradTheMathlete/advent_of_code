import re

def process_input(input_data):
    pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_data)
    return pairs

def task_01(multiplication_pairs) -> int:
    sol = 0
    for i, j in multiplication_pairs:
        sol += eval(i) * eval(j)
    return sol

def main(input_data):
    processed_data = process_input(input_data)
    output_01 = task_01(processed_data)
    return output_01

if __name__ == "__main__":
    test_input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    challenge_input = open("2024/inputs/day_03.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')
