with open("day14_input.txt", "r") as f:
    lines = f.read().splitlines()


template = None
pairs = []
for line in lines:
    if not line:
        continue
    if " -> " in line:
        pairs.append(line.split(" -> "))
    else:
        template = line

print(f"Template: {template}")

for i in range(10):
    segs = [template[j : j + 2] for j in range(0, len(template) - 1)]

    for k in range(len(segs)):
        for pair in pairs:
            if segs[k] == pair[0]:
                segs[k] = pair[0][0] + pair[1] + pair[0][1]

    template = segs[0]
    for seg in segs[1:]:
        template += seg[-2:]

    print(f"After step {i+1}: {template}")

from collections import Counter

counts = Counter(template).most_common()

print(counts[0][1] - counts[-1][1])
