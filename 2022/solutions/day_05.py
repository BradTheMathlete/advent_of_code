from string import ascii_letters


test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
challenge_input_loc = "2022/inputs/day_05.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    raw_start_stacks, raw_instructions = input_data.split('\n\n')
    start_stacks = process_start_stacks(raw_start_stacks)
    instructions = process_instructions(raw_instructions)
    return start_stacks, instructions


def process_start_stacks(raw_start_stacks):
    no_stacks = len(raw_start_stacks.split('\n')[-1]) // 4 + 1
    start_stacks = {i + 1: [] for i in range(no_stacks)}
    for i in reversed(raw_start_stacks.split('\n')):
        for j in range(no_stacks):
            c = i[4 * j + 1]
            if c in ascii_letters:
                start_stacks[j + 1].append(c)
    return start_stacks


def process_instructions(raw_instructions):
    temp = raw_instructions.replace('move ', '').replace('from ', '').replace('to ', '')
    instructions = [[eval(x) for x in i.split()] for i in temp.split('\n')]
    return instructions


def execute_instructions(start_stacks, instructions):
    stacks = start_stacks
    for i in instructions:
        stacks[i[2]] += list(reversed(stacks[i[1]][-i[0]:]))
        stacks[i[1]] = stacks[i[1]][:-i[0]]
    output = ''
    for s in stacks.values():
        output += s[-1]
    return output
