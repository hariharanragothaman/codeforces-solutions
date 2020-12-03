def count_swaps(arr, n):
    max_val_index = arr.index(max(arr))
    c = max(arr)
    arr.pop(max_val_index)
    arr.insert(0, c)
    arr = arr[::-1]
    d = arr.index(min(arr))
    print(max_val_index + d)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    count_swaps(arr, n)
