string = input()
low = [c for c in string if c.islower()]
upper = [c for c in string if c.isupper()]

output = ''

if len(low) >= len(upper):
    for i in range(len(string)):
        output += string[i].lower()
else:
    for i in range(len(string)):
        output += string[i].upper()

print(output)