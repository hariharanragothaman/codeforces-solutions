import sys

if __name__ == '__main__':
    vertices = int(input())

    # Tree formation
    from collections import defaultdict, deque
    hmap = defaultdict(list)
    i = 1
    while i < vertices:
        parent = input()
        hmap[parent].append(str(i+1))
        i += 1
    #print(hmap)

    #q = deque(hmap)
    #print(q)

    # Question is - every non-leaf vertex has atleast 3 leaf children
    for key, value in hmap.items():
        tmp = [c for c in value if c not in hmap]
        if len(tmp) < 3:
            print('No')
            sys.exit()
    print('Yes')