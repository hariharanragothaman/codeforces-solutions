def solve(s):
    alpha = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    hmap = {}
    i = 1
    for c in alpha:
        hmap[i] = c
        i += 1
    # print(hmap)

    steps = len(s)
    max_char = sorted(c for c in s)[-1]
    # print("The steps are:", steps)
    # print("The max_char is:", max_char)

    # inital sanity check if something is not there in order
    for i in range(1, steps+1):
        if hmap[i] not in s:
            return 'NO'

    # Assuming everything is in order - need to check
    si = ei = s.find('a')
    # print(si, ei)

    for i in range(2, steps+1):
        idx = s.find(hmap[i])
        # print("The idx is:", idx)
        if idx <= si:
            si = idx
        elif idx >= ei:
            ei = idx
        else:
            # print("The offending char is:", hmap[i])
            return 'NO'
        # print("si and ei are", si, ei)
    return 'YES'


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        s = input()
        # print(s)
        res = solve(s)
        print(res)
        i += 1