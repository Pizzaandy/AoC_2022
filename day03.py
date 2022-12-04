sacks = open("inputs/day03.txt").read().splitlines()

def priority(char: str):
    return (ord(char) - 96) % 58

data = [set(s[:len(s)//2]) & set(s[len(s)//2:]) for s in sacks]
print("Part 1:", sum(priority("".join(c)) for c in data))

groups = zip(*3*[iter(sacks)])
data = [set.intersection(*map(set, group)) for group in groups]
print("Part 2:", sum(priority("".join(c)) for c in data))