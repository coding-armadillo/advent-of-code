with open("day06_input.txt", "r") as f:
    fish = [int(i) for i in f.read().strip().split(",")]

print(f"Initial state: {fish}")

for _ in range(80):
    new_fish = []
    for i in range(len(fish)):

        fish[i] -= 1

        if fish[i] < 0:
            fish[i] = 6
            new_fish.append(8)

    fish.extend(new_fish)

    print(f"After {str(_+1):2s} day{'s' if _ else ''}: {fish}")

print(len(fish))
