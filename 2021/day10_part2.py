with open("day10_input.txt", "r") as f:
    lines = f.read().splitlines()


mapping = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
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
                return 0
            last = stack.pop()
            if last != match[c]:
                return 0

    if len(stack) == 0:
        return 0

    score = 0
    while len(stack) > 0:
        last = stack.pop()
        score *= 5
        score += mapping[last]

    return score


scores = [check(line) for line in lines]
scores = [s for s in scores if s > 0]
print(len(scores))
print(sorted(scores)[len(scores) // 2])
