import re
from copy import deepcopy

data, ops = open("inputs/day05.txt").read().split("\n\n")

data = data.splitlines()[:-1]
rows = [[*line[1::4].ljust(9, " ")] for line in data]
stacks = [[c for c in column if c != " "] for column in zip(*rows[::-1])]

ops = [re.findall(r"\d+", line) for line in ops.splitlines()]
ops = [list(map(int, op)) for op in ops]
ops = [[count, source-1, dest-1] for count, source, dest in ops]

part1 = deepcopy(stacks)
part2 = deepcopy(stacks)

for op in ops:
    count, source, dest = op
    part1[dest] += reversed(part1[source][-count:])
    del part1[source][-count:]

    part2[dest] += part2[source][-count:]
    del part2[source][-count:]

print("Part 1:", "".join(stack.pop() for stack in part1))
print("Part 2:", "".join(stack.pop() for stack in part2))
