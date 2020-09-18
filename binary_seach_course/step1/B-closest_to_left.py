from bisect import bisect_left, bisect_right

def closest_to_left(arr, val):
    idx = bisect_right(arr, val)
    return idx

if __name__ == '__main__':
    n, k = list(map(int, input().split())) # length of array and queries
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    for i in range(k):
        idx = closest_to_left(arr, queries[i])
        print(idx)