def swap_same(a, b, c):
    if a == b or a == c:
        return True

    for i in range(len(c)):
        if c[i] != a[i] and c[i] != b[i]:
            return False
    return True


if __name__ == "__main__":
    t = int(input())

    while t > 0:
        a = input()
        b = input()
        c = input()

        op = swap_same(a, b, c)
        if op:
            print('YES')
        else:
            print('NO')
        t -= 1