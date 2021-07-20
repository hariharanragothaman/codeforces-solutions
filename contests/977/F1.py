import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

start_time = time.time()


def longest_increasing_subsequence(arr, k):
    temp = []
    for n in arr:
        index = bisect_left(temp, n)
        if index == len(temp):
            if not temp or (temp[-1] + 1 == n):
                temp.append(n)
        # else:
        #     temp[index] = n
        # print(f"The temp is: {temp}")
    return temp


def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_increasing_subsequence(arr, n)
    print(len(result))
    op = [arr.index(c)+1 for c in result]
    print(*op)


if __name__ == "__main__":
    ONLINE_JUDGE = __debug__
    # ONLINE_JUDGE = False

    # If it's Local - Get I/P from file
    if not ONLINE_JUDGE:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if not ONLINE_JUDGE:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
