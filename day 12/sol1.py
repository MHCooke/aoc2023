import itertools
import multiprocessing
from typing import List


def detect_groups(springs: str) -> List[int]:
    output = []
    spring_counter = 0
    for spring in springs:
        if spring == '#':
            spring_counter += 1
        if spring == '.' and spring_counter > 0:
            output.append(spring_counter)
            spring_counter = 0
    if spring_counter > 0:
        output.append(spring_counter)
    return output


assert detect_groups('#.#.###') == [1, 1, 3]
assert detect_groups('.#...#....###.') == [1, 1, 3]
assert detect_groups('.#.###.#.######') == [1, 3, 1, 6]
assert detect_groups('#....######..#####.') == [1, 6, 5]


def process_line(line: str) -> int:
    line_parts = line.strip().split(' ')
    springs = line_parts[0]
    groups = list(map(int, line_parts[1].split(',')))
    needed_springs = sum(groups) - springs.count('#')
    needed_normal = springs.count('?') - needed_springs
    valid_counter = 0
    for chance in set(itertools.permutations('#'*needed_springs + '.'*needed_normal, needed_normal+needed_springs)):
        test_line = springs
        for char in chance:
            test_line = test_line.replace('?', char, 1)
        if detect_groups(test_line) == groups:
            valid_counter += 1
    return valid_counter


with open('input.txt') as f:
    lines = f.readlines()


if __name__ == '__main__':
    with multiprocessing.Pool(15) as p:
        res = p.map(process_line, lines)
        print(res)
        print(sum(res))