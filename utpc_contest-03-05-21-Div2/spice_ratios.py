
if __name__ == '__main__':
    m, n, s, t = list(map(int, input().split()))
    p1 = m // s
    p2 = n // t
    p = min(p1, p2)
    print(s*p, t*p, end=' ')