N = 3
i = 0
vowels = 'aeiou'
ex = [5, 7, 5]
op = []

while i < N:
    line = input()
    cnt = len([c for c in line if c in vowels])
    op.append(cnt)
    i += 1
if op != ex:
    print("NO")
else:
    print("YES")