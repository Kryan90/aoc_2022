def draw_crt(row, x):
    crt_i = len(row)
    if abs(crt_i - x) <= 1:
        return '#'
    else:
        return '.'

def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f.readlines()]

    x = 1
    cycle = 0
    total = 0
    crt_row = []
    rows = []
    for line in data:
        parts = line.split(' ')
        if len(parts) > 1:
            v = parts[1]
            for _ in range(2):
                cycle += 1
                if len(crt_row) == 40:
                    rows.append(crt_row)
                    crt_row = []
                crt_row.append(draw_crt(crt_row, x))
                if cycle == 20 or not (cycle - 20) % 40:
                    ss = cycle * x
                    print(f"Signal strength - cycle #{cycle} - {ss}")
                    total += ss
            x += int(v)
        else:
            cycle += 1
            if len(crt_row) == 40:
                rows.append(crt_row)
                crt_row = []
            crt_row.append(draw_crt(crt_row, x))
            if cycle == 20 or not (cycle - 20) % 40:
                ss = cycle * x
                print(f"Signal strength - cycle #{cycle} - {ss}")
                total += ss
    rows.append(crt_row)
    for row in rows:
        print(''.join(row))
    return


if __name__ == '__main__':
    main()
