def process_input(input_data):
    return [eval(i) for i in list(input_data)]

def original_blocks(disk_map):
    blocks = []
    for i, j in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(j):
                blocks.append(str(i//2))
        else:
            for _ in range(j):
                blocks.append('.')
    return blocks

def has_free_space(blocks) -> bool:
    for i in range(len(blocks)):
        if blocks[i] == '.':
            return True
    return False

def move_blocks(blocks):
    updated_blocks = blocks.copy()
    while has_free_space(updated_blocks):
        if updated_blocks[-1] != '.':
            first_free = updated_blocks.index('.')
            updated_blocks[first_free] = updated_blocks[-1]
        updated_blocks.pop()
    return updated_blocks

def calculate_checksum(blocks) -> int:
    count = 0
    for i, j in enumerate(blocks):
        if j != '.':
            count += (i * eval(j))
    return count

def task_01(disk_map) -> int:
    o_blocks = original_blocks(disk_map)
    return calculate_checksum(move_blocks(o_blocks))

def find_space_position(blocks, size) -> int:
    for i in range(len(blocks) - size + 1):
        if blocks[i: i + size] == ['.'] * size:
            return i

def move_full_blocks(blocks):
    updated_blocks = blocks.copy()
    max_id = updated_blocks[-1]
    for i in reversed(range(eval(max_id) + 1)):
        id_count = updated_blocks.count(str(i))
        if id_count > 0 and '.' * id_count in ''.join(updated_blocks):
            id_pos = updated_blocks.index(str(i))
            space_pos = find_space_position(updated_blocks, id_count)
            if space_pos < id_pos:
                for j in range(id_count):
                    updated_blocks[id_pos + j] = '.'
                    updated_blocks[space_pos + j] = str(i)
    return updated_blocks

def task_02(disk_map) -> int:
    o_blocks = original_blocks(disk_map)
    return calculate_checksum(move_full_blocks(o_blocks))

def main(input_data):
    disk_map = process_input(input_data)
    output_01 = task_01(disk_map)
    output_02 = task_02(disk_map)
    return output_01, output_02

if __name__ == "__main__":
    test_input = '2333133121414131402'
    challenge_input = open("2024/inputs/day_09.txt").read()

    # test_01 = main(test_input)
    test_01, test_02 = main(test_input)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')