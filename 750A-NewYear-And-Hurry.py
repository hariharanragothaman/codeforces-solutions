from bisect import bisect_right
from itertools import accumulate
import operator

vals = input().split()
time = 240
n, k = int(vals[0]), int(vals[1])
remaining = time - k

arr = []
for i in range(1, n+1):
    arr.append(i*5)

add_arr = list(accumulate(arr, operator.add))

# We need to find the right most value less than or equal to x

op = bisect_right(add_arr, remaining)
print(op)
