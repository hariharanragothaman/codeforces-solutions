if __name__ == '__main__':
    s = input()
    if all(c.isupper() for c in s):
        res = s.swapcase()
        print(res)

    elif s[0].islower() and all(c.isupper() for c in s[1:]):
            res = s.swapcase()
            print(res)
    else:
        print(s)