ops = open("inputs/day10.txt").read().splitlines()

X = 1
cycle_count = 0
signal_strengths = []
pixels = ["." for _ in range(240)]

for op in ops:
    if op == "noop":
        cycle_count += 1
        if cycle_count in [20 + n * 40 for n in range(6)]:
            signal_strengths.append((X, cycle_count))
        if abs(X - ((cycle_count-1) % 40)) <= 1:
            pixels[cycle_count - 1] = "#"
        continue
    cmd, value = op.split()
    if cmd == "addx":
        for i in range(2):
            cycle_count += 1
            if cycle_count in [20 + n*40 for n in range(6)]:
                signal_strengths.append(X * cycle_count)
            if abs(X - ((cycle_count-1) % 40)) <= 1:
                pixels[cycle_count - 1] = "#"
            if i == 1:
                X += int(value)

for line in zip(*[iter(pixels)]*40):
    print("".join(line))