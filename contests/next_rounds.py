n = int(input())
k = int(input())

print("The value of n & k are",n,k)

s = []
while n > 0:
    val = int(input())
    s.append(val)
    n -= 1

print("S is:", s)

s = sorted(s, reverse=True)
v = [c for c in s if c >= k]
print("v is:", v)
print(len(v))