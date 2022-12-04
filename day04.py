input = open("inputs/day04.txt").read().splitlines()
ranges = [[*map(int, line.replace(",", "-").split("-"))] for line in input]

contained = [(a <= c <= d <= b or c <= a <= b <= d) for a, b, c, d in ranges]
print("Part 1:", sum(contained))

overlapped = [(a <= d and c <= b) for a, b, c, d in ranges]
print("Part 2:", sum(overlapped))