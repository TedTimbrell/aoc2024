
def load_input():
    with open("day9/input.txt", "r", encoding="utf-8") as f:
        return f.read().strip("\n ")

def checksum(disk):
    return sum(
        idx * val
        for idx, val in enumerate(disk)
        if isinstance(val, int)
    )

def create_disk(rep):
    disk = []
    empty_ranges =[]
    for idx, char in enumerate(rep):
        leng = int(char)
        if idx % 2:
            prior = len(disk)
            disk.extend(["."] * leng)
            empty_ranges.append((prior, prior + leng))
        else:
            disk.extend([idx // 2] * leng)
    return disk, empty_ranges

def main():
    rep = load_input()
    disk = []
    for idx, char in enumerate(rep):
        leng = int(char)
        if idx % 2:
            # prior = len(disk)
            disk.extend(["."] * leng)
            # empty_space.extend(range(prior, prior + leng))
        else:
            # prior = len(disk)
            disk.extend([idx // 2] * leng)
            # ids.extend(range(prior, prior + leng))
    trailing = len(disk) - 1
    for leading in range(len(disk)):
        if disk[leading] == ".":
            while trailing > leading and disk[trailing] == ".":
                trailing -= 1
            disk[leading] = disk[trailing]
            disk[trailing] = "."
        
    print(checksum(disk))
    




        



if __name__ == "__main__":
    main()