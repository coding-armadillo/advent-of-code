with open("day10_input.txt", "r") as f:
    lines = f.read().splitlines()


mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

match = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


def check(line):
    stack = []
    for c in line:
        if c in match.values():
            stack.append(c)
        elif c in match.keys():
            if len(stack) == 0:
                return mapping[c]
            last = stack.pop()
            if last != match[c]:
                return mapping[c]

    return 0


print(sum(check(line) for line in lines))
