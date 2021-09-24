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


invalid_input = [
    "eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946",
    "hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007",
]
valid_input = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f",
    "eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
]


def valid_byr(byr: str) -> bool:
    if len(byr) != 4:
        return False
    if eval(byr) < 1920 or eval(byr) > 2002:
        return False
    return True


def valid_iyr(iyr: str) -> bool:
    if len(iyr) != 4:
        return False
    if eval(iyr) < 2010 or eval(iyr) > 2020:
        return False
    return True


def valid_eyr(eyr: str) -> bool:
    if len(eyr) != 4:
        return False
    if eval(eyr) < 2020 or eval(eyr) > 2030:
        return False
    return True


def valid_hgt(hgt: str) -> bool:
    if hgt[-2:] not in ["cm", "in"]:
        return False
    if hgt[-2:] == "cm" and (eval(hgt[:-2]) < 150 or eval(hgt[:-2]) > 193):
        return False
    if hgt[-2:] == "in" and (eval(hgt[:-2]) < 59 or eval(hgt[:-2]) > 76):
        return False
    return True


def valid_hcl(hcl: str) -> bool:
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False
    for i in range(1, 7):
        if hcl[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
            return False
    return True


def valid_ecl(ecl: str) -> bool:
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return True


def valid_pid(pid: str) -> bool:
    if len(pid) != 9:
        return False
    for i in range(9):
        if pid[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True


def valid_fields(passport: dict) -> bool:
    if not valid_byr(passport["byr"]):
        return False
    if not valid_iyr(passport["iyr"]):
        return False
    if not valid_eyr(passport["eyr"]):
        return False
    if not valid_hgt(passport["hgt"]):
        return False
    if not valid_hcl(passport["hcl"]):
        return False
    if not valid_ecl(passport["ecl"]):
        return False
    if not valid_pid(passport["pid"]):
        return False
    return True


def challenge_02(passports: list, fields: list) -> int:
    valid_passports = 0
    for passport in process_input(passports):
        passport_dict = to_dict(passport)
        if fields_present(passport_dict, fields) and valid_fields(passport_dict):
            valid_passports += 1
    return valid_passports


print(challenge_02(invalid_input, required_fields))
print(challenge_02(valid_input, required_fields))
print(challenge_02(challenge_input, required_fields))
