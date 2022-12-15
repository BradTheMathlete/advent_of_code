import numpy as np
from typing import List

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """.split("\n\n")
challenge_input_loc = "2021/inputs/day_04.txt"
challenge_input = open(challenge_input_loc).read().split("\n\n")


def process_input(bingo_input: List[str]):
    numbers = [eval(i) for i in bingo_input[0].split(",")]
    boards = [
        np.fromstring(i, dtype=int, sep='\n').reshape(5, 5)
        for i in bingo_input[1:]
    ]
    return numbers, boards


x, y = process_input(test_input)

b3 = y[2]
winner = False
for i in range(1, len(x)):
    for j in range(5):
        print(i, j, set(x[:i]), set(b3[j, :]))
        if len(set(x[:i]).intersection(set(b3[j, :]))) == 5:
            print("row", j, "is a winner!")
            winner = True
            break
        if len(set(x[:i]).intersection(set(b3[:, j]))) == 5:
            print("row", j, "is a winner!")
            winner = True
            break
    if winner:
        break
