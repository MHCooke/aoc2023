from itertools import combinations

def empty_rows(table):
    return ['#' not in row for row in table]

with open('input.txt') as f:
    pre_expansion = [line.strip() for line in f]

empty_ys = empty_rows(pre_expansion)
empty_xs = empty_rows(zip(*pre_expansion))

galaxies = []
y = 0
for row, expand_y in zip(pre_expansion, empty_ys):
    x = 0
    for col, expand_x in zip(row, empty_xs):
        if col == '#':
            galaxies.append((x, y))
        x += 1_000_000 if expand_x else 1
    y += 1_000_000 if expand_y else 1

distances = []
for first, second in combinations(galaxies, 2):
    x1, y1 = first
    x2, y2 = second
    x_diff = x2 - x1
    y_diff = y2 - y1
    distances.append(abs(x_diff) + abs(y_diff))
    continue

print(sum(distances))
