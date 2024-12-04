def process_input(input_data):
    list1 = []
    list2 = []
    temp = input_data.replace('   ', ',').split('\n')
    for i in temp:
        a, b = i.split(',')
        list1.append(eval(a))
        list2.append(eval(b))
    return list1, list2

def task_01(list1, list2):
    list1.sort()
    list2.sort()
    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])
    return diff

def task_02(list1, list2):
    similarity_score = 0
    for i in list1:
        similarity_score += (i * list2.count(i))
    return similarity_score

def main(input_data):
    list1, list2 = process_input(input_data)
    output_01 = task_01(list1, list2)
    output_02 = task_02(list1, list2)
    return output_01, output_02

if __name__ == "__main__":
    test_input = '3   4\n4   3\n2   5\n1   3\n3   9\n3   3'
    challenge_input = open("2024/inputs/day_01.txt").read()

    test_01, test_02 = main(test_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')
 