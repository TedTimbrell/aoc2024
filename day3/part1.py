class InvalidNumber(Exception):
    pass


def _get_number_starting_at(s, idx, expecting_end_char):
    start = idx
    while idx < len(s) and s[idx].isdigit():
        idx += 1

    print(s[start:idx], idx >= len(s), idx - start > 3, s[idx] != expecting_end_char)
    if idx >= len(s) or not (1 <= idx - start <= 3) or s[idx] != expecting_end_char:
        raise InvalidNumber
    return int(s[start:idx]), idx


def main():
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        contents = f.read()
    # contents = "mul(3,4)mul(4,5)"
    start_idx = 0
    mul_string = "mul("
    do_string = "do()"
    do_idx = 0
    dont_string = "don't()"
    dont_idx = 0
    enabled = True
    total = 0
    idx = 0
    while idx < len(contents):
        print(contents[idx], start_idx)
        if enabled and contents[idx] == mul_string[start_idx]:
            start_idx += 1
        else:
            start_idx = 0
        if contents[idx] == do_string[do_idx]:
            do_idx += 1
        else:
            do_idx = 0
        if contents[idx] == dont_string[dont_idx]:
            dont_idx += 1
        else:
            dont_idx = 0

        if do_idx >= len(do_string):
            enabled = True
            do_idx = 0
        if dont_idx >= len(dont_string):
            enabled = False
            dont_idx = 0

        if start_idx >= len(mul_string):
            num_start = idx + 1
            try:
                num_1, n_idx = _get_number_starting_at(contents, num_start, ",")
                num_2, n_idx = _get_number_starting_at(contents, n_idx + 1, ")")
                total += num_1 * num_2
                idx = n_idx
            except InvalidNumber:
                pass
            start_idx = 0

        idx += 1
    print(total)


if __name__ == "__main__":
    main()
