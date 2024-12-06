from utils import load_input, is_valid_update


def main():
    conditions, updates = load_input()
    print(len(conditions), len(updates))
    total = 0
    for update in updates:
        if is_valid_update(conditions, update):
            total += update[len(update) // 2]
    print(total)


if __name__ == "__main__":
    main()
