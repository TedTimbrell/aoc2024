"""A better attempt at part 2 of the solution for day 9 using heaps representing the lengths and starts of """

import heapq
from collections import defaultdict
from part1 import load_input, checksum


def create_ranges(rep):
    disk = []
    disk_length = 0
    for idx, char in enumerate(rep):
        leng = int(char)
        if idx % 2:
            disk.append((disk_length, disk_length + leng, None))
        else:
            disk.append((disk_length, disk_length + leng, idx // 2))
        disk_length += leng
    return disk


def _create_distance_heaps(ranges):
    distance_heaps = defaultdict(list)
    for start, end, val in ranges:
        if val is None:
            distance_heaps[end - start].append((start, end, None))
    for key in distance_heaps:
        heapq.heapify(distance_heaps[key])
    return distance_heaps


def _yield_reversed_ranges(ranges):
    for r in reversed(ranges):
        if r[2] is not None:
            yield r


def _flip_tuple(tuple):
    flipped_start, flipped_end, val = tuple
    return -1 * flipped_start, -1 * flipped_end, val


# NOTE: This is wrong, we can't pull from the front for these distance heaps, we need to pull from the end
# we just need to filter out values that have already passed from being selected
def _relevant_queue(distance_heaps, placed, current_end):
    options = [
        (h[0][0], h) for h in distance_heaps.values() if h and h[0][0] >= current_end
    ]
    if placed and -1 * placed[0][1] >= current_end:
        options.append((-1 * placed[0][0], placed))
    if options:
        return max(options)[1]
    return None


def main():
    rep = load_input()
    ranges = create_ranges(rep)

    distance_heaps = _create_distance_heaps(ranges)
    placed = []

    new_ranges = []

    for start, end, value in _yield_reversed_ranges(ranges):
        # handle placing ranges we've already swapped into the new ranges
        while placed and _flip_tuple(placed[0])[0] >= end:
            tup = heapq.heappop(placed)
            tup = _flip_tuple(tup)
            new_ranges.append(tup)
        if value is not None:
            pass
        else:
            new_ranges.append(
                start,
                end,
            )


if __name__ == "__main__":
    main()
