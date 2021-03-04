"""
The key part of the question if it can be transformed.

So if 2 strings are 'ab' and 'ba' - The answer should be NO
"""

from collections import Counter

a = input()
b = input()
vowels = 'aeiou'

if len(a) != len(b):
    print('NO')
else:
    i = 0
    flag = True
    while i < len(a):
        if a[i] in vowels and b[i] in vowels or (a[i] not in vowels and b[i] not in vowels):
            flag = True
        else:
            flag = False
            print('NO')
            break
        i += 1
    if flag:
        print('YES')

"""
ctr1 = Counter(a)
ctr2 = Counter(b)
vowels = 'aeiou'
a_vcnt, a_const, b_vcnt, b_const = 0, 0, 0, 0

for k, v in ctr1.items():
    if k in vowels:
        a_vcnt += v
    else:
        a_const += v

for k, v in ctr2.items():
    if k in vowels:
        b_vcnt += v
    else:
        b_const += v

if a_vcnt == b_vcnt and a_const == b_const:
    print('YES')
else:
    print('NO')
"""
