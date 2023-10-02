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
segs = [template[j : j + 2] for j in range(0, len(template) - 1)]

from collections import Counter

counts = Counter(segs)


for i in range(40):
    result = Counter()
    for key in counts:
        for pair in pairs:
            if key == pair[0]:
                result[key[0] + pair[1]] += counts[key]
                result[pair[1] + key[1]] += counts[pair[0]]

    counts = result


chars = Counter()
chars[template[0]] += 1

for key, value in counts.items():
    chars[key[1]] += value

chars = chars.most_common()
print(chars)
print(chars[0][1] - chars[-1][1])
