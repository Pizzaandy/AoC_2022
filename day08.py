data = open("inputs/day08.txt").read().splitlines()

grid = [[int(c) for c in line] for line in data]
visible = [[0 for c in line] for line in data]
scenic_score = [[1 for c in line] for line in data]

def rotate_90(matrix):
    return [list(x) for x in zip(*matrix[::-1])]

for _ in range(4):
    for i, row in enumerate(grid):
        tallest = -1
        for j, height in enumerate(row):
            if height > tallest:
                tallest = height
                visible[i][j] = 1
            for k, h in enumerate(row[j+1:]):
                if h >= height or k == len(row[j+1:]) - 1:
                    scenic_score[i][j] *= (k + 1)
                    break
    grid = rotate_90(grid)
    visible = rotate_90(visible)
    scenic_score = rotate_90(scenic_score)

print("Part 1:", sum(map(sum, visible)))
print("Part 2:", max(map(max, scenic_score)))

