def _is_safe(report: list[int]):
    is_increasing = None
    for first_num, next_num in zip(report, report[1:]):
        if is_increasing is None:
            is_increasing = next_num - first_num > 0
        elif is_increasing and next_num < first_num:
            return False
        elif not is_increasing and next_num > first_num:
            return False

        if not (1 <= abs(first_num - next_num) <= 3):
            return False
    return True


def main():

    with open("day2/input.txt", "r", encoding="utf-8") as f:
        reports = [
            [int(strnum) for strnum in line.strip("\n").split(" ")]
            for line in f.readlines()
        ]
    num_safe = sum(int(_is_safe(report)) for report in reports)
    print(num_safe)


if __name__ == "__main__":
    main()
