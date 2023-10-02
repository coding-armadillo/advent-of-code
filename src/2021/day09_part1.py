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
            low_points.append(obs[i][j])


print(sum(low_points) + len(low_points))
