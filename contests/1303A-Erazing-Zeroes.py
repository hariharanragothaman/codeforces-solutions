"""
> Understanding the question..
We are trying to find continuous sub segments.
minimum number of zeroes to erase to make it continuous sub-segments
"""

from collections import deque

def count_minimum(strs):
    if strs.count('1') == 0:
        return 0

    idx = strs.find('1')
    ns = strs[idx:]
    q = deque(ns)
    cnt = 0

    while q:
        ch = q.popleft()
        if ch == '0' and q.count('1') > 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    t = int(input())
    while t:
        string = input()
        result = count_minimum(string)
        print(result)
        t -= 1