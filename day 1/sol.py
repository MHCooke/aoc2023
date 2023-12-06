# # Part 1
#
# # Long
# with open('input.txt') as f:
#     print(
#         sum(
#             int(
#                 ''.join([[char for char in line if char.isnumeric()][i] for i in (0, -1)])
#             )
#             for line in f.readlines()
#         )
#     )
#
# # Short
# with open('input.txt') as f: print(sum(int(''.join([[char for char in line if char.isnumeric()][i] for i in (0, -1)])) for line in f.readlines()))

# Part 2

# Long
with open('input.txt') as f:
    print(
        sum(
            int(
                ''.join(
                    [
                        [
                            line[index] if line[index].isnumeric() else f'{number}'
                            for index in range(len(line))
                            for number, word in enumerate(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'))
                            if line[index:index+len(word)] == word or line[index].isnumeric()
                        ][i]
                        for i in (0, -1)
                    ]
                )
            )
            for line in f.readlines()
        )
    )

# Shortest
# with open('input.txt') as f: print(sum(int(''.join([[l[i] if l[i].isnumeric() else f'{n}' for i in range(len(l)) for n, w in enumerate(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')) if l[i:i+len(w)] == w or l[i].isnumeric()][i] for i in (0, -1)])) for l in f.readlines()))
# Short but readable
# with open('input.txt') as f: print(sum(int(''.join([[line[index] if line[index].isnumeric() else f'{number}' for index, char in enumerate(line) for number, word in enumerate(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')) if line[index:index+len(word)] == word or line[index].isnumeric()][i] for i in (0, -1)])) for line in f.readlines()))
