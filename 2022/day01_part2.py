all_calories = []
calories = 0

with open("day01_input.txt") as f:
    for line in f:
        if not line.strip():
            all_calories.append(calories)
            calories = 0
            continue
        calories += int(line)

print(sum(sorted(all_calories)[-3:]))
