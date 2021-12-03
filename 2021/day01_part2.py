with open("day01_input.txt", "r") as f:
    data = [int(i) for i in f.read().splitlines()]

three_measurement_data = []
for i in range(2, len(data)):
    three_measurement_data.append(sum(data[i - 2 : i + 1]))

count = 0
for i in range(1, len(three_measurement_data)):
    if three_measurement_data[i] > three_measurement_data[i - 1]:
        count += 1

print(count)
