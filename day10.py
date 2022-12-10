ops = open("inputs/day10.txt").read().splitlines()

X = 1
cycles = 0
signals = []
pixels = 240 * ["."]

for op in ops:
    cycles_required = 2 if "addx" in op else 1
    for i in range(cycles_required):
        cycles += 1
        if (cycles - 20) % 40 == 0:
            signals.append(X * cycles)
        sprite_x = (cycles - 1) % 40
        if sprite_x - 1 <= X <= sprite_x + 1:
            pixels[cycles - 1] = "█"
        if i == 1:
            X += int(op.split()[1])

print("Part 1:", sum(signals))
print("Part 2:")
for line in zip(*[iter(pixels)]*40):
    print("".join(line))

