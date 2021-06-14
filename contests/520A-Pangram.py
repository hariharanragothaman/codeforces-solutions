from collections import Counter

alpha = 'abcdefghijklmnopqrstuvwxyz'
N = int(input())
word = input().lower()
ctr = Counter(word)
flag = True

for i, char in enumerate(alpha):
    cnt = ctr.get(char, 0)
    if cnt == 0:
        flag = False
        break

if flag == True:
    print("YES")
else:
    print("NO")