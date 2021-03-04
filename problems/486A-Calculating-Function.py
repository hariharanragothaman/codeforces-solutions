# f(n) = -1 + 2 - 3 + .... + (-1)^n * (n)
# Task is to calculate f(n) for an integer.

# Solution thoughts:
# Arithmetic progression formula =  (n/2) * ( 2a + (n-1) * d)
# so basically - sum of odd numbers and sum of even numbers
"""
f(6)

if num is even - then - n/2 terms will be there
if num is odd -

2 + 4 + 6 ....     AP - a = 2, d = 2
-1 + -3 + -5 ..    AP - a = -1 d = -2
"""
def calculate_sum(num):
    n = num / 2
    even_sum = (n / 2) * (2 * 2 + (n - 1) * 2)
    odd_sum = (n / 2) * (2 * (-1) + (n - 1) * (-2))
    op = int(even_sum + odd_sum)
    return op


if __name__ == '__main__':
    num = int(input())
    """
    if num % 2 == 0:
        res = calculate_sum(num)
        print(res)
    else:
        res = calculate_sum(num - 1)
        res = res - num
        print(res)
    """
    if num % 2 == 0:
        print(int(num//2))
    else:
        print(int((num-1)/2 - num))