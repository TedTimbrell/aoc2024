from part1 import (
    DIRECTIONS,
    load_map,
    add_pos,
    is_inbounds,
    get_locations,
    get_guard_start,
)


def is_loop(guard_map):
    current_direction = 0
    visited = set()
    current_loc = get_guard_start(guard_map)
    visited = set()
    while is_inbounds(current_loc, guard_map):
        if (current_loc, current_direction) in visited:
            return True
        visited.add((current_loc, current_direction))
        while (
            (new_pos := add_pos(current_loc, current_direction))
            and is_inbounds(new_pos, guard_map)
            and guard_map[new_pos[0]][new_pos[1]] == "#"
        ):
            current_direction = (current_direction + 1) % len(DIRECTIONS)
        current_loc = new_pos
    return False


def main():
    guard_map = load_map()
    guard_start = get_guard_start(guard_map)
    locations = get_locations(guard_map)
    # we can't place an obstruction in the guard's current location
    locations.remove(guard_start)
    total = 0
    for location in locations:
        guard_map[location[0]][location[1]] = "#"

        if is_loop(guard_map):
            total += 1
        guard_map[location[0]][location[1]] = "."

    print(total)


if __name__ == "__main__":
    main()
