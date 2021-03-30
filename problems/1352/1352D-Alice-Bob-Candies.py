from collections import deque

def calculate_moves(nums):
    moves, atot, btot = 0, 0, 0
    q = deque(nums)
    print("The queue is:", q)

    aprev, bprev = 0, 0

    while q:
        asum, bsum = 0, 0
        af, bf = False, False

        while q and asum <= bprev:
            asum += q.popleft()
            af = True

        if af:
            atot += asum
            moves += 1
            aprev = asum

        print("After alice move: The queue is:", q)

        while q and bsum <= aprev:
            print("The queue is:", q)
            bsum += q.pop()
            bf = True

        if bf:
            btot += bsum
            moves += 1
            bprev = bsum

        print("After bob move: The queue is:", q)
        print("--------------------------")

    print("The bsum is:", bsum)

    res = (moves, atot, btot)
    return res

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        arr = input().split()
        arr = [int(c) for c in arr]
        op = calculate_moves(arr)
        print(*op)
        t -= 1