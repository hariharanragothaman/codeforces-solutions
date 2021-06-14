hash_map = {}
N = int(input())
i = 0
inputs = []

while i < N:
    name, value = input().split()
    value = int(value)
    inputs.append((name, value))
    if name not in hash_map: hash_map[name] = value
    else: hash_map[name] += value
    i += 1

hash_map = {k:v for k, v in sorted(hash_map.items(), key=lambda x:x[1], reverse=True)}
max_value = list(hash_map.values())[0]

candidates = []
cnt_map = {}

for key, value in hash_map.items():
    if value == max_value:
        candidates.append(key)

for c in candidates:
    cnt_map[c] = 0

for name, value in inputs:
    if name in cnt_map:
        cnt_map[name] += value
        if cnt_map[name] >= max_value:
            print(name)
            break