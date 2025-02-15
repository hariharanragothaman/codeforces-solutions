def solve(arr, n):
    s = sum(arr)
    if s % n != 0:
        return -1
    avg = s // n
    cnt = 0
    for c in arr:
        if c > avg:
            cnt += 1
    return cnt


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        arr = list(map(int, input().split()))
        res = solve(arr, n)
        print(res)
        i += 1
