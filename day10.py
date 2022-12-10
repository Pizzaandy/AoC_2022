ops = open("inputs/day10.txt").read().splitlines()

X = 1

cycle_count = 0
signal_strengths = [0]
op_queue = [[], []]

def execute_op(op):
    if op == "noop":
        return
    cmd, val = op.split()
    print(f"executed {op}")
    if cmd == "addx":
        global X
        X += int(val)

def queue_op(op):
    if len(op_queue) == 1:
        op_queue.append([])
    if op == "noop":
        return
    op_queue[1].append(op)
    print(f"queued {op}")

while op_queue:
    cycle_count += 1
    print(f"cycle {cycle_count} begin")
    if ops:
        queue_op(ops.pop(0))
    signal_strengths.append((X, cycle_count))
    for op in op_queue.pop(0):
        execute_op(op)
    print(f"cycle {cycle_count} end\n")

print(signal_strengths[20])