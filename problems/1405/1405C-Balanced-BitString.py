from collections import Counter

def balanced_string_k(strs, n, k):
    """
    for i in range(len(strs)):
        for j in range(i+1, len(strs)+1):
            print(strs[i:j])
    """
    for i in range(0, len(strs)-k+1):
        print("The substring is:", strs[i:i+k])
        substr = strs[i:i+k]
        ctr = Counter(substr)
        print("The counter hashmap is:", ctr)

        if '?' in substr:
            zcnt = ctr.get('0', 0)
            ocnt = ctr.get('1', 0)
            qcnt = ctr.get('?', 0)

            if ctr['0'] == k // 2  and ctr['1'] != k // 2:
                diff = abs(zcnt-ocnt)
                if qcnt < diff:
                    return False

            elif ctr['1'] == k // 2  and ctr['0'] != k // 2:
                diff = abs(zcnt-ocnt)
                if qcnt < diff:
                    return False

            elif ctr['1'] != k // 2 and ctr['0'] != k // 2:

                print("Entering here", qcnt)
                tdiff = k - ctr.get('1', 0) - ctr.get('0', 0)

                if qcnt < tdiff:
                    return False

        elif '?' not in substr:
            if ctr['0'] != k // 2 or ctr['1'] != k // 2:
                return False

    return True



if __name__ == '__main__':
    t = int(input())
    while t > 0:
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        string = input()
        res = balanced_string_k(string, n, k)
        if res:
            print('YES')
        else:
            print('NO')
        t -= 1