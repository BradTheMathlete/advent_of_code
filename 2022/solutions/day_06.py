test_input_0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_input_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_input_2 = "nppdvjthqldpwncqszvftbrmjlhg"
test_input_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_input_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
challenge_input_loc = "2022/inputs/day_06.txt"
challenge_input = open(challenge_input_loc).read()


def find_subroutine(stream):
    loc = 4
    while True:
        if len(set((stream[loc - 4:loc]))) == 4:
            return loc
        loc += 1
