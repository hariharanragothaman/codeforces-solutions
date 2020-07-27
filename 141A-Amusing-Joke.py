from collections import Counter
string1 = input()
string2 = input()
string3 = input()

stdin = string1 + string2
if Counter(stdin) == Counter(string3):
    print("YES")
else:
    print("NO")