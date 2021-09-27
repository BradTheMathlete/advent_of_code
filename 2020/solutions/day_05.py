test_input = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
challenge_input_loc = "2020/inputs/day_05.txt"
challenge_input = open(challenge_input_loc).read().splitlines()


def middle_index(given_list: list) -> int:
    return len(given_list) // 2


def find_row(boarding_pass: str) -> int:
    list_of_rows = list(range(128))
    row_characters = boarding_pass[:7]
    for r in row_characters:
        if r == 'F':
            list_of_rows = list_of_rows[:middle_index(list_of_rows)]
        elif r == 'B':
            list_of_rows = list_of_rows[middle_index(list_of_rows):]
        else:
            raise ValueError
    return list_of_rows[0]


def find_seat(boarding_pass: str) -> int:
    list_of_seats = list(range(8))
    seat_characters = boarding_pass[7:]
    for s in seat_characters:
        if s == 'L':
            list_of_seats = list_of_seats[:middle_index(list_of_seats)]
        elif s == 'R':
            list_of_seats = list_of_seats[middle_index(list_of_seats):]
        else:
            raise ValueError
    return list_of_seats[0]


def seat_id(boarding_pass: str) -> int:
    return (find_row(boarding_pass) * 8) + find_seat(boarding_pass)


def max_id(boarding_passes: list) -> int:
    max_seat_id = 0
    for bp in boarding_passes:
        candidate = seat_id(bp)
        if candidate > max_seat_id:
            max_seat_id = candidate
    return max_seat_id


print(max_id(test_input))
print(max_id(challenge_input))
