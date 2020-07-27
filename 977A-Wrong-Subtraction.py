inp = input()
n, k = inp.split()
k = int(k)

while k > 0:
    if n[-1] != '0':
        n = str(int(n)-1)
    elif n[-1] == '0':
        n = str(int(n)//10)
    k -= 1

print(n)