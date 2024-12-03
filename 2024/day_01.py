test_input = '3   4\n4   3\n2   5\n1   3\n3   9\n3   3'
challenge_input_loc = "2024/input.txt"
challenge_input = open(challenge_input_loc).read()


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
    diff = []
    for i in range(len(list1)):
        diff.append(abs(list1[i] - list2[i]))
    return sum(diff)

if __name__ == "__main__":
    list1, list2 = process_input(challenge_input)
    output = task_01(list1, list2)
    print(output)
#     with open('data\day1_data.txt', 'r') as data_file:
#         input_data = data_file.read()
 
#     day1_part2(data=input_data)
 