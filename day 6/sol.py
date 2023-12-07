with open('input.txt') as f:
    pairs = list(zip(*[list(map(int, list(filter(None, line.strip().split(' ')))[1:])) for line in f]))

per_race = 1
for time, distance in pairs:
    winners = 0
    for hold in range(time):
        if hold * (time-hold) > distance:
            winners += 1
    per_race *= winners

print(per_race)
