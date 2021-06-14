"""

---

Intuition

n-1
distinct numbers - n-1

10, 20, 30, 40
40, 30, 20, 10


10 10 20 30 40
Left shift
20 30 40 10 10

10 10 20 30 30 30 40 50


"""


def gen_permute_iter(arr):
    if len(arr) < 1:
        yield arr
    else:
        for perm in gen_permute_iter(arr[1:]):
            for i in range(len(arr)):
                yield perm[:i] + arr[0:1] + perm[i:]


def reorder_the_array(arr, n):
    mx = 0
    for c in gen_permute_iter(arr):
        cnt = 0
        for d in zip(arr, c):
            if d[1] > d[0]:
                cnt += 1
        mx = max(mx, cnt)
    print(mx)


def reorder_the_array2(arr, n):
    from collections import Counter
    ctr = Counter(arr)
    mx = max(ctr.values())
    print(n - mx)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    reorder_the_array2(arr, n)