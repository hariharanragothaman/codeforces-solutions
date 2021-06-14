def find_sort_possible(a, p):
    start = a
    end = sorted(a)

    p = [c-1 for c in p]
    pairs = [(c, c+1) for c in p]

    print("The pairs are:", pairs)

    while start != end:
        cnt = 0
        for p1, p2 in pairs:
            print(p1, p2)
            print(start)
            if start[p1] > start[p2]:
                print("Valid swap possible")
                start[p1], start[p2] = start[p2], start[p1]
                cnt += 1

        if cnt == 0:
            print("Reached here")
            break

    if start == end:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        p = list(map(int, input().split()))
        find_sort_possible(a, p)
        i += 1