from collections import deque


def count_problems(n, k):
    q = deque(n)
    cnt = 0
    while q:
        if q[0] <= k:
            q.popleft()
            cnt += 1
        elif q[-1] <= k:
            q.pop()
            cnt += 1
        else:
            break
    print(cnt)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    problems = list(map(int, input().split()))
    count_problems(problems, k)
