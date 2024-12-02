from operator import add
from functools import reduce

with open("day01_input.txt", "r") as f:
    data = [[int(d) for d in row.split()] for row in f.read().splitlines()]

print(
    reduce(
        add,
        [
            abs(a - b)
            for a, b in zip(sorted(r[0] for r in data), sorted(r[1] for r in data))
        ],
    )
)
