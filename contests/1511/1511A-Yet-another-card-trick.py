from collections import deque

def yet_another_card_trick(arr, queries):
    res = []
    q = deque(arr)
    for c in queries:
        idx = q.index(c)
        res.append(idx)
        del q[idx]
        q.appendleft(c)
    res = [c+1 for c in res]
    print(*res)

# So slicing is faster than trying to del and append - Interesting.

def yet_another_trick(arr, queries):
    for i in queries:
        t = arr.index(i)
        print(t+1,end=" ")
        temp = arr[t]
        arr[1:t+1] = arr[:t]
        arr[0] = temp

if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    yet_another_card_trick(arr, queries)
