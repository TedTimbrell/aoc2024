import dataclasses
from typing import Optional
from part1 import load_input, checksum


@dataclasses.dataclass
class Block:
    length: int
    idx: Optional[int]


def create_blocks(rep):
    disk = []
    disk_length = 0
    for idx, char in enumerate(rep):
        leng = int(char)
        if idx % 2:
            disk.append(Block(leng, None))
        else:
            disk.append(Block(leng, idx // 2))
        disk_length += leng
    return disk


def disk_from_blocks(blocks):
    disk = []
    for block in blocks:
        disk.extend([block.idx if block.idx is not None else "."] * block.length)
    return disk


def main():
    rep = load_input()
    blocks = create_blocks(rep)
    from collections import Counter

    print(Counter((b.length for b in blocks if b.idx is None)))
    reversed_blocks = list(reversed(blocks))
    start_idx = 0
    def_to_delete = []
    while start_idx < len(reversed_blocks):
        block = reversed_blocks[start_idx]
        if block.idx is not None:
            fitting_tup = next(
                (
                    (len(reversed_blocks) - 1 - idx, b)
                    for idx, b in enumerate(reversed(reversed_blocks))
                    if b
                    and b.idx is None
                    and b.length >= block.length
                    and len(reversed_blocks) - 1 - idx > start_idx
                ),
                None,
            )
            if fitting_tup is not None:
                empty_idx, empty_block = fitting_tup
                empty_length = empty_block.length

                empty_block.length = block.length
                empty_block.idx = block.idx
                if (remaining := (empty_length - block.length)) > 0:
                    reversed_blocks.insert(
                        empty_idx,
                        Block(
                            remaining,
                            None,
                        ),
                    )
                block.idx = None

        start_idx += 1

    reversed_blocks = [
        block for idx, block in enumerate(reversed_blocks) if idx not in def_to_delete
    ]

    print(checksum(disk_from_blocks(reversed(reversed_blocks))))


if __name__ == "__main__":
    main()
