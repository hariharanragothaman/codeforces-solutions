
def adjacent_replacements(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] -= 1
    print(*arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    adjacent_replacements(arr)