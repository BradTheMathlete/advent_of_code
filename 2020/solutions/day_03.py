test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]
challenge_input_loc = "2020/inputs/day_03.txt"
challenge_input = open(challenge_input_loc).read().splitlines()


def challenge_01(geology: list, right: int, down: int) -> int:
    trees = 0
    x = 0
    y = 0
    while y < len(geology):
        if geology[y][x] == "#":
            trees += 1
        x = (x + right) % len(geology[y])
        y += down
    return trees


print(challenge_01(test_input, 3, 1))
print(challenge_01(challenge_input, 3, 1))

slopes = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2},
]


def challenge_02(geology: list, traversals: list) -> int:
    total_trees = 1
    for i in traversals:
        total_trees *= challenge_01(geology, i['right'], i['down'])
    return total_trees


print(challenge_02(test_input, slopes))
print(challenge_02(challenge_input, slopes))
