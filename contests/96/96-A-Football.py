def football(s):
    szero = s.split('0')
    sone = s.split('1')
    print(s)
    if any(c for c in szero if len(c) >= 7) or any(c for c in sone if len(c) >= 7):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    s = input()
    football(s)