with open("day06_input.txt") as f:
    buffer = f.read()

    offset = 14
    for i in range(0, len(buffer) - offset):
        if len(set(buffer[i : i + offset])) == offset:
            break

    print(i + offset)
