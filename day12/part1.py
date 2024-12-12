from collections import Counter


def load_input():
    with open("day12/input.txt", "r", encoding="utf-8") as f:
        return [line.strip("\n ") for line in f.readlines()]


def main():
    input_map = load_input()
    seen = set()

    def _find_price(row, col):
        sides = 0
        area = 0
        pieces = [(row, col)]
        while pieces:
            r, c = pieces.pop()
            area += 1
            seen.add((r, c))
            for rdiff, cdiff in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nrow = r + rdiff
                ncol = c + cdiff
                if (
                    0 <= nrow < len(input_map)
                    and 0 <= ncol < len(input_map[0])
                    and input_map[nrow][ncol] == input_map[row][col]
                ):
                    if (nrow, ncol) not in seen:
                        pieces.append((nrow, ncol))
                        seen.add((nrow, ncol))
                else:
                    sides += 1

        return area * sides

    cost = 0
    for row in range(len(input_map)):
        for col in range(len(input_map[row])):
            if (row, col) not in seen:
                cost += _find_price(row, col)
    print(cost)


if __name__ == "__main__":
    main()
