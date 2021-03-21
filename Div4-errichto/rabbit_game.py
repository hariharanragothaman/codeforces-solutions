
def find_how_many_can_eat(arr):
    fcnt, scnt = 1, 1
    fstop, sstop = len(arr), -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            fcnt += 1
        else:
            fstop = i
            break

    if fcnt == len(arr):
        return fcnt

    c = -1
    if fstop != len(arr):
        c = fstop

    for j in range(len(arr)-1, c, -1):
        if arr[j-1] >= arr[j]:
            scnt += 1
        else:
            break

    return fcnt + scnt





if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_how_many_can_eat(arr)
    print(result)