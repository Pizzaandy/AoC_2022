inventories = open("inputs/day01.txt").read().split("\n\n")
totals = [sum(map(int, inventory.splitlines())) for inventory in inventories]
print("Part 1:", max(totals))
print("Part 2:", sum(sorted(totals)[-3:]))