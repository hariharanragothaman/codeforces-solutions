N = input()
arr = input().split()
arr = arr[::-1]

output = []

for i, c in enumerate(arr):
    if c not in output:
        output.append(c)

print(len(output))
output = output[::-1]
print(' '.join(c for c in output))
