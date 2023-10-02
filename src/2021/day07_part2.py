with open("day07_input.txt", "r") as f:
    crabs = [int(i) for i in f.read().strip().split(",")]

print(len(crabs))

from collections import Counter

crabs = Counter(crabs)


outcome = {}

for key in range(0, max(crabs.keys()) + 1):
    result = 0
    for key2 in crabs:
        result += sum(range(1, abs(key2 - key) + 1)) * crabs[key2]
    outcome[key] = result

min_key = min(outcome, key=outcome.get)
print(min_key)
print(outcome[min_key])
