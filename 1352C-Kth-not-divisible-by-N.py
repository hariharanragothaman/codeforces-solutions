"""
You are given two positive integers n and k.
Print the k-th positive integer that is not divisible by n.

For example, if n=3, and k=7, then all numbers
that are not divisible by 3 are: 1,2,4,5,7,8,10,11,13….
The 7-th number among them is 10.
"""

def solve_eff(num, k):
    diff = (k-1) // (num-1)
    return k + diff


def solve(num, k):
    res, cnt = 0, 0
    s = 1
    while cnt != k:
        if s % num != 0:
            cnt += 1
        s += 1
    return s - 1


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        nk = input().split()
        number, kth = int(nk[0]), int(nk[1])
        output = solve_eff(number, kth)
        print(output)
        t -= 1
