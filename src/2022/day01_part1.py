max_calories = 0
calories = 0

with open("day01_input.txt") as f:
    for line in f:
        if not line.strip():
            if calories > max_calories:
                max_calories = calories
            calories = 0
            continue
        calories += int(line)

print(max_calories)
