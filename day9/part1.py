def load_input():
    with open("day9/input.txt", "r", encoding="utf-8") as f:
        return f.read().strip("\n ")


def checksum(disk):
    return sum(idx * val for idx, val in enumerate(disk) if isinstance(val, int))


def create_disk(rep):
    disk = []
    for idx, char in enumerate(rep):
        leng = int(char)
        if idx % 2:
            disk.extend(["."] * leng)
        else:
            disk.extend([idx // 2] * leng)
    return disk


def main():
    rep = load_input()
    disk = create_disk(rep)
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
