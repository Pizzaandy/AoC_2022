buffer = open("inputs/day06.txt").read()

def find_marker(data, n):
    for i in range(len(data)):
        if len(set(data[i:i+n])) == n:
            return i + n

print("Part 1:", find_marker(buffer, 4))
print("Part 2:", find_marker(buffer, 14))