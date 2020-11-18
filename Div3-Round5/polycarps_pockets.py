from collections import Counter

def find_pockets(arr):
    ctr = Counter(arr)
    values = list(ctr.values())
    pockets = 0
    while values:
        values = [c-1 for c in values if c != 0]
        pockets += 1
    print(pockets-1)


if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().split()))
    find_pockets(arr)