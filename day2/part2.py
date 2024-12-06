def _is_safe(report: list[int], without=None):
    is_increasing = None
    report = list(report[r] for r in range(len(report)) if without != r)
    for first_idx, second_idx in zip(range(len(report)), range(1, len(report))):
        first_num = report[first_idx]
        next_num = report[second_idx]

        if is_increasing is None:
            is_increasing = next_num - first_num > 0
        elif is_increasing and next_num < first_num:
            if without is None:
                return (
                    _is_safe(report, 0)
                    or _is_safe(report, 1)
                    or _is_safe(report, first_idx)
                    or _is_safe(report, second_idx)
                )
            return False
        elif not is_increasing and next_num > first_num:
            if without is None:
                return (
                    _is_safe(report, 0)
                    or _is_safe(report, 1)
                    or _is_safe(report, first_idx)
                    or _is_safe(report, second_idx)
                )
            return False

        if not (1 <= abs(first_num - next_num) <= 3):
            if without is None:
                return _is_safe(report, first_idx) or _is_safe(report, second_idx)
            return False
    return True


def main():
    test_report = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
        "29 24 23 20 18 15 12 8",
    ]
    with open("day2/input.txt", "r", encoding="utf-8") as f:
        reports = [
            [int(strnum) for strnum in line.strip("\n").split(" ")]
            for line in f.readlines()
        ]
    print(len(reports))
    safe = list(_is_safe(report) for report in reports)
    # print(safe)
    # print(num_safe)
    print(sum(safe))


if __name__ == "__main__":
    main()
