import re
import math

def process_input(input_data):
    robot_info = []
    for i in input_data.split('\n'):
        robot_info.append(re.findall(r'[\=\,](\-?\d+)', i))
    for i, j in enumerate(robot_info):
        robot_info[i] = [eval(k) for k in j]
    return robot_info

def move_robot(p_and_v, w, h, seconds):
    new_x = (p_and_v[0] + (p_and_v[2] * seconds)) % w
    new_y = (p_and_v[1] + (p_and_v[3] * seconds)) % h
    return new_x, new_y

def calculate_safety_factor(r_positions) -> int:
    height = len(r_positions)
    width = len(r_positions[0])
    quadrant_counts = [0] * 4
    for i in range(height):
        for j in range(width):
            if i < height // 2:
                if j < width // 2:
                    quadrant_counts[0] += r_positions[i][j]
                elif j > width // 2:
                    quadrant_counts[1] += r_positions[i][j]
            elif i > height // 2:
                if j < width // 2:
                    quadrant_counts[2] += r_positions[i][j]
                elif j > width // 2:
                    quadrant_counts[3] += r_positions[i][j]
    return math.prod(quadrant_counts)

def task_01(robot_info, width, height) -> int:
    robot_positions = [[0] * width for _ in range(height)]
    for r in robot_info:
        new_x, new_y = move_robot(r, width, height, seconds=100)
        robot_positions[new_y][new_x] += 1
    return calculate_safety_factor(robot_positions)

def main(input_data, width, height):
    robot_info = process_input(input_data)
    output_01 = task_01(robot_info, width, height)
    # output_02 = task_02(machine_inputs)
    return output_01

if __name__ == "__main__":
    test_input = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
    challenge_input = open("2024/inputs/day_14.txt").read()

    test_01 = main(test_input, width=11, height=7)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input, width=101, height=103)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')