

if __name__ == '__main__':
    i = 0
    val = 0
    n = int(input())
    while i < n:
        s = input()
        if '++' in s:
            val += 1
        elif '--' in s:
            val -= 1
        i += 1
    print(val)