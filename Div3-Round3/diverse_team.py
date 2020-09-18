from collections import Counter

def diverse_teams(nums, k):
    ctr = Counter(nums)
    if k <= len(ctr.keys()):
        print('YES')
        candidates = list(ctr.keys())[:k]
        print("The candidates are", candidates)
        for c in candidates:
            print(nums.index(c) + 1, end=' ')
    else:
        print('NO')


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    diverse_teams(arr, k)
