from collections import deque

def solve(s, nums):
    q = deque(nums)
    while q:
        xi, yi = q.popleft()
        if s <= xi:
            return False
        elif s > xi:
            s += yi
    return True


if __name__ == '__main__':
    s, n = list(map(int, input().split()))
    i = 0
    arr = []
    while i < n:
        xi, yi = list(map(int, input().split()))
        arr.append((xi, yi))
        i += 1
    arr = sorted(arr)
    if solve(s, arr):
        print('YES')
    else:
        print('NO')