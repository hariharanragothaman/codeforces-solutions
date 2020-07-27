from itertools import combinations


def find_gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def max_gcd(a):
    mx = 0
    nums = list(range(1, a+1))
    for c in combinations(nums, 2):
        mx = max(mx, find_gcd(c[0], c[1]))
    return mx

def find_maximum_gcd(a):
    return 

n = int(input())
while n > 0:
    a = int(input())
    result = max_gcd(a)
    print(result)
    n -= 1