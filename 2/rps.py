POINTS = {
    'R': 1,
    'P': 2,
    'S': 3,
}

CRYPT_MAP = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

MOVE_MAP = {
    'X': {
        'R': 'S',
        'P': 'R',
        'S': 'P',
    },
    'Y': {x: x for x in ['R', 'P', 'S']},
    'Z': {
        'R': 'P',
        'P': 'S',
        'S': 'R',
    }
}


def play(game):
    if game[0] == game[1]:
        return 3
    if game[0] == 'R' and game[1] == 'P':
        return 6
    elif game[0] == 'P' and game[1] == 'S':
        return 6
    elif game[0] == 'S' and game[1] == 'R':
        return 6

    return 0


def part1(data):
    print(sum(play(game) + POINTS[game[1]] for game in [[CRYPT_MAP[game[0]], CRYPT_MAP[game[1]]] for game in data]))


def part2(data):
    print(sum(play(game) + POINTS[game[1]] for game in [(CRYPT_MAP[move], MOVE_MAP[outcome][CRYPT_MAP[move]]) for move, outcome in data]))


def main():
    with open('input.txt', 'r') as f:
        data = [line.strip().split(' ') for line in f.readlines()]

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
