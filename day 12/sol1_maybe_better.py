def process_line(springs, groups):
    total_broken = sum(groups)
    total_working = len(springs) - total_broken
    known_broken = springs.count('#')
    known_working = springs.count('.')
    total_unknown = springs.count('?')
    required_working = total_working - known_working
    required_broken = total_broken - known_broken

    minimum_working = len(groups) - 1
    spare_working = total_working - minimum_working
    known_excess_working = known_working - minimum_working if known_working > minimum_working else 0
    loose_working = spare_working - known_excess_working
    print(loose_working)


with open('input.txt') as f:
    lines = [line.strip() for line in f]

for line in lines:
    springs, raw_groups = line.strip().split(' ')
    groups = [int(g) for g in raw_groups.split(',')]
    process_line(springs, groups)
