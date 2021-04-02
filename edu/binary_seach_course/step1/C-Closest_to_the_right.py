from bisect import bisect_right


def get_closest_to_right(arr, q):
    index = bisect_right(arr, q)
    if q in arr:
        return index
    return index + 1

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    for q in queries:
        res = get_closest_to_right(arr, q)
        print(res, end='\n')