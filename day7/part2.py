from part1 import load_input, solve_equation, Operator


def main():
    equations = load_input()
    total = 0
    for target, items in equations:
        if any(
            solve_equation(
                target, items, 0, 0, [Operator.ADD, Operator.MULTIPLY, Operator.CONCAT]
            )
        ):
            total += target
    print(total)


if __name__ == "__main__":
    main()
