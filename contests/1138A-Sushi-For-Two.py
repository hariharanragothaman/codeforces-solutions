from collections import defaultdict

def sushi_for_two(arr):
    hash_map = defaultdict(list)
    prev = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            hash_map[arr[i - 1]].append(i - prev)
            prev = i

    if prev != len(arr) - 1:
        hash_map[arr[-1]].append(len(arr) - prev)

    hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda x: len(x[1]))}
    vals = list(hash_map.values())
    return max(vals[0]) * 2

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    output = sushi_for_two(arr)
    print(output)
