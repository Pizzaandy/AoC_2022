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
score_calc = [
    lambda h: ((h + 2) % 3), # lose
    lambda h: h + 3, # draw
    lambda h: ((h + 1) % 3) + 6, # win
]
for opponent_hand, result in games:
    score += score_calc[result](opponent_hand) + 1
print("Part 2:", score)
