def load_input():
    with open("day10/input.txt", "r", encoding="utf-8") as f:
        return [[int(x) for x in x.strip("\n ")] for x in f.readlines()]


def main():
    top_map = load_input()
    count_cache = {}

    def _count_peaks(row, column):
        # nonlocal count_cache
        # nonlocal top_map
        if (row, column) in count_cache:
            return count_cache[(row, column)]

        if top_map[row][column] == 9:
            return 1
        new_peaks = 0
        for rdiff, cdiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            nrow = row + rdiff
            ncol = column + cdiff

            if (
                0 <= nrow < len(top_map)
                and 0 <= ncol < len(top_map[0])
                and top_map[nrow][ncol] == top_map[row][column] + 1
            ):
                new_peaks += _count_peaks(nrow, ncol)

        count_cache[(row, column)] = new_peaks
        return new_peaks

    count = 0
    for row in range(len(top_map)):
        for col in range(len(top_map[row])):
            if top_map[row][col] == 0:
                count += _count_peaks(row, col)
    print(count)


if __name__ == "__main__":
    main()
