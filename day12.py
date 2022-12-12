import numpy as np
import heapq

data = open("inputs/day12.txt").read().splitlines()
grid = np.array([list(s) for s in data])
start = tuple([int(arr[0]) for arr in np.where(grid == "S")])
goal = tuple([int(arr[0]) for arr in np.where(grid == "E")])
grid[grid == "S"] = "a"
grid[grid == "E"] = "z"

def heuristic(a, b):
    return sum(abs(v1 - v2) for v1, v2 in zip(a,b))

def astar(array, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    closed = set()
    came_from = {}
    gscores = {start: 0}
    fscores = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscores[start], start))
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            result = []
            while current in came_from:
                result.append(current)
                current = came_from[current]
            return result
        closed.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            if not (0 <= neighbor[0] < array.shape[0]):
                continue
            if not (0 <= neighbor[1] < array.shape[1]):
                continue
            if ord(array[neighbor]) - ord(array[current]) > 1:
                continue

            gscore = gscores[current] + heuristic(current, neighbor)
            if neighbor in closed and gscore >= gscores.get(neighbor, 0):
                continue
            if (gscore < gscores.get(neighbor, 0) or
                    neighbor not in [i[1] for i in oheap]):
                came_from[neighbor] = current
                gscores[neighbor] = gscore
                fscores[neighbor] = gscore + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscores[neighbor], neighbor))

all_a = [(int(x), int(y)) for x, y in np.dstack(np.where(grid == "a"))[0]]
potential_routes = [res for a in all_a if (res := astar(grid, a, goal))]
potential_routes.sort(key = len)

print("Part 1:", len(astar(grid, start, goal)))
print("Part 2:", len(potential_routes[0]))
