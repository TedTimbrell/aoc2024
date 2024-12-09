from part1 import load_input, get_location_list


def yield_in_line(grid, row, column, rdiff, cdiff):
    idx = 0

    while 0 <= (n_row := row + rdiff * idx) < len(grid) and 0 <= (
        n_col := column + cdiff * idx
    ) < len(grid[0]):
        yield (n_row, n_col)
        idx += 1


def main():
    grid = load_input()
    node_locations = get_location_list(grid)

    antinode_locations = set()

    for char, locations in node_locations.items():
        for idx1 in range(len(locations)):
            l1 = locations[idx1]
            r1, c1 = l1
            for idx2 in range(idx1 + 1, len(locations)):
                l2 = locations[idx2]
                r2, c2 = l2

                rdiff = r2 - r1
                cdiff = c2 - c1

                antinode_locations.update(
                    yield_in_line(grid, r1, c1, -1 * rdiff, -1 * cdiff)
                )
                antinode_locations.update(yield_in_line(grid, r2, c2, rdiff, cdiff))

    print(len(antinode_locations))


if __name__ == "__main__":
    main()
