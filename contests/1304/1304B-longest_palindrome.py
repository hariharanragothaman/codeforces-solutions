
if __name__ == '__main__':
    t, n = map(int, input().split())
    i = 0

    left, right = [], []

    while i < t:
        s = input()
        if any(s == c[::-1] for c in left):
            right.append(s)
        else:
            left.append(s)
        i += 1

    res = ''
    tmp = []
    for c in left:
        if c[::-1] in right:
            res += c
        else:
            tmp.append(c)

    tmp_palindrome = [c for c in tmp if c == c[::-1]]
    rev = res[::-1]

    if tmp_palindrome:
        tmp_palindrome = sorted(tmp_palindrome, key=len, reverse=True)
        res += tmp_palindrome[0]

    res += rev

    if not res:
        print(0)
    else:
        print(len(res))
        print(res)