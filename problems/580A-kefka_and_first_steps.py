
def kefka(arr, n):
    mx = cnt = 1
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            cnt += 1
            mx = max(mx, cnt)
        else:
            cnt = 1
    print(mx)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    kefka(arr, n)