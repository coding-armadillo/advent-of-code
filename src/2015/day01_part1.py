with open("day01_input.txt", "r") as f:
    s = f.read()

floor = 0
for c in s:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

print(floor)
