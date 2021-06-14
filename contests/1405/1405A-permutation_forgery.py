"""
https://codeforces.com/contest/1405/problem/A
"""

def generate_permutation(arr):
    return arr[::-1]

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = input().split()
        arr = [int(c) for c in arr]
        res = generate_permutation(arr)
        print(*res)
        t -= 1