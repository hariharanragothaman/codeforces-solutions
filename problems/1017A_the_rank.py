N = int(input())
hash_map = {}
i = 1
while i <= N:
    arr = input().split()
    arr = [int(c) for c in arr]
    hash_map[i] = sum(arr)
    i += 1

hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)}
print(hash_map)
keys = list(hash_map.keys())
print(keys.index(1)+1)