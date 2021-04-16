
import itertools

def find_photogenic(arr, k):
    even = [c for c in arr if c%2 == 0]
    odd = [c for c in arr if c %2 != 0]
    result = odd + even
    print(*result)



if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n:
        k = int(input())
        arr = list(map(int, input().split()))
        find_photogenic(arr, k)
        i += 1