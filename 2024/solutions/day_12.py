import numpy as np

def process_input(input_data):
    farm_map = [list(i) for i in input_data.split('\n')]
    crop_list = list(set(list(input_data)) - set(['\n']))
    return farm_map, crop_list

def unvisited_regions(crop, farm_map, visited_map) -> bool:
    locations = np.where((np.array(farm_map) == crop) & (np.array(visited_map) == '.'))
    return len(locations[0]) > 0

def find_crop(crop, farm_map, visited_map):
    locations = np.where((np.array(farm_map) == crop) & (np.array(visited_map) == '.'))
    return [int(locations[0][0]), int(locations[1][0])]

def determine_neighbours(row, col, farm_map, visited_map):
    map_size = len(farm_map)
    value = farm_map[row][col]
    neighbours = []
    if row - 1 >= 0 and farm_map[row - 1][col] == value and visited_map[row - 1][col] != 'X':
        neighbours.append([row - 1, col])
    if col + 1 < map_size and farm_map[row][col + 1] == value and visited_map[row][col + 1] != 'X':
        neighbours.append([row, col + 1])
    if row + 1 < map_size and farm_map[row + 1][col] == value and visited_map[row + 1][col] != 'X':
        neighbours.append([row + 1, col])
    if col - 1 >= 0 and farm_map[row][col - 1] == value and visited_map[row][col - 1] != 'X':
        neighbours.append([row, col - 1])
    return neighbours

def depth_first_search(v_coords, v_map, farm_map, row, col):
    if (row, col) not in v_coords:
        v_coords.add((row, col))
        v_map[row][col] = 'X'
    for n_row, n_col in determine_neighbours(row, col, farm_map, v_map):
        depth_first_search(v_coords, v_map, farm_map, n_row, n_col)

def determine_region(start_row, start_col, farm_map, visited_map):
    visited_coords = set()
    depth_first_search(visited_coords, visited_map, farm_map, start_row, start_col)
    return visited_coords

def calculate_perimeter(coords, farm_map) -> int:
    perimeter = 0
    map_size = len(farm_map)
    visited_map = [['.'] * map_size for _ in range(map_size)]
    for row, col in coords:
        perimeter += 4 - len(determine_neighbours(row, col, farm_map, visited_map))
    return perimeter

def task_01(farm_map, crop_list) -> int:
    price = 0
    map_size = len(farm_map)
    visited_map = [['.'] * map_size for _ in range(map_size)]
    for c in crop_list:
        while unvisited_regions(c, farm_map, visited_map):
            start_row, start_col = find_crop(c, farm_map, visited_map)
            region_coords = determine_region(start_row, start_col, farm_map, visited_map)
            perimeter = calculate_perimeter(region_coords, farm_map)
            price += len(region_coords) * perimeter
    return price

def neighbour_direction(row, col, n_row, n_col) -> str:
    if row - 1 == n_row:
        return 'u'
    if col + 1 == n_col:
        return 'r'
    if row + 1 == n_row:
        return 'd'
    if col - 1 == n_col:
        return 'l'

def count_two_neighbour_corners(row, col, neighbours, farm_map) -> int:
    value = farm_map[row][col]
    n_directions = [neighbour_direction(row, col, n[0], n[1]) for n in neighbours]
    if ('u' in n_directions and 'd' in n_directions) or ('l' in n_directions and 'r' in n_directions):
        return 0
    if 'u' in n_directions and 'r' in n_directions:
        if farm_map[row - 1][col + 1] == value:
            return 1
    if 'd' in n_directions and 'r' in n_directions:
        if farm_map[row + 1][col + 1] == value:
            return 1
    if 'u' in n_directions and 'l' in n_directions:
        if farm_map[row - 1][col - 1] == value:
            return 1
    if 'd' in n_directions and 'l' in n_directions:
        if farm_map[row + 1][col - 1] == value:
            return 1
    return 2

def count_three_neighbour_corners(row, col, neighbours, farm_map) -> int:
    corners = 0
    value = farm_map[row][col]
    n_directions = [neighbour_direction(row, col, n[0], n[1]) for n in neighbours]
    if 'u' not in n_directions or 'r' not in n_directions:
        if farm_map[row + 1][col - 1] != value:
            corners += 1
    if 'd' not in n_directions or 'r' not in n_directions:
        if farm_map[row - 1][col - 1] != value:
            corners += 1
    if 'u' not in n_directions or 'l' not in n_directions:
        if farm_map[row + 1][col + 1] != value:
            corners += 1
    if 'd' not in n_directions or 'l' not in n_directions:
        if farm_map[row - 1][col + 1] != value:
            corners += 1
    return corners

def count_four_neighbour_corners(row, col, farm_map) -> int:
    corners = 0
    value = farm_map[row][col]
    if farm_map[row + 1][col - 1] != value:
        corners += 1
    if farm_map[row - 1][col - 1] != value:
        corners += 1
    if farm_map[row + 1][col + 1] != value:
        corners += 1
    if farm_map[row - 1][col + 1] != value:
        corners += 1
    return corners

def count_corners(row, col, farm_map) -> int:
    map_size = len(farm_map)
    visited_map = [['.'] * map_size for _ in range(map_size)]
    neighbours = determine_neighbours(row, col, farm_map, visited_map)
    if len(neighbours) == 0:
        return 4
    if len(neighbours) == 1:
        return 2
    if len(neighbours) == 2:
        return count_two_neighbour_corners(row, col, neighbours, farm_map)
    if len(neighbours) == 3:
        return count_three_neighbour_corners(row, col, neighbours, farm_map)
    if len(neighbours) == 4:
        return count_four_neighbour_corners(row, col, farm_map)

def count_all_corners(region_coords, farm_map) -> int:
    corners = 0
    for row, col in region_coords:
        corners += count_corners(row, col, farm_map)
    return corners

def task_02(farm_map, crop_list) -> int:
    price = 0
    map_size = len(farm_map)
    visited_map = [['.'] * map_size for _ in range(map_size)]
    for c in crop_list:
        while unvisited_regions(c, farm_map, visited_map):
            start_row, start_col = find_crop(c, farm_map, visited_map)
            region_coords = determine_region(start_row, start_col, farm_map, visited_map)
            corners = count_all_corners(region_coords, farm_map)
            price += len(region_coords) * corners
    return price

def main(input_data):
    farm_map, crop_list = process_input(input_data)
    output_01 = task_01(farm_map, crop_list)
    output_02 = task_02(farm_map, crop_list)
    return output_01, output_02

if __name__ == "__main__":
    test_input_01 = 'AAAA\nBBCD\nBBCC\nEEEC'
    test_input_02 = 'OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO'
    test_input_03 = 'RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE'
    test_input_04 = 'EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE'
    test_input_05 = 'AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA'
    challenge_input = open("2024/inputs/day_12.txt").read()

    # test_01 = main(test_input_03)
    test_01, test_02 = main(test_input_03)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')