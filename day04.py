input = open("inputs/day04.txt").read().splitlines()
ranges = [line.replace(",", "-").split("-") for line in input]
ranges = [list(map(int, r)) for r in ranges]

def contains(r):
    a1, a2, b1, b2 = r
    a_contains = (a1 <= b1 and a2 >= b2)
    b_contains = (b1 <= a1 and b2 >= a2)
    return a_contains or b_contains

print("Part 1:", sum(map(contains, ranges)))

def overlaps(r):
    a1, a2, b1, b2 = r
    return a1 <= b2 and b1 <= a2

print("Part 2:", sum(map(overlaps, ranges)))