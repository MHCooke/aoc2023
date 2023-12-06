# # Part 1
# with open('scratch_1.txt') as f:
#     grid = [[c for c in l.strip()] for l in f.readlines()]
#
# accum = 0
# gear_table = {}
# for row in range(len(grid)):
#     build_num = ''
#     for col in range(len(grid[row])):
#         if grid[row][col].isnumeric():
#             build_num += grid[row][col]
#         if build_num and (col == len(grid[row]) - 1 or not grid[row][col + 1].isnumeric()):
#             has_symbol = False
#             for row1 in range(row-1, row+2):
#                 if 0 <= row1 < len(grid):
#                     for col1 in range(col-len(build_num), col+2):
#                         if 0 <= col1 < len(grid[row]):
#                             if not grid[row1][col1].isnumeric() and grid[row1][col1] != '.':
#                                 has_symbol = True
#             if has_symbol:
#                 accum += int(build_num)
#             build_num = ''
#
# print('Total:', accum)

# Part 2
with open('scratch_1.txt') as f:
    grid = [[c for c in l.strip()] for l in f.readlines()]

gear_table = {}
for row in range(len(grid)):
    build_num = ''
    for col in range(len(grid[row])):
        if grid[row][col].isnumeric():
            build_num += grid[row][col]
        if build_num and (col == len(grid[row]) - 1 or not grid[row][col + 1].isnumeric()):
            has_symbol = None
            for row1 in range(row-1, row+2):
                if 0 <= row1 < len(grid):
                    for col1 in range(col-len(build_num), col+2):
                        if 0 <= col1 < len(grid[row]):
                            if grid[row1][col1] == '*':
                                has_symbol = (row1, col1)
            if has_symbol is not None:
                if has_symbol not in gear_table:
                    gear_table[has_symbol] = []
                gear_table[has_symbol].append(int(build_num))
            build_num = ''

print(sum([values[0] * values[1] for values in gear_table.values() if len(values) == 2]))