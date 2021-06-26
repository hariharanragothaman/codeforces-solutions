
def solve(arr):
    arr = sorted(arr, key=lambda x:x[0])
    print(arr)
    count = 0
    for a, b in arr:
        if b == 1:
            count += 1
        elif b == -1:
            count -= 1
    print(count)


if __name__ == '__main__':
    te = int(input())
    i = 0
    arr = []
    while i < te:
        t, l, r = list(map(int, input().split()))
        if t == 1:
            arr.append((l, 1))
            arr.append((r, -1))
        elif t == 2:
            arr.append((l, 1))
            arr.append((r, -1))
        elif t == 3:
            arr.append((l, 1))
            arr.append((r, -1))
        i += 1

    solve(arr)