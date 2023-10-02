with open("day15_input.txt", "r") as f:
    risks = [[int(d) for d in line] for line in f.read().splitlines()]

rows, cols = len(risks), len(risks[0])

# reference: https://stackabuse.com/dijkstras-algorithm-in-python/

from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [
            [-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)
        ]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight


def dijkstra(graph, start_vertex):
    D = {v: float("inf") for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


g = Graph(rows * cols)
for i in range(rows):
    for j in range(cols):

        if i < rows - 1:
            g.add_edge((i + 1) * cols + j, i * cols + j, risks[i][j])
            g.add_edge(i * cols + j, (i + 1) * cols + j, risks[i + 1][j])

        if j < cols - 1:
            g.add_edge(i * cols + j + 1, i * cols + j, risks[i][j])
            g.add_edge(i * cols + j, i * cols + j + 1, risks[i][j + 1])


D = dijkstra(g, 0)
print(f"Cost of shortest path is {D[rows*cols-1]}")
