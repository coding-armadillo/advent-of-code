priorities = 0

with open("day03_input.txt") as f:
    groups = f.readlines()
    groups = [groups[3 * i : 3 * i + 3] for i in range(0, len(groups) // 3)]

    for g in groups:
        items = None
        for line in g:
            line = line.strip()
            if not items:
                items = set(line)
            else:
                items = items.intersection(set(line))
        overlap = items.pop()

        if overlap.isupper():
            priorities += ord(overlap) - ord("A") + 27
        else:
            priorities += ord(overlap) - ord("a") + 1

print(priorities)
