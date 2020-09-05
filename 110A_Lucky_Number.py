# Lucky numbers are just 4 and 7
# number nearly lucky if the number of lucky digits in it is a lucky number

s = input()
value = s.count('4') + s.count('7')
if value == 4 or value == 7:
    print("YES")
else:
    print("NO")
