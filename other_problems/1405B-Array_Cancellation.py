"""
https://codeforces.com/contest/1405/problem/B

-3 5 -3 1

# Choose i, j - decrement i by 1 and increment u by 1


1 2 - (5,-3)  - Do Op 3 times - [-3, 2, 0, 1]
1,0 - (-3, 0) - Do op 2 times - - [-1, 0, 0, 1]
3,0 -

"""
def min_coins(arr):


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = input().split()
        arr = [int(c) for c in arr]
        res = min_coins(arr)
        print(res)
        t -= 1