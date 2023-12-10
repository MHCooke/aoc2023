from typing import List


def differences(seq: List[int]) -> List[int]:
    return [a - b for a, b in zip(seq[1:], seq)]


with open('input.txt') as f:
    sequences = [[int(num) for num in line.split(' ')] for line in f]

    total = 0
    for seq in sequences:
        tower = [seq]
        diff = True
        while diff:
            new_row = differences(tower[-1])
            tower.append(new_row)
            diff = len(set(new_row)) > 1

        for i in range(len(tower)-1, 0, -1):
            tower[i-1].append(tower[i-1][-1] + tower[i][-1])

        total += tower[0][-1]

    print(total)
