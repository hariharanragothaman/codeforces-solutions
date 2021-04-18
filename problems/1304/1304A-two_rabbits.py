import sys

def will_the_rabbits_meet(x, y, a, b):
    """
    cnt = 0
    while x != y:
        if x > y or y < x:
            return -1
        x += a
        y -= b
        cnt += 1
    return cnt
    """
    left, right = 0, 10**18
    while left < right:
        mid = left + right + 1 >> 1
        print("The mid value is:", mid)
        if x + a * mid <= y - b * mid:
            left = mid
        else:
            right = mid - 1

    if (x+a*left) == (y-b*left):
        return left
    else:
        return -1

    # return (y-x) // (a+b) - check first if division is possible

if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        x, y, a, b = list(map(int, input().split()))
        result = will_the_rabbits_meet(x, y, a, b)
        print(result)
        i += 1