with open("day01_input.txt", "r") as f:
    data = [int(i) for i in f.read().splitlines()]

fuels = [mass // 3 - 2 for mass in data]
print(sum(fuels))
