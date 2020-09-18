from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def deencrypt(strs, n):
    f = sorted(factors(n))
    for i in f:
        strs = strs[:i][::-1] + strs[i:]
    print(strs)


if __name__ == '__main__':
    n = int(input())
    strs = input()
    deencrypt(strs, n)
