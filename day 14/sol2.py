from typing import List

with open('scratch_1.txt') as f:
    grid = [[c for c in row.strip()] for row in f]


def tilt_row_left(grid: List[List[str]]) -> List[List[str]]:
    for row in range(len(grid)):
        for origin_index in range(1, len(grid[row])):
            char = grid[row][origin_index]
            if char != 'O':
                continue
            next_index = origin_index
            while next_index > 0 and grid[row][next_index - 1] == '.':
                next_index -= 1
            if next_index != origin_index:
                grid[row][next_index] = char
                grid[row][origin_index] = '.'
    return grid


def tilt_row_right(grid: List[List[str]]) -> List[List[str]]:
    for row in range(len(grid)):
        for origin_index in range(len(grid[row])-1, -1, -1):
            char = grid[row][origin_index]
            if char != 'O':
                continue
            next_index = origin_index
            while next_index < len(grid[row]) - 1 and grid[row][next_index + 1] == '.':
                next_index += 1
            if next_index != origin_index:
                grid[row][next_index] = char
                grid[row][origin_index] = '.'
    return grid


def tilt_col_up(grid: List[List[str]]) -> List[List[str]]:
    for col in range(len(grid[0])):
        for origin_index in range(1, len(grid)):
            char = grid[origin_index][col]
            if char != 'O':
                continue
            next_index = origin_index
            while next_index > 0 and grid[next_index - 1][col] == '.':
                next_index -= 1
            if next_index != origin_index:
                grid[next_index][col] = char
                grid[origin_index][col] = '.'
    return grid


def tilt_col_down(grid: List[List[str]]) -> List[List[str]]:
    for col in range(len(grid[0])):
        for origin_index in range(len(grid)-1, -1, -1):
            char = grid[origin_index][col]
            if char != 'O':
                continue
            next_index = origin_index
            while next_index < len(grid) - 1 and grid[next_index + 1][col] == '.':
                next_index += 1
            if next_index != origin_index:
                grid[next_index][col] = char
                grid[origin_index][col] = '.'
    return grid

weights = []
smallest = 0
loops = []
loop_length = 1
loop_detected = False
while not loop_detected:
    grid = tilt_col_up(grid)
    grid = tilt_row_left(grid)
    grid = tilt_col_down(grid)
    grid = tilt_row_right(grid)
    total = 0
    for i, row in enumerate(grid):
        total += row.count('O') * (len(grid) - i)
    weights.append(total)
    if total == min(weights):
        loops.append(loop_length)
        loop_length = 1
        smallest = min(weights)
    else:
        loop_length += 1
    if len(loops) > 3 and loops[-3] == loops[-2] == loops[-1] > 1:
        loop_detected = True

loop_length = loops[-1]
loop_start = loops.index(loop_length)
run_in = sum(loops[:loop_start])
print('run in', run_in)
print('loop length', loop_length)
weight_loop = weights[-loop_length-1:]
target = 1_000_000_000
weight_loop_index = (target - run_in) % loop_length
print(weight_loop, f'[{weight_loop_index}]')
print(weight_loop[weight_loop_index])