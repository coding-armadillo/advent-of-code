with open("day09_input.txt", "r") as f:
    obs = [[int(i) for i in line] for line in f.read().splitlines()]


low_points = []
for i in range(0, len(obs)):
    for j in range(0, len(obs[i])):
        to_compare = []
        if i > 0:
            to_compare.append(obs[i - 1][j])
        if i < len(obs) - 1:
            to_compare.append(obs[i + 1][j])
        if j > 0:
            to_compare.append(obs[i][j - 1])
        if j < len(obs[i]) - 1:
            to_compare.append(obs[i][j + 1])

        if all(obs[i][j] < x for x in to_compare):
            low_points.append((i, j))

basin_sizes = []


def find_basin(i, j, points):
    points.append((i, j))

    up = i
    while True:
        if up > 0:
            if obs[up - 1][j] > obs[up][j] and obs[up - 1][j] < 9:
                find_basin(up - 1, j, points)
                up -= 1
            else:
                break
        else:
            break

    down = i
    while True:
        if down < len(obs) - 1:
            if obs[down + 1][j] > obs[down][j] and obs[down + 1][j] < 9:
                find_basin(down + 1, j, points)
                down += 1
            else:
                break
        else:
            break

    left = j
    while True:
        if left > 0:
            if obs[i][left - 1] > obs[i][left] and obs[i][left - 1] < 9:
                find_basin(i, left - 1, points)
                left -= 1
            else:
                break
        else:
            break

    right = j
    while True:
        if right < len(obs[i]) - 1:
            if obs[i][right + 1] > obs[i][right] and obs[i][right + 1] < 9:
                find_basin(i, right + 1, points)
                right += 1
            else:
                break
        else:
            break


for i, j in low_points:
    points = []
    find_basin(i, j, points)
    basin_sizes.append(len(set(points)))

import functools

print(functools.reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:]))
