def process_input(input_data):
    temp = input_data.split('\n\n')
    rules = []
    updates = []
    for r in temp[0].split('\n'):
        rules.append([eval(i) for i in r.split('|')])
    for u in temp[1].split('\n'):
        updates.append([eval(i) for i in u.split(',')])
    return rules, updates

def relevant_rule(rule, update) -> bool:
    return len(set(rule).intersection(set(update))) == 2

def rule_followed(rule, update) -> bool:
    return update.index(rule[0]) < update.index(rule[1])

def is_valid(rules, update) -> bool:
    for r in rules:
        if relevant_rule(r, update):
            if not rule_followed(r, update):
                return False
    return True

def middle_value(update) -> int:
    middle_index = int((len(update) - 1) / 2)
    return update[middle_index]

def task_01(rules, updates) -> int:
    count = 0
    for u in updates:
        if is_valid(rules, u):
            count += middle_value(u)
    return count

def main(input_data):
    rules, updates = process_input(input_data)
    output_01 = task_01(rules, updates)
    return output_01

if __name__ == "__main__":
    test_input = """47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n
75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"""
    challenge_input = open("2024/inputs/day_05.txt").read()

    test_01 = main(test_input)
    # test_01, test_02 = main(test_input)
    challenge_01 = main(challenge_input)
    # challenge_01, challenge_02 = main(challenge_input)

    print('finished')