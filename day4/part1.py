_XMAS = "XMAS"


def _contains_xmas(word_search, pos, direction):
    idx = 0
    row, col = pos
    rdiff, cdiff = direction
    while (
        0 <= row < len(word_search)
        and 0 <= col < len(word_search[0])
        and idx < len(_XMAS)
        and word_search[row][col] == _XMAS[idx]
    ):
        idx += 1
        row += rdiff
        col += cdiff
    return idx == len(_XMAS)


def main():
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        word_search = [
            list(line.strip("\n")) for line in f.readlines() if line.strip("\n ")
        ]
    print(word_search[0])
    count = 0
    for row in range(len(word_search)):
        for col in range(len(word_search[0])):
            for rdiff in range(-1, 2):
                for cdiff in range(-1, 2):
                    if rdiff != 0 or cdiff != 0:
                        if _contains_xmas(word_search, (row, col), (rdiff, cdiff)):
                            count += 1
    print(count)


if __name__ == "__main__":
    main()
