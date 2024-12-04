with open("day02_input.txt", "r") as f:
    data = [[int(d) for d in row.split()] for row in f.read().splitlines()]

safe = 0
for row in data:
    diff_safe = all(
        [abs(row[i] - row[i + 1]) in [1, 2, 3] for i in range(len(row) - 1)]
    )
    trend_safe = all([row[i] - row[i + 1] > 0 for i in range(len(row) - 1)]) or all(
        [row[i] - row[i + 1] < 0 for i in range(len(row) - 1)]
    )
    if diff_safe and trend_safe:
        safe += 1

print(safe)
