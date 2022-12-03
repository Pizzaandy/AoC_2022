from itertools import zip_longest
sacks = open("inputs/day03.txt").read().split("\n")

def priority(char: str):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38

data = ["".join(set(s[:len(s)//2]) & set(s[len(s)//2:])) for s in sacks]
print("Part 1:", sum(priority(c) for c in data))

groups = zip(*3*[iter(sacks)])
data = ["".join(set.intersection(*map(set, group))) for group in groups]
print("Part 2:", sum(priority(c) for c in data))