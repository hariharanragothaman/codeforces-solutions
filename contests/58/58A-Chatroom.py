
def is_sub_sequence2(s, t):
    t = iter(t)
    return all(c in t for c in s)

string =  input()
res = is_sub_sequence2('hello', string)
if res:
    print('YES')
else:
    print('NO')