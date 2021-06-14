def solve(arr, n):
    start = 1
    cost = 0
    cost += arr[0] - start
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            cost += (n - arr[i-1]) + arr[i]
        else:
            cost += arr[i] - arr[i-1]
    print(cost)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    solve(arr, n)