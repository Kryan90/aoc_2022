import math
import operator


class Monkey:

    def __init__(self, name, items, op, test):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.inspections = 0

    def inspect(self, item, mod=None):
        self.inspections += 1
        wl = self.op(item)
        if mod:  # part 2, use the LCM to reduce worry level
            wl = wl % mod
        else:  # part 1, divide worry by 3
            wl = int(wl/3)
        return (wl, self.test[2]) if wl % self.test[0] else (wl, self.test[1])  # (item, target monkey)

    @classmethod
    def from_lines(cls, lines):
        _, op, arg = lines[2].split('=')[1].strip().split(' ')
        if op == '*':
            op = operator.mul
        elif op == '+':
            op = operator.add

        if arg == 'old':
            op_f = lambda x: int(op(x, x))
        else:
            op_f = lambda x: int(op(x, int(arg)))

        return cls(
            name=int(lines[0].split(' ')[1].strip(':')),
            items=[int(i.strip()) for i in lines[1].split(':')[1].split(',')],
            op=op_f,
            test=(int(lines[3].split(' ')[-1]), int(lines[4].split(' ')[-1]), int(lines[5].split(' ')[-1]))  # (divisor, true target, false target)
        )

def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f.readlines()]

    monkeys = [Monkey.from_lines(data[i:i+6]) for i, line in enumerate(data) if line.startswith('Monkey')]

    lcm = math.prod(set([m.test[0] for m in monkeys]))

    for r in range(10000):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item, m = monkey.inspect(monkey.items.pop(0), mod=lcm)
                monkeys[m].items.append(item)
    inspections = sorted([m.inspections for m in monkeys], reverse=True)
    print(f"Total monkey business: {inspections[0] * inspections[1]}")



if __name__ == '__main__':
    main()
