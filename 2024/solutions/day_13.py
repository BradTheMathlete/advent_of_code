import re
import pulp

def process_input(input_data):
    machine_inputs = []
    for i in input_data.split('\n\n'):
        machine_inputs.append(re.findall(r'X[\+\=](\d*), Y[\+\=](\d*)', i))
    return machine_inputs

def optimise(machine_input):
    problem = pulp.LpProblem('claw_machine', pulp.LpMinimize)
    a = pulp.LpVariable('A', lowBound=0, upBound=100, cat='Integer')
    b = pulp.LpVariable('B', lowBound=0, upBound=100, cat='Integer')
    problem += 3 * a + b
    for i in range(2):
        problem += eval(machine_input[0][i]) * a + eval(machine_input[1][i]) * b == eval(machine_input[2][i])
    solution = problem.solve(pulp.apis.coin_api.PULP_CBC_CMD(msg=0))
    feasible = solution == 1
    return feasible, problem

def task_01(machine_inputs) -> int:
    count = 0
    for m in machine_inputs:
        f, p = optimise(m)
        if f:
            count += int(pulp.value(p.objective))
    return count

def simultaneous_equations(machine_input):
    ax = eval(machine_input[0][0])
    bx = eval(machine_input[1][0])
    px = eval(machine_input[2][0]) + 10000000000000
    ay = eval(machine_input[0][1])
    by = eval(machine_input[1][1])
    py = eval(machine_input[2][1]) + 10000000000000
    b, b_remainder = divmod((ax * py) - (ay * px), (ax * by) - (ay * bx))
    a, a_remainder = divmod(px - (bx * b), ax)
    feasible = a_remainder == 0 and b_remainder == 0
    return feasible, a, b

def task_02(machine_inputs) -> int:
    count = 0
    for m in machine_inputs:
        f, a, b = simultaneous_equations(m)
        if f:
            count += (3 * a) + b
        pass
    return count

def main(input_data):
    machine_inputs = process_input(input_data)
    output_01 = task_01(machine_inputs)
    output_02 = task_02(machine_inputs)
    return output_01, output_02

if __name__ == "__main__":
    test_input = '''Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400\n
Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176\n
Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450\n
Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279'''
    challenge_input = open("2024/inputs/day_13.txt").read()

    # test_01 = main(test_input)
    test_01, test_02 = main(test_input)
    # challenge_01 = main(challenge_input)
    challenge_01, challenge_02 = main(challenge_input)

    print('finished')