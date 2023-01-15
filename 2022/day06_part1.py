with open("day06_input.txt") as f:
    buffer = f.read()

    for i in range(0, len(buffer) - 4):
        if len(set(buffer[i : i + 4])) == 4:
            break

    print(i + 4)
