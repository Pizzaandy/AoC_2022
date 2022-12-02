from functools import reduce

# 0 - rock, 1 - paper, 2 - scissors
input = open("input.txt").read().split("\n")
games = [("ABC".index(line[0]), "XYZ".index(line[2])) for line in input]

score = 0
for opponent_hand, my_hand in games:
    score += my_hand + 1
    if (opponent_hand + 1) % 3 == my_hand:
        score += 6
    elif opponent_hand == my_hand:
        score += 3
print("Part 1:", score)

score = 0
outcomes = [
    lambda h: ((h + 2) % 3),
    lambda h: h + 3,
    lambda h: ((h + 1) % 3) + 6,
]

for opponent_hand, result in games:
    score += outcomes[result](opponent_hand) + 1
print("Part 2:", score)
