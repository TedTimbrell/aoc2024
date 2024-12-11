def load_input():
    with open("day11/input.txt", "r", encoding="utf-8") as f:
        return f.read().strip("\n ").split(" ")


def main():
    stones = load_input()
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) % 2 == 0:
                new_stones.append(stone[: len(stone) // 2])
                new_stones.append(str(int(stone[len(stone) // 2 :])))
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones
    print(len(stones))


if __name__ == "__main__":
    main()
