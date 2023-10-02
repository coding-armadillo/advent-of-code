with open("day15_input.txt", "r") as f:
    lines = [[int(d) for d in line] for line in f.read().splitlines()]

rows, cols = len(lines), len(lines[0])


lines_5x = [[0] * cols * 5 for i in range(rows * 5)]
for ii in range(5):
    for jj in range(5):
        for i in range(rows):
            for j in range(cols):
                lines_5x[ii * rows + i][jj * cols + j] = (
                    lines[i][j] + ii + jj - 1
                ) % 9 + 1


# Using the networkx library instead

import networkx as nx

g = nx.DiGraph()
rows *= 5
cols *= 5

for i in range(rows):
    for j in range(cols):
        if i < rows - 1:
            g.add_edge((i, j), (i + 1, j), weight=lines_5x[i + 1][j])
            g.add_edge((i + 1, j), (i, j), weight=lines_5x[i][j])

        if j < cols - 1:
            g.add_edge((i, j), (i, j + 1), weight=lines_5x[i][j + 1])
            g.add_edge((i, j + 1), (i, j), weight=lines_5x[i][j])

paths = nx.shortest_path(
    g,
    source=(0, 0),
    target=(rows - 1, cols - 1),
    weight="weight",
)

# print(paths)

cost = 0
for i, j in paths[1:]:
    cost += lines_5x[i][j]

print(f"Cost of shortest path is {cost}")
