with open("day08_input.txt", "r") as f:
    obs = [line.split(" | ") for line in f.read().splitlines()]

count = 0
for o in obs:
    output_values = o[1].split()
    for output_value in output_values:
        if len(output_value) in [2, 3, 4, 7]:
            count += 1

print(count)
