from utils import (
    load_input,
    yield_relevant_conditions,
    build_dependency_map,
    is_valid_update,
)


def get_incorrect_entries(relevant_conditions, update):
    dependencies, dep_count = build_dependency_map(relevant_conditions)
    incorrect_entries = []
    for num in update:
        if dep_count[num] != 0:
            incorrect_entries.append(num)
        for dep in dependencies[num]:
            dep_count[dep] -= 1
    return incorrect_entries


def topological_sort(relevant_conditions, update):
    dependencies, dep_count = build_dependency_map(relevant_conditions)
    current = [dep for dep in update if dep_count[dep] == 0]
    new_update = []
    while current:
        new_update.extend(current)
        new_current = []
        for num in current:
            for dep in dependencies[num]:
                dep_count[dep] -= 1
                if dep_count[dep] == 0:
                    new_current.append(dep)
        current = new_current
    return new_update


def main():
    conditions, updates = load_input()
    print(len(conditions), len(updates))
    total = 0
    count_valid = 0
    count_invalid = 0
    for update in updates:
        relevant_conditions = list(yield_relevant_conditions(conditions, update))
        if not is_valid_update(conditions, update):
            corrected_update = topological_sort(relevant_conditions, update)
            total += corrected_update[len(corrected_update) // 2]
            count_invalid += 1
        else:
            count_valid += 1
    print(f"{count_valid=} {count_invalid=}")

    print(total)


if __name__ == "__main__":
    main()
