from collections import deque


def main():
    with open('input.txt') as f:
        data = f.read()

    q = deque(maxlen=14)  # deque feels like cheating :shrug:
    for i, c in enumerate(data, 1):
        q.append(c)
        if len(set(q)) == 14:
            print(i)
            print(''.join(q))
            break


if __name__ == '__main__':
    main()
