# with open('scratch_1.txt') as f:
#     accum = 0
#     for line in f.readlines():
#         game, rounds = line.split(':')
#         id = game.split(' ')[1]
#         possible = []
#         for round in rounds.strip().split(';'):
#             result = {'red': 0, 'green': 0, 'blue': 0}
#             for set in round.strip().split(','):
#                 num, colour = set.strip().split(' ')
#                 result[colour] += int(num)
#                 if result['red'] <= 12 and result['green'] <= 13 and result['blue'] <= 14:
#                     possible.append(True)
#                 else:
#                     possible.append(False)
#         if all(possible):
#             accum += int(id)
#
#     print(accum)


with open('scratch_1.txt') as f:
    accum = 0
    for line in f.readlines():
        game, rounds = line.split(':')
        id = game.split(' ')[1]
        result = {'red': 0, 'green': 0, 'blue': 0}
        for round in rounds.strip().split(';'):
            
            for set in round.strip().split(','):
                num, colour = set.strip().split(' ')
                result[colour] = max(result[colour], int(num))

        power = 1
        for num in result.values():
            power *= int(num)

        accum += power

    print(accum)
