n = int(input())
presents = map(int, input().split())
hash_map = {}

for i, v in enumerate(presents):
    hash_map[v] = i + 1

print(hash_map)

for i in range(n):
    print(hash_map[i+1])