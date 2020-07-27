n = int(input())
result = []

while n > 0:
    s = input()
    if len(s) < 10:
        result.append(s)
    else:
        sg = s[0] + str(len(s)-2) + s[-1]
        result.append(sg)
    n -= 1

for char in result:
    print(char)