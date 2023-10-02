with open("day01_input.txt", "r") as f:
    data = [int(i) for i in f.read().splitlines()]

count = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        count += 1

print(count)
