from ast import literal_eval
from functools import cmp_to_key

data = open("inputs/day13.txt").read().replace("\n\n", "\n").splitlines()
all_packets = [literal_eval(s) for s in data]
pairs = zip(*[iter(all_packets)]*2)

def compare_items(a, b):
    if type(a) != type(b):
        a = a if isinstance(a, list) else [a]
        b = b if isinstance(b, list) else [b]

    if isinstance(a, int):
        if a == b:
            return 0
        return 1 if a < b else -1

    if isinstance(a, list):
        for x, y in zip(a, b):
            if (res := compare_items(x, y)) == 0:
                continue
            return res
        if len(b) == len(a):
            return 0
        return 1 if len(a) < len(b) else -1

part1 = [(i+1) * (compare_items(*t) == 1) for i, t in enumerate(pairs)]
print("Part 1:", sum(part1))

all_packets += [[[2]], [[6]]]
part2 = sorted(all_packets, key=cmp_to_key(compare_items), reverse=True)
print("Part 2:", (part2.index([[2]]) + 1) * (part2.index([[6]]) + 1))