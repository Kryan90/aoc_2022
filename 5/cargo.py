class Map:

    def __init__(self, lines):
        self.lines = lines
        self.cols = {}
        self._parse()

    def _parse(self):
        for line in self.lines:
            slots = line.replace('[', '').replace(']', '').replace('    ', ' ').split(' ')
            for i, item in enumerate(slots, 1):
                if item:
                    self.cols.setdefault(i, []).append(item)

    def move(self, count, src, dst, m9001=False):
        if not m9001:
            for i in range(count):
                self.cols[dst].insert(0, self.cols[src].pop(0))
        else:
            for i in range(count):
                self.cols[dst].insert(i, self.cols[src].pop(0))

    def print(self):
        # caution, reading this code may induce nausea
        max_row = max(len(col) for col in self.cols.values())
        rows = [[] for _ in range(max_row)]
        for i, row in enumerate(rows):
            for j in range(len(self.cols)):
                col = self.cols[j+1]
                if max_row - len(col) - i > 0:
                    row.append('_')
                else:
                    row.append(col[i - (max_row - len(col))])
        for row in rows:
            print(''.join(row))

    def top(self):
        val = ''
        for i in sorted(self.cols.keys()):
            val += self.cols[i][0]
        return val


def run(data, m9001=False):
    m = Map(data[:data.index('')-1])
    print("initial:")
    m.print()
    for line in data[data.index('')+1:]:
        s = line.split(' ')
        m.move(*map(int, [s[1], s[3], s[5]]), m9001)
    print("\nfinal:")
    m.print()
    print("\nTop of stacks:")
    print(m.top())
    print()


def main():
    with open('input.txt', 'r') as f:
        data = [l.rstrip() for l in f.readlines()]

    run(data)
    run(data, m9001=True)


if __name__ == '__main__':
    main()
