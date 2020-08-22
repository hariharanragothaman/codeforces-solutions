n = int(input())
arr = [input() for i in range(n)]

groups = 0
prev = None
i = 0
while i < n:
    if arr[i] != prev:
        groups += 1
    prev = arr[i]
    i += 1

print(groups)
