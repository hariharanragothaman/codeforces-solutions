from bisect import bisect_left

def binary_search_bisect(array, val):
    index = bisect_left(array, val)
    if index != len(array) and array[index] == val:
        return index
    else:
        return -1


def binary_search(arr, q):
    if len(arr) == 0:
        return -1

    left, right = 0, len(arr)-1
    while left <= right:
        pivot = (left + right) // 2
        if arr[pivot] < q:
            left = pivot+1
        elif arr[pivot] > q:
            right = pivot-1
        else:
            return pivot
    return -1

if __name__ == '__main__':
    n, k = list(map(int, input().split())) # length of array and queries
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    idx = -1

    for i in range(k):
        idx = binary_search_bisect(arr, queries[i])
        if idx != -1:
            print('YES')
        else:
            print('NO')