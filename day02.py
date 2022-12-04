# 0 - rock, 1 - paper, 2 - scissors
input = open("inputs/day02.txt").read().splitlines()
hands = [("ABC".index(line[0]), "XYZ".index(line[2])) for line in input]

def score(h1, h2):
    if (h1 + 1) % 3 == h2:
        return h2 + 1 + 6
    elif h1 == h2:
        return h2 + 1 + 3
    return h2 + 1

print("Part 1:", sum(score(h1, h2) for h1, h2 in hands))
print("Part 2:", sum(score(h1, (h1 + h2 - 1) % 3) for h1, h2 in hands))
