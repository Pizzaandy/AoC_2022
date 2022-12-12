import re
from math import floor

data = open("inputs/day11.txt").read().split("\n\n")

class Monkey:
    monkeys = []
    def __init__(self, s):
        Monkey.monkeys.append(self)
        stmts = [line.split(":")[1].strip() for line in s.splitlines()]
        self.items = [int(s) for s in stmts[1].split(",")]
        self.operation = eval('lambda old: ' + stmts[2].split("=")[1])
        self.test = int(re.findall(r"\d+", stmts[3])[0])
        self.true_monkey = int(re.findall(r"\d+", stmts[4])[0])
        self.false_monkey = int(re.findall(r"\d+", stmts[5])[0])
        self.inspections = 0

    def execute_turn(self, reduce_worry):
        while self.items:
            item = self.operation(self.items.pop(0))
            self.inspections += 1
            if reduce_worry:
                item = floor(item / 3)
            else:
                item = item % (2*3*5*7*11*13*17*19)
            if item % self.test == 0:
                Monkey.monkeys[self.true_monkey].items.append(item)
            else:
                Monkey.monkeys[self.false_monkey].items.append(item)

monkeys = [Monkey(s) for s in data]

for _ in range(20):
    for monkey in monkeys:
        monkey.execute_turn(reduce_worry=True)
monkeys.sort(key=lambda x: x.inspections, reverse=True)
print("Part 1:", monkeys[0].inspections * monkeys[1].inspections)

Monkey.monkeys.clear()
monkeys = [Monkey(s) for s in data]

for i in range(0, 10_000):
    for monkey in monkeys:
        monkey.execute_turn(reduce_worry=False)
monkeys.sort(key=lambda x: x.inspections, reverse=True)
print("Part 2:", monkeys[0].inspections * monkeys[1].inspections)