from itertools import product

HAS_LEFT = {'-', 'J', '7', 'S'}
HAS_RIGHT = {'-', 'L', 'F', 'S'}
HAS_TOP = {'|', 'L', 'J', 'S'}
HAS_BOTTOM = {'|', '7', 'F', 'S'}

HORIZONTAL = set(product(HAS_RIGHT, HAS_LEFT))
VERTICAL = set(product(HAS_TOP, HAS_BOTTOM))


def v(x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def find_end(x, y, last_x, last_y, count=0):
    while count == 0 or grid[y][x] != 'S':
        current = grid[y][x]
        loop_map[y][x] = current
        if x + 1 != last_x and v(x+1, y) and (current, grid[y][x + 1]) in HORIZONTAL:
            x, y, last_x, last_y, count = x + 1, y, x, y, count+1
            continue
        if x - 1 != last_x and v(x-1, y) and (grid[y][x - 1], current) in HORIZONTAL:
            x, y, last_x, last_y, count = x - 1, y, x, y, count+1
            continue
        if y + 1 != last_y and v(x, y+1) and (grid[y + 1][x], current) in VERTICAL:
            x, y, last_x, last_y, count = x, y + 1, x, y, count+1
            continue
        if y - 1 != last_y and v(x, y-1) and (current, grid[y - 1][x]) in VERTICAL:
            x, y, last_x, last_y, count = x, y - 1, x, y, count+1
            continue
        return None
    return count + 1


with open('input.txt') as f:
    grid = [line.strip() for line in f]

loop_map = [[' ' for _ in grid[0]] for _ in grid]

s_x, s_y = [(x, y) for y, row in enumerate(grid) for x, col in enumerate(row) if col == 'S'][0]

find_end(s_x, s_y, s_x, s_y)

inside_counter = 0
for y, row in enumerate(loop_map):
    line_type = 'none'
    inside = False
    for x, col in enumerate(row):
        if line_type == 'none':
            if col == '|':
                inside = not inside
            if col == 'F':
                line_type = 'bottom'
            if col == 'L':
                line_type = 'top'
            if col == ' ' and inside:
                inside_counter += 1
                loop_map[y][x] = '#'
        elif line_type == 'bottom':
            if col == 'J':
                inside = not inside
                line_type = 'none'
            if col == '7':
                line_type = 'none'
        elif line_type == 'top':
            if col == '7':
                inside = not inside
                line_type = 'none'
            if col == 'J':
                line_type = 'none'

print(inside_counter)
