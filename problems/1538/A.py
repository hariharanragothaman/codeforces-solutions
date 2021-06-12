

def solve(arr, n):
    # Getting the min and max values
    amin = min(arr)
    amax = max(arr)

    # Getting the index of the minimum and maximum values
    imin = arr.index(amin) + 1
    imax = arr.index(amax) + 1

    # Getting the index from the right
    iminr = n - imin + 1
    imaxr = n - imax + 1

    print(min(max(imin, imax),
              max(iminr, imaxr),
              imin + imaxr,
              iminr + imax))


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)
        i += 1