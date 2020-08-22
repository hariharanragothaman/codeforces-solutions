string = input()
string = [c for c in string]
print(max(string) * string.count(max(string)))