with open("day03_input.txt", "r") as f:
    data = f.read().splitlines()

cols = len(data[0])
rows = len(data)

gamma_rate, epsilon_rate = "", ""

for col in range(cols):
    ones = 0
    for row in range(rows):
        if data[row][col] == "1":
            ones += 1

    if ones > rows / 2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(gamma_rate, epsilon_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
