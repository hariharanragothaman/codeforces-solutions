"""
https://codeforces.com/gym/102397/problem/B
"""

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

if __name__ == '__main__':
    area = int(input())
    fs = list(factors(area))
    l = fs[0]
    b = area // fs[0]
    print(l, b)
