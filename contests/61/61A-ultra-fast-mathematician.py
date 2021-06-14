a = input()
b = input()
op = ''

for c in zip(a, b):
    x, y = c
    if x != y:
        op += '1'
    else:
        op += '0'
print(op)
