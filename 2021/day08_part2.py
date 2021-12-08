with open("day08_input.txt", "r") as f:
    obs = [line.split(" | ") for line in f.read().splitlines()]


def _sorted(digit):
    return "".join(sorted(digit))


def solve(digits):
    mapping = {}
    five_segs = []
    six_segs = []

    cf, bcdf, acf, abcdefg = None, None, None, None
    for digit in digits:
        if len(digit) == 2:
            mapping[_sorted(digit)] = "1"
            cf = digit
        elif len(digit) == 3:
            mapping[_sorted(digit)] = "7"
            acf = digit
        elif len(digit) == 4:
            mapping[_sorted(digit)] = "4"
            bcdf = digit
        elif len(digit) == 7:
            mapping[_sorted(digit)] = "8"
            abcdefg = digit
        elif len(digit) == 5:
            five_segs.append(digit)
        elif len(digit) == 6:
            six_segs.append(digit)

    bd = set(bcdf) - set(cf)
    eg = set(abcdefg) - (set(cf) | set(bcdf) | set(acf))

    for digit in six_segs:
        _digit = set(digit)
        if _digit >= bd and _digit >= eg:
            mapping[_sorted(digit)] = "6"
        elif _digit >= bd:
            mapping[_sorted(digit)] = "9"
        elif _digit >= eg:
            mapping[_sorted(digit)] = "0"

    for digit in five_segs:
        _digit = set(digit)
        if _digit >= bd:
            mapping[_sorted(digit)] = "5"
        elif _digit >= eg:
            mapping[_sorted(digit)] = "2"
        else:
            mapping[_sorted(digit)] = "3"

    return mapping


count = 0
for o in obs:
    output_values = o[1].split()
    digits = o[0].split()
    mapping = solve(digits)
    value = ""
    for digit in output_values:
        value += mapping[_sorted(digit)]

    count += int(value)

print(count)
