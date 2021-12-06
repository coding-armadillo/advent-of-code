with open("day06_input.txt", "r") as f:
    fish = [int(i) for i in f.read().strip().split(",")]


from collections import Counter

fish = Counter(fish)
print(fish)

for _ in range(256):
    for i in range(-1, 9):
        if i == 8:
            fish[i] = fish[-1]
        elif i != 6:
            fish[i] = fish[i + 1]
        else:
            fish[i] = fish[-1] + fish[i + 1]


print(sum([v for k, v in fish.items() if k >= 0]))
