from dataclasses import dataclass, field
from typing import List


@dataclass
class Knot:
    x: int
    y: int

    def move(self, d):
        match d:
            case 'R':
                self.x += 1
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1

    def __str__(self):
        return f"({self.x},{self.y})"

@dataclass
class Rope:
    knots: List[Knot]
    visits: List = field(default_factory=list)

    def __post_init__(self):
        self.visits.append((self.knots[-1].x, self.knots[-1].y))

    def move(self, d):
        for i in range(len(self.knots)-1):
            h, t = self.knots[i], self.knots[i+1]
            if i == 0:
                h.move(d)
            dx, dy = h.x - t.x, h.y - t.y
            if abs(dx) <= 1 and abs(dy) <= 1:  # adjacent
                continue
            elif dy == 0:  # same row
                t.x += int(dx/2)
            elif dx == 0:  # same col
                t.y += int(dy/2)
            elif abs(dy) > abs(dx):  # I think there is probably a better way for these diagonal cases
                t.y += int(dy/2)
                t.x += dx
            elif abs(dx) > abs(dy):
                t.x += int(dx/2)
                t.y += dy
            else:
                t.x += int(dx/2)
                t.y += int(dy/2)
        self.visits.append((self.knots[-1].x, self.knots[-1].y))


    def visited(self):
        print(f"Rope({len(self.knots)}) tail visits: {len(set(self.visits))}")

def main():
    with open('input.txt', 'r') as f:
        moves = [(d, int(c)) for d, c in [l.strip().split(' ') for l in f.readlines()]]

    # part 1
    rope = Rope([Knot(0,0), Knot(0,0)])
    for d, count in moves:
        for _ in range(count):
            rope.move(d)
    rope.visited()

    # part 2
    rope = Rope(knots=[Knot(0,0) for _ in range(10)])
    for d, count in moves:
        for _ in range(count):
            rope.move(d)
    rope.visited()


if __name__ == '__main__':
    main()
