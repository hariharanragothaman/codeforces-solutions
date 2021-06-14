N = input()
word = input()
binary = '1' * word.count('n') + '0' * word.count('z')
binary = [c for c in binary]
print(' '.join(c for c in binary))