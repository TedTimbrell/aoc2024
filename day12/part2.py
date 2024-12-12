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
        edges = set()
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
                    edges.add((r, c, (rdiff, cdiff)))
        sides = 0
        while edges:
            key = edges.pop()
            r, c, (diff) = key
            sides += 1
            for rdiff, cdiff in _DIRECTION_MAPPING[diff]:
                idx = 1
                while (pos := (r + rdiff * idx, c + cdiff * idx, diff)) in edges:
                    idx += 1
                    edges.remove(pos)

        return area * sides

    cost = 0
    for row in range(len(input_map)):
        for col in range(len(input_map[row])):
            if (row, col) not in seen:
                cost += _find_price(row, col)
    print(cost)


if __name__ == "__main__":
    main()
