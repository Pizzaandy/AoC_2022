# 0 - rock, 1 - paper, 2 - scissors
char_to_hand = {
    "A": "rock", "B": "paper", "C": "scissors",
    "X": "rock", "Y": "paper", "Z": "scissors",
}
loses_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}
hand_to_score = {
    "rock": 1, "paper": 2, "scissors": 3,
}

games = open("input.txt").read().split("\n")

throws = [("ABC".index(game[0]), "XYZ".index(game[2])) for game in games]
score = 0
for throw in throws:
    score += throw[0] + 1
    if throw[0] == throw[1] + 1 % 2:
        score += 6
    elif throw[0] == throw[1]:
        score += 3

print("Part 1:", score)

score = 0
for game in games:
    opponent_throw, player_throw = game.split()
    opponent_hand = char_to_hand[opponent_throw]

    if player_throw == "X":
        player_hand = loses_against[opponent_hand]
    elif player_throw == "Y":
        player_hand = opponent_hand
    elif player_throw == "Z":
        player_hand = loses_against[loses_against[opponent_hand]]

    score += hand_to_score[player_hand]
    if opponent_hand == loses_against[player_hand]:
        score += 6
    elif opponent_hand == player_hand:
        score += 3

print("Part 2:", score)