def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f.readlines()]

    inventories = []
    start = 0
    for i, num in enumerate(data):
        if num == '':
            inventories.append(sum(int(v) for v in data[start:i]))
            start = i + 1
    inventories = sorted(inventories)
    print(inventories[-1])
    print(sum(inventories[-3:]))


if __name__ == '__main__':
    main()
