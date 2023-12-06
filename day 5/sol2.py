with open('input.txt') as f:
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

processed = []
to_process = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
for map_group in maps:
    processed = []
    for s_start, s_length in to_process:
        mapped = False
        for m_dest, m_src, m_length in map_group:
            if m_src <= s_start < m_src + m_length:  # Seed starts within mapping range
                mapped = True
                if s_start + s_length < m_src + m_length:  # Seed ends within mapping range
                    processed.append((m_dest + (s_start - m_src), s_length))  # New seed is mapped completely
                else:  # Seed starts within range but ends past it
                    # New seed is mapped partially
                    processed.append((m_dest + (s_start - m_src), (m_src + m_length) - s_start))
                    to_process.append((m_src + m_length, (s_start + s_length) - (m_src + m_length)))  # Seed starts at end of mapping and runs to original seed end
            elif s_start < m_src < s_start + s_length:  # Seed starts below mapping and ends after it starts
                mapped = True
                if s_start + s_length < m_src + m_length:  # Seed ends within mapping range
                    processed.append((m_dest, (s_start + s_length) - m_src))  # mapped seed starts at mapping range and runs to end of seed
                    to_process.append((s_start, m_src - s_start))  # split off seed starts at seed start and runs to bottom of mapping range
                else:  # Seed is a superset of mapping range
                    to_process.append((s_start, m_src - s_start))  # portion of seed below mapping
                    processed.append((m_dest, m_length))  # portion of seed within mapping
                    to_process.append((m_src + m_length, (s_start + s_length) - (m_src + m_length)))  # portion of seed after mapping

        if not mapped:
            processed.append((s_start, s_length))

    to_process = processed

print(min(processed, key=lambda x: x[0]))
