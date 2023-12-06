with open('example.txt') as f:
    seeds = list(map(int, f.readline().split(':')[1].strip().split(' ')))
    maps_as_strs = f.readlines() + ['\n']

maps = []
cur_map = []
for line in maps_as_strs:
    if 'map:' in line:
        cur_map = []
    elif line == '\n' and cur_map:
        maps.append(cur_map)
    else:
        cur_map.append([int(val) for val in line.strip().split(' ') if val != ''])

for i, _ in enumerate(seeds):
    for map_group in maps:
        for mapping in map_group:
            if mapping[1] <= seeds[i] <= mapping[1] + mapping[2]:
                seeds[i] = mapping[0] + (seeds[i] - mapping[1])
                break

print(min(seeds))
