T = int(input())

while T > 0:
    N, K = input().split()
    N, K = int(N), int(K)
    A = input().split()
    A = [int(c) for c in A]
    cnt = 0
    lt = 0

    # find out where all one is in the array
    idx = [i for i, c in enumerate(A) if c == 1]
    print(idx)

    print("Case #1: ", cnt)
    T -= 1