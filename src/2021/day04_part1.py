with open("day04_input.txt", "r") as f:
    lines = f.read().splitlines()


draws = lines[0].split(",")


lines = [line for line in lines[1:] if line]
boards = []
for i in range(0, len(lines) // 5):
    boards.append([])
    for j in range(5):
        boards[i].append(lines[i * 5 + j].split())


marks = {}
for i in range(len(boards)):
    marks[i] = {}
    for row in range(5):
        for col in range(5):
            marks[i][boards[i][row][col]] = (row, col)


winning_locations = []
for row in range(5):
    winning_locations.append([(row, col) for col in range(5)])
for col in range(5):
    winning_locations.append([(row, col) for row in range(5)])


def wins(locations, winning_locations=winning_locations):
    for winning_location in winning_locations:
        if all(loc in locations for loc in winning_location):
            return winning_location

    return None


plays = {}
for i in range(len(boards)):
    plays[i] = []

num_plays = {}
for i in range(len(boards)):
    count = 0
    for draw in draws:
        count += 1
        if draw in marks[i]:
            plays[i].append(marks[i][draw])

        if wins(plays[i]):
            num_plays[i] = count, len(plays[i])
            break


fastest_win = min(num_plays, key=lambda x: num_plays[x][0])
print(fastest_win)


sum_unmarked = 0
for row in range(5):
    for col in range(5):
        if (row, col) not in plays[fastest_win]:
            sum_unmarked += int(boards[fastest_win][row][col])

row, col = plays[fastest_win][-1]
num_call = int(boards[fastest_win][row][col])


print(sum_unmarked, num_call)
print(sum_unmarked * num_call)
