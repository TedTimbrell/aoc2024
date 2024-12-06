_XMAS = "XMAS"


def _contains_string(word_search, string, pos, direction):
    idx = 0
    row, col = pos
    rdiff, cdiff = direction
    while (
        0 <= row < len(word_search)
        and 0 <= col < len(word_search[0])
        and idx < len(string)
        and word_search[row][col] == string[idx]
    ):
        idx += 1
        row += rdiff
        col += cdiff
    return idx == len(string)


def main():
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        word_search = [
            list(line.strip("\n")) for line in f.readlines() if line.strip("\n ")
        ]
    count = 0
    for row in range(1, len(word_search) - 1):
        for col in range(1, len(word_search[0]) - 1):

            if (
                _contains_string(word_search, "MAS", (row - 1, col - 1), (1, 1))
                or _contains_string(word_search, "SAM", (row - 1, col - 1), (1, 1))
            ) and (
                _contains_string(word_search, "SAM", (row - 1, col + 1), (1, -1))
                or _contains_string(word_search, "MAS", (row - 1, col + 1), (1, -1))
            ):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
