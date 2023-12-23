from typing import Optional, List


def find_reflection_line(line: str, start: int = 0, end = None) -> Optional[int]:
    if end is None:
        end = len(line) - 1
    for i in range(start, end):
        centre = i
        i_m = i + 1
        while i >= 0 and i_m < len(line):
            if line[i] != line[i_m]:
                break
            i -= 1
            i_m += 1
        else:
            return centre + 1


def find_reflection_mirror(mirror: List[str], row: int = 0, reflection_point: int = 0, reflection_limit: Optional[int] = None) -> Optional[int]:
    if reflection_limit is None:
        reflection_limit = len(mirror[row]) - 1
    while reflection_point := find_reflection_line(mirror[row], reflection_point, reflection_limit):
        if row == len(mirror) - 1:
            return reflection_point
        if found := find_reflection_mirror(mirror, row + 1, reflection_point - 1, reflection_point):
            return found


with open('input.txt') as f:
    mirrors = []
    mirror = []
    for line in f:
        if line == '\n':
            mirrors.append(mirror)
            mirror = []
        else:
            mirror.append(line.strip())
    mirrors.append(mirror)

base_reflections = []
for mirror in mirrors:
    if width := find_reflection_mirror(mirror):
        base_reflections.append(width)
    elif height := find_reflection_mirror(list(zip(*mirror))):
        base_reflections.append(100 * height)

print(sum(base_reflections))
