test_input_0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_input_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_input_2 = "nppdvjthqldpwncqszvftbrmjlhg"
test_input_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_input_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
challenge_input_loc = "2022/inputs/day_06.txt"
challenge_input = open(challenge_input_loc).read()


def find_subroutine(stream, dist_len):
    loc = dist_len
    while True:
        if len(set((stream[loc - dist_len:loc]))) == dist_len:
            return loc
        loc += 1


p1_output = find_subroutine(challenge_input, 4)
p2_output = find_subroutine(challenge_input, 14)
