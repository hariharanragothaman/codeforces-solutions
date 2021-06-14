def line_world(arr, n, t):
    g = {}
    tmp = list(range(1, n))

    for c in zip(tmp, arr):
        e1, e2 = c[0], sum(c)
        g[e1] = e2

    start, end = 1, n

    # Implement classic 1D DFS
    visited = set()
    visited.add(start)

    while start in g:
        start = g[start]
        visited.add(start)

    if t in visited:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    n, t  = map(int, input().split())
    arr = list(map(int, input().split()))
    line_world(arr, n, t)