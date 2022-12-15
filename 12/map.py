import concurrent.futures
from collections import deque
from concurrent.futures import ProcessPoolExecutor
from string import ascii_lowercase

def shortest_path(m, start, end):
    h, w = len(m), len(m[0])

    visited = []
    paths = deque([[start, 0]])
    while paths:
        p, d = paths.popleft()
        if p in visited:
            continue
        visited.append(p)
        px, py = p
        neighbors = []
        if px != 0:
            # left neighbor
            neighbors.append((px-1,py))
        if px != w-1:
            # right neighbor
            neighbors.append((px+1,py))
        if py != 0:
            # top neighbor
            neighbors.append((px,py-1))
        if py != h-1:
            # bottom neighbor
            neighbors.append((px,py+1))

        for n in neighbors:
            if m[n[1]][n[0]] - m[py][px] <= 1:
                if n == end:
                    return d + 1
                if n not in visited:
                    paths.append([n, d + 1])


def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f.readlines()]

    m = []
    start, end = None, None
    for i, line in enumerate(data):
        row = []
        for j, v in enumerate(line):
            if v == 'S':
                start = (j, i)
                v = 'a'
            elif v == 'E':
                end = (j, i)
                v = 'z'
            row.append(ascii_lowercase.index(v))
        m.append(row)

    # part 1
    print(shortest_path(m, start, end))

    # part 2
    starts = [(j,i) for i in range(len(m)) for j in range(len(m[i])) if m[i][j] == 0]
    distances = []
    with ProcessPoolExecutor() as executor:  # who needs better algorithms when you have multiprocessing?!
        futures = {executor.submit(shortest_path, m, s, end) for s in starts}
        for future in concurrent.futures.as_completed(futures):
            d = future.result()
            if d is not None:
                distances.append(d)
    print(min(distances))

if __name__ == '__main__':
    main()
