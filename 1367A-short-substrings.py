n = int(input())

def guess(string):
    output = string[0]
    i = 1
    while i < len(string):
        output += string[i]
        i += 2
    return output

while n > 0:
    string = input()
    res = guess(string)
    print(res)
    n -= 1