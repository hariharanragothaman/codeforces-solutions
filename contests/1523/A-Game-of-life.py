def solve(A, n, k):
    if 1 not in A: return ''.join(str(c) for c in A)

    j = 0
    while j < k:
        idx = []
        for i in range(n):
            if A[i] == 0:
                left = A[i - 1] if 0 <= i - 1 < n else 0
                right = A[i + 1] if 0 <= i + 1 < n else 0
                if left == 0 and right == 1:
                    idx.append(i)
                elif left == 1 and right == 0:
                    idx.append(i)

        if not idx:
            break

        for i in range(n):
            if i in idx:
                A[i] = 1
        j += 1

    return "".join(str(c) for c in A)


if __name__ == "__main__":
    t = int(input())
    i = 0
    while i < t:
        n, iteration = list(map(int, input().split()))
        gl = [int(c) for c in input()]
        res = solve(gl, n, iteration)
        print(res)
        i += 1
