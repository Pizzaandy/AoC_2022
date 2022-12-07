import re

data = open("inputs/day07.txt").read()
dir_lists = re.split(r"\$ cd ([\w./]+)\n", data)[1:]

sizes = {}
path = []

for cd, items in zip(*[iter(dir_lists)]*2):
    if cd == "..":
        path.pop()
        continue
    else:
        path.append(cd)

    file_sizes = sum(int(num) for num in re.findall(r'\d+', items))

    for i in range(len(path)):
        key = "/".join(path[:len(path)-i])
        sizes.setdefault(key, 0)
        sizes[key] += file_sizes

space_needed = 30000000 - (70000000 - sizes["/"])

print("Part 1:", sum(s for s in sizes.values() if s <= 100000))
print("Part 2:", min(s for s in sizes.values() if s >= space_needed))




