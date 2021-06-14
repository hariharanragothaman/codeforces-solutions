

if __name__ == '__main__':
    t = int(input())
    i = 0
    cnt = 0
    while i < t:
        arr = list(map(int, input().split()))
        if arr.count(1) >= 2:
            cnt += 1
        i += 1
    print(cnt)