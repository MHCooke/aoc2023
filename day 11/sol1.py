from itertools import combinations


def expand_rows(table):
    output = []
    for row in table:
        output.append(row)
        if '#' not in row:
            output.append(tuple('.'*len(row)))
    return output


with open('input.txt') as f:
    expanded = list(zip(*expand_rows(zip(*expand_rows(map(str.strip, f.readlines()))))))

galaxies = []
for y, row in enumerate(expanded):
    for x, col in enumerate(row):
        if col == '#':
            galaxies.append((x, y))

distances = []
for first, second in combinations(galaxies, 2):
    x1, y1 = first
    x2, y2 = second
    x_diff = x2 - x1
    y_diff = y2 - y1
    distances.append(abs(x_diff) + abs(y_diff))
    continue

print(sum(distances))
