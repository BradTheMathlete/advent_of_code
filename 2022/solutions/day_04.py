test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
challenge_input_loc = "2022/inputs/day_04.txt"
challenge_input = open(challenge_input_loc).read()


def process_input(input_data):
    temp = [i.split(',') for i in input_data.split('\n')]
    return [[[eval(x) for x in i.split('-')] for i in j] for j in temp]


def check_overlap_1(assignment_pair):
    a1 = assignment_pair[0]
    a2 = assignment_pair[1]
    if a1[0] >= a2[0] and a1[1] <= a2[1]:
        return True
    if a2[0] >= a1[0] and a2[1] <= a1[1]:
        return True
    return False


def check_overlap_2(assignment_pair):
    a1 = assignment_pair[0]
    a2 = assignment_pair[1]
    if a2[0] <= a1[0] <= a2[1]:
        return True
    if a2[0] <= a1[1] <= a2[1]:
        return True
    if a1[0] <= a2[0] <= a1[1]:
        return True
    if a1[0] <= a2[1] <= a1[1]:
        return True
    return False


def count_overlaps_1(processed_data):
    overlaps = [check_overlap_1(i) for i in processed_data]
    return sum(overlaps)


def count_overlaps_2(processed_data):
    overlaps = [check_overlap_2(i) for i in processed_data]
    return sum(overlaps)
