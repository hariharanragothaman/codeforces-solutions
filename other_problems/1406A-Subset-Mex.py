from collections import deque
from collections import Counter
from itertools import islice

def find_missing(nums):
    nums = list(nums)
    nums.sort()
    missing  = 0
    for i in range(len(nums)):
        if nums[i] == missing:
            missing += 1
    return missing


def find_mex(arr):
    ctr = Counter(arr)
    arr.sort()
    #print("The sorted array is:", arr)
    seta, setb = set(), set()

    #nums = [arr[i:i+2] for i in range(0, len(arr), 2)]

    for i, c in enumerate(arr):
        if ctr[c] >=2:
            seta.add(c)
            setb.add(c)
        else:
            seta.add(c)

    #print(seta, setb)
    missing1 = find_missing(seta)
    missing2 = find_missing(setb)

    return missing1 + missing2

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        arr = list(map(int, input().split()))
        op = find_mex(arr)
        print(op)
        t -= 1