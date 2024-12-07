from enum import Enum


class Operator(Enum):
    ADD = "add"
    MULTIPLY = "multiply"
    CONCAT = "concat"


def load_input():
    with open("day7/input.txt", "r", encoding="utf-8") as f:
        equations = [
            tuple(val.strip() for val in line.strip("\n ").split(":"))
            for line in f.readlines()
        ]
    parsed = []
    for eq in equations:
        output, items = eq
        parsed.append((int(output), [int(item) for item in items.strip().split(" ")]))
    return parsed


def solve_equation(target, nums, idx, prior, operators):
    if idx >= len(nums):
        yield target == prior
    else:
        if idx != 0:
            if Operator.MULTIPLY in operators:
                yield from solve_equation(
                    target, nums, idx + 1, prior * nums[idx], operators
                )
            if Operator.CONCAT in operators:
                yield from solve_equation(
                    target,
                    nums,
                    idx + 1,
                    prior * (10 ** len(str(nums[idx]))) + nums[idx],
                    operators,
                )
        if Operator.ADD in operators:
            yield from solve_equation(
                target, nums, idx + 1, prior + nums[idx], operators
            )


def main():
    equations = load_input()
    total = 0
    for target, items in equations:
        if any(solve_equation(target, items, 0, 0, [Operator.ADD, Operator.MULTIPLY])):
            total += target
    print(total)


if __name__ == "__main__":
    main()
