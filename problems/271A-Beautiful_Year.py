n = int(input())
n += 1

while n <= 10000:
    year = [c for c in str(n)]
    if len(set(year)) == 4:
        print(n)
        break
    n += 1