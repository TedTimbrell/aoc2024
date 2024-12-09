import bisect
import dataclasses
from typing import Optional
from part1 import load_input, checksum, create_disk

@dataclasses.dataclass
class Block:
    length: int
    idx: Optional[int]
    start: int
    end: int

def create_blocks(rep):
    disk = []
    disk_length = 0
    for idx, char in enumerate(rep):
        leng = int(char)
        if idx % 2:
            disk.append(Block(leng, None, disk_length, disk_length + leng))
        else:
            disk.append(Block(leng, idx // 2, disk_length, disk_length + leng))
        disk_length += leng
    return disk


def main():
    rep = load_input()
    disk = create_disk(rep)
    blocks = create_blocks(rep)
    
    sorted_empty_blocks = sorted([b for b in blocks if b.idx is None], key=lambda x: (x.length, x.start, x.end))
    new_disk = []
    for block in reversed(blocks):
        if block.idx is not None:
            bisect.bisect_left(sorted_empty_blocks, block)





if __name__ == "__main__":
    main()