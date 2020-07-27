result = 0

matrix = []

k = 5
while k > 0:
    row = input().split()
    row = [int(c) for c in row]
    matrix.append(row)
    k -= 1

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            result = abs(i-3) + abs(j-3)
print(result)