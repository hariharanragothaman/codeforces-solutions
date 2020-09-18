from bisect import bisect_left, bisect_right

def find_between(arr, n, k):
    """
    1. Find where the left can be inserted towards the left - and count it
    2. find where the right can be inserted and count it
    """
    left_index = bisect_left(arr, n)
    right_index = bisect_right(arr, k)
    return right_index - left_index

if __name__ == "__main__":
    n = input()
    arr = list(map(int, input().split()))
    t = int(input())
    arr.sort()

    while t > 0:
        n, k = list(map(int, input().split()))
        op = find_between(arr, n, k)
        print(op)
        t -= 1 