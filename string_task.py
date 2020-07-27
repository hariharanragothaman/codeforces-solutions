s = input().lower()
vowels = 'aeiouy'
s = '.' + '.'.join(c for c in s if c not in vowels)
print(s)