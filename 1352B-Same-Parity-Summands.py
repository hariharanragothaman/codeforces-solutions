def parity_sum(num, k):
    # Both are odd
    if num % 2 != 0 and k % 2 == 0:
        return False

    # Both are odd



if __name__ == '__main__':
    t = int(input())
    while t > 0:
        nk = input().split()
        n = nk[0]
        k = mk[1]
        res = parity_sum(n, k)
        if res:
            print('YES')
        else:
            print('NO')
        t -= 1