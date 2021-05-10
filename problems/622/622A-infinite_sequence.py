from math import ceil, sqrt

def find_position(n):
    """
    1 1 1
    2 2 3
    3 3 6
    4 4 10
    5 5 15
    6 6 21
    7 7 28

    1   1 2  1 2 3  1 2 3 4   1 2 3 4 5

    1   2 3  4 5 6  7 8 9 10  11 12 13 14 15


    till a point to see how many nums = n * (n+1) // 2
    n * (n+1) / 2 -- <= input_value


    lOGIC SEEMS LIKE THIS
    a = (-1 + ceil(sqrt(1+ (4*n)) )) // 2
    b = (-1 + ceil(sqrt(1+ (4*n)))) // 2

    c = a if a > 0 else b

    pos = (c * (c+1)) // 2

    diff = pos - n
    return c - diff
    """
    for i in range(1, 2*(10**14)+1):
        if (i*(i+1)//2) >= n:
            res = (i * (i+1) // 2 ) - n
            return i - res

if __name__ == '__main__':
    n = int(input())
    # To find the number of on the nth position
    res = find_position(n)
    print(res)

# Another smarter way to do this is..
"""
n = int(input())
x = 1
while n > x:
    n -= x
    x += 1
print(n)
"""