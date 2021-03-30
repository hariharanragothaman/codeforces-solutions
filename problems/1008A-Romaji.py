def romaji(s):
    vowels = 'aeiou'

    if len(s) == 1 and s not in vowels and s != 'n':
        return False

    i = 0
    while i < len(s)-1:
        # Exception
        if s[i] == 'n':
            i += 1
        elif s[i] not in vowels and s[i+1] in vowels:
            i += 2
        # Standard non-bernalese scenario
        elif s[i] not in vowels and s[i+1] not in vowels:
            return False
        # Exception
        elif s[i] in vowels:
            i += 1

    # Checking for boundary condition
    if s[-1] == 'n' or s[-1] in vowels:
        return True
    else:
        return False

    return True

def romaji_optimized(s):
    vowels = 'aeiou'
    for c in zip(s, s[1:]):
        # Exceptions should always come first
        if c[0] in vowels or c[0] == 'n':
            continue
        if c[0] not in vowels and c[1] not in vowels:
            return False
    # Checking for boundary condition
    if s[-1] == 'n' or s[-1] in vowels:
        return True
    else:
        return False
    return True


if __name__ == '__main__':
    s = input()
    if romaji_optimized(s):
        print('YES')
    else:
        print('NO')