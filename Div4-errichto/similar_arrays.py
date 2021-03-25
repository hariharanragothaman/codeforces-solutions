
"""
(1-x) + (3-x) + (9-x)
3x + 13 = 8
x = 5/3 =

1 3 9
-------------------------
Sum is what he is asking?
1 1 1  0 + 2 + 8 = 10
2 2 2  1 + 1 + 7 = 9
3 3 3  2 + 0 + 6 = 6
4 4 4  3 + 1 + 5 = 9
5 5 5  4 + 2 + 4 = 10
6 6 6  5 + 3 + 3 = 11
7 7 7  6 + 4 + 2 = 12


The range can be from 1--max(arr)
1 -- max(arr) time complexity will be too large...
"""

def get_distance(arr):
    min_dist = float('inf')
    for i in range(0, max(arr)+1):
        pivot_sum = sum(abs(i - c) for c in arr)
        min_dist = min(min_dist, pivot_sum)
    print(min_dist)

def get_distance_optimized(arr):
    arr.sort()
    n = len(arr)
    if n % 2 != 0:
        pivot = arr[n//2]
    else:
        pivot = arr[n//2]
    pivot_sum = sum(abs(pivot - c) for c in arr)
    print(pivot_sum)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    get_distance_optimized(arr)