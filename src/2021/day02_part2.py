with open("day02_input.txt", "r") as f:
    data = [cmd.split() for cmd in f.read().splitlines()]

horizontal_position, depth, aim = 0, 0, 0

for action, value in data:
    value = int(value)
    if action == "forward":
        horizontal_position += value
        depth += aim * value
    elif action == "up":
        aim -= value
    elif action == "down":
        aim += value


print(horizontal_position, depth, aim)

print(horizontal_position * depth)
