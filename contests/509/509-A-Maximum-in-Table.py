

def find_maximum(n):
    arr = [[0]*n]*n
    arr[0] = [1] * n
    for c in arr:
        c[0] = 1

    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[-1][-1])

if __name__ == '__main__':
    n = int(input())
    find_maximum(n)