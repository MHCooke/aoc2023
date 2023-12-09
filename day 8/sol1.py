DIR_MAP = {
    'L': 0,
    'R': 1
}

with open('input.txt') as f:
    instructions = f.readline().strip()

    nodes = {node[:3]: (node[7:10], node[12:15]) for node in f if node != '\n'}

    instruction_index = 0
    nodes_visited = 0
    next_node = 'AAA'
    while next_node != 'ZZZ':
        direction = instructions[instruction_index]
        next_node = nodes[next_node][DIR_MAP[direction]]
        instruction_index = (instruction_index + 1) % len(instructions)
        nodes_visited += 1

    print(nodes_visited)
