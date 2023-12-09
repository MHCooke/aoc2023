from functools import reduce

DIR_MAP = {
    'L': 0,
    'R': 1
}


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


with open('input.txt') as f:
    instructions = f.readline().strip()

    nodes = {node[:3]: (node[7:10], node[12:15]) for node in f if node != '\n'}

    instruction_index = 0
    start_nodes = [node for node in nodes if node[2] == 'A']
    loops = []
    for node in start_nodes:
        next_node = node
        cur_node = '   '
        nodes_visited = 0
        while not cur_node[2] == 'Z':
            direction = instructions[instruction_index]
            cur_node = nodes[next_node][DIR_MAP[direction]]
            instruction_index = (instruction_index + 1) % len(instructions)
            nodes_visited += 1
            next_node = cur_node
        loops.append(nodes_visited)

    print(loops)
    print(reduce(lcm, loops))
