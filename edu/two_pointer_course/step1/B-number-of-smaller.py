from bisect import bisect_left

def number_of_smaller(arr1, arr2):
    res = []
    for n in arr2:
        idx = bisect_left(arr1, n)
        res.append(idx)
    print(*res)


if __name__ == '__main__':
    m, n = input().split()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    number_of_smaller(arr1, arr2)
