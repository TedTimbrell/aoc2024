from collections import defaultdict


def load_input():
    with open("day8/input.txt", "r", encoding="utf-8") as f:
        return [line.strip(" \n") for line in f.readlines()]


def is_valid_location(grid, row, column):
    return 0 <= row < len(grid) and 0 <= column < len(grid[row])


def get_location_list(grid):
    node_locations = defaultdict(list)
    for ridx, row in enumerate(grid):
        for cidx, char in enumerate(row):
            if char != ".":
                node_locations[char].append((ridx, cidx))
    return node_locations


def print_grid(grid, antinode_locations):
    for ridx, row in enumerate(grid):
        vals = []
        for cidx, col in enumerate(row):
            if (ridx, cidx) in antinode_locations and grid[ridx][cidx] == ".":
                vals.append("#")
            else:
                vals.append(col)
        print("".join(vals))


def main():
    grid = load_input()
    node_locations = get_location_list(grid)

    antinode_locations = set()

    for locations in node_locations.values():
        for idx1 in range(len(locations)):
            l1 = locations[idx1]
            r1, c1 = l1
            for idx2 in range(idx1 + 1, len(locations)):
                l2 = locations[idx2]
                r2, c2 = l2

                rdiff = r2 - r1
                cdiff = c2 - c1

                antinode_r = rdiff * -1 + r1
                antinode_c = cdiff * -1 + c1
                if is_valid_location(grid, antinode_r, antinode_c):
                    antinode_locations.add((antinode_r, antinode_c))
                antinode_r = rdiff + r2
                antinode_c = cdiff + c2
                if is_valid_location(grid, antinode_r, antinode_c):
                    antinode_locations.add((antinode_r, antinode_c))
    print(len(antinode_locations))


if __name__ == "__main__":
    main()
