priorities = 0

with open("day03_input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        overlap = set(first).intersection(set(second)).pop()
        if overlap.isupper():
            priorities += ord(overlap) - ord("A") + 27
        else:
            priorities += ord(overlap) - ord("a") + 1

print(priorities)
