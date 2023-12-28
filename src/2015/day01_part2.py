with open("day01_input.txt", "r") as f:
    s = f.read()

floor = 0
for i in range(len(s)):
    c = s[i]
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    if floor == -1:
        break

print(i + 1)
