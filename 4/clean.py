def extract_sections(line):
    sections = []
    for assignment in line.split(','):
        start, end = tuple(map(int, assignment.split('-')))
        sections.append([*range(start, end + 1)])
    return sections


def part1(data):
    total = 0
    for line in data:
        sections = extract_sections(line)
        if set(sections[0]).issubset(sections[1]) or set(sections[1]).issubset(sections[0]):
            total += 1

    print(total)


def part2(data):
    total = 0
    for line in data:
        sections = extract_sections(line)
        if set(sections[0]).intersection(sections[1]):
            total += 1

    print(total)


def main():
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
