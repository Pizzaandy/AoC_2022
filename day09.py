import numpy as np

data = open("inputs/day09.txt").read().splitlines()
moves = [line.split() for line in data]
moves = [(c, int(dist)) for c, dist in moves]

H = 0 + 0j
T = 0 + 0j
visited_pt1 = set()

knots = 9 * [0j]
visited_pt2 = set()

def update_knot(current, next):
    delta = next - current
    if abs(delta) > 1.5:
        current += np.sign(delta.real) + np.sign(delta.imag) * 1j
    return current

for c, distance in moves:
    direction = np.around(np.exp("RULD".find(c) * np.pi * 0.5j))
    for i in range(distance):
        H += direction
        T = update_knot(T, H)
        visited_pt1.add(T)

        for j, knot in enumerate(knots):
            knots[j] = update_knot(knot, knots[j-1] if j else H)
        visited_pt2.add(knots[-1])

print("Part 1:", len(visited_pt1))
print("Part 2:", len(visited_pt2))