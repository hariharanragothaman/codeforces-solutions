def less_or_equal(A, n, k):
    A = sorted(A)
    if k == 0:
        if A[0] == 1:
            print(-1)
        else:
            print(1)
    elif k < n and A[k - 1] == A[k]:
        print(-1)
    else:
        print(A[k - 1])

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    less_or_equal(arr, n, k)