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
