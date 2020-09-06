n = int(input())

while n > 0:
    l = int(input())
    arr = map(int, input().split())
    arr = sorted(arr)
    diff = float('inf')
    for i in range(1, len(arr)):
        diff = min(diff, abs(arr[i]-arr[i-1]))
    print(diff)
    n -= 1