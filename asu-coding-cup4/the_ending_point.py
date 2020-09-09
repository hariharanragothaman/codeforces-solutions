if __name__ == '__main__':
    pos = input().split()
    x, y = int(pos[0]), int(pos[1])
    pattern = str(input())

    for s in pattern:
        if s == 'U':
            y += 1
        elif s == 'D':
            y -= 1
        elif s == 'L':
            x -= 1
        elif s == 'R':
            x += 1

    print(x, y)