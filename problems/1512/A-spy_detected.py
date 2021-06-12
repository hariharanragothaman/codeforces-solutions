from collections import Counter

def find_spy(arr):
    ctr = Counter(arr)
    for k, v in ctr.items():
        if v == 1:
            return arr.index(k) + 1


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        arr = list(map(int, input().split()))
        result = find_spy(arr)
        print(result)
        i += 1