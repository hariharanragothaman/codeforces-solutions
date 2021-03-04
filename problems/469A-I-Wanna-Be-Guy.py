def is_possible(a, b, levels):
    s3 = a.union(b)
    hmap = dict(zip(list(range(1, levels+1)), [False]*levels ))
    for l in s3:
        hmap[l] = True
    if all(c for c in hmap.values()) == True:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
    # Another smart way to do this is to check if levels == len(set) instead of doing hashmap and wasting time

if __name__ == '__main__':
    levels = int(input())
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    p1.pop(0)
    p2.pop(0)
    p1 = set(p1)
    p2 = set(p2)
    is_possible(p1, p2, levels)