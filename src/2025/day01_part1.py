with open("day01_input.txt", "r") as f:
    data = [(row[0], int(row[1:])) for row in f.read().splitlines()]

s, c = 50, 0

for d, n in data:
    n %= 100
    if d == "L":
        s -= n
        if s < 0:
            s += 100
    elif d == "R":
        s += n
        if s > 99:
            s -= 100
    print(f"The dial is rotated {d}{n} to {s}")
    if s == 0:
        c += 1
print("Answer is", c)
