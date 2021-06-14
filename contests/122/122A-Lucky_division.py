from functools import reduce

def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )


def lucky_division(n):
    ff = factors(n)
    lucky = set(['4', '7'])
    for c in ff:
        if all(k in lucky for k in str(c)):
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    n = int(input())
    res = lucky_division(n)
    print(res)