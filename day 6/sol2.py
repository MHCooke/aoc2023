with open('input.txt') as f:
    time, distance = [int(line.replace(' ', '').split(':')[1]) for line in f]
    print(sum(1 for hold in range(time) if hold * (time - hold) > distance))
