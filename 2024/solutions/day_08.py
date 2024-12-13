import numpy as np
import itertools as it

def process_input(input_data):
    antenna_map = [list(i) for i in input_data.split('\n')]
    frequencies = list(set(list(input_data)) - set(['.', '\n']))
    return antenna_map, frequencies

def find_antennas(frequency, antenna_map):
    locations = np.where(np.array(antenna_map) == frequency)
    coords = []
    for i in range(len(locations[0])):
        coords.append([int(locations[0][i]), int(locations[1][i])])
    return coords

def list_of_pairs(no_antennas):
    return list(it.combinations(list(range(no_antennas)), 2))

def dist_between_antennas(a1, a2):
    ver_dist = a1[0] - a2[0]
    hor_dist = a1[1] - a2[1]
    return [ver_dist, hor_dist]

def antinode_positions(a1, a2):
    dist = dist_between_antennas(a1, a2)
    anti_1 = [a1[0] + dist[0], a1[1] + dist[1]]
    anti_2 = [a2[0] - dist[0], a2[1] - dist[1]]
    return [anti_1, anti_2]

def count_antinodes(antinode_map) -> int:
    count = 0
    map_size = len(antinode_map)
    for i in range(map_size):
        for j in range(map_size):
            if antinode_map[i][j] == '#':
                count += 1
    return count

def task_01(antenna_map, frequencies) -> int:
    map_size = len(antenna_map)
    antinode_map = [['.']* map_size for _ in range(map_size)]
    for f in frequencies:
        f_antennas = find_antennas(f, antenna_map)
        pairs = list_of_pairs(len(f_antennas))
        for i, j in pairs:
            new_antinodes = antinode_positions(f_antennas[i], f_antennas[j])
            for n in new_antinodes:
                if 0 <= n[0] < map_size and 0 <= n[1] < map_size:
                    antinode_map[n[0]][n[1]] = '#'
    return count_antinodes(antinode_map)

def main(input_data):
    antenna_map, frequencies = process_input(input_data)
    output_01 = task_01(antenna_map, frequencies)
    # output_02 = task_02(equations)
    return output_01

if __name__ == "__main__":
    test_input = '............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............'
    challenge_input = open("2024/inputs/day_08.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')