test_input = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",
]
challenge_input_loc = "2020/inputs/day_05.txt"
challenge_input = open(challenge_input_loc).read().splitlines()


list_of_rows = list(range(128))
list_of_seats = list(range(8))


def middle_index(given_list: list) -> int:
    return len(given_list)//2

