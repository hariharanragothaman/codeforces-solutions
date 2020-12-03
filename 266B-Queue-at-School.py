from collections import deque

def find_position(arr, n, t):
    arr = deque(arr)
    while t > 0:
        i = 1
        while i < len(arr):
            if arr[i] == 'G' and arr[i-1] == 'B':
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i += 2
            else:
                i += 1
        t -= 1
    print(''.join(arr))

if __name__ == '__main__':
    n, t = map(int, input().split())
    arr = input()
    find_position(arr, n, t)
