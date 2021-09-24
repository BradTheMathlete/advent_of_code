test_input = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
    "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm",
    "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in"
]
challenge_input_loc = "2020/inputs/day_04.txt"
challenge_input = open(challenge_input_loc).read().split("\n\n")


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]


def process_input(unprocessed_input: list) -> list:
    return [i.replace("\n", " ").split() for i in unprocessed_input]


def to_dict(passport: list) -> dict:
    return {i[:3]: i[4:] for i in passport}


def fields_present(passport: dict, fields: list) -> bool:
    for f in fields:
        if f not in passport:
            return False
    return True


def challenge_01(passports: list, fields: list) -> int:
    valid_passports = 0
    for passport in process_input(passports):
        passport_dict = to_dict(passport)
        if fields_present(passport_dict, fields):
            valid_passports += 1
    return valid_passports


print(challenge_01(test_input, required_fields))
print(challenge_01(challenge_input, required_fields))
