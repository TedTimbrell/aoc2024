DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def load_map():
    with open("day6/test_input.txt", "r", encoding="utf-8") as f:
        return [list(line.strip("\n ")) for line in f.readlines()]


def is_inbounds(pos, board):
    row, col = pos
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return True
    return False


def add_pos(pos, current_direction):
    rdiff, cdiff = DIRECTIONS[current_direction]
    row, col = pos
    return (row + rdiff, col + cdiff)


def get_guard_start(guard_map):
    return next(
        (row, col)
        for row in range(len(guard_map))
        for col in range(len(guard_map[0]))
        if guard_map[row][col] == "^"
    )


def get_locations(guard_map):
    current_direction = 0
    current_loc = get_guard_start(guard_map)
    visited = set()
    while is_inbounds(current_loc, guard_map):
        visited.add(current_loc)
        while (
            (new_pos := add_pos(current_loc, current_direction))
            and is_inbounds(new_pos, guard_map)
            and guard_map[new_pos[0]][new_pos[1]] == "#"
        ):
            current_direction = (current_direction + 1) % len(DIRECTIONS)
        current_loc = new_pos
    return visited


def main():
    guard_map = load_map()
    print(len(get_locations(guard_map)))


if __name__ == "__main__":
    main()
