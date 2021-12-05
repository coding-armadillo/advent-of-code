with open("day05_input.txt", "r") as f:
    lines = f.read().splitlines()

lines = [line.split(" -> ") for line in lines]
lines = [(tuple(line[0].split(",")), tuple(line[1].split(","))) for line in lines]
print(len(lines))

lines = [
    ((int(coord1[0]), int(coord1[1])), (int(coord2[0]), int(coord2[1])))
    for coord1, coord2 in lines
    if coord1[0] == coord2[0] or coord1[1] == coord2[1]
]
print(len(lines))

from collections import Counter

diagram = Counter()
for coord1, coord2 in lines:
    if coord1[0] == coord2[0]:
        for i in range(min(coord1[1], coord2[1]), max(coord1[1], coord2[1]) + 1):
            diagram[(coord1[0], i)] += 1
    elif coord1[1] == coord2[1]:
        for i in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1):
            diagram[(i, coord1[1])] += 1

print(len([i for i in diagram.values() if i > 1]))
