with open("day02_input.txt", "r") as f:
    data = [cmd.split() for cmd in f.read().splitlines()]

horizontal_position, depth = 0, 0

for action, value in data:
    value = int(value)
    if action == "forward":
        horizontal_position += value
    elif action == "up":
        depth -= value
    elif action == "down":
        depth += value

print(horizontal_position, depth)

print(horizontal_position * depth)
