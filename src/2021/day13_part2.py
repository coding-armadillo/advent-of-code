with open("day13_input.txt", "r") as f:
    lines = f.read().splitlines()


dots = []
actions = []
for line in lines:
    if not line:
        continue
    if "," in line:
        x, y = line.split(",")
        dots.append((int(x), int(y)))
    else:
        actions.append(line.split()[-1].split("="))

previous = dots[:]

for axis, value in actions:
    result = []
    value = int(value)
    if axis == "x":
        for dot in previous:
            if dot[0] < value:
                result.append((dot[0], dot[1]))
            else:
                result.append((2 * value - dot[0], dot[1]))

    elif axis == "y":
        for dot in previous:
            if dot[1] < value:
                result.append((dot[0], dot[1]))
            else:
                result.append((dot[0], 2 * value - dot[1]))

    print(len(set(result)))

    previous = result[:]

max_x = max(result, key=lambda x: x[0])[0]
max_y = max(result, key=lambda x: x[1])[1]
print(max_x, max_y)

for y in range(max_y + 1):
    for x in range(max_x + 1):
        if (x, y) in result:
            print("#", end="")
        else:
            print(" ", end="")
    print()

from PIL import Image

img = Image.new("RGB", (max_x + 1, max_y + 1), "black")
pixels = img.load()
for dot in set(result):
    pixels[dot[0], dot[1]] = (255, 255, 255)
img.show()
