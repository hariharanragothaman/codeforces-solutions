
def solve(a, b, c, d):
    if b >= c*d:
        return -1

    cyan = a + b
    red = c
    res = 1

    while cyan > (red * d):
        cyan += b
        red += c
        res += 1

    return res

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))
    res = solve(a, b, c, d)
    print(res)