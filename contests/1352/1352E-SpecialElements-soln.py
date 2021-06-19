from collections import defaultdict, Counter

def solve2(arr, n):
    hmap = defaultdict(int)
    ans = 0

    for i in range(n):
        curr_sum = arr[i]
        for j in range(i+1, n):
            curr_sum += arr[j]
            "The Sum we are searching for is a number in the array - which has to be less than n" \
            "Since  𝑎=[𝑎1,𝑎2,…,𝑎𝑛] (1≤𝑎𝑖≤𝑛) "
            if 0 < curr_sum <= n:
                hmap[curr_sum] += 1

    ctr = Counter(arr)
    for k, v in hmap.items():
        if k in arr:
            ans += ctr[k]
    print(ans)


def solve(arr, n):
    c = [0] * (n + 1)
    ans = 0
    for i in range(n):
        s = arr[i]
        for j in range(i + 1, n):
            s += arr[j]
            if 0 < s <= n:
                c[s] += 1

    for i in range(n):
        ans += c[arr[i]] > 0
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)