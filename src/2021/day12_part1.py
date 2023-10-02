with open("day12_input.txt", "r") as f:
    segs = f.read().splitlines()


graph = {}
for seg in segs:
    node1, node2 = seg.split("-")
    if node1 not in graph:
        graph[node1] = [node2]
    else:
        graph[node1].append(node2)

    if node2 not in graph:
        graph[node2] = [node1]
    else:
        graph[node2].append(node1)

from pprint import pprint

pprint(graph)


paths = []


def breadth_first_search(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        paths.append(path)
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path or node.isupper():
            newpath = breadth_first_search(graph, node, end, path)
            if newpath:
                paths.append(newpath)
    return None


breadth_first_search(graph, "start", "end")

for path in paths:
    print(",".join(path))

print(len(paths))
