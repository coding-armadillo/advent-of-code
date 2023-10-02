with open("day11_input.txt", "r") as f:
    obs = [[int(i) for i in line] for line in f.read().splitlines()]


def increase(obs):
    for i in range(len(obs)):
        for j in range(len(obs[i])):
            obs[i][j] += 1


def has_flash(obs):
    locations = []
    for i in range(len(obs)):
        for j in range(len(obs[i])):
            if obs[i][j] > 9:
                locations.append((i, j))
    return locations


def display(obs):
    for i in range(len(obs)):
        print("".join([str(i) for i in obs[i]]))


from collections import Counter


print("Before any steps:")
display(obs)
print()


count = 0
octopuses = sum([len(obs[i]) for i in range(len(obs))])
while True:
    increase(obs)

    flashes = set()
    while True:
        locations = has_flash(obs)
        flashes.update(locations)

        if locations:
            c = Counter()
            for i, j in locations:
                obs[i][j] = 0
                if i > 0:
                    c[(i - 1, j)] += 1
                    if j > 0:
                        c[(i - 1, j - 1)] += 1
                    if j < len(obs[i]) - 1:
                        c[(i - 1, j + 1)] += 1
                if i < len(obs) - 1:
                    c[(i + 1, j)] += 1
                    if j > 0:
                        c[(i + 1, j - 1)] += 1
                    if j < len(obs[i]) - 1:
                        c[(i + 1, j + 1)] += 1
                if j > 0:
                    c[(i, j - 1)] += 1
                if j < len(obs[i]) - 1:
                    c[(i, j + 1)] += 1
            for i, j in c:
                if (i, j) not in flashes:
                    obs[i][j] += c[(i, j)]
            if c:
                continue
        break

    print(f"After step {count+1}:")
    display(obs)
    print(f"Flashes: {len(flashes)}")
    print()

    count += 1
    if len(flashes) == octopuses:
        break

print(f"Total steps: {count}")
