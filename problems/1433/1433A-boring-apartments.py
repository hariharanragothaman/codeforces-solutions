
def solve(num):
    snum = str(num)
    start = snum[0]
    n = len(snum)
    total = 0

    each_level_count = 10
    total += (int(start)-1) * each_level_count

    for i in range(1, n+1):
        total += i

    return total


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        result = solve(n)
        print(result)
        i += 1