with open("day01_input.txt", "r") as f:
    changes = [int(i) for i in f.read().splitlines()]

print(sum(changes))
