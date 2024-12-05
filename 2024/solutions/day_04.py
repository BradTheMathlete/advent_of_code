import numpy as np

def process_input(input_data):
    output_array = np.array([list(i) for i in input_data.split('\n')])
    return output_array

def search_for_xmas(list_to_search) -> int:
    target = list('XMAS')
    count = 0
    for i in range(len(list_to_search) - len(target) + 1):
        if list_to_search[i:i+len(target)] == target:
            count += 1
    return count

def task_01(puzzle_input) -> int:
    count = 0
    puzzle_size = puzzle_input.shape[0]
    for row in puzzle_input:
        count += search_for_xmas(row.tolist())
        count += search_for_xmas(np.flip(row).tolist())
    for col in puzzle_input.T:
        count += search_for_xmas(col.tolist())
        count += search_for_xmas(np.flip(col).tolist())
    for k in range(4 - puzzle_size, puzzle_size + 1 - 4):
        d_f = np.diag(puzzle_input, k=k)
        count += search_for_xmas(d_f.tolist())
        count += search_for_xmas(np.flip(d_f).tolist())
        d_b = np.diag(np.flip(puzzle_input, axis=1), k=k)
        count += search_for_xmas(d_b.tolist())
        count += search_for_xmas(np.flip(d_b).tolist())
    return count

def main(input_data):
    processed_data = process_input(input_data)
    output_01 = task_01(processed_data)
    return output_01

if __name__ == "__main__":
    test_input = 'MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX'
    challenge_input = open("2024/inputs/day_04.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')
