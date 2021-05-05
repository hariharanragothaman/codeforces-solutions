def solve(s, d):

    alpha = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    # print(alpha)
    hmap = {}
    for c in alpha:
        hmap[c] = False

    # print(hmap)

    s = [c for c in s]
    tmp = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            tmp.append(s[i])

    for k in tmp:
        if hmap[k]:
            return True
        hmap[k] = True
    return False



if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        d = int(input())
        s = input()
        result = solve(s, d)
        if not result:
            print('YES')
        else:
            print('NO')

        i += 1