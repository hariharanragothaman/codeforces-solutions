def solve(s, n):
    cnt = result = 0
    for i in range(0, n):
        if s[i] == 'x':
            cnt += 1
            if cnt > 2:
                result += 1
        elif s[i] != 'x':
            cnt = 0
    print(result)


if __name__ == '__main__':
    n = int(input())
    s = input()
    solve(s, n)