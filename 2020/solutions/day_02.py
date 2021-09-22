test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
challenge_input_loc = "2020/inputs/day_02.txt"
challenge_input = open(challenge_input_loc).read().splitlines()


def challenge_01(password_db: list) -> int:
    valid_passwords = 0
    for i in password_db:
        i = i.replace("-", " ").replace(":", "").split()
        lb = eval(i[0])
        ub = eval(i[1])
        required_char = i[2]
        password = i[3]
        occurrences = password.count(required_char)
        if lb <= occurrences <= ub:
            valid_passwords += 1
    return valid_passwords


print(challenge_01(test_input))
print(challenge_01(challenge_input))


def challenge_02(password_db: list) -> int:
    valid_passwords = 0
    for i in password_db:
        i = i.replace("-", " ").replace(":", "").split()
        pos_1 = eval(i[0]) - 1
        pos_2 = eval(i[1]) - 1
        required_char = i[2]
        password = i[3]
        if (password[pos_1] + password[pos_2]).count(required_char) == 1:
            valid_passwords += 1
    return valid_passwords


print(challenge_02(test_input))
print(challenge_02(challenge_input))
