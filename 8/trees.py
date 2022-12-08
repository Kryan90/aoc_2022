def main():
    with open('input.txt') as f:
        data = [l.strip() for l in f.readlines()]

    grid = []
    for line in data:
        grid.append([int(c) for c in line])

    rows = len(grid)
    cols = len(grid[0])

    # part 1
    visible = []
    for i, row in enumerate(grid):
        if i == 0 or i == rows - 1:  # on the border
            visible.extend([(x, i) for x in range(cols)])
            continue

        for j, t in enumerate(row):
            if j == 0 or j == cols - 1:  # on the border
                visible.append((j, i))
                continue

            if t > max(row[:j]) or t > max(row[j + 1:]):  # look left, look right
                visible.append((j, i))
                continue

            if t > max(r[j] for r in grid[:i]) or t > max(r[j] for r in grid[i + 1:]):  # look up, look down
                visible.append((j, i))
                continue

    print(f"Total visible: {len(visible)}")

    # part 2
    score = 0
    for i, row in enumerate(grid):
        if i == 0 or i == rows - 1:  # Borders will always have 0 scenic score
            continue

        for j, t in enumerate(row):
            if j == 0 or j == cols - 1:  # border
                continue

            l, r, u, d = 0, 0, 0, 0

            left = row[:j]
            for c in range(len(left)):
                l += 1
                if t <= left[-1-c]:
                    break

            right = row[j + 1:]
            for c in range(len(right)):
                r += 1
                if t <= right[c]:
                    break

            up = [r[j] for r in grid[:i]]
            for c in range(len(up)):
                u += 1
                if t <= up[-1-c]:
                    break

            down = [r[j] for r in grid[i + 1:]]
            for c in range(len(down)):
                d += 1
                if t <= down[c]:
                    break

            score = score if (s := l * r * u * d) < score else s

    print(f"Best scenic score: {score}")

if __name__ == '__main__':
    main()