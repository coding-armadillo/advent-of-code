from collections import Counter
from operator import add
from functools import reduce

with open("day01_input.txt", "r") as f:
    data = [[int(d) for d in row.split()] for row in f.read().splitlines()]


c = Counter(r[1] for r in data)

print(reduce(add, [c[a] * a for a in [r[0] for r in data]]))
