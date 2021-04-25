import heapq

def max_profit(arr, n , k):
    """
    Basically to find the overall profit, we can just use the heapq
    """
    klargest = heapq.nlargest(k, arr)
    #print(klargest)
    print(sum(klargest))

    size = 0
    result = []

    for c in arr:
        if c in klargest:
            klargest.remove(c)
            result.append(size+1)
            size = 0
        else:
            size += 1
    # Appending the remaining
    result[-1] += size

    print(*result)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    max_profit(arr, n, k)