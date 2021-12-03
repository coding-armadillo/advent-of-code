with open("day03_input.txt", "r") as f:
    data = f.read().splitlines()

cols = len(data[0])

oxygen_generator_rating, co2_scrubber_rating = "", ""

selections = data[:]
for col in range(cols):
    ones = 0
    for row in selections:
        if row[col] == "1":
            ones += 1

    if ones >= len(selections) / 2:
        selections = [row for row in selections if row[col] == "1"]
    else:
        selections = [row for row in selections if row[col] == "0"]

    if len(selections) == 1:
        oxygen_generator_rating += selections[0]
        break

selections = data[:]
for col in range(cols):
    ones = 0
    for row in selections:
        if row[col] == "1":
            ones += 1

    if ones < len(selections) / 2:
        selections = [row for row in selections if row[col] == "1"]
    else:
        selections = [row for row in selections if row[col] == "0"]

    if len(selections) == 1:
        co2_scrubber_rating += selections[0]
        break


print(oxygen_generator_rating, co2_scrubber_rating)

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))
