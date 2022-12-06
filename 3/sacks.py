import string


def part1(data):
    items = [set(sack[:int(len(sack)/2)]).intersection(sack[-int(len(sack)/2):]).pop() for sack in data]
    total = sum(string.ascii_letters.index(i)+1 for i in items)
    print(total)


def part2(data):
    groups = [data[i*3:(i+1)*3] for i in range(int(len(data)/3))]
    total = sum(
        string.ascii_letters.index(i)+1 for i in [
            set(group[0]).intersection(group[1]).intersection(group[2]).pop() for group in groups
        ]
    )
    print(total)


def main():
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
