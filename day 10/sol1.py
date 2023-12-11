from itertools import product

HAS_LEFT = {'-', 'J', '7', 'S'}
HAS_RIGHT = {'-', 'L', 'F', 'S'}
HAS_TOP = {'|', 'L', 'J', 'S'}
HAS_BOTTOM = {'|', '7', 'F', 'S'}

HORIZONTAL = set(product(HAS_RIGHT, HAS_LEFT))
VERTICAL = set(product(HAS_TOP, HAS_BOTTOM))


def find_end(x, y, last_x, last_y, count=0):
    while count == 0 or grid[y][x] != 'S':
        current = grid[y][x]
        if x + 1 != last_x and x + 1 < len(grid[y]) and (current, grid[y][x + 1]) in HORIZONTAL:
            x, y, last_x, last_y, count = x + 1, y, x, y, count+1
            continue
        if x - 1 != last_x and x - 1 >= 0 and (grid[y][x - 1], current) in HORIZONTAL:
            x, y, last_x, last_y, count = x - 1, y, x, y, count+1
            continue
        if y + 1 != last_y and y + 1 < len(grid) and (grid[y + 1][x], current) in VERTICAL:
            x, y, last_x, last_y, count = x, y + 1, x, y, count+1
            continue
        if y - 1 != last_y and y - 1 >= 0 and (current, grid[y - 1][x]) in VERTICAL:
            x, y, last_x, last_y, count = x, y - 1, x, y, count+1
            continue
        return None
    return count + 1


with open('input.txt') as f:
    grid = [line.strip() for line in f]

s_x, s_y = [(x, y) for y, row in enumerate(grid) for x, col in enumerate(row) if col == 'S'][0]

print(find_end(s_x, s_y, s_x, s_y) // 2)
