from collections import Counter


def load_input():
    with open("day12/input.txt", "r", encoding="utf-8") as f:
        return [line.strip("\n ") for line in f.readlines()]


_DIRECTION_MAPPING = {
    (1, 0): ((0, -1), (0, 1)),
    (-1, 0): ((0, -1), (0, 1)),
    (0, 1): ((1, 0), (-1, 0)),
    (0, -1): ((1, 0), (-1, 0)),
}


def main():
    input_map = load_input()
    seen = set()

    def _find_price(row, col):
        sides = 0
        area = 0
        pieces = [(row, col)]
        pos_side_counts = Counter()
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
                    pos_side_counts[(r, c, (rdiff, cdiff))] += 1

        sides = 0
        while pos_side_counts:
            key = next(iter(pos_side_counts.keys()))
            pos_side_counts[key] -= 1
            if pos_side_counts[key] == 0:
                del pos_side_counts[key]
            r, c, (diff) = key
            sides += 1
            for rdiff, cdiff in _DIRECTION_MAPPING[diff]:
                idx = 1
                while (
                    pos := (r + rdiff * idx, c + cdiff * idx, diff)
                ) in pos_side_counts:
                    idx += 1
                    pos_side_counts[pos] -= 1
                    if pos_side_counts[pos] == 0:
                        del pos_side_counts[pos]

        print(area, sides)
        return area * sides

    cost = 0
    for row in range(len(input_map)):
        for col in range(len(input_map[row])):
            if (row, col) not in seen:
                cost += _find_price(row, col)
    print(cost)


if __name__ == "__main__":
    main()
