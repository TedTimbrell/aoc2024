"""I didn't realize this problem was just a system of equations until part 2. So
much for a decade and a half of math education..."""

import math
import re

REGEX = r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)"""
import dataclasses


@dataclasses.dataclass
class Puzzle:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int


def yield_input():
    with open("day13/input.txt", "r", encoding="utf-8") as f:
        file = f.read()
        for match in re.findall(REGEX, file):
            yield Puzzle(*[int(match[idx]) for idx in range(6)])


_A_COST = 3
_B_COST = 1


def main():
    tokens_to_win = 0
    for puzzle in yield_input():
        min_cost = None
        for idx in range(
            math.ceil(max(puzzle.prize_x / puzzle.a_x, puzzle.prize_y / puzzle.a_y)) + 1
        ):

            remaining_x = puzzle.prize_x - (puzzle.a_x * idx)
            remaining_y = puzzle.prize_y - (puzzle.a_y * idx)

            if (
                remaining_x % puzzle.b_x == 0
                and remaining_y % puzzle.b_y == 0
                and remaining_x / puzzle.b_x == remaining_y / puzzle.b_y
            ):
                cost = _A_COST * idx + _B_COST * (remaining_x / puzzle.b_x)
                if min_cost is None:
                    min_cost = cost
                min_cost = min(cost, min_cost)

        if min_cost is not None:
            tokens_to_win += min_cost

    print(tokens_to_win)


if __name__ == "__main__":
    main()
