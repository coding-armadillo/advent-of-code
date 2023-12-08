with open("day01_input.txt", "r") as f:
    data = ["".join(c for c in row if c.isdigit()) for row in f.read().splitlines()]

values = [int(d[0] + d[-1]) for d in data]
print(sum(values))
