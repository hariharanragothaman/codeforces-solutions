n = int(input())
while n > 0:
    string = input()
    string = sorted(string)
    if string[0] == string[-1]:
        print('-1')
    else:
        print(''.join(c for c in string))
    n -= 1