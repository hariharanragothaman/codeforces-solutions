

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    cnt = 0
    while n != 0:
        n = n // 2
        n = round(n)
        cnt += 1
    print(cnt)