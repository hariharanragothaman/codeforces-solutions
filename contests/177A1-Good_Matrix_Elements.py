N = int(input())
matrix = []
i = 0

while i < N:
    rows = input().split()
    rows = [int(c) for c in rows]
    matrix.append(rows)
    i += 1

print(matrix)

# To get some of the left diagonal + right diagonal + middle row + middle column
