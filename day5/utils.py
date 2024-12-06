from collections import defaultdict


def load_input(use_sample_input=True):
    conditions = []
    updates = []
    with open(
        "day5/input.txt" if use_sample_input else "day5/test_input.txt",
        "r",
        encoding="utf-8",
    ) as f:
        parsing_conditions = True
        for line in f.readlines():
            line = line.strip(" \n")
            if line == "":
                parsing_conditions = False
            elif parsing_conditions:
                conditions.append(tuple(int(x) for x in line.split("|")))
            else:
                updates.append(tuple(int(x) for x in line.split(",")))
    return conditions, updates


def yield_relevant_conditions(conditions, update):
    update = set(update)
    for val1, val2 in conditions:
        if val1 in update and val2 in update:
            yield (val1, val2)


def build_dependency_map(conditions):
    dependencies = defaultdict(set)
    dep_count = defaultdict(int)
    for val1, val2 in conditions:
        dependencies[val1].add(val2)
        dep_count[val2] += 1
    return dependencies, dep_count


def is_valid_update(conditions, update):
    relevant_conditions = list(yield_relevant_conditions(conditions, update))
    dependencies, dep_count = build_dependency_map(relevant_conditions)
    for num in update:
        if dep_count[num] != 0:
            return False
        for dep in dependencies[num]:
            dep_count[dep] -= 1
    return True
