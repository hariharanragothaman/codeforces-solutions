n = int(input())
string = input()
cnt = 0
for i in range(1, n):
    if string[i] == string[i-1]:
        cnt += 1
print(cnt)