from collections import Counter
string = input()
ctr = Counter(string)
if len(ctr) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
