def birthday_sage(arr, n):

    if len(arr) < 3:
        return 0, arr

    op = []
    cnt = 0
    arr.sort()

    while arr:
        value = arr.pop()
        op.append(value)
        if arr:
            cube = arr.pop(0)
            cnt += 1
            op.append(cube)
    return cnt, op


def birthday_sage_efficient(arr, n):
    arr.sort()
    for i in range(0, n-1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return ((n-1) // 2), arr


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    cnt, arr = birthday_sage_efficient(arr, n)
    print(cnt)
    print(' '.join(str(c) for c in arr))