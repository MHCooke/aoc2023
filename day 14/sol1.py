from typing import List

with open('scratch_1.txt') as f:
    grid = [[c for c in row.strip()] for row in f]


def tilt_list(row: List[str]) -> List[str]:
    output_row = list(row)
    for origin_index in range(1, len(row)):
        char = output_row[origin_index]
        if char != 'O':
            continue
        next_index = origin_index
        while next_index > 0 and output_row[next_index - 1] == '.':
            next_index -= 1
        if next_index != origin_index:
            output_row[next_index] = char
            output_row[origin_index] = '.'
    return output_row

assert tilt_list(['.', '.', '.', 'O']) == ['O', '.', '.', '.']
assert tilt_list(['O', '.', '.', '.']) == ['O', '.', '.', '.']
assert tilt_list(['.', '.', 'O', 'O']) == ['O', 'O', '.', '.']
assert tilt_list(['.', 'O', '#', '.']) == ['O', '.', '#', '.']
assert tilt_list(['O', '#', '#', '.']) == ['O', '#', '#', '.']


transformed = zip(*grid)
tilted = [tilt_list(row) for row in transformed]
grid = list(zip(*tilted))

total = 0
for i, row in enumerate(grid):
    print(''.join(row))
    total += row.count('O') * (len(grid) - i)

print(total)
