def main():
    l1 = []
    l2 = []
    with open("day1/day_1_input.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n ")
            print(line)
            vals = [part for part in line.split(" ") if part]
            n1, n2 = vals
            l1.append(int(n1))
            l2.append(int(n2))

    l1.sort()
    l2.sort()
    diff = sum(abs(n1 - n2) for n1, n2 in zip(l1, l2))
    print(diff)


if __name__ == "__main__":
    main()
