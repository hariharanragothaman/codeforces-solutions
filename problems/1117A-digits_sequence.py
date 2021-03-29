

if __name__ == '__main__':
    k = int(input())
    s = list(range(1, 10001))
    s = ''.join(str(c) for c in s)
    print(s[k-1])