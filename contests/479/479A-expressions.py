"""
Given 3 numbers, find the maximum possible answer if you insert + and *
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    res =  a + b + c

    res = max(res,
              (a+b)*c,
              a*(b+c),
              a*b*c)

    print(res)