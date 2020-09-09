from collections import deque
from itertools import accumulate
import operator

def helper(q, val, idx, hashmap):
    while q:
        prefix_sum = list(accumulate(q, operator.add))
        if val in prefix_sum and val != prefix_sum[0]:
            hashmap[idx] = True
            break
        q.popleft()


def find_special_elements(nums):
    special = 0
    hashmap = {}
    for i in range(len(nums)):
        hashmap[i] = False

    for i in range(0, len(nums)):
        q1 = deque(nums[:i])
        q2 = deque(nums[i+1:])
        helper(q1, nums[i], i, hashmap)
        helper(q2, nums[i], i, hashmap)

    for v in hashmap.values():
        if v:
            special += 1

    return special

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = input().split()
        arr = [int(c) for c in arr]
        op = find_special_elements(arr)
        print(op)
        t -= 1