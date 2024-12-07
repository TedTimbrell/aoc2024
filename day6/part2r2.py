from part1 import (
    DIRECTIONS,
    load_map,
    get_guard_start,
    is_inbounds,
    get_locations,
)
from bisect import bisect_right


def create_obstacle_lists(guard_map):
    row_obstacles = [
        sorted([col for col, cell in enumerate(row) if cell == "#"])
        for row in guard_map
    ]
    col_obstacles = [
        sorted([row for row, cell in enumerate(col) if cell == "#"])
        for col in zip(*guard_map)
    ]
    return row_obstacles, col_obstacles


def update_obstacle_lists(row_obstacles, col_obstacles, location, add=True):
    row, col = location
    if add:
        row_obstacles[row].append(col)
        col_obstacles[col].append(row)
    else:
        row_obstacles[row].remove(col)
        col_obstacles[col].remove(row)
    row_obstacles[row].sort()
    col_obstacles[col].sort()


def find_next_position(current_loc, current_direction, row_obstacles, col_obstacles):
    row, col = current_loc
    if current_direction == 0:  # Up
        obstacles = col_obstacles[col]
        idx = bisect_right(obstacles, row)
        return (obstacles[idx - 1] + 1, col) if idx > 0 else (-1, col)
    elif current_direction == 1:  # Right
        obstacles = row_obstacles[row]
        idx = bisect_right(obstacles, col)
        return (
            (row, obstacles[idx] - 1)
            if idx < len(obstacles)
            else (row, len(row_obstacles[row]))
        )
    elif current_direction == 2:  # Down
        obstacles = col_obstacles[col]
        idx = bisect_right(obstacles, row)
        return (
            (obstacles[idx] - 1, col)
            if idx < len(obstacles)
            else (len(col_obstacles[col]), col)
        )
    elif current_direction == 3:  # Left
        obstacles = row_obstacles[row]
        idx = bisect_right(obstacles, col)
        return (row, obstacles[idx - 1] + 1) if idx > 0 else (row, -1)


def is_loop(guard_map, row_obstacles, col_obstacles):
    current_direction = 0
    visited = set()
    current_loc = get_guard_start(guard_map)
    while is_inbounds(current_loc, guard_map):
        if (current_loc, current_direction) in visited:
            return True
        visited.add((current_loc, current_direction))
        while (
            (
                new_pos := find_next_position(
                    current_loc, current_direction, row_obstacles, col_obstacles
                )
            )
            and is_inbounds(new_pos, guard_map)
            and new_pos == current_loc
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
    row_obstacles, col_obstacles = create_obstacle_lists(guard_map)
    total = 0
    for location in locations:
        guard_map[location[0]][location[1]] = "#"
        # print(row_obstacles)
        # print(col_obstacles)
        # print(location, "location")
        update_obstacle_lists(row_obstacles, col_obstacles, location, add=True)

        if is_loop(guard_map, row_obstacles, col_obstacles):
            total += 1

        guard_map[location[0]][location[1]] = "."
        update_obstacle_lists(row_obstacles, col_obstacles, location, add=False)

    print(total)


if __name__ == "__main__":
    main()
