import numpy as np

def process_input(input_data):
    t_map = []
    for i in input_data.split('\n'):
        t_map.append([eval(j) for j in i])
    return t_map

def find_trailheads(t_map):
    trailheads = np.where(np.array(t_map) == 0)
    coords = []
    for i in range(len(trailheads[0])):
        coords.append([int(trailheads[0][i]), int(trailheads[1][i])])
    return coords

def determine_neighbours(row, col, t_map):
    map_size = len(t_map)
    value = t_map[row][col]
    neighbours = []
    if row - 1 >= 0 and t_map[row - 1][col] == value + 1:
        neighbours.append([row - 1, col])
    if col + 1 < map_size and t_map[row][col + 1] == value + 1:
        neighbours.append([row, col + 1])
    if row + 1 < map_size and t_map[row + 1][col] == value + 1:
        neighbours.append([row + 1, col])
    if col - 1 >= 0 and t_map[row][col - 1] == value + 1:
        neighbours.append([row, col - 1])
    return neighbours

def depth_first_search(visited_coords, t_map, row, col):
    if (row, col) not in visited_coords:
        visited_coords.add((row, col))
    for n_row, n_col in determine_neighbours(row, col, t_map):
        depth_first_search(visited_coords, t_map, n_row, n_col)

def count_peaks_reached(visited_coords, t_map) -> int:
    count = 0
    for row, col in visited_coords:
        if t_map[row][col] == 9:
            count += 1
    return count

def determine_score(th_row, th_col, t_map) -> int:
    visited_coords = set()
    depth_first_search(visited_coords, t_map, th_row, th_col)
    return count_peaks_reached(visited_coords, t_map)

def task_01(topographic_map) -> int:
    count = 0
    trailheads = find_trailheads(topographic_map)
    for th_row, th_col in trailheads:
        count += determine_score(th_row, th_col, topographic_map)
    return count

def main(input_data):
    topographic_map = process_input(input_data)
    output_01 = task_01(topographic_map)
    # output_02 = task_02(topographic_map)
    return output_01

if __name__ == "__main__":
    test_input = '89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732'
    challenge_input = open("2024/inputs/day_10.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')