string1 = input().lower()
string2 = input().lower()
if string1 == string2:
    print(0)
elif string2 > string1:
    print(-1)
else:
    print(1)
