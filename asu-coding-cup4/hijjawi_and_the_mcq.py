def mcq(string):
    mcs = ('a', 'b', 'c', 'd', 'e')
    chs = (0, 0, 0, 0, 0, 0)
    cnt = dict(zip(mcs, chs))

    for s in string:
        cnt[s] += 1

    cnt = {k:v for k, v in sorted(cnt.items(), key=lambda x:x[1])}
    vals = list(cnt.values())
    return vals[0], vals[-1]

if __name__ == '__main__':
    n = input()
    string = input()
    rmin, rmax = mcq(string)
    print(rmin, rmax)
