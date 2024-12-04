import re

def process_input_01(input_data):
    pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_data)
    return pairs

def process_input_02(input_data):
    splits = [i.split("don't()")[0] for i in input_data.split('do()')]
    pairs = []
    for p in splits:
        pairs += re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', p)
    return pairs

def multiply_and_sum(multiplication_pairs) -> int:
    sol = 0
    for i, j in multiplication_pairs:
        sol += eval(i) * eval(j)
    return sol

def main(input_data):
    processed_data_01 = process_input_01(input_data)
    output_01 = multiply_and_sum(processed_data_01)
    processed_data_02 = process_input_02(input_data)
    output_02 = multiply_and_sum(processed_data_02)
    return output_01, output_02

if __name__ == "__main__":
    test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    challenge_input = open("2024/inputs/day_03.txt").read()

    # test_01 = main(test_input)
    test_01, test_02 = main(test_input)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')
