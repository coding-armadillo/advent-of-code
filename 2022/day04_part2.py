count = 0

with open("day04_input.txt") as f:
    sections = f.readlines()
    for section in sections:
        section = section.strip()
        r1, r2 = section.split(",")

        r1_start, r1_stop = int(r1.split("-")[0]), int(r1.split("-")[1]) + 1
        r1 = set(range(r1_start, r1_stop))

        r2_start, r2_stop = int(r2.split("-")[0]), int(r2.split("-")[1]) + 1
        r2 = set(range(r2_start, r2_stop))

        if r1.intersection(r2):
            count += 1

print(count)
