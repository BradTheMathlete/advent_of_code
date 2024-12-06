import numpy as np

def process_input(input_data):
    return [list(i) for i in input_data.split('\n')]

def find_guard(map):
    location = np.where(np.array(map) == '^')
    row = int(location[0][0])
    col = int(location[1][0])
    return row, col

def is_obstacle(row, col, map) -> bool:
    map_size = len(map)
    if row < 0 or row >= map_size or col < 0 or col >= map_size:
        return False
    if map[row][col] == '#':
        return True
    return False

def next_position(row, col, facing):
    if facing == 'up':
        return row - 1, col
    if facing == 'right':
        return row, col + 1
    if facing == 'down':
        return row + 1, col
    if facing == 'left':
        return row, col - 1

def turn_guard(facing) -> str:
    if facing == 'up':
        return 'right'
    if facing == 'right':
        return 'down'
    if facing == 'down':
        return 'left'
    if facing == 'left':
        return 'up'

def count_visited_positions(visited_map) -> int:
    count = 0
    map_size = len(visited_map)
    for i in range(map_size):
        for j in range(map_size):
            if visited_map[i][j] == 'X':
                count += 1
    return count

def task_01(map) -> int:
    map_size = len(map)
    visited = [['.']* map_size for _ in range(map_size)]
    facing = 'up'
    row , col = find_guard(map)
    while 0 <= row < map_size and 0 <= col < map_size:
        next_r, next_c = next_position(row, col, facing)
        if is_obstacle(next_r, next_c, map):
            facing = turn_guard(facing)
        else:
            visited[row][col] = 'X'
            row, col = next_r, next_c
    return count_visited_positions(visited)

def main(input_data):
    map = process_input(input_data)
    output_01 = task_01(map)
    # output_02 = task_02(rules, updates)
    # return output_01, output_02
    return output_01

if __name__ == "__main__":
    test_input = '....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...'
    challenge_input = open("2024/inputs/day_06.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')