import re

from part1 import Puzzle, REGEX


def yield_input():

    with open("day13/input.txt", "r", encoding="utf-8") as f:
        file = f.read()
        for match in re.findall(REGEX, file):
            yield Puzzle(
                *[
                    int(match[idx]) + (0 if idx < 4 else 10000000000000)
                    for idx in range(6)
                ]
            )


_A_COST = 3
_B_COST = 1


def _compute_b(puzzle: Puzzle):
    return (puzzle.a_x * puzzle.prize_y - puzzle.a_y * puzzle.prize_x) / (
        puzzle.a_x * puzzle.b_y - puzzle.a_y * puzzle.b_x
    )


def _compute_a(puzzle: Puzzle, b: int):
    return (puzzle.prize_x - b * puzzle.b_x) / puzzle.a_x


def main():
    tokens_to_win = 0
    for puzzle in yield_input():
        num_b = _compute_b(puzzle)
        if num_b % 1 == 0:
            num_a = _compute_a(puzzle, int(num_b))
            if num_a % 1 == 0:
                tokens_to_win += _A_COST * num_a + _B_COST * num_b

    print(tokens_to_win)


if __name__ == "__main__":
    main()
