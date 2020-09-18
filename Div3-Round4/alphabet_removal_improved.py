

n, k = map(int, input().split())
string = input()
hmap = 'abcdefghijklmnopqrstuvwxyz'

scnt = 0

for c in hmap:
    if k < 1:
        break
    scnt = string.count(c)
    string = string.replace(c, '', min(scnt, k))
    k -= scnt

print(string)