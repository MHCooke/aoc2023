# with open('scratch_1.txt') as f:
#     accum = 0
#     for line in [l.split(':')[1].strip() for l in f]:
#         mine, winning = [set(map(int, filter(None, half.split(' ')))) for half in line.split('|')]
#         score = 0
#         for num in mine:
#             if num in winning:
#                 if score == 0:
#                     score += 1
#                 else:
#                     score *= 2
#         accum += score
#
# print(accum)


with open('scratch_1.txt') as f:
    cards = [[l.split(':')[1].strip(), 1] for l in f]
    for number, line in enumerate(cards):
        mine, winning = [set(map(int, filter(None, half.split(' ')))) for half in line[0].split('|')]
        score = sum(1 for num in mine if num in winning)
        for card in range(number + 1, number + 1 + score):
            cards[card][1] += 1 * line[1]

print(sum(card[1] for card in cards))
