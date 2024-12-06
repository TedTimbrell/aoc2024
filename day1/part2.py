from collections import Counter


def main():
    l1 = []
    l2 = []

    with open("day1/day_1_input.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n ")
            vals = [part for part in line.split(" ") if part]
            n1, n2 = vals
            l1.append(int(n1))
            l2.append(int(n2))

    l2_counts = Counter(l2)
    similarity_score = 0
    for num in l1:
        similarity_score += num * l2_counts[num]
    print(similarity_score)
    return similarity_score


if __name__ == "__main__":
    main()
